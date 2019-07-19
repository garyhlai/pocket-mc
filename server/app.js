const bodyParser = require("body-parser");
const express = require("express");
const app = express();
const port = 5000;

app.get("/", (req, res) => {
  res.send("Hello Wolrd");
});

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  next();
});

app.post("/suggest", function(req, res) {
  // sanitize the input posted to your route for security
  //input = req.sanitize(req.body);
  userInput = req.body.userInput;
  //console.log(userInput);
  //input = "Yo";

  // import the node helper function
  const { spawn } = require("child_process");

  // run the python process with input posted in the route
  const pythonProcess = spawn("python3", ["./script/suggestor.py", userInput]);
  console.log("spawned: " + pythonProcess.pid);

  // take the output from the python stdout process
  pythonProcess.stdout.on("data", data => {
    suggestions = data.toString();
    console.log(suggestions);
    res.send({ suggestions: suggestions });
  });
});

app.get("/express_backend", (req, res) => {
  res.send({ express: "backend is connected to react!!" });
});

app.listen(port, () => console.log(`server listening on port ${port}!`));
