// exports.detect = function(arr){
//     var result = new Map();
//     result.set("blast",0);
//     result.set("leaf_scald",0);
//     result.set("narrow_brown_spot",0)
//     result.set("sheath_rot",0);
//     result.set("red_stripe",0);
//     result.set("bakanae",0);
//     result.set("false_smut",0);
//     result.set("rice_grassy_stunt",0);
//     result.set("brown_spot",0);
//     result.set("tungro",0);
//     result.set("bacterial_blight",0);
//     result.set("sheath_blight",0);
//     arr.forEach(function(currentValue){
//         console.log("shape current value"+currentValue);
//         switch(currentValue){
//             case "circle":
//                 result.set("brown_spot",result.get("brown_spot")+1);
//                 break;
//             case "diamond":
//                 result.set("blast",result.get("blast")+1);
//                 break;
//             case "linear":
//                 result.set("narrow_brown_spot",result.get("narrow_brown_spot")+1);
//                 break;
//             case "stripe":
//                 result.set("red_stripe",result.get("red_stripe")+1);
//                 result.set("bacterial_blight",result.get("bacterial_blight")+1);
//                 break;
//         }
//     })
//     return result;
// }

exports.detect = function(arr){
    var result = {
        "blast": 0,
        "leaf_scald": 0,
        "narrow_brown_spot": 0,
        "sheath_rot": 0,
        "red_stripe": 0,
        "bakanae": 0,
        "false_smut": 0,
        "rice_grassy_stunt": 0,
        "brown_spot": 0,
        "tungro": 0,
        "bacterial_blight": 0,
        "sheath_blight": 0
    }
    arr.forEach(function(currentValue){
        console.log("shape current value"+currentValue);
        switch(currentValue){
            case "circle":
                result.brown_spot = result.brown_spot + 1;
                break;
            case "diamond":
                result.blast = result.blast + 1;
                break;
            case "linear":
                result.narrow_brown_spot = result.narrow_brown_spot + 1;
                break;
            case "stripe":
                result.red_stripe = result.red_stripe + 1;
                result.bacterial_blight = result.bacterial_blight + 1;
                break;
        }
    })
    return result;
}