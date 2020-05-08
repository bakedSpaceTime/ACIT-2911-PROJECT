const Score = require('../models/score');


class ScoreRepo {
    ScoreRepo() {
    }

    // async addScore(scoreObj) {
    //     var result = await scoreObj.save();
    //     return {obj: result, errorMessage: ""}
    // }

    async addScore(scoreObj) {
        try {
            var error = await scoreObj.validateSync();
            if (error) {
                let response = {errorMessage: error.message}
                return response
            }
            const result = await scoreObj.save();
            let response = {
                obj: result,
                errorMessage: ""
            }
            return response;
        } catch (error) {
            return {errorMessage: error.message}
        }
    }

    async getAllScores() {
        var scores = await Score.find().sort({score: -1, date: 1}).exec();
        return scores;
    }

    async deleteAllScores() {
        let deleted = await Score.remove({}).exec()
        return deleted;
    }   
}
module.exports = ScoreRepo;
