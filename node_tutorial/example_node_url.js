var http = require('http')

const urlserver = http.createServer(function (res, req) {
   res.writeHead(200, {'Content-Type': 'text/html'}); 
   res.write(req.url);
   res.end();
});

urlserver.listen(8080, () => {
    console.log('Running on port 8080')
}
)