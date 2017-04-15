exports.detect = function(arr){
    var result = new Map();
    result.set("blast",0);
    result.set("leaf_scald",0);
    result.set("narrow_brown_spot",0)
    result.set("sheath_rot",0);
    result.set("red_stripe",0);
    result.set("bakanae",0);
    result.set("false_smut",0);
    result.set("rice_grassy_stunt",0);
    result.set("brown_spot",0);
    result.set("tungro",0);
    result.set("bacterial_blight",0);
    result.set("sheath_blight",0);
    arr.forEach(function(currentValue){
        console.log("color current value"+currentValue);
        switch(currentValue){
            case "dark":
                result.set("blast",result.get("blast")+1);
                result.set("leaf_scald",result.get("leaf_scald")+1);
                result.set("narrow_brown_spot",result.get("narrow_brown_spot")+1);
                result.set("sheath_rot",result.get("sheath_rot")+1);
                break;
            case "green":
                result.set("blast",result.get("blast")+1);
                result.set("red_stripe",result.get("red_stripe")+1);
                result.set("bakanae",result.get("bakanae")+1);
                result.set("false_smut",result.get("false_smut")+1);
                result.set("rice_grassy_stunt",result.get("rice_grassy_stunt")+1);
                break;
            case "purple":
                result.set("brown_spot",result.get("brown_spot")+1);
                break;
            case "red":
                result.set("blast",result.get("blast")+1);
                result.set("leaf_scald",result.get("leaf_scald")+1);
                result.set("brown_spo",result.get("brown_spo")+1);
                result.set("sheath_rot",result.get("sheath_rot")+1);
                break;
            case "yellow":
                result.set("red_stripe",result.get("red_stripe")+1);
                result.set("bakanae",result.get("bakanae")+1);
                result.set("tungro",result.get("tungro")+1);
                result.set("rice_grassy_stunt",result.get("rice_grassy_stunt")+1);
                result.set("bacterial_blight",result.get("bacterial_blight")+1);
                break;
        }
    })
    return result;
}