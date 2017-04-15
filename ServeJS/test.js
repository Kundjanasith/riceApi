var http = require('http');
var https = require('https');
var fs = require('fs');

var file = fs.createWriteStream("file2.jpg");
var request = https.get("https://firebasestorage.googleapis.com/v0/b/javebratt-4eb54.appspot.com/o/images%2FIMG_2606.PNG?alt=media&token=c3ee8602-08ff-404e-8df5-298354fc515d", function(response) {
  response.pipe(file);
});
