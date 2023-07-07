var http = require('http');
var dt = require('./exampleModule');

const server = http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write('The date and time is: ' + dt.myDateTime() + '\nHello World!');
  res.end();
});

server.listen(8080, () => {
    console.log('Server is running on port 8080');
  });