// var mongoose = require('mongoose');
// var db = mongoose.createConnection('localhost', 'reflections');



var databaseUrl = "reflections"; // "username:password@example.com/mydb"
var collections = ["words"];
var db = require("mongojs").connect(databaseUrl, collections);

	db.words.findOne({name: 'Robert Tunney'}, function(err, user) {
  		if( err || !user) console.log("No user found with entered name");
  		else {
  			keywords = [];
  			for (keyword in user.keywords) {
  				keywords.push(keyword);
  			}
  			console.log(keywords);
  		}
	});
};

display_user();