var chai = require('chai');
var chaiHttp = require('chai-http');
var app = require('../app.js');

chai.use(chaiHttp);
chai.should();

describe("API Scores", () => {
    describe("GET and POST /", () => {
        // it("Tests all the scores returned by API.", (done) => {
        //     chai.request(app)
        //     .get('/Api/Score')
        //     .end((err, res) => {
        //         res.should.have.status(200);
        //         res.body.should.be.a('object');
        //         // console.log(JSON.stringify(res.body.scores))
        //         done();
        //     })
        // })

        it("Tests POST and return response from API.", (done) => {
            chai.request(app)
            .post('/Api/Score/AddScore')
            .send({'name': 'Bob', 'score': 8999})
            .end((err,res) => {
                console.log("Showing output.")
                console.log(JSON.stringify(res.body));
                res.body.score.name.should.equal('Bob');
                res.body.score.score.should.equal(8999);
                done();
            })
        })

        it("Tests invalid POST and receipt content from API.", (done) => {
            chai.request(app)
            .post('/Api/Score/AddScore')
            .send({'name': 'Jack'})
            .end((err,res) => {
                console.log("Showing output.")
                console.log(JSON.stringify(res.body));
                res.body.errorMessage.should.be.a('string');
                done();
            })
        })
    })
})