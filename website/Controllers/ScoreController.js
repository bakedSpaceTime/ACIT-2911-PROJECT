const Score = require('../models/score');
const ScoreRepo = require('../Data/ScoreRepo');
const _scoreRepo = new ScoreRepo();

exports.AddScore = async function(req, res) {
    let name = req.body.name;
    let score = req.body.score;
    let tempScoreObj = new Score({
        "name": name,
        "score": score,
        "date": new Date(),
    })
    let response = await _scoreRepo.addScore(tempScoreObj)
    if (response.errorMessage == "") {
        res.json({'errorMessage': "", 'score': response.obj})
    } else {
        res.json({'errorMessage': response.errorMessage})
    }
}

exports.AllScores = async function(req, res) {
    let scores = await _scoreRepo.getAllScores();
    res.json({scores: scores});
}

exports.Delete = async function(req, res) {
    let response = await _scoreRepo.deleteAllScores();
    if (response) {
        res.json({"message": response})
    } else {
        res.json({"message": ""})
    }
}