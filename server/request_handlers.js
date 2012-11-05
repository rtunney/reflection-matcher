var querystring = require("querystring")
function create_body (name, words, word, matches) {
	var body = '<html>' +
	'<body>' +
	'<h1>Make me a match!</h1>' +
	'<form action="/words" method="post">' +
  	'<label>Full Name: </label>' +
  	'<textarea name="text" rows="1" cols="30"></textarea><br>' +
  	'<input type="submit" value="Submit"></submit><br>' +
	'</form>' +
	'<ul id="kwlist">' +
	//keywords + 
	'</ul>' +
	'</body>' +
	'</html>'
}

function start(response, postData) {
	console.log("Request handler 'start' was called.");
	var body = '<html>' +
	'<body>' +
	'<h1>Make me a match!</h1>' +
	'<form action="/words" method="post">' +
  	'<label>Full Name: </label>' +
  	'<textarea name="text" rows="1" cols="30">Default</textarea><br>' +
  	'<input type="submit" value="Submit"></submit><br>' +
	'</form>' +
	'<ul id="kwlist"></ul>' +
	//'<script src="display_keywords.js"></script>' +
	'</body>' +
	'</html>'
	response.writeHead(200, {"Content-Type":"text/html"});
	response.write(body);
	response.end();
}

function words(response, postData) {
	console.log("Request handler 'upload' was called");
	response.writeHead(200, {"Content-Type":"text/plain"});
	var name = querystring.parse(postData).text;
	response.write("You've sent: " + name);
	response.end();
}

exports.start = start
exports.words = words