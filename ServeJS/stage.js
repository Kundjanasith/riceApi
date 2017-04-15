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
//         console.log("stage current value"+currentValue);
//         switch(currentValue){
//             case "crop":
//                 result.set("sheath_rot",result.get("sheath_rot")+1);
//                 result.set("brown_spot",result.get("brown_spot")+1);
//                 break;
//             case "flowering":
//                 result.set("false_smut",result.get("false_smut")+1);
//                 break;
//             case "reproductive":
//                 result.set("red_stripe",result.get("red_stripe")+1);
//                 break;
//             case "tillering":
//                 result.set("rice_grassy_stunt",result.get("rice_grassy_stunt")+1);
//                 result.set("sheath_blight",result.get("sheath_blight")+1);
//                 result.set("tungro",result.get("tungro")+1);
//                 result.set("bakanae",result.get("bakanae")+1);
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
        console.log("stage current value"+currentValue);
        switch(currentValue){
            case "crop":
                result.sheath_rot = result.sheath_rot + 1;
                result.brown_spot = result.brown_spot + 1;
                break;
            case "flowering":
                result.false_smut = result.false_smut + 1;
                break;
            case "reproductive":
                result.red_stripe = result.red_stripe + 1;
                break;
            case "tillering":
                result.rice_grassy_stunt = result.rice_grassy_stunt + 1;
                result.sheath_blight = result.sheath_blight + 1;
                result.tungro = result.tungro + 1;
                result.bakanae = result.bakanae + 1;
                break;
        }
    })
    return result;
}