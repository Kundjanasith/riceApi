var express = require('express');
var app = express();
var router = express.Router();

const analyseModule = require('./analyse');


router.use( function ( req, res, next ) {
	next();
});


// app.get('/up',function(req,res){
//    var first = storageRef.child('/home/nicco/Scrivania/0first.eps');
//    var uploadTask = storageRef.child('images/' + file.name).put(file);
//  })
var https = require('https');
var fs = require('fs');

router.get( '/analysis/:reqMsg', function ( req, res ) {
	var reqMsg = req.params.reqMsg;
	var resMsg = analyseModule.analyse(reqMsg);
    fs.writeFile("getResult/rule_res.txt", resMsg, function(err) {
        if(err) {
            return console.log(err);
        }
    console.log("The file was saved!");
}); 
	res.send(resMsg);
});


var exec = require('child_process').exec;
var execProcess = require("./exec_process.js");
router.get( '/upload/:link', function ( req, res ) {
  var obj = req.params.link;
  console.log(obj);
  var url1 = obj.split('Kundjanasith').join('https://');
  var url2 = url1.split('Thonglek').join('/');
  var url3 = url2.split(' ').join('%20');
  var url4 = url3.split('5710545023').join('?');
  var url5 = url4.split('images/').join('images%2F');
  var file = fs.createWriteStream("backEnd/res.png");
  console.log("PP"+url5);
  var request = https.get(url5, function(response) {
    response.pipe(file);

    execProcess.result("sh backEnd/test.sh ", function(err, response){
        if(!err){
            console.log(response);
            console.log("Bash Start . . .")
            fs.readFile('backEnd/result.txt', 'utf8', function(err, data) {
                if (err) throw err;
                console.log('Data >> '+data);
                analyseModule.imgPro(data);
                // res.sendFile(__dirname+'/backEnd/res_img.png');
                var j = {
                    status: "ok"
                };
                res.send(j);
            });
            console.log("Bash Finish . . .")
        }else {
            console.log(err);
        }
    });

    execProcess.result("python  getResult/resultI.py", function(err, response){
        if(!err){
            console.log(response);
            
        }else {
            console.log(err);
        }
    });

    execProcess.result("python  getResult/resultT.py", function(err, response){
        if(!err){
            console.log(response);
        }else {
            console.log(err);
        }
    });


  });
});

router.get( '/img', function ( req, res ) {
    res.sendFile(__dirname+'/backEnd/res_img.png');
});

router.get( '/resultI', function ( req, res ) {
    res.sendFile(__dirname+'/getResult/resultI.txt');
});

router.get( '/resultT', function ( req, res ) {
    res.sendFile(__dirname+'/getResult/resultT.txt');
});

router.get( '/test', function ( req, res ) {
	console.log("Test");
	res.send("mmmmm");
});

router.get( '/', function ( req, res ) {
	res.sendFile(__dirname+'/index.html');
});

app.use( '/', router );
app.listen(1919,function(){
	console.log("Running 1919");
});
