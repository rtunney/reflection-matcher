var server = require('./server');
var router = require('./router');
var request_handlers = require('./request_handlers');

var handler_dict = {}
//Takes a path in the domain and returns a handler
//function. 

handler_dict['/'] = request_handlers.start;
handler_dict['/start'] = request_handlers.start;
handler_dict['/words'] = request_handlers.words;

server.start(router.route, handler_dict);