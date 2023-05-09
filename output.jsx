
const http = require('http');

const hostname = '127.0.0.1';
const port = 80;




const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end(htmlCode);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
htmlCode = `{
  var a = 10
  var elems = {"one","two","three","Fourr","Five"}
}

<html>
    <head>
      whatever
    </head>
    <body>
        <div id = "container">
            Whatever i have Done
        </div>
        <div>
        {
          for( var i = 0; i < elems.length;i++){
            elems[i]
          }
        }
        </div>
    </body>
</html>`