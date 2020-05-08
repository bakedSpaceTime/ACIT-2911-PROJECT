var mongoose = require('mongoose');

var scoreSchema = mongoose.Schema({
    name: { type: String, required: true },
    score: { type: Number, required: true},
    date: { type: Date, required: true },
    },
    {versionKey: false, collection: "scores"},
);
let Score = mongoose.model('Score', scoreSchema);
module.exports = Score;
