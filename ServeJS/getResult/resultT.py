import json
from pprint import pprint

#rule base
json_data=open('getResult/rule_res.txt').read()
data = json.loads(json_data)
Rbacterial_blight = data['bacterial_blight']
print(Rbacterial_blight)
# Rbakanae = data['bakanae']
# print(Rbakanae)
Rblast = data['blast']
print(Rblast)
Rbrown_spot = data['brown_spot']
print(Rbrown_spot)
Rfalse_smut = data['false_smut']
print(Rfalse_smut)
Rleaf_scald = data['leaf_scald']
print(Rleaf_scald)
Rnarrow_brown_spot = data['narrow_brown_spot'] 
print(Rnarrow_brown_spot)
Rred_stripe = data['red_stripe']
print(Rred_stripe)
Rrice_grassy_stunt = data['rice_grassy_stunt']
print(Rrice_grassy_stunt) 
Rsheath_blight = data['sheath_blight'] 
print(Rsheath_blight)
Rsheath_rot = data['sheath_rot'] 
print(Rsheath_rot)
Rtungro = data['tungro']
print(Rtungro)

Rbacterial_blight = (Rbacterial_blight/3.0)*100
bacterial_blight = Rbacterial_blight
Rblast = (Rblast/8.0)*100
blast = Rblast
Rbrown_spot = (Rbrown_spot/6.0)*100
brown_spot = Rbrown_spot
Rfalse_smut = (Rfalse_smut/2.0)*100
false_smut = Rfalse_smut
Rleaf_scald = (Rleaf_scald/3.0)*100
leaf_scald = Rleaf_scald
Rnarrow_brown_spot = (Rnarrow_brown_spot/3.0)*100
narrow_brown_spot = Rnarrow_brown_spot 
Rred_stripe = (Rred_stripe/4.0)*100
red_stripe = Rred_stripe 
Rrice_grassy_stunt = (Rrice_grassy_stunt/4.0)*100
rice_grassy_stunt = Rrice_grassy_stunt 
Rsheath_blight = (Rsheath_blight/1.0)*100
sheath_blight = Rsheath_blight 
Rsheath_rot = (Rsheath_rot/3.0)*100
sheath_rot = Rsheath_rot
Rtungro = (Rtungro/2.0)*100
tungro = Rtungro

fileJ = {
    "bacterial_blight": bacterial_blight,
    "blast": blast,
    "brown_spot": brown_spot,
    "false_smut": false_smut,
    "leaf_scald": leaf_scald,
    "narrow_brown_spot": narrow_brown_spot,
    "red_stripe": red_stripe,
    "rice_grassy_stunt": rice_grassy_stunt,
    "sheath_blight": sheath_blight,
    "sheath_rot": sheath_rot,
    "tungro": tungro
}
with open('getResult/resultT.txt', 'w') as outfile:
    json.dump(fileJ, outfile)