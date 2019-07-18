const bodyParser = require("body-parser");
const express = require("express");
const app = express();
const port = 5000;

app.get("/", (req, res) => {
  res.send("Hello Wolrd");
});

app.post("/suggest", function(req, res) {
  // sanitize the input posted to your route for security
  //input = req.sanitize(req.body);
  input = req.body;
  console.log(input);
  //input = "Yo";

  // import the node helper function
  const { spawn } = require("child_process");

  // run the python process with input posted in the route
  const pythonProcess = spawn("python3", ["./script/suggestor.py", input]);

  // take the output from the python stdout process
  pythonProcess.stdout.on("data", data => {
    output = data.toString();
    console.log(output);
  });
});

app.get("/express_backend", (req, res) => {
  res.send({ express: "backend is connected to react!!" });
});

app.listen(port, () => console.log(`server listening on port ${port}!`));
