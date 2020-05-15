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

import pygame
import game
from settings import GAME_SETTINGS, VIRUS_SETTINS, VIRUS_SPRITES
from moving_entity import MovingEntity
from path_finder import RouteMap
from random import randint, seed
seed(17)


class Virus(MovingEntity):
    def __init__(self, game_ref, virus_num, level_map):

        if type(game_ref) is not game.Game:
            raise TypeError("invalid reference")

        super().__init__(game_ref, VIRUS_SPRITES, VIRUS_SETTINS[virus_num], default_sprite="right")
        
        #### These lines not needed once proper sprites are used
        self.image = pygame.transform.scale(self.image, (27,27))
        self.rect.inflate_ip(-5, -5)
        #################

        # set default direction
        # self.directions["right"] = True
        self.route_map = RouteMap(level_map)
        self.force_new_path = False
        self.path = None
        self.prev_node = None
        self.prev_node_i = None
        self.end_node = None
        self.node_count = 0
        self.start_path()

    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
        self.move()
        self.redraw()
    
    def move(self):
        self.path_position()

        if self.is_valid_direction("left"):
            self.rect.x -= self.velocity
        elif self.is_valid_direction("right"):
            self.rect.x += self.velocity
        elif self.is_valid_direction("up"):
            self.rect.y -= self.velocity
        elif self.is_valid_direction("down"):
            self.rect.y += self.velocity
    
    def path_position(self):
        collide_i = self.rect.collidelist(self.route_map.node_graph)
        if collide_i != -1:
            current_node = self.route_map.node_graph[collide_i]
            rect_contains_center = current_node.rect.collidepoint(self.rect.center)
            if rect_contains_center == 1:
                # print(f"before!:\n\tcurrent node: {current_node}\n\tnd node:{self.end_node}\n\t{self.path}\n")

                while current_node == self.end_node or self.force_new_path:
                    # print("end reached")
                    self.update_path()
                    # print(f"\nafter!:\n\tend node:{self.end_node}\n\t{self.path}\n")

                    if current_node not in self.path:
                        self.path.appendleft(current_node)
                    # print(f"\tafter again\n\t\t{self.path}")
                    self.force_new_path = False
                    
                self.snap_to_node(current_node)
                self.switch_directions() 

    def start_path(self):
        self.update_path()
        node_closest_to_me = self.route_map.find_closest_node(self.rect.center)
        self.snap_to_node(node_closest_to_me)

    def update_path(self):
        node_closest_to_player = self.route_map.find_closest_node(self.game_ref.player.rect.center)
        node_closest_to_me = self.route_map.find_closest_node(self.rect.center)

        result = self.route_map.solve(node_closest_to_me, node_closest_to_player)
        self.path = result[0]

        if len(self.path) <= 1 or not result[1][2]:
            self.random_path()

        self.end_node = self.path[-1]
        self.node_count = 0

    def random_path(self):
        while len(self.path) <= 1:
            node_closest_to_me = self.route_map.find_closest_node(self.rect.center)
            rand_index = randint(0, len(self.route_map.node_graph) - 1)
            # print("random i ", rand_index)
            random_node = self.route_map.node_graph[rand_index]
            result = self.route_map.solve(node_closest_to_me, random_node)
            self.path = result[0]
        # print("end random")

    def snap_to_node(self, node):
        if self.can_snap_to_node():
            self.prev_node = node
            self.prev_node_i = self.path.index(node)
            self.rect.center = node.rect.center
            self.node_count += 1

    def can_snap_to_node(self):
        if self.prev_node == None:
            return True
        else:
            prev_snap = self.prev_node.rect.center
            delta_x = abs(prev_snap[0] - self.rect.center[0])
            delta_y = abs(prev_snap[1] - self.rect.center[1])
            min_dist = GAME_SETTINGS["tile_side_length"] // 2
            return (delta_x > min_dist or delta_y > min_dist)

    def switch_directions(self):
        # Basic Behavior
        # Not sure how we want it to behave
        
        # if self.will_hit_wall("left"):
        #     self.directions["left"] = False
        #     self.directions["right"] = True
        # elif self.will_hit_wall("right"):
        #     self.directions["right"] = False
        #     self.directions["left"] = True
        
        key_str = self.direction_of_next_node()
        
        if key_str in self.directions.keys():
            for direction in self.directions:
                if direction == key_str:
                    self.directions[direction] = True
                else:
                    self.directions[direction] = False
        else:
            self.force_new_path = True
            for direction in self.directions:
                self.directions[direction] = False

    def direction_of_next_node(self):
        if len(self.path) > 1:
        
            reference_node = self.prev_node
            
            # print("index", self.prev_node_i + 1)
            next_node = self.path[self.prev_node_i + 1]
            dir_int = None
            # print(reference_node.neighbours)
            # print(next_node, reference_node, self.end_node)
            for i, neighbour in enumerate(reference_node.neighbours):
                if neighbour == next_node:
                    dir_int = i

            convert = {
                0: "down",
                1: "right",
                2: "up",
                3: "left",
            }

            return convert.get(dir_int, None)
