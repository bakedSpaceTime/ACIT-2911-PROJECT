var HomeController = require('./Controllers/HomeController');
var ScoreController = require('./Controllers/ScoreController');

module.exports = function(app){
    app.get('/',      HomeController.Index);
    app.get('/Download', HomeController.Download);
    app.get('/HowToPlay', HomeController.HowToPlay);
    app.post('/Api/Score/AddScore', ScoreController.AddScore)
    app.get('/Api/Score', ScoreController.AllScores)
    app.get('/Api/Score/DeleteScores', ScoreController.Delete)
};
