const colorModule = require('./color');
const placeModule = require('./place');
const shapeModule = require('./shape');
const stageModule = require('./stage');

function printMap(result){
	var blast = result.get("blast");
    var leaf_scald = result.get("leaf_scald");
    var narrow_brown_spot = result.get("narrow_brown_spot")
    var sheath_rot = result.get("sheath_rot");
    var red_stripe = result.get("red_stripe");
    var bakanae = result.get("bakanae");
    var false_smut = result.get("false_smut");
    var rice_grassy_stunt = result.get("rice_grassy_stunt");
    var brown_spot = result.get("brown_spot");
    var tungro = result.get("tungro");
    var bacterial_blight = result.get("bacterial_blight");
    var sheath_blight = result.get("sheath_blight");
	console.log("Blast : "+blast);
	console.log("Leaf_scald : "+leaf_scald);
	console.log("Narrow_brown_spot : "+narrow_brown_spot);
	console.log("Sheath_rot : "+sheath_rot);
	console.log("Red_stripe : "+red_stripe);
	console.log("False_smut : "+false_smut);
	console.log("Rice_grassy_stunt : "+rice_grassy_stunt);
	console.log("Brown_spot : "+brown_spot);
	console.log("Tungro  : "+tungro);
	console.log("Bacterial_blight : "+bacterial_blight);
	console.log("Sheath_blight : "+sheath_blight);
}

// function mergeMap(res1,res2,res3,res4){
//     var result = new Map();
//     result.set("blast",res1.get("blast")+res2.get("blast")+res3.get("blast")+res4.get("blast"));
//     result.set("leaf_scald",res1.get("leaf_scald")+res2.get("leaf_scald")+res3.get("leaf_scald")+res4.get("leaf_scald"));
//     result.set("narrow_brown_spot",res1.get("narrow_brown_spot")+res2.get("narrow_brown_spot")+res3.get("narrow_brown_spot")+res4.get("narrow_brown_spot"))
//     result.set("sheath_rot",res1.get("sheath_rot")+res2.get("sheath_rot")+res3.get("sheath_rot")+res4.get("sheath_rot"));
//     result.set("red_stripe",res1.get("red_stripe")+res2.get("red_stripe")+res3.get("red_stripe")+res4.get("red_stripe"));
//     result.set("bakanae",res1.get("bakanae")+res2.get("bakanae")+res3.get("bakanae")+res4.get("bakanae"));
//     result.set("false_smut",res1.get("false_smut")+res2.get("false_smut")+res3.get("false_smut")+res4.get("false_smut"));
//     result.set("rice_grassy_stunt",res1.get("rice_grassy_stunt")+res2.get("rice_grassy_stunt")+res3.get("rice_grassy_stunt")+res4.get("rice_grassy_stunt"));
//     result.set("brown_spot",res1.get("brown_spot")+res2.get("brown_spot")+res3.get("brown_spot")+res4.get("brown_spot"));
//     result.set("tungro",res1.get("tungro")+res2.get("tungro")+res3.get("tungro")+res4.get("tungro"));
//     result.set("bacterial_blight",res1.get("bacterial_blight")+res2.get("bacterial_blight")+res3.get("bacterial_blight")+res4.get("bacterial_blight"));
//     result.set("sheath_blight",res1.get("sheath_blight")+res2.get("sheath_blight")+res3.get("sheath_blight")+res4.get("sheath_blight"));
//     return result;
// }

function mergeMap(res1,res2,res3,res4){
    var res = {
        "blast": res1.blast + res2.blast + res3.blast + res4.blast,
        "leaf_scald": res1.leaf_scald + res2.leaf_scald + res3.leaf_scald + res4.leaf_scald,
        "narrow_brown_spot": res1.narrow_brown_spot + res2.narrow_brown_spot + res3.narrow_brown_spot + res4.narrow_brown_spot,
        "sheath_rot": res1.sheath_rot + res2.sheath_rot + res3.sheath_rot + res4.sheath_rot,
        "red_stripe": res1.red_stripe + res2.red_stripe + res3.red_stripe + res4.red_stripe,
        "bakanae": res1.bakanae + res2.bakanae + res3.bakanae + res4.bakanae,
        "false_smut": res1.false_smut + res2.false_smut + res3.false_smut + res4.false_smut,
        "rice_grassy_stunt": res1.rice_grassy_stunt + res2.rice_grassy_stunt + res3.rice_grassy_stunt + res4.rice_grassy_stunt,
        "brown_spot": res1.brown_spot + res2.brown_spot + res3.brown_spot + res4.brown_spot,
        "tungro": res1.tungro + res2.tungro + res3.tungro + res4.tungro,
        "bacterial_blight": res1.bacterial_blight + res2.bacterial_blight + res3.bacterial_blight + res4.bacterial_blight,
        "sheath_blight": res1.sheath_blight + res2.sheath_blight + res3.sheath_blight + res4.sheath_blight
    }
    return res;
}

// exports.analyse = function(arr){
//     var json = JSON.parse(arr);
//     var color = json.color;
// 	var place = json.place;
// 	var shape = json.shape;
// 	var stage = json.stage;
//     var colorResult = colorModule.detect(color);
//     var placeResult = placeModule.detect(place);
//     var shapeResult = shapeModule.detect(shape);
//     var stageResult = stageModule.detect(stage);
//     var res = mergeMap(colorResult,placeResult,shapeResult,stageResult);
//     printMap(res)
//     var resSend = {
//         "blast": res.get("blast"),
//         "leaf_scald": res.get("leaf_scald"),
//         "narrow_brown_spot": res.get("narrow_brown_spot"),
//         "sheath_rot": res.get("sheath_rot"),
//         "red_stripe": res.get("red_stripe"),
//         "bakanae": res.get("bakanae"),
//         "false_smut": res.get("false_smut"),
//         "rice_grassy_stunt": res.get("rice_grassy_stunt"),
//         "brown_spot": res.get("brown_spot"),
//         "tungro": res.get("tungro"),
//         "bacterial_blight": res.get("bacterial_blight"),
//         "sheath_blight": res.get("sheath_blight")
//     }
//     return JSON.stringify(resSend);
// }

exports.analyse = function(arr){
    var json = JSON.parse(arr);
    var color = json.color;
	var place = json.place;
	var shape = json.shape;
	var stage = json.stage;
    var colorResult = colorModule.detect(color);
    var placeResult = placeModule.detect(place);
    var shapeResult = shapeModule.detect(shape);
    var stageResult = stageModule.detect(stage);
    var res = mergeMap(colorResult,placeResult,shapeResult,stageResult);
    console.log("????"+JSON.stringify(res));
    return JSON.stringify(res);
}
