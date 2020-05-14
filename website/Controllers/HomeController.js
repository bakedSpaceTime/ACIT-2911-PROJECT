const ScoreRepo = require('../Data/ScoreRepo');
const _scoreRepo = new ScoreRepo();

exports.Index = async function(req, res) {
    let scores = await _scoreRepo.getAllScores();
    res.render('home/index', {scores: scores, page: 'home'});
};

exports.Download = async function(req, res) {
    res.render('home/download', {page: 'download'});
};

exports.HowToPlay = async function(req, res) {
    res.render('home/howtoplay', {page: 'howtoplay'})
}