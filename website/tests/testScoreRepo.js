var chai = require('chai');
var expect = chai.expect;
var sinon = require('sinon');
var ScoreRepository = require('../Data/ScoreRepo');

describe('Testing Score Repository', function() {
    var stubValue = {
        name: 'James',
        map: 'walmart',
        score: 1000
    }
    describe('create()', function() {
        it("mimic adding a new score to the database", async function() {
            var scoreRepo = new ScoreRepository();
            var stub = sinon.stub(scoreRepo, "addScore").returns(stubValue);
            var score = await scoreRepo.addScore(stubValue);
            expect(stub.calledOnce).to.be.true;
            expect(score.name).to.equal(stubValue.name);
            expect(score.score).to.equal(stubValue.score);
        })
    })


    describe('getAllScores()', function() {
        it("retrieve all scores", async function() {
            var allScoresStub = [{'name': 'Pat', 'score': 500, 'date': new Date()}]
            var scoreRepo = new ScoreRepository();
            var stub = sinon.stub(scoreRepo, 'getAllScores').returns(allScoresStub);
            var scores = await scoreRepo.getAllScores();
            expect(stub.calledOnce).to.be.true; 
            expect(scores).to.be.a('array');
        })
    })

    describe('deletedAllScores()', function() {
        it("deleteAllScores", async function() {
            var deleteStub = {
                "n": 46,
                "ok": 1,
                "deletedCount": 46
            }
            var scoreRepo = new ScoreRepository();
            var stub = sinon.stub(scoreRepo, 'deleteAllScores').returns(deleteStub);
            var response = await scoreRepo.deleteAllScores();
            expect(stub.calledOnce).to.be.true; 
            expect(response).to.be.a('object');
        })
    })
})