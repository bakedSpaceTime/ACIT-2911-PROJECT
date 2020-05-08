"""
Pandemic Run
Course: ACIT 2911, Agile Development
Authors:
- Jaskaran Saini, A01055847
- Jeffery Law, A00864331
- Ming Yen Hsieh, A01170219
- Tushya Iyer, A01023434
- Shivar Pillay, A01079978
- Shivam Patel, A01185250
"""
from collections import deque
from settings import GAME_SETTINGS, WALL_LIST
import pygame
from math import sqrt

class RouteMap():

    class RouteNode():
        def __init__(self,index_pos:tuple, x_pos = 0, y_pos = 0):
            self.index_pos = index_pos
            self.neighbours = [None, None, None, None]
            
            self.rect = pygame.Rect(x_pos, y_pos, GAME_SETTINGS["tile_side_length"], GAME_SETTINGS["tile_side_length"])

        def __str__(self):
            return f"<RouteNode: ({self.index_pos[0]},{self.index_pos[1]},{self.rect.width},{self.rect.height})>"
        
        def __repr__(self):
            return f"<RouteNode: ({self.index_pos[0]},{self.index_pos[1]},{self.rect.width},{self.rect.height})>"

        def __eq__(self, other):
            if not isinstance(other, type(self)):
                return False
            else:
                return self.index_pos == other.index_pos

    def __init__(self, level_map):

        self.level_map = level_map
        self.width = len(self.level_map[0]) + 1
        self.height = len(self.level_map) + 1

        self.all_points = [None] * self.height
        for i in range(len(self.all_points)):
            self.all_points[i] = [None] * self.width

        self.node_graph = []
        # print(f"width:{self.width}, height: {self.height}")
        
        self.load_map()

    def load_map(self):
        self.get_all_nodes()
        self.find_neighbours()
        self.create_node_graph()
    
    def create_node_graph(self):
        for row in self.all_points:
            for node in row:
                if isinstance(node, self.RouteNode):
                    self.node_graph.append(node)

    def get_all_nodes(self):
         for y, line in enumerate(self.level_map):
            # print(line)
            for x, char in enumerate(line):
                if char == '+':
                    node = self.RouteNode((x,y), x * GAME_SETTINGS["tile_side_length"], y * GAME_SETTINGS["tile_side_length"])
                    self.all_points[y][x] = node
                    
    def find_neighbours(self):
        for row in self.all_points:
            for node in row:
                if node != None:
                    x = node.index_pos[0]
                    y = node.index_pos[1]
                    surroundings = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
                    for i, point in enumerate(surroundings):
                        # print(f"node: {node}, surrounding point: {point}")
                        current_char =  self.level_map[point[1]][point[0]]
                        if current_char == "l" or current_char == "+":
                            neighbour = self.determine_neighbour(y, x, i)
                            # print(f"node: ({node}), direction: {i}, neighbour: ({neighbour})")
                            node.neighbours[i] = neighbour
    
    def determine_neighbour(self, row, column, direction):
        if direction == 0:
            current = None
            i = 1
            while current != "+" and row + i < len(self.level_map):
                current = self.level_map[row + i][column]
                i += 1
            # print(f"direction: {direction}, char found: {current}, node at point: {self.all_points[row + i - 1][column]}, i: {i}, row: {row}")
            return self.all_points[row + i -1][column]

        elif direction == 1:
            current = None
            i = 1
            while current != "+"  and column + i < len(self.level_map[0]):
                current = self.level_map[row][column + i]
                i += 1
            return self.all_points[row][column + i - 1]

        elif direction == 2:
            current = None
            i = 1
            while current != "+"  and row - i >= 0:
                current = self.level_map[row - i][column]
                i += 1
            return self.all_points[row - i + 1][column]

        elif direction == 3:
            current = None
            i = 1
            while current != "+"  and column - i >= 0:
                current = self.level_map[row][column - i]
                i += 1
            return self.all_points[row][column - i + 1]

    def solve(self, start, end):
        # Credit: https://github.com/mikepound/mazesolving/blob/master/depthfirst.py
        # With edits made by us
        
        height = self.height
        stack = deque([start])
        prev = [None] * (self.width * self.height)
        visited = [False] * (self.width * self.height)
        count = 0

        completed = False
        while stack:
            count += 1
            current = stack.pop()

            if current == end:
                completed = True
                break

            visited[current.index_pos[0] * (height - 1) + current.index_pos[1]] = True

            for n in current.neighbours:
                if n != None:
                    npos = n.index_pos[0] * (height - 1) + n.index_pos[1]
                    # print(f"current: ({current}), n: {n}, npos: {npos}")
                    if visited[npos] == False:
                        stack.append(n)
                        prev[npos] = current

        path = deque()
        current = end
        while (current != None):
            path.appendleft(current)
            # print(current.index_pos[0] * (height - 1) + current.index_pos[1])
            current = prev[current.index_pos[0] * (height - 1) + current.index_pos[1]]

        return [path, [count, len(path), completed]]

    def find_closest_node(self, position_to_check: tuple):
        x_pos = position_to_check[0]
        y_pos = position_to_check[1]

        closest_node = None
        min_distance = float("inf")

        for node in self.node_graph:
            delta_x = x_pos - node.rect.x
            delta_y = y_pos - node.rect.y
            dist_mag = sqrt( delta_x**2 + delta_y**2)

            if dist_mag < min_distance:
                min_distance = dist_mag
                closest_node = node

        return closest_node

if __name__ == "__main__":

    mappy = RouteMap(WALL_LIST)
    # print(mappy.node_graph, len(mappy.node_graph))
    # print()
    # for node in mappy.node_graph:
    #     print(f"node:{node},\nneighbours: {node.neighbours}\n")
    results = mappy.solve(mappy.node_graph[0], mappy.node_graph[-1])
    print(results)
    print(list(results[0]))
