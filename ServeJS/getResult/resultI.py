import json
from pprint import pprint

#rule base
json_data=open('rule_res.txt').read()
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

#img pro
file = open('../backEnd/result.txt', 'r') 
disS = []
perS = []
for line in file.readlines():
    dis = (line.split(','))[0]
    dis = (dis.split(':'))[0]
    dis = (dis.split('] '))[1]
    per = (line.split(', '))[1]
    per = (per.split(')'))[0]
    disS.append(dis)
    perS.append(per)
dictI = {}
for i in range(0,len(disS)):
    dictI[disS[i]] = perS[i]    
    print(i)
print(dictI)
Ibacterial_blight = dictI['Bacterial blight ']
print(Ibacterial_blight)
# Ibakanae = dictI['Bakanae ']
# print(Ibakanae)
Iblast = dictI['Blast node and neck ']
print(Iblast)
Ibrown_spot = dictI['Brown spot ']
print(Ibrown_spot)
Ifalse_smut = dictI['False smut ']
print(Ifalse_smut)
Ileaf_scald = dictI['Leaf scald ']
print(Ileaf_scald)
Inarrow_brown_spot = dictI['Narrow brown spot '] 
print(Inarrow_brown_spot)
Ired_stripe = dictI['Red stripe ']
print(Ired_stripe)
Irice_grassy_stunt = dictI['Rice grassy stunt ']
print(Irice_grassy_stunt) 
Isheath_blight = dictI['Sheath blight '] 
print(Isheath_blight)
Isheath_rot = dictI['Sheath rot '] 
print(Isheath_rot)
Itungro = dictI['Tungroc ']
print(Itungro)

#result
Rbacterial_blight = (Rbacterial_blight/3.0)*50
Ibacterial_blight = float(Ibacterial_blight)/2.0
bacterial_blight = Rbacterial_blight + Ibacterial_blight
Rblast = (Rblast/8.0)*50
Iblast = float(Iblast)/2.0
blast = Rblast + Iblast
Rbrown_spot = (Rbrown_spot/6.0)*50
Ibrown_spot = float(Ibrown_spot)/2.0
brown_spot = Rbrown_spot + Ibrown_spot
Rfalse_smut = (Rfalse_smut/2.0)*50
Ifalse_smut = float(Ifalse_smut)/2.0
false_smut = Rfalse_smut + Ifalse_smut
Rleaf_scald = (Rleaf_scald/3.0)*50
Ileaf_scald = float(Ileaf_scald)/2.0
leaf_scald = Rleaf_scald + Ileaf_scald
Rnarrow_brown_spot = (Rnarrow_brown_spot/3.0)*50
Inarrow_brown_spot = float(Inarrow_brown_spot)/2.0
narrow_brown_spot = Rnarrow_brown_spot + Inarrow_brown_spot
Rred_stripe = (Rred_stripe/4.0)*50
Ired_stripe = float(Ired_stripe)/2.0
red_stripe = Rred_stripe + Ired_stripe
Rrice_grassy_stunt = (Rrice_grassy_stunt/4.0)*50
Irice_grassy_stunt = float(Irice_grassy_stunt)/2.0
rice_grassy_stunt = Rrice_grassy_stunt + Irice_grassy_stunt
Rsheath_blight = (Rsheath_blight/1.0)*50
Isheath_blight = float(Isheath_blight)/2.0
sheath_blight = Rsheath_blight + Isheath_blight
Rsheath_rot = (Rsheath_rot/3.0)*50
Isheath_rot = float(Isheath_rot)/2.0
sheath_rot = Rsheath_rot + Isheath_rot
Rtungro = (Rtungro/2.0)*50
Itungro = float(Itungro)/2.0
tungro = Rtungro + Itungro

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
with open('resultI.txt', 'w') as outfile:
    json.dump(fileJ, outfile)