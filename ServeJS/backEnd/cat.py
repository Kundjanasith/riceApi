
import sys

path = sys.argv[1]

in_put = open(path,'r')
in_ = in_put.read()

D_01 = open('img-db/01_bacterial_blight/01_sum.txt', 'r')
D_001 = D_01.read()

D_02 = open('img-db/02_bacterial_leaf_streak/02_sum.txt','r')
D_002 = D_02.read()

D_03 = open('img-db/03_bacterial_sheath_brown_rot/03_sum.txt','r')
D_003 = D_03.read()

D_04 = open('img-db/04_bakanae/04_sum.txt','r')
D_004 = D_04.read()

D_05 = open('img-db/05_blast_leaf_and_collar/05_sum.txt','r')
D_005 = D_05.read()

D_06 = open('img-db/06_blast_node_and_neck/06_sum.txt','r')
D_006 = D_06.read()

D_07 = open('img-db/07_brown_spot/07_sum.txt','r')
D_007 = D_07.read()

D_08 = open('img-db/08_false_smut/08_sum.txt','r')
D_008 = D_08.read()

D_09 = open('img-db/09_leaf_scald/09_sum.txt','r')
D_009 = D_09.read()

D_10 = open('img-db/10_narrow_brown_spot/10_sum.txt','r')
D_010 = D_10.read()

D_11 = open('img-db/11_red_stripe/11_sum.txt','r')
D_011 = D_11.read()

D_12 = open('img-db/12_rice_grassy_stunt/12_sum.txt','r')
D_012 = D_12.read()

D_13 = open('img-db/13_rice_ragged_stunt/13_sum.txt','r')
D_013 = D_13.read()

D_14 = open('img-db/14_rice_stripe_virus_disease/14_sum.txt','r')
D_014 = D_14.read()

D_15 = open('img-db/15_rice_yellow_mottle_virus/15_sum.txt','r')
D_015 = D_15.read()

D_16 = open('img-db/16_sheath_blight/16_sum.txt','r')
D_016 = D_16.read()

D_17 = open('img-db/17_sheath_rot/17_sum.txt','r')
D_017 = D_17.read()

D_18 = open('img-db/18_stem_rot/18_sum.txt','r')
D_018 = D_18.read()

D_19 = open('img-db/19_tungroc/19_sum.txt','r')
D_019 = D_19.read()

in_blue_x = 0
in_blue_y = 0
in_green_x = 0
in_green_y = 0
in_purple_x = 0
in_purple_y = 0
in_red_x = 0
in_red_y = 0
in_yellow_x = 0
in_yellow_y = 0
inputs = []
for x in in_.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        inputs.append(temp)

for x in inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D01_blue_x = 0
D01_blue_y = 0
D01_green_x = 0
D01_green_y = 0
D01_purple_x = 0
D01_purple_y = 0
D01_red_x = 0
D01_red_y = 0
D01_yellow_x = 0
D01_yellow_y = 0
D01_inputs = []
for x in D_001.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D01_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D01_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D01_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D01_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D01_inputs.append(temp)

for x in D01_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D02_blue_x = 0
D02_blue_y = 0
D02_green_x = 0
D02_green_y = 0
D02_purple_x = 0
D02_purple_y = 0
D02_red_x = 0
D02_red_y = 0
D02_yellow_x = 0
D02_yellow_y = 0
D02_inputs = []
for x in D_002.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D02_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D02_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D02_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D02_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D02_inputs.append(temp)

for x in D02_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D03_blue_x = 0
D03_blue_y = 0
D03_green_x = 0
D03_green_y = 0
D03_purple_x = 0
D03_purple_y = 0
D03_red_x = 0
D03_red_y = 0
D03_yellow_x = 0
D03_yellow_y = 0
D03_inputs = []
for x in D_003.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D03_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D03_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D03_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D03_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D03_inputs.append(temp)

for x in D03_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D04_blue_x = 0
D04_blue_y = 0
D04_green_x = 0
D04_green_y = 0
D04_purple_x = 0
D04_purple_y = 0
D04_red_x = 0
D04_red_y = 0
D04_yellow_x = 0
D04_yellow_y = 0
D04_inputs = []
for x in D_004.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D04_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D04_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D04_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D04_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D04_inputs.append(temp)

for x in D04_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D05_blue_x = 0
D05_blue_y = 0
D05_green_x = 0
D05_green_y = 0
D05_purple_x = 0
D05_purple_y = 0
D05_red_x = 0
D05_red_y = 0
D05_yellow_x = 0
D05_yellow_y = 0
D05_inputs = []
for x in D_005.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D05_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D05_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D05_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D05_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D05_inputs.append(temp)

for x in D05_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D06_blue_x = 0
D06_blue_y = 0
D06_green_x = 0
D06_green_y = 0
D06_purple_x = 0
D06_purple_y = 0
D06_red_x = 0
D06_red_y = 0
D06_yellow_x = 0
D06_yellow_y = 0
D06_inputs = []
for x in D_006.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D06_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D06_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D06_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D06_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D06_inputs.append(temp)

for x in D06_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D07_blue_x = 0
D07_blue_y = 0
D07_green_x = 0
D07_green_y = 0
D07_purple_x = 0
D07_purple_y = 0
D07_red_x = 0
D07_red_y = 0
D07_yellow_x = 0
D07_yellow_y = 0
D07_inputs = []
for x in D_007.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D07_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D07_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D07_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D07_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D07_inputs.append(temp)

for x in D07_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D08_blue_x = 0
D08_blue_y = 0
D08_green_x = 0
D08_green_y = 0
D08_purple_x = 0
D08_purple_y = 0
D08_red_x = 0
D08_red_y = 0
D08_yellow_x = 0
D08_yellow_y = 0
D08_inputs = []
for x in D_008.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D08_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D08_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D08_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D08_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D08_inputs.append(temp)

for x in D08_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D09_blue_x = 0
D09_blue_y = 0
D09_green_x = 0
D09_green_y = 0
D09_purple_x = 0
D09_purple_y = 0
D09_red_x = 0
D09_red_y = 0
D09_yellow_x = 0
D09_yellow_y = 0
D09_inputs = []
for x in D_009.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D09_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D09_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D09_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D09_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D09_inputs.append(temp)

for x in D09_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D10_blue_x = 0
D10_blue_y = 0
D10_green_x = 0
D10_green_y = 0
D10_purple_x = 0
D10_purple_y = 0
D10_red_x = 0
D10_red_y = 0
D10_yellow_x = 0
D10_yellow_y = 0
D10_inputs = []
print "----------------------------------"
for x in D_010.split("\n"):
    col = x.split(":")[0]
    print col
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        print temp.x
        D10_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D10_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D10_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D10_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D10_inputs.append(temp)
print D10_inputs[0]

for x in D10_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D11_blue_x = 0
D11_blue_y = 0
D11_green_x = 0
D11_green_y = 0
D11_purple_x = 0
D11_purple_y = 0
D11_red_x = 0
D11_red_y = 0
D11_yellow_x = 0
D11_yellow_y = 0
D11_inputs = []
for x in D_011.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D11_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D11_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D11_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D11_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D11_inputs.append(temp)

for x in D11_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D12_blue_x = 0
D12_blue_y = 0
D12_green_x = 0
D12_green_y = 0
D12_purple_x = 0
D12_purple_y = 0
D12_red_x = 0
D12_red_y = 0
D12_yellow_x = 0
D12_yellow_y = 0
D12_inputs = []
for x in D_012.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D12_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D12_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D12_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D12_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D12_inputs.append(temp)

for x in D12_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D13_blue_x = 0
D13_blue_y = 0
D13_green_x = 0
D13_green_y = 0
D13_purple_x = 0
D13_purple_y = 0
D13_red_x = 0
D13_red_y = 0
D13_yellow_x = 0
D13_yellow_y = 0
D13_inputs = []
for x in D_013.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D13_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D13_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D13_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D13_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D13_inputs.append(temp)

for x in D13_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D14_blue_x = 0
D14_blue_y = 0
D14_green_x = 0
D14_green_y = 0
D14_purple_x = 0
D14_purple_y = 0
D14_red_x = 0
D14_red_y = 0
D14_yellow_x = 0
D14_yellow_y = 0
D14_inputs = []
for x in D_014.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D14_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D14_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D14_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D14_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D14_inputs.append(temp)

for x in D14_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D15_blue_x = 0
D15_blue_y = 0
D15_green_x = 0
D15_green_y = 0
D15_purple_x = 0
D15_purple_y = 0
D15_red_x = 0
D15_red_y = 0
D15_yellow_x = 0
D15_yellow_y = 0
D15_inputs = []
for x in D_015.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D15_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D15_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D15_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D15_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D15_inputs.append(temp)

for x in D15_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D16_blue_x = 0
D16_blue_y = 0
D16_green_x = 0
D16_green_y = 0
D16_purple_x = 0
D16_purple_y = 0
D16_red_x = 0
D16_red_y = 0
D16_yellow_x = 0
D16_yellow_y = 0
D16_inputs = []
for x in D_016.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D16_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D16_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D16_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D16_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D16_inputs.append(temp)

for x in D16_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D17_blue_x = 0
D17_blue_y = 0
D17_green_x = 0
D17_green_y = 0
D17_purple_x = 0
D17_purple_y = 0
D17_red_x = 0
D17_red_y = 0
D17_yellow_x = 0
D17_yellow_y = 0
D17_inputs = []
for x in D_017.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D17_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D17_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D17_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D17_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D17_inputs.append(temp)

for x in D17_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D18_blue_x = 0
D18_blue_y = 0
D18_green_x = 0
D18_green_y = 0
D18_purple_x = 0
D18_purple_y = 0
D18_red_x = 0
D18_red_y = 0
D18_yellow_x = 0
D18_yellow_y = 0
D18_inputs = []
for x in D_018.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D18_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D18_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D18_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D18_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D18_inputs.append(temp)

for x in D18_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

D19_blue_x = 0
D19_blue_y = 0
D19_green_x = 0
D19_green_y = 0
D19_purple_x = 0
D19_purple_y = 0
D19_red_x = 0
D19_red_y = 0
D19_yellow_x = 0
D19_yellow_y = 0
D19_inputs = []
for x in D_019.split("\n"):
    col = x.split(":")[0]
    if col == "BLUE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Blue(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Blue()
        D19_inputs.append(temp)
    if col == "GREEN ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Green(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Green()
        D19_inputs.append(temp)
    if col == "PURPLE ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Purple(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Purple()
        D19_inputs.append(temp)
    if col == "RED ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Red(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Red()
        D19_inputs.append(temp)
    if col == "YELLOW ":
        t = x.split(":")[1]
        x_c = t.split(",")[0]
        y_c = t.split(",")[1]
        class Yellow(object):
            c = col
            x = int(x_c)
            y = int(y_c)
        temp = Yellow()
        D19_inputs.append(temp)

for x in D19_inputs:
    print x.c+":"+str(x.x)+","+str(x.y)

inputs_x = 0
inputs_y = 0
for i in inputs:
    inputs_x = inputs_x + int(i.x)
    inputs_y = inputs_y + int(i.y)

map = {}
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
D01_x = 0
D01_y = 0
for i in D01_inputs:
    D01_x = D01_x + int(i.x)
    D01_y = D01_y + int(i.y)

print "01"
res_01 = 0
if D01_inputs[0].x > inputs[0].x:
    if D01_inputs[0].x != 0:
        res_01 = res_01 + ( ( float(inputs[0].x)  / D01_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_01 = res_01 + 10
else:
    if inputs[0].x != 0:
        res_01 = res_01 + ( ( float(D01_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D01_inputs[0].x == 0:
            res_01 = res_01 + 10
if D01_inputs[1].x > inputs[1].x:
    if D01_inputs[1].x != 0:
        res_01 = res_01 + ( ( float(inputs[1].x)  / D01_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_01 = res_01 + 10
else:
    if inputs[1].x != 0:
        res_01 = res_01 + ( ( float(D01_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D01_inputs[1].x == 0:
            res_01 = res_01 + 10
if D01_inputs[2].x > inputs[2].x:
    if D01_inputs[2].x != 0:
        res_01 = res_01 + ( ( float(inputs[2].x)  / D01_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_01 = res_01 + 10
else:
    if inputs[2].x != 0:
        res_01 = res_01 + ( ( float(D01_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D01_inputs[2].x == 0:
            res_01 = res_01 + 10
if D01_inputs[3].x > inputs[3].x:
    if D01_inputs[3].x != 0:
        res_01 = res_01 + ( ( float(inputs[3].x)  / D01_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_01 = res_01 + 10
else:
    if inputs[3].x != 0:
        res_01 = res_01 + ( ( float(D01_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D01_inputs[3].x == 0:
            res_01 = res_01 + 10
if D01_inputs[4].x > inputs[4].x:
    if D01_inputs[4].x != 0:
        res_01 = res_01 + ( ( float(inputs[4].x)  / D01_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_01 = res_01 + 10
else:
    if inputs[4].x != 0:
        res_01 = res_01 + ( ( float(D01_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D01_inputs[4].x == 0:
            res_01 = res_01 + 10
if D01_inputs[0].y > inputs[0].y:
    if D01_inputs[0].y != 0:
        res_01 = res_01 + ( ( float(inputs[0].y)  / D01_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_01 = res_01 + 10
else:
    if inputs[0].y != 0:
        res_01 = res_01 + ( ( float(D01_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D01_inputs[0].y == 0:
            res_01 = res_01 + 10
if D01_inputs[1].y > inputs[1].y:
    if D01_inputs[1].y != 0:
        res_01 = res_01 + ( ( float(inputs[1].y)  / D01_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_01 = res_01 + 10
else:
    if inputs[1].y != 0:
        res_01 = res_01 + ( ( float(D01_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D01_inputs[1].y == 0:
            res_01 = res_01 + 10
if D01_inputs[2].y > inputs[2].y:
    if D01_inputs[2].y != 0:
        res_01 = res_01 + ( ( float(inputs[2].y)  / D01_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_01 = res_01 + 10
else:
    if inputs[2].y != 0:
        res_01 = res_01 + ( ( float(D01_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D01_inputs[2].y == 0:
            res_01 = res_01 + 10
if D01_inputs[3].y > inputs[3].y:
    if D01_inputs[3].y != 0:
        res_01 = res_01 + ( ( float(inputs[3].y)  / D01_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_01 = res_01 + 10
else:
    if inputs[3].y != 0:
        res_01 = res_01 + ( ( float(D01_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D01_inputs[3].y == 0:
            res_01 = res_01 + 10
if D01_inputs[4].y > inputs[4].y:
    if D01_inputs[4].y != 0:
        res_01 = res_01 + ( ( float(inputs[4].y)  / D01_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_01 = res_01 + 10
else:
    if inputs[4].y != 0:
        res_01 = res_01 + ( ( float(D01_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D01_inputs[4].y == 0:
            res_01 = res_01 + 10
# if D01_x >= inputs_x :
#     per01_x = ( inputs_x * 50 ) / D01_x
# else:
#     per01_x = ( D01_x * 50 ) / inputs_x
# if per01_x > 50 :
#     per01_x = 50
# if D01_y >= inputs_y :
#     per01_y = ( inputs_y * 50 ) / D01_y
# else:
#     per01_y = ( D01_y * 50 ) / inputs_y
# if per01_y > 50 :
#     per01_y = 50
# per01 = per01_x + per01_y
print "[ 01 ] Bacterial blight : "+str(res_01) + " %"
map['[ 01 ] Bacterial blight : '] = res_01

D02_x = 0
D02_y = 0
for i in D02_inputs:
    D02_x = D02_x + int(i.x)
    D02_y = D02_y + int(i.y)

print "02"
res_02 = 0
if D02_inputs[0].x > inputs[0].x:
    if D02_inputs[0].x != 0:
        res_02 = res_02 + ( ( float(inputs[0].x)  / D02_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_02 = res_02 + 10
else:
    if inputs[0].x != 0:
        res_02 = res_02 + ( ( float(D02_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D02_inputs[0].x == 0:
            res_02 = res_02 + 10
if D02_inputs[1].x > inputs[1].x:
    if D02_inputs[1].x != 0:
        res_02 = res_02 + ( ( float(inputs[1].x)  / D02_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_02 = res_02 + 10
else:
    if inputs[1].x != 0:
        res_02 = res_02 + ( ( float(D02_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D02_inputs[1].x == 0:
            res_02 = res_02 + 10
if D02_inputs[2].x > inputs[2].x:
    if D02_inputs[2].x != 0:
        res_02 = res_02 + ( ( float(inputs[2].x)  / D02_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_02 = res_02 + 10
else:
    if inputs[2].x != 0:
        res_02 = res_02 + ( ( float(D02_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D02_inputs[2].x == 0:
            res_02 = res_02 + 10
if D02_inputs[3].x > inputs[3].x:
    if D02_inputs[3].x != 0:
        res_02 = res_02 + ( ( float(inputs[3].x)  / D02_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_02 = res_02 + 10
else:
    if inputs[3].x != 0:
        res_02 = res_02 + ( ( float(D02_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D02_inputs[3].x == 0:
            res_02 = res_02 + 10
if D02_inputs[4].x > inputs[4].x:
    if D02_inputs[4].x != 0:
        res_02 = res_02 + ( ( float(inputs[4].x)  / D02_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_02 = res_02 + 10
else:
    if inputs[4].x != 0:
        res_02 = res_02 + ( ( float(D02_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D02_inputs[4].x == 0:
            res_02 = res_02 + 10
if D02_inputs[0].y > inputs[0].y:
    if D02_inputs[0].y != 0:
        res_02 = res_02 + ( ( float(inputs[0].y)  / D02_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_02 = res_02 + 10
else:
    if inputs[0].y != 0:
        res_02 = res_02 + ( ( float(D02_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D02_inputs[0].y == 0:
            res_02 = res_02 + 10
if D02_inputs[1].y > inputs[1].y:
    if D02_inputs[1].y != 0:
        res_02 = res_02 + ( ( float(inputs[1].y)  / D02_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_02 = res_02 + 10
else:
    if inputs[1].y != 0:
        res_02 = res_02 + ( ( float(D02_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D02_inputs[1].y == 0:
            res_02 = res_02 + 10
if D02_inputs[2].y > inputs[2].y:
    if D02_inputs[2].y != 0:
        res_02 = res_02 + ( ( float(inputs[2].y)  / D02_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_02 = res_02 + 10
else:
    if inputs[2].y != 0:
        res_02 = res_02 + ( ( float(D02_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D02_inputs[2].y == 0:
            res_02 = res_02 + 10
if D02_inputs[3].y > inputs[3].y:
    if D02_inputs[3].y != 0:
        res_02 = res_02 + ( ( float(inputs[3].y)  / D02_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_02 = res_02 + 10
else:
    if inputs[3].y != 0:
        res_02 = res_02 + ( ( float(D02_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D02_inputs[3].y == 0:
            res_02 = res_02 + 10
if D02_inputs[4].y > inputs[4].y:
    if D02_inputs[4].y != 0:
        res_02 = res_02 + ( ( float(inputs[4].y)  / D02_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_02 = res_02 + 10
else:
    if inputs[4].y != 0:
        res_02 = res_02 + ( ( float(D02_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D02_inputs[4].y == 0:
            res_02 = res_02 + 10
# if D02_x >= inputs_x :
#     per02_x = ( inputs_x * 50 ) / D02_x
# else:
#     per02_x = ( D02_x * 50 ) / inputs_x
# if per02_x > 50 :
#     per02_x = 50
# if D02_y >= inputs_y :
#     per02_y = ( inputs_y * 50 ) / D02_y
# else:
#     per02_y = ( D02_y * 50 ) / inputs_y
# if per02_y > 50 :
#     per02_y = 50
# per02 = per02_x + per02_y
print "[ 02 ] Bacterial leaf streak : "+str(res_02) + " %"
map['[ 02 ] Bacterial leaf streak : '] = res_02


D03_x = 0
D03_y = 0
for i in D03_inputs:
    D03_x = D03_x + int(i.x)
    D03_y = D03_y + int(i.y)
print "03"
res_03 = 0
if D03_inputs[0].x > inputs[0].x:
    if D03_inputs[0].x != 0:
        res_03 = res_03 + ( ( float(inputs[0].x)  / D03_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_03 = res_03 + 10
else:
    if inputs[0].x != 0:
        res_03 = res_03 + ( ( float(D03_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D03_inputs[0].x == 0:
            res_03 = res_03 + 10
if D03_inputs[1].x > inputs[1].x:
    if D03_inputs[1].x != 0:
        res_03 = res_03 + ( ( float(inputs[1].x)  / D03_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_03 = res_03 + 10
else:
    if inputs[1].x != 0:
        res_03 = res_03 + ( ( float(D03_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D03_inputs[1].x == 0:
            res_03 = res_03 + 10
if D03_inputs[2].x > inputs[2].x:
    if D03_inputs[2].x != 0:
        res_03 = res_03 + ( ( float(inputs[2].x)  / D03_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_03 = res_03 + 10
else:
    if inputs[2].x != 0:
        res_03 = res_03 + ( ( float(D03_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D03_inputs[2].x == 0:
            res_03 = res_03 + 10
if D03_inputs[3].x > inputs[3].x:
    if D03_inputs[3].x != 0:
        res_03 = res_03 + ( ( float(inputs[3].x)  / D03_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_03 = res_03 + 10
else:
    if inputs[3].x != 0:
        res_03 = res_03 + ( ( float(D03_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D03_inputs[3].x == 0:
            res_03 = res_03 + 10
if D03_inputs[4].x > inputs[4].x:
    if D03_inputs[4].x != 0:
        res_03 = res_03 + ( ( float(inputs[4].x)  / D03_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_03 = res_03 + 10
else:
    if inputs[4].x != 0:
        res_03 = res_03 + ( ( float(D03_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D03_inputs[4].x == 0:
            res_03 = res_03 + 10
if D03_inputs[0].y > inputs[0].y:
    if D03_inputs[0].y != 0:
        res_03 = res_03 + ( ( float(inputs[0].y)  / D03_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_03 = res_03 + 10
else:
    if inputs[0].y != 0:
        res_03 = res_03 + ( ( float(D03_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D03_inputs[0].y == 0:
            res_03 = res_03 + 10
if D03_inputs[1].y > inputs[1].y:
    if D03_inputs[1].y != 0:
        res_03 = res_03 + ( ( float(inputs[1].y)  / D03_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_03 = res_03 + 10
else:
    if inputs[1].y != 0:
        res_03 = res_03 + ( ( float(D03_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D03_inputs[1].y == 0:
            res_03 = res_03 + 10
if D03_inputs[2].y > inputs[2].y:
    if D03_inputs[2].y != 0:
        res_03 = res_03 + ( ( float(inputs[2].y)  / D03_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_03 = res_03 + 10
else:
    if inputs[2].y != 0:
        res_03 = res_03 + ( ( float(D03_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D03_inputs[2].y == 0:
            res_03 = res_03 + 10
if D03_inputs[3].y > inputs[3].y:
    if D03_inputs[3].y != 0:
        res_03 = res_03 + ( ( float(inputs[3].y)  / D03_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_03 = res_03 + 10
else:
    if inputs[3].y != 0:
        res_03 = res_03 + ( ( float(D03_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D03_inputs[3].y == 0:
            res_03 = res_03 + 10
if D03_inputs[4].y > inputs[4].y:
    if D03_inputs[4].y != 0:
        res_03 = res_03 + ( ( float(inputs[4].y)  / D03_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_03 = res_03 + 10
else:
    if inputs[4].y != 0:
        res_03 = res_03 + ( ( float(D03_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D03_inputs[4].y == 0:
            res_03 = res_03 + 10
# if D03_x >= inputs_x :
#     per03_x = ( inputs_x * 50 ) / D03_x
# else:
#     per03_x = ( D03_x * 50 ) / inputs_x
# if per03_x > 50 :
#     per03_x = 50
# if D03_y >= inputs_y :
#     per03_y = ( inputs_y * 50 ) / D03_y
# else:
#     per03_y = ( D03_y * 50 ) / inputs_y
# if per03_y > 50 :
#     per03_y = 50
# per03 = per03_x + per03_y
print "[ 03 ] Bacterial sheath brown rot : "+str(res_03) + " %"
map['[ 03 ] Bacterial sheath brown rot : '] = res_03

D04_x = 0
D04_y = 0
for i in D04_inputs:
    D04_x = D04_x + int(i.x)
    D04_y = D04_y + int(i.y)
print "04"
res_04 = 0
if D04_inputs[0].x > inputs[0].x:
    if D04_inputs[0].x != 0:
        res_04 = res_04 + ( ( float(inputs[0].x)  / D04_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_04 = res_04 + 10
else:
    if inputs[0].x != 0:
        res_04 = res_04 + ( ( float(D04_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D04_inputs[0].x == 0:
            res_04 = res_04 + 10
if D04_inputs[1].x > inputs[1].x:
    if D04_inputs[1].x != 0:
        res_04 = res_04 + ( ( float(inputs[1].x)  / D04_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_04 = res_04 + 10
else:
    if inputs[1].x != 0:
        res_04 = res_04 + ( ( float(D04_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D04_inputs[1].x == 0:
            res_04 = res_04 + 10
if D04_inputs[2].x > inputs[2].x:
    if D04_inputs[2].x != 0:
        res_04 = res_04 + ( ( float(inputs[2].x)  / D04_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_04 = res_04 + 10
else:
    if inputs[2].x != 0:
        res_04 = res_04 + ( ( float(D04_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D04_inputs[2].x == 0:
            res_04 = res_04 + 10
if D04_inputs[3].x > inputs[3].x:
    if D04_inputs[3].x != 0:
        res_04 = res_04 + ( ( float(inputs[3].x)  / D04_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_04 = res_04 + 10
else:
    if inputs[3].x != 0:
        res_04 = res_04 + ( ( float(D04_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D04_inputs[3].x == 0:
            res_04 = res_04 + 10
if D04_inputs[4].x > inputs[4].x:
    if D04_inputs[4].x != 0:
        res_04 = res_04 + ( ( float(inputs[4].x)  / D04_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_04 = res_04 + 10
else:
    if inputs[4].x != 0:
        res_04 = res_04 + ( ( float(D04_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D04_inputs[4].x == 0:
            res_04 = res_04 + 10
if D04_inputs[0].y > inputs[0].y:
    if D04_inputs[0].y != 0:
        res_04 = res_04 + ( ( float(inputs[0].y)  / D04_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_04 = res_04 + 10
else:
    if inputs[0].y != 0:
        res_04 = res_04 + ( ( float(D04_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D04_inputs[0].y == 0:
            res_04 = res_04 + 10
if D04_inputs[1].y > inputs[1].y:
    if D04_inputs[1].y != 0:
        res_04 = res_04 + ( ( float(inputs[1].y)  / D04_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_04 = res_04 + 10
else:
    if inputs[1].y != 0:
        res_04 = res_04 + ( ( float(D04_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D04_inputs[1].y == 0:
            res_04 = res_04 + 10
if D04_inputs[2].y > inputs[2].y:
    if D04_inputs[2].y != 0:
        res_04 = res_04 + ( ( float(inputs[2].y)  / D04_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_04 = res_04 + 10
else:
    if inputs[2].y != 0:
        res_04 = res_04 + ( ( float(D04_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D04_inputs[2].y == 0:
            res_04 = res_04 + 10
if D04_inputs[3].y > inputs[3].y:
    if D04_inputs[3].y != 0:
        res_04 = res_04 + ( ( float(inputs[3].y)  / D04_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_04 = res_04 + 10
else:
    if inputs[3].y != 0:
        res_04 = res_04 + ( ( float(D04_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D04_inputs[3].y == 0:
            res_04 = res_04 + 10
if D04_inputs[4].y > inputs[4].y:
    if D04_inputs[4].y != 0:
        res_04 = res_04 + ( ( float(inputs[4].y)  / D04_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_04 = res_04 + 10
else:
    if inputs[4].y != 0:
        res_04 = res_04 + ( ( float(D04_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D04_inputs[4].y == 0:
            res_04 = res_04 + 10
print "[ 04 ] Bakanae : "+str(res_04) + " %"
map['[ 04 ] Bakanae : '] = res_04

D05_x = 0
D05_y = 0
for i in D05_inputs:
    D05_x = D05_x + int(i.x)
    D05_y = D05_y + int(i.y)
print "05"
res_05 = 0
if D05_inputs[0].x > inputs[0].x:
    if D05_inputs[0].x != 0:
        res_05 = res_05 + ( ( float(inputs[0].x)  / D05_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_05 = res_05 + 10
else:
    if inputs[0].x != 0:
        res_05 = res_05 + ( ( float(D05_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D05_inputs[0].x == 0:
            res_05 = res_05 + 10
if D05_inputs[1].x > inputs[1].x:
    if D05_inputs[1].x != 0:
        res_05 = res_05 + ( ( float(inputs[1].x)  / D05_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_05 = res_05 + 10
else:
    if inputs[1].x != 0:
        res_05 = res_05 + ( ( float(D05_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D05_inputs[1].x == 0:
            res_05 = res_05 + 10
if D05_inputs[2].x > inputs[2].x:
    if D05_inputs[2].x != 0:
        res_05 = res_05 + ( ( float(inputs[2].x)  / D05_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_05 = res_05 + 10
else:
    if inputs[2].x != 0:
        res_05 = res_05 + ( ( float(D05_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D05_inputs[2].x == 0:
            res_05 = res_05 + 10
if D05_inputs[3].x > inputs[3].x:
    if D05_inputs[3].x != 0:
        res_05 = res_05 + ( ( float(inputs[3].x)  / D05_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_05 = res_05 + 10
else:
    if inputs[3].x != 0:
        res_05 = res_05 + ( ( float(D05_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D05_inputs[3].x == 0:
            res_05 = res_05 + 10
if D05_inputs[4].x > inputs[4].x:
    if D05_inputs[4].x != 0:
        res_05 = res_05 + ( ( float(inputs[4].x)  / D05_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_05 = res_05 + 10
else:
    if inputs[4].x != 0:
        res_05 = res_05 + ( ( float(D05_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D05_inputs[4].x == 0:
            res_05 = res_05 + 10
if D05_inputs[0].y > inputs[0].y:
    if D05_inputs[0].y != 0:
        res_05 = res_05 + ( ( float(inputs[0].y)  / D05_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_05 = res_05 + 10
else:
    if inputs[0].y != 0:
        res_05 = res_05 + ( ( float(D05_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D05_inputs[0].y == 0:
            res_05 = res_05 + 10
if D05_inputs[1].y > inputs[1].y:
    if D05_inputs[1].y != 0:
        res_05 = res_05 + ( ( float(inputs[1].y)  / D05_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_05 = res_05 + 10
else:
    if inputs[1].y != 0:
        res_05 = res_05 + ( ( float(D05_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D05_inputs[1].y == 0:
            res_05 = res_05 + 10
if D05_inputs[2].y > inputs[2].y:
    if D05_inputs[2].y != 0:
        res_05 = res_05 + ( ( float(inputs[2].y)  / D05_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_05 = res_05 + 10
else:
    if inputs[2].y != 0:
        res_05 = res_05 + ( ( float(D05_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D05_inputs[2].y == 0:
            res_05 = res_05 + 10
if D05_inputs[3].y > inputs[3].y:
    if D05_inputs[3].y != 0:
        res_05 = res_05 + ( ( float(inputs[3].y)  / D05_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_05 = res_05 + 10
else:
    if inputs[3].y != 0:
        res_05 = res_05 + ( ( float(D05_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D05_inputs[3].y == 0:
            res_05 = res_05 + 10
if D05_inputs[4].y > inputs[4].y:
    if D05_inputs[4].y != 0:
        res_05 = res_05 + ( ( float(inputs[4].y)  / D05_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_05 = res_05 + 10
else:
    if inputs[4].y != 0:
        res_05 = res_05 + ( ( float(D05_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D05_inputs[4].y == 0:
            res_05 = res_05 + 10
# if D05_x >= inputs_x :
#     per05_x = ( inputs_x * 50 ) / D05_x
# else:
#     per05_x = ( D05_x * 50 ) / inputs_x
# if per05_x > 50 :
#     per05_x = 50
# if D05_y >= inputs_y :
#     per05_y = ( inputs_y * 50 ) / D05_y
# else:
#     per05_y = ( D05_y * 50 ) / inputs_y
# if per05_y > 50 :
#     per05_y = 50
# per05 = per05_x + per05_y
print "[ 05 ] Blast leaf and collar : "+str(res_05) + " %"
map['[ 05 ] Blast leaft and collar : '] = res_05

D06_x = 0
D06_y = 0
for i in D06_inputs:
    D06_x = D06_x + int(i.x)
    D06_y = D06_y + int(i.y)
print "06"
res_06 = 0
if D06_inputs[0].x > inputs[0].x:
    if D06_inputs[0].x != 0:
        res_06 = res_06 + ( ( float(inputs[0].x)  / D06_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_06 = res_06 + 10
else:
    if inputs[0].x != 0:
        res_06 = res_06 + ( ( float(D06_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D06_inputs[0].x == 0:
            res_06 = res_06 + 10
if D06_inputs[1].x > inputs[1].x:
    if D06_inputs[1].x != 0:
        res_06 = res_06 + ( ( float(inputs[1].x)  / D06_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_06 = res_06 + 10
else:
    if inputs[1].x != 0:
        res_06 = res_06 + ( ( float(D06_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D06_inputs[1].x == 0:
            res_06 = res_06 + 10
if D06_inputs[2].x > inputs[2].x:
    if D06_inputs[2].x != 0:
        res_06 = res_06 + ( ( float(inputs[2].x)  / D06_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_06 = res_06 + 10
else:
    if inputs[2].x != 0:
        res_06 = res_06 + ( ( float(D06_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D06_inputs[2].x == 0:
            res_06 = res_06 + 10
if D06_inputs[3].x > inputs[3].x:
    if D06_inputs[3].x != 0:
        res_06 = res_06 + ( ( float(inputs[3].x)  / D06_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_06 = res_06 + 10
else:
    if inputs[3].x != 0:
        res_06 = res_06 + ( ( float(D06_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D06_inputs[3].x == 0:
            res_06 = res_06 + 10
if D06_inputs[4].x > inputs[4].x:
    if D06_inputs[4].x != 0:
        res_06 = res_06 + ( ( float(inputs[4].x)  / D06_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_06 = res_06 + 10
else:
    if inputs[4].x != 0:
        res_06 = res_06 + ( ( float(D06_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D06_inputs[4].x == 0:
            res_06 = res_06 + 10
if D06_inputs[0].y > inputs[0].y:
    if D06_inputs[0].y != 0:
        res_06 = res_06 + ( ( float(inputs[0].y)  / D06_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_06 = res_06 + 10
else:
    if inputs[0].y != 0:
        res_06 = res_06 + ( ( float(D06_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D06_inputs[0].y == 0:
            res_06 = res_06 + 10
if D06_inputs[1].y > inputs[1].y:
    if D06_inputs[1].y != 0:
        res_06 = res_06 + ( ( float(inputs[1].y)  / D06_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_06 = res_06 + 10
else:
    if inputs[1].y != 0:
        res_06 = res_06 + ( ( float(D06_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D06_inputs[1].y == 0:
            res_06 = res_06 + 10
if D06_inputs[2].y > inputs[2].y:
    if D06_inputs[2].y != 0:
        res_06 = res_06 + ( ( float(inputs[2].y)  / D06_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_06 = res_06 + 10
else:
    if inputs[2].y != 0:
        res_06 = res_06 + ( ( float(D06_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D06_inputs[2].y == 0:
            res_06 = res_06 + 10
if D06_inputs[3].y > inputs[3].y:
    if D06_inputs[3].y != 0:
        res_06 = res_06 + ( ( float(inputs[3].y)  / D06_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_06 = res_06 + 10
else:
    if inputs[3].y != 0:
        res_06 = res_06 + ( ( float(D06_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D06_inputs[3].y == 0:
            res_06 = res_06 + 10
if D06_inputs[4].y > inputs[4].y:
    if D06_inputs[4].y != 0:
        res_06 = res_06 + ( ( float(inputs[4].y)  / D06_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_06 = res_06 + 10
else:
    if inputs[4].y != 0:
        res_06 = res_06 + ( ( float(D06_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D06_inputs[4].y == 0:
            res_06 = res_06 + 10
# if D06_x >= inputs_x :
#     per06_x = ( inputs_x * 50 ) / D06_x
# else:
#     per06_x = ( D06_x * 50 ) / inputs_x
# if per06_x > 50 :
#     per06_x = 50
# if D06_y >= inputs_y :
#     per06_y = ( inputs_y * 50 ) / D06_y
# else:
#     per06_y = ( D06_y * 50 ) / inputs_y
# if per06_y > 50 :
#     per06_y = 50
# per06 = per06_x + per06_y
print "[ 06 ] Blast node and neck : "+str(res_06) + " %"
map['[ 06 ] Blast node and neck : '] = res_06

D07_x = 0
D07_y = 0
for i in D07_inputs:
    D07_x = D07_x + int(i.x)
    D07_y = D07_y + int(i.y)
print "07"
res_07 = 0
if D07_inputs[0].x > inputs[0].x:
    if D07_inputs[0].x != 0:
        res_07 = res_07 + ( ( float(inputs[0].x)  / D07_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_07 = res_07 + 10
else:
    if inputs[0].x != 0:
        res_07 = res_07 + ( ( float(D07_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D07_inputs[0].x == 0:
            res_07 = res_07 + 10
if D07_inputs[1].x > inputs[1].x:
    if D07_inputs[1].x != 0:
        res_07 = res_07 + ( ( float(inputs[1].x)  / D07_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_07 = res_07 + 10
else:
    if inputs[1].x != 0:
        res_07 = res_07 + ( ( float(D07_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D07_inputs[1].x == 0:
            res_07 = res_07 + 10
if D07_inputs[2].x > inputs[2].x:
    if D07_inputs[2].x != 0:
        res_07 = res_07 + ( ( float(inputs[2].x)  / D07_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_07 = res_07 + 10
else:
    if inputs[2].x != 0:
        res_07 = res_07 + ( ( float(D07_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D07_inputs[2].x == 0:
            res_07 = res_07 + 10
if D07_inputs[3].x > inputs[3].x:
    if D07_inputs[3].x != 0:
        res_07 = res_07 + ( ( float(inputs[3].x)  / D07_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_07 = res_07 + 10
else:
    if inputs[3].x != 0:
        res_07 = res_07 + ( ( float(D07_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D07_inputs[3].x == 0:
            res_07 = res_07 + 10
if D07_inputs[4].x > inputs[4].x:
    if D07_inputs[4].x != 0:
        res_07 = res_07 + ( ( float(inputs[4].x)  / D07_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_07 = res_07 + 10
else:
    if inputs[4].x != 0:
        res_07 = res_07 + ( ( float(D07_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D07_inputs[4].x == 0:
            res_07 = res_07 + 10
if D07_inputs[0].y > inputs[0].y:
    if D07_inputs[0].y != 0:
        res_07 = res_07 + ( ( float(inputs[0].y)  / D07_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_07 = res_07 + 10
else:
    if inputs[0].y != 0:
        res_07 = res_07 + ( ( float(D07_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D07_inputs[0].y == 0:
            res_07 = res_07 + 10
if D07_inputs[1].y > inputs[1].y:
    if D07_inputs[1].y != 0:
        res_07 = res_07 + ( ( float(inputs[1].y)  / D07_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_07 = res_07 + 10
else:
    if inputs[1].y != 0:
        res_07 = res_07 + ( ( float(D07_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D07_inputs[1].y == 0:
            res_07 = res_07 + 10
if D07_inputs[2].y > inputs[2].y:
    if D07_inputs[2].y != 0:
        res_07 = res_07 + ( ( float(inputs[2].y)  / D07_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_07 = res_07 + 10
else:
    if inputs[2].y != 0:
        res_07 = res_07 + ( ( float(D07_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D07_inputs[2].y == 0:
            res_07 = res_07 + 10
if D07_inputs[3].y > inputs[3].y:
    if D07_inputs[3].y != 0:
        res_07 = res_07 + ( ( float(inputs[3].y)  / D07_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_07 = res_07 + 10
else:
    if inputs[3].y != 0:
        res_07 = res_07 + ( ( float(D07_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D07_inputs[3].y == 0:
            res_07 = res_07 + 10
if D07_inputs[4].y > inputs[4].y:
    if D07_inputs[4].y != 0:
        res_07 = res_07 + ( ( float(inputs[4].y)  / D07_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_07 = res_07 + 10
else:
    if inputs[4].y != 0:
        res_07 = res_07 + ( ( float(D07_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D07_inputs[4].y == 0:
            res_07 = res_07 + 10
# if D07_x >= inputs_x :
#     per07_x = ( inputs_x * 50 ) / D07_x
# else:
#     per07_x = ( D07_x * 50 ) / inputs_x
# if per07_x > 50 :
#     per07_x = 50
# if D07_y >= inputs_y :
#     per07_y = ( inputs_y * 50 ) / D07_y
# else:
#     per07_y = ( D07_y * 50 ) / inputs_y
# if per07_y > 50 :
#     per07_y = 50
# per07 = per07_x + per07_y
print "[ 07 ] Brown spot : "+str(res_07) + " %"
map['[ 07 ] Brown spot : '] = res_07

D08_x = 0
D08_y = 0
for i in D08_inputs:
    D08_x = D08_x + int(i.x)
    D08_y = D08_y + int(i.y)
print "08"
res_08 = 0
if D08_inputs[0].x > inputs[0].x:
    if D08_inputs[0].x != 0:
        res_08 = res_08 + ( ( float(inputs[0].x)  / D08_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_08 = res_08 + 10
else:
    if inputs[0].x != 0:
        res_08 = res_08 + ( ( float(D08_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D08_inputs[0].x == 0:
            res_08 = res_08 + 10
if D08_inputs[1].x > inputs[1].x:
    if D08_inputs[1].x != 0:
        res_08 = res_08 + ( ( float(inputs[1].x)  / D08_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_08 = res_08 + 10
else:
    if inputs[1].x != 0:
        res_08 = res_08 + ( ( float(D08_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D08_inputs[1].x == 0:
            res_08 = res_08 + 10
if D08_inputs[2].x > inputs[2].x:
    if D08_inputs[2].x != 0:
        res_08 = res_08 + ( ( float(inputs[2].x)  / D08_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_08 = res_08 + 10
else:
    if inputs[2].x != 0:
        res_08 = res_08 + ( ( float(D08_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D08_inputs[2].x == 0:
            res_08 = res_08 + 10
if D08_inputs[3].x > inputs[3].x:
    if D08_inputs[3].x != 0:
        res_08 = res_08 + ( ( float(inputs[3].x)  / D08_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_08 = res_08 + 10
else:
    if inputs[3].x != 0:
        res_08 = res_08 + ( ( float(D08_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D08_inputs[3].x == 0:
            res_08 = res_08 + 10
if D08_inputs[4].x > inputs[4].x:
    if D08_inputs[4].x != 0:
        res_08 = res_08 + ( ( float(inputs[4].x)  / D08_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_08 = res_08 + 10
else:
    if inputs[4].x != 0:
        res_08 = res_08 + ( ( float(D08_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D08_inputs[4].x == 0:
            res_08 = res_08 + 10
if D08_inputs[0].y > inputs[0].y:
    if D08_inputs[0].y != 0:
        res_08 = res_08 + ( ( float(inputs[0].y)  / D08_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_08 = res_08 + 10
else:
    if inputs[0].y != 0:
        res_08 = res_08 + ( ( float(D08_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D08_inputs[0].y == 0:
            res_08 = res_08 + 10
if D08_inputs[1].y > inputs[1].y:
    if D08_inputs[1].y != 0:
        res_08 = res_08 + ( ( float(inputs[1].y)  / D08_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_08 = res_08 + 10
else:
    if inputs[1].y != 0:
        res_08 = res_08 + ( ( float(D08_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D08_inputs[1].y == 0:
            res_08 = res_08 + 10
if D08_inputs[2].y > inputs[2].y:
    if D08_inputs[2].y != 0:
        res_08 = res_08 + ( ( float(inputs[2].y)  / D08_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_08 = res_08 + 10
else:
    if inputs[2].y != 0:
        res_08 = res_08 + ( ( float(D08_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D08_inputs[2].y == 0:
            res_08 = res_08 + 10
if D08_inputs[3].y > inputs[3].y:
    if D08_inputs[3].y != 0:
        res_08 = res_08 + ( ( float(inputs[3].y)  / D08_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_08 = res_08 + 10
else:
    if inputs[3].y != 0:
        res_08 = res_08 + ( ( float(D08_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D08_inputs[3].y == 0:
            res_08 = res_08 + 10
if D08_inputs[4].y > inputs[4].y:
    if D08_inputs[4].y != 0:
        res_08 = res_08 + ( ( float(inputs[4].y)  / D08_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_08 = res_08 + 10
else:
    if inputs[4].y != 0:
        res_08 = res_08 + ( ( float(D08_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D08_inputs[4].y == 0:
            res_08 = res_08 + 10
# if D08_x >= inputs_x :
#     per08_x = ( inputs_x * 50 ) / D08_x
# else:
#     per08_x = ( D08_x * 50 ) / inputs_x
# if per08_x > 50 :
#     per08_x = 50
# if D08_y >= inputs_y :
#     per08_y = ( inputs_y * 50 ) / D08_y
# else:
#     per08_y = ( D08_y * 50 ) / inputs_y
# if per08_y > 50 :
#     per08_y = 50
# per08 = per08_x + per08_y
print "[ 08 ] False smut : "+str(res_08) + " %"
map['[ 08 ] False smut : '] = res_08

D09_x = 0
D09_y = 0
for i in D09_inputs:
    D09_x = D09_x + int(i.x)
    D09_y = D09_y + int(i.y)
print "09"
res_09 = 0
if D09_inputs[0].x > inputs[0].x:
    if D09_inputs[0].x != 0:
        res_09 = res_09 + ( ( float(inputs[0].x)  / D09_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_09 = res_09 + 10
else:
    if inputs[0].x != 0:
        res_09 = res_09 + ( ( float(D09_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D09_inputs[0].x == 0:
            res_09 = res_09 + 10
if D09_inputs[1].x > inputs[1].x:
    if D09_inputs[1].x != 0:
        res_09 = res_09 + ( ( float(inputs[1].x)  / D09_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_09 = res_09 + 10
else:
    if inputs[1].x != 0:
        res_09 = res_09 + ( ( float(D09_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D09_inputs[1].x == 0:
            res_09 = res_09 + 10
if D09_inputs[2].x > inputs[2].x:
    if D09_inputs[2].x != 0:
        res_09 = res_09 + ( ( float(inputs[2].x)  / D09_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_09 = res_09 + 10
else:
    if inputs[2].x != 0:
        res_09 = res_09 + ( ( float(D09_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D09_inputs[2].x == 0:
            res_09 = res_09 + 10
if D09_inputs[3].x > inputs[3].x:
    if D09_inputs[3].x != 0:
        res_09 = res_09 + ( ( float(inputs[3].x)  / D09_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_09 = res_09 + 10
else:
    if inputs[3].x != 0:
        res_09 = res_09 + ( ( float(D09_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D09_inputs[3].x == 0:
            res_09 = res_09 + 10
if D09_inputs[4].x > inputs[4].x:
    if D09_inputs[4].x != 0:
        res_09 = res_09 + ( ( float(inputs[4].x)  / D09_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_09 = res_09 + 10
else:
    if inputs[4].x != 0:
        res_09 = res_09 + ( ( float(D09_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D09_inputs[4].x == 0:
            res_09 = res_09 + 10
if D09_inputs[0].y > inputs[0].y:
    if D09_inputs[0].y != 0:
        res_09 = res_09 + ( ( float(inputs[0].y)  / D09_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_09 = res_09 + 10
else:
    if inputs[0].y != 0:
        res_09 = res_09 + ( ( float(D09_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D09_inputs[0].y == 0:
            res_09 = res_09 + 10
if D09_inputs[1].y > inputs[1].y:
    if D09_inputs[1].y != 0:
        res_09 = res_09 + ( ( float(inputs[1].y)  / D09_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_09 = res_09 + 10
else:
    if inputs[1].y != 0:
        res_09 = res_09 + ( ( float(D09_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D09_inputs[1].y == 0:
            res_09 = res_09 + 10
if D09_inputs[2].y > inputs[2].y:
    if D09_inputs[2].y != 0:
        res_09 = res_09 + ( ( float(inputs[2].y)  / D09_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_09 = res_09 + 10
else:
    if inputs[2].y != 0:
        res_09 = res_09 + ( ( float(D09_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D09_inputs[2].y == 0:
            res_09 = res_09 + 10
if D09_inputs[3].y > inputs[3].y:
    if D09_inputs[3].y != 0:
        res_09 = res_09 + ( ( float(inputs[3].y)  / D09_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_09 = res_09 + 10
else:
    if inputs[3].y != 0:
        res_09 = res_09 + ( ( float(D09_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D09_inputs[3].y == 0:
            res_09 = res_09 + 10
if D09_inputs[4].y > inputs[4].y:
    if D09_inputs[4].y != 0:
        res_09 = res_09 + ( ( float(inputs[4].y)  / D09_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_09 = res_09 + 10
else:
    if inputs[4].y != 0:
        res_09 = res_09 + ( ( float(D09_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D09_inputs[4].y == 0:
            res_09 = res_09 + 10
# if D09_x >= inputs_x :
#     per09_x = ( inputs_x * 50 ) / D09_x
# else:
#     per09_x = ( D09_x * 50 ) / inputs_x
# if per09_x > 50 :
#     per09_x = 50
# if D09_y >= inputs_y :
#     per09_y = ( inputs_y * 50 ) / D09_y
# else:
#     per09_y = ( D09_y * 50 ) / inputs_y
# if per09_y > 50 :
#     per09_y = 50
# per09 = per09_x + per09_y
print "[ 09 ] Leaf scald : "+str(res_09) + " %"
map['[ 09 ] Leaf scald : '] = res_09

D10_x = 0
D10_y = 0
for i in D10_inputs:
    D10_x = D10_x + int(i.x)
    D10_y = D10_y + int(i.y)
print "10"
res_10 = 0
# print D10_inputs[0].x
if D10_inputs[0].x > inputs[0].x:
    if D10_inputs[0].x != 0:
        res_10 = res_10 + ( ( float(inputs[0].x)  / D10_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_10 = res_10 + 10
else:
    if inputs[0].x != 0:
        res_10 = res_10 + ( ( float(D10_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D10_inputs[0].x == 0:
            res_10 = res_10 + 10
if D10_inputs[1].x > inputs[1].x:
    if D10_inputs[1].x != 0:
        res_10 = res_10 + ( ( float(inputs[1].x)  / D10_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_10 = res_10 + 10
else:
    if inputs[1].x != 0:
        res_10 = res_10 + ( ( float(D10_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D10_inputs[1].x == 0:
            res_10 = res_10 + 10
if D10_inputs[2].x > inputs[2].x:
    if D10_inputs[2].x != 0:
        res_10 = res_10 + ( ( float(inputs[2].x)  / D10_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_10 = res_10 + 10
else:
    if inputs[2].x != 0:
        res_10 = res_10 + ( ( float(D10_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D10_inputs[2].x == 0:
            res_10 = res_10 + 10
if D10_inputs[3].x > inputs[3].x:
    if D10_inputs[3].x != 0:
        res_10 = res_10 + ( ( float(inputs[3].x)  / D10_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_10 = res_10 + 10
else:
    if inputs[3].x != 0:
        res_10 = res_10 + ( ( float(D10_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D10_inputs[3].x == 0:
            res_10 = res_10 + 10
if D10_inputs[4].x > inputs[4].x:
    if D10_inputs[4].x != 0:
        res_10 = res_10 + ( ( float(inputs[4].x)  / D10_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_10 = res_10 + 10
else:
    if inputs[4].x != 0:
        res_10 = res_10 + ( ( float(D10_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D10_inputs[4].x == 0:
            res_10 = res_10 + 10
if D10_inputs[0].y > inputs[0].y:
    if D10_inputs[0].y != 0:
        res_10 = res_10 + ( ( float(inputs[0].y)  / D10_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_10 = res_10 + 10
else:
    if inputs[0].y != 0:
        res_10 = res_10 + ( ( float(D10_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D10_inputs[0].y == 0:
            res_10 = res_10 + 10
if D10_inputs[1].y > inputs[1].y:
    if D10_inputs[1].y != 0:
        res_10 = res_10 + ( ( float(inputs[1].y)  / D10_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_10 = res_10 + 10
else:
    if inputs[1].y != 0:
        res_10 = res_10 + ( ( float(D10_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D10_inputs[1].y == 0:
            res_10 = res_10 + 10
if D10_inputs[2].y > inputs[2].y:
    if D10_inputs[2].y != 0:
        res_10 = res_10 + ( ( float(inputs[2].y)  / D10_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_10 = res_10 + 10
else:
    if inputs[2].y != 0:
        res_10 = res_10 + ( ( float(D10_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D10_inputs[2].y == 0:
            res_10 = res_10 + 10
if D10_inputs[3].y > inputs[3].y:
    if D10_inputs[3].y != 0:
        res_10 = res_10 + ( ( float(inputs[3].y)  / D10_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_10 = res_10 + 10
else:
    if inputs[3].y != 0:
        res_10 = res_10 + ( ( float(D10_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D10_inputs[3].y == 0:
            res_10 = res_10 + 10
if D10_inputs[4].y > inputs[4].y:
    if D10_inputs[4].y != 0:
        res_10 = res_10 + ( ( float(inputs[4].y)  / D10_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_10 = res_10 + 10
else:
    if inputs[4].y != 0:
        res_10 = res_10 + ( ( float(D10_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D10_inputs[4].y == 0:
            res_10 = res_10 + 10
# if D10_x >= inputs_x :
#     per10_x = ( inputs_x * 50 ) / D10_x
# else:
#     per10_x = ( D10_x * 50 ) / inputs_x
# if per10_x > 50 :
#     per10_x = 50
# if D10_y >= inputs_y :
#     per10_y = ( inputs_y * 50 ) / D10_y
# else:
#     per10_y = ( D10_y * 50 ) / inputs_y
# if per10_y > 50 :
#     per10_y = 50
# per10 = per10_x + per10_y
print "[ 10 ] Narrow brown spot : "+str(res_10) + " %"
map['[ 10 ] Narrow brown spot : '] = res_10

D11_x = 0
D11_y = 0
for i in D11_inputs:
    D11_x = D11_x + int(i.x)
    D11_y = D11_y + int(i.y)
print "11"
res_11 = 0
if D11_inputs[0].x > inputs[0].x:
    if D11_inputs[0].x != 0:
        res_11 = res_11 + ( ( float(inputs[0].x)  / D11_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_11 = res_11 + 10
else:
    if inputs[0].x != 0:
        res_11 = res_11 + ( ( float(D11_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D11_inputs[0].x == 0:
            res_11 = res_11 + 10
if D11_inputs[1].x > inputs[1].x:
    if D11_inputs[1].x != 0:
        res_11 = res_11 + ( ( float(inputs[1].x)  / D11_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_11 = res_11 + 10
else:
    if inputs[1].x != 0:
        res_11 = res_11 + ( ( float(D11_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D11_inputs[1].x == 0:
            res_11 = res_11 + 10
if D11_inputs[2].x > inputs[2].x:
    if D11_inputs[2].x != 0:
        res_11 = res_11 + ( ( float(inputs[2].x)  / D11_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_11 = res_11 + 10
else:
    if inputs[2].x != 0:
        res_11 = res_11 + ( ( float(D11_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D11_inputs[2].x == 0:
            res_11 = res_11 + 10
if D11_inputs[3].x > inputs[3].x:
    if D11_inputs[3].x != 0:
        res_11 = res_11 + ( ( float(inputs[3].x)  / D11_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_11 = res_11 + 10
else:
    if inputs[3].x != 0:
        res_11 = res_11 + ( ( float(D11_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D11_inputs[3].x == 0:
            res_11 = res_11 + 10
if D11_inputs[4].x > inputs[4].x:
    if D11_inputs[4].x != 0:
        res_11 = res_11 + ( ( float(inputs[4].x)  / D11_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_11 = res_11 + 10
else:
    if inputs[4].x != 0:
        res_11 = res_11 + ( ( float(D11_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D11_inputs[4].x == 0:
            res_11 = res_11 + 10
if D11_inputs[0].y > inputs[0].y:
    if D11_inputs[0].y != 0:
        res_11 = res_11 + ( ( float(inputs[0].y)  / D11_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_11 = res_11 + 10
else:
    if inputs[0].y != 0:
        res_11 = res_11 + ( ( float(D11_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D11_inputs[0].y == 0:
            res_11 = res_11 + 10
if D11_inputs[1].y > inputs[1].y:
    if D11_inputs[1].y != 0:
        res_11 = res_11 + ( ( float(inputs[1].y)  / D11_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_11 = res_11 + 10
else:
    if inputs[1].y != 0:
        res_11 = res_11 + ( ( float(D11_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D11_inputs[1].y == 0:
            res_11 = res_11 + 10
if D11_inputs[2].y > inputs[2].y:
    if D11_inputs[2].y != 0:
        res_11 = res_11 + ( ( float(inputs[2].y)  / D11_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_11 = res_11 + 10
else:
    if inputs[2].y != 0:
        res_11 = res_11 + ( ( float(D11_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D11_inputs[2].y == 0:
            res_11 = res_11 + 10
if D11_inputs[3].y > inputs[3].y:
    if D11_inputs[3].y != 0:
        res_11 = res_11 + ( ( float(inputs[3].y)  / D11_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_11 = res_11 + 10
else:
    if inputs[3].y != 0:
        res_11 = res_11 + ( ( float(D11_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D11_inputs[3].y == 0:
            res_11 = res_11 + 10
if D11_inputs[4].y > inputs[4].y:
    if D11_inputs[4].y != 0:
        res_11 = res_11 + ( ( float(inputs[4].y)  / D11_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_11 = res_11 + 10
else:
    if inputs[4].y != 0:
        res_11 = res_11 + ( ( float(D11_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D11_inputs[4].y == 0:
            res_11 = res_11 + 10
# if D11_x >= inputs_x :
#     per11_x = ( inputs_x * 50 ) / D11_x
# else:
#     per11_x = ( D11_x * 50 ) / inputs_x
# if per11_x > 50 :
#     per11_x = 50
# if D11_y >= inputs_y :
#     per11_y = ( inputs_y * 50 ) / D11_y
# else:
#     per11_y = ( D11_y * 50 ) / inputs_y
# if per11_y > 50 :
#     per11_y = 50
# per11 = per11_x + per11_y
print "[ 11 ] Red stripe : "+str(res_11) + " %"
map['[ 11 ] Red stripe : '] = res_11

D12_x = 0
D12_y = 0
for i in D12_inputs:
    D12_x = D12_x + int(i.x)
    D12_y = D12_y + int(i.y)
print "12"
res_12 = 0
if D12_inputs[0].x > inputs[0].x:
    if D12_inputs[0].x != 0:
        res_12 = res_12 + ( ( float(inputs[0].x)  / D12_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_12 = res_12 + 10
else:
    if inputs[0].x != 0:
        res_12 = res_12 + ( ( float(D12_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D12_inputs[0].x == 0:
            res_12 = res_12 + 10
if D12_inputs[1].x > inputs[1].x:
    if D12_inputs[1].x != 0:
        res_12 = res_12 + ( ( float(inputs[1].x)  / D12_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_12 = res_12 + 10
else:
    if inputs[1].x != 0:
        res_12 = res_12 + ( ( float(D12_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D12_inputs[1].x == 0:
            res_12 = res_12 + 10
if D12_inputs[2].x > inputs[2].x:
    if D12_inputs[2].x != 0:
        res_12 = res_12 + ( ( float(inputs[2].x)  / D12_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_12 = res_12 + 10
else:
    if inputs[2].x != 0:
        res_12 = res_12 + ( ( float(D12_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D12_inputs[2].x == 0:
            res_12 = res_12 + 10
if D12_inputs[3].x > inputs[3].x:
    if D12_inputs[3].x != 0:
        res_12 = res_12 + ( ( float(inputs[3].x)  / D12_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_12 = res_12 + 10
else:
    if inputs[3].x != 0:
        res_12 = res_12 + ( ( float(D12_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D12_inputs[3].x == 0:
            res_12 = res_12 + 10
if D12_inputs[4].x > inputs[4].x:
    if D12_inputs[4].x != 0:
        res_12 = res_12 + ( ( float(inputs[4].x)  / D12_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_12 = res_12 + 10
else:
    if inputs[4].x != 0:
        res_12 = res_12 + ( ( float(D12_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D12_inputs[4].x == 0:
            res_12 = res_12 + 10
if D12_inputs[0].y > inputs[0].y:
    if D12_inputs[0].y != 0:
        res_12 = res_12 + ( ( float(inputs[0].y)  / D12_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_12 = res_12 + 10
else:
    if inputs[0].y != 0:
        res_12 = res_12 + ( ( float(D12_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D12_inputs[0].y == 0:
            res_12 = res_12 + 10
if D12_inputs[1].y > inputs[1].y:
    if D12_inputs[1].y != 0:
        res_12 = res_12 + ( ( float(inputs[1].y)  / D12_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_12 = res_12 + 10
else:
    if inputs[1].y != 0:
        res_12 = res_12 + ( ( float(D12_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D12_inputs[1].y == 0:
            res_12 = res_12 + 10
if D12_inputs[2].y > inputs[2].y:
    if D12_inputs[2].y != 0:
        res_12 = res_12 + ( ( float(inputs[2].y)  / D12_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_12 = res_12 + 10
else:
    if inputs[2].y != 0:
        res_12 = res_12 + ( ( float(D12_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D12_inputs[2].y == 0:
            res_12 = res_12 + 10
if D12_inputs[3].y > inputs[3].y:
    if D12_inputs[3].y != 0:
        res_12 = res_12 + ( ( float(inputs[3].y)  / D12_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_12 = res_12 + 10
else:
    if inputs[3].y != 0:
        res_12 = res_12 + ( ( float(D12_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D12_inputs[3].y == 0:
            res_12 = res_12 + 10
if D12_inputs[4].y > inputs[4].y:
    if D12_inputs[4].y != 0:
        res_12 = res_12 + ( ( float(inputs[4].y)  / D12_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_12 = res_12 + 10
else:
    if inputs[4].y != 0:
        res_12 = res_12 + ( ( float(D12_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D12_inputs[4].y == 0:
            res_12 = res_12 + 10
# if D12_x >= inputs_x :
#     per12_x = ( inputs_x * 50 ) / D12_x
# else:
#     per12_x = ( D12_x * 50 ) / inputs_x
# if per12_x > 50 :
#     per12_x = 50
# if D12_y >= inputs_y :
#     per12_y = ( inputs_y * 50 ) / D12_y
# else:
#     per12_y = ( D12_y * 50 ) / inputs_y
# if per12_y > 50 :
#     per12_y = 50
# per12 = per12_x + per12_y
print "[ 12 ] Rice grassy stunt : "+str(res_12) + " %"
map['[ 12 ] Rice grassy stunt : '] = res_12

D13_x = 0
D13_y = 0
for i in D13_inputs:
    D13_x = D13_x + int(i.x)
    D13_y = D13_y + int(i.y)
print "13"
res_13 = 0
if D13_inputs[0].x > inputs[0].x:
    if D13_inputs[0].x != 0:
        res_13 = res_13 + ( ( float(inputs[0].x)  / D13_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_13 = res_13 + 10
else:
    if inputs[0].x != 0:
        res_13 = res_13 + ( ( float(D13_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D13_inputs[0].x == 0:
            res_13 = res_13 + 10
if D13_inputs[1].x > inputs[1].x:
    if D13_inputs[1].x != 0:
        res_13 = res_13 + ( ( float(inputs[1].x)  / D13_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_13 = res_13 + 10
else:
    if inputs[1].x != 0:
        res_13 = res_13 + ( ( float(D13_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D13_inputs[1].x == 0:
            res_13 = res_13 + 10
if D13_inputs[2].x > inputs[2].x:
    if D13_inputs[2].x != 0:
        res_13 = res_13 + ( ( float(inputs[2].x)  / D13_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_13 = res_13 + 10
else:
    if inputs[2].x != 0:
        res_13 = res_13 + ( ( float(D13_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D13_inputs[2].x == 0:
            res_13 = res_13 + 10
if D13_inputs[3].x > inputs[3].x:
    if D13_inputs[3].x != 0:
        res_13 = res_13 + ( ( float(inputs[3].x)  / D13_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_13 = res_13 + 10
else:
    if inputs[3].x != 0:
        res_13 = res_13 + ( ( float(D13_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D13_inputs[3].x == 0:
            res_13 = res_13 + 10
if D13_inputs[4].x > inputs[4].x:
    if D13_inputs[4].x != 0:
        res_13 = res_13 + ( ( float(inputs[4].x)  / D13_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_13 = res_13 + 10
else:
    if inputs[4].x != 0:
        res_13 = res_13 + ( ( float(D13_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D13_inputs[4].x == 0:
            res_13 = res_13 + 10
if D13_inputs[0].y > inputs[0].y:
    if D13_inputs[0].y != 0:
        res_13 = res_13 + ( ( float(inputs[0].y)  / D13_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_13 = res_13 + 10
else:
    if inputs[0].y != 0:
        res_13 = res_13 + ( ( float(D13_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D13_inputs[0].y == 0:
            res_13 = res_13 + 10
if D13_inputs[1].y > inputs[1].y:
    if D13_inputs[1].y != 0:
        res_13 = res_13 + ( ( float(inputs[1].y)  / D13_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_13 = res_13 + 10
else:
    if inputs[1].y != 0:
        res_13 = res_13 + ( ( float(D13_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D13_inputs[1].y == 0:
            res_13 = res_13 + 10
if D13_inputs[2].y > inputs[2].y:
    if D13_inputs[2].y != 0:
        res_13 = res_13 + ( ( float(inputs[2].y)  / D13_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_13 = res_13 + 10
else:
    if inputs[2].y != 0:
        res_13 = res_13 + ( ( float(D13_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D13_inputs[2].y == 0:
            res_13 = res_13 + 10
if D13_inputs[3].y > inputs[3].y:
    if D13_inputs[3].y != 0:
        res_13 = res_13 + ( ( float(inputs[3].y)  / D13_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_13 = res_13 + 10
else:
    if inputs[3].y != 0:
        res_13 = res_13 + ( ( float(D13_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D13_inputs[3].y == 0:
            res_13 = res_13 + 10
if D13_inputs[4].y > inputs[4].y:
    if D13_inputs[4].y != 0:
        res_13 = res_13 + ( ( float(inputs[4].y)  / D13_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_13 = res_13 + 10
else:
    if inputs[4].y != 0:
        res_13 = res_13 + ( ( float(D13_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D13_inputs[4].y == 0:
            res_13 = res_13 + 10
# if D13_x >= inputs_x :
#     per13_x = ( inputs_x * 50 ) / D13_x
# else:
#     per13_x = ( D13_x * 50 ) / inputs_x
# if per13_x > 50 :
#     per13_x = 50
# if D13_y >= inputs_y :
#     per13_y = ( inputs_y * 50 ) / D13_y
# else:
#     per13_y = ( D13_y * 50 ) / inputs_y
# if per13_y > 50 :
#     per13_y = 50
# per13 = per13_x + per13_y
print "[ 13 ] Rice ragged stunt : "+str(res_13) + " %"
map['[ 13 ] Rice ragged stunt : '] = res_13

D14_x = 0
D14_y = 0
for i in D14_inputs:
    D14_x = D14_x + int(i.x)
    D14_y = D14_y + int(i.y)
print "14"
res_14 = 0
if D14_inputs[0].x > inputs[0].x:
    if D14_inputs[0].x != 0:
        res_14 = res_14 + ( ( float(inputs[0].x)  / D14_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_14 = res_14 + 10
else:
    if inputs[0].x != 0:
        res_14 = res_14 + ( ( float(D14_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D14_inputs[0].x == 0:
            res_14 = res_14 + 10
if D14_inputs[1].x > inputs[1].x:
    if D14_inputs[1].x != 0:
        res_14 = res_14 + ( ( float(inputs[1].x)  / D14_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_14 = res_14 + 10
else:
    if inputs[1].x != 0:
        res_14 = res_14 + ( ( float(D14_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D14_inputs[1].x == 0:
            res_14 = res_14 + 10
if D14_inputs[2].x > inputs[2].x:
    if D14_inputs[2].x != 0:
        res_14 = res_14 + ( ( float(inputs[2].x)  / D14_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_14 = res_14 + 10
else:
    if inputs[2].x != 0:
        res_14 = res_14 + ( ( float(D14_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D14_inputs[2].x == 0:
            res_14 = res_14 + 10
if D14_inputs[3].x > inputs[3].x:
    if D14_inputs[3].x != 0:
        res_14 = res_14 + ( ( float(inputs[3].x)  / D14_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_14 = res_14 + 10
else:
    if inputs[3].x != 0:
        res_14 = res_14 + ( ( float(D14_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D14_inputs[3].x == 0:
            res_14 = res_14 + 10
if D14_inputs[4].x > inputs[4].x:
    if D14_inputs[4].x != 0:
        res_14 = res_14 + ( ( float(inputs[4].x)  / D14_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_14 = res_14 + 10
else:
    if inputs[4].x != 0:
        res_14 = res_14 + ( ( float(D14_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D14_inputs[4].x == 0:
            res_14 = res_14 + 10
if D14_inputs[0].y > inputs[0].y:
    if D14_inputs[0].y != 0:
        res_14 = res_14 + ( ( float(inputs[0].y)  / D14_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_14 = res_14 + 10
else:
    if inputs[0].y != 0:
        res_14 = res_14 + ( ( float(D14_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D14_inputs[0].y == 0:
            res_14 = res_14 + 10
if D14_inputs[1].y > inputs[1].y:
    if D14_inputs[1].y != 0:
        res_14 = res_14 + ( ( float(inputs[1].y)  / D14_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_14 = res_14 + 10
else:
    if inputs[1].y != 0:
        res_14 = res_14 + ( ( float(D14_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D14_inputs[1].y == 0:
            res_14 = res_14 + 10
if D14_inputs[2].y > inputs[2].y:
    if D14_inputs[2].y != 0:
        res_14 = res_14 + ( ( float(inputs[2].y)  / D14_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_14 = res_14 + 10
else:
    if inputs[2].y != 0:
        res_14 = res_14 + ( ( float(D14_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D14_inputs[2].y == 0:
            res_14 = res_14 + 10
if D14_inputs[3].y > inputs[3].y:
    if D14_inputs[3].y != 0:
        res_14 = res_14 + ( ( float(inputs[3].y)  / D14_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_14 = res_14 + 10
else:
    if inputs[3].y != 0:
        res_14 = res_14 + ( ( float(D14_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D14_inputs[3].y == 0:
            res_14 = res_14 + 10
if D14_inputs[4].y > inputs[4].y:
    if D14_inputs[4].y != 0:
        res_14 = res_14 + ( ( float(inputs[4].y)  / D14_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_14 = res_14 + 10
else:
    if inputs[4].y != 0:
        res_14 = res_14 + ( ( float(D14_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D14_inputs[4].y == 0:
            res_14 = res_14 + 10
# if D14_x >= inputs_x :
#     per14_x = ( inputs_x * 50 ) / D14_x
# else:
#     per14_x = ( D14_x * 50 ) / inputs_x
# if per14_x > 50 :
#     per14_x = 50
# if D14_y >= inputs_y :
#     per14_y = ( inputs_y * 50 ) / D14_y
# else:
#     per14_y = ( D14_y * 50 ) / inputs_y
# if per14_y > 50 :
#     per14_y = 50
# per14 = per14_x + per14_y
print "[ 14 ] Rice stripe virus disease : "+str(res_14) + " %"
map['[ 14 ] Rice stripe virus disease : '] = res_14

D15_x = 0
D15_y = 0
for i in D15_inputs:
    D15_x = D15_x + int(i.x)
    D15_y = D15_y + int(i.y)
print "15"
res_15 = 0
if D15_inputs[0].x > inputs[0].x:
    if D15_inputs[0].x != 0:
        res_15 = res_15 + ( ( float(inputs[0].x)  / D15_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_15 = res_15 + 10
else:
    if inputs[0].x != 0:
        res_15 = res_15 + ( ( float(D15_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D15_inputs[0].x == 0:
            res_15 = res_15 + 10
if D15_inputs[1].x > inputs[1].x:
    if D15_inputs[1].x != 0:
        res_15 = res_15 + ( ( float(inputs[1].x)  / D15_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_15 = res_15 + 10
else:
    if inputs[1].x != 0:
        res_15 = res_15 + ( ( float(D15_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D15_inputs[1].x == 0:
            res_15 = res_15 + 10
if D15_inputs[2].x > inputs[2].x:
    if D15_inputs[2].x != 0:
        res_15 = res_15 + ( ( float(inputs[2].x)  / D15_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_15 = res_15 + 10
else:
    if inputs[2].x != 0:
        res_15 = res_15 + ( ( float(D15_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D15_inputs[2].x == 0:
            res_15 = res_15 + 10
if D15_inputs[3].x > inputs[3].x:
    if D15_inputs[3].x != 0:
        res_15 = res_15 + ( ( float(inputs[3].x)  / D15_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_15 = res_15 + 10
else:
    if inputs[3].x != 0:
        res_15 = res_15 + ( ( float(D15_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D15_inputs[3].x == 0:
            res_15 = res_15 + 10
if D15_inputs[4].x > inputs[4].x:
    if D15_inputs[4].x != 0:
        res_15 = res_15 + ( ( float(inputs[4].x)  / D15_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_15 = res_15 + 10
else:
    if inputs[4].x != 0:
        res_15 = res_15 + ( ( float(D15_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D15_inputs[4].x == 0:
            res_15 = res_15 + 10
if D15_inputs[0].y > inputs[0].y:
    if D15_inputs[0].y != 0:
        res_15 = res_15 + ( ( float(inputs[0].y)  / D15_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_15 = res_15 + 10
else:
    if inputs[0].y != 0:
        res_15 = res_15 + ( ( float(D15_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D15_inputs[0].y == 0:
            res_15 = res_15 + 10
if D15_inputs[1].y > inputs[1].y:
    if D15_inputs[1].y != 0:
        res_15 = res_15 + ( ( float(inputs[1].y)  / D15_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_15 = res_15 + 10
else:
    if inputs[1].y != 0:
        res_15 = res_15 + ( ( float(D15_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D15_inputs[1].y == 0:
            res_15 = res_15 + 10
if D15_inputs[2].y > inputs[2].y:
    if D15_inputs[2].y != 0:
        res_15 = res_15 + ( ( float(inputs[2].y)  / D15_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_15 = res_15 + 10
else:
    if inputs[2].y != 0:
        res_15 = res_15 + ( ( float(D15_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D15_inputs[2].y == 0:
            res_15 = res_15 + 10
if D15_inputs[3].y > inputs[3].y:
    if D15_inputs[3].y != 0:
        res_15 = res_15 + ( ( float(inputs[3].y)  / D15_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_15 = res_15 + 10
else:
    if inputs[3].y != 0:
        res_15 = res_15 + ( ( float(D15_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D15_inputs[3].y == 0:
            res_15 = res_15 + 10
if D15_inputs[4].y > inputs[4].y:
    if D15_inputs[4].y != 0:
        res_15 = res_15 + ( ( float(inputs[4].y)  / D15_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_15 = res_15 + 10
else:
    if inputs[4].y != 0:
        res_15 = res_15 + ( ( float(D15_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D15_inputs[4].y == 0:
            res_15 = res_15 + 10
# if D15_x >= inputs_x :
#     per15_x = ( inputs_x * 50 ) / D15_x
# else:
#     per15_x = ( D15_x * 50 ) / inputs_x
# if per15_x > 50 :
#     per15_x = 50
# if D15_y >= inputs_y :
#     per15_y = ( inputs_y * 50 ) / D15_y
# else:
#     per15_y = ( D15_y * 50 ) / inputs_y
# if per15_y > 50 :
#     per15_y = 50
# per15 = per15_x + per15_y
print "[ 15 ] Rice yellow mottle virus : "+str(res_15) + " %"
map['[ 15 ] Rice yellow mottle virus : '] = res_15

D16_x = 0
D16_y = 0
for i in D16_inputs:
    D16_x = D16_x + int(i.x)
    D16_y = D16_y + int(i.y)
print "16"
res_16 = 0
if D16_inputs[0].x > inputs[0].x:
    if D16_inputs[0].x != 0:
        res_16 = res_16 + ( ( float(inputs[0].x)  / D16_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_16 = res_16 + 10
else:
    if inputs[0].x != 0:
        res_16 = res_16 + ( ( float(D16_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D16_inputs[0].x == 0:
            res_16 = res_16 + 10
if D16_inputs[1].x > inputs[1].x:
    if D16_inputs[1].x != 0:
        res_16 = res_16 + ( ( float(inputs[1].x)  / D16_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_16 = res_16 + 10
else:
    if inputs[1].x != 0:
        res_16 = res_16 + ( ( float(D16_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D16_inputs[1].x == 0:
            res_16 = res_16 + 10
if D16_inputs[2].x > inputs[2].x:
    if D16_inputs[2].x != 0:
        res_16 = res_16 + ( ( float(inputs[2].x)  / D16_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_16 = res_16 + 10
else:
    if inputs[2].x != 0:
        res_16 = res_16 + ( ( float(D16_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D16_inputs[2].x == 0:
            res_16 = res_16 + 10
if D16_inputs[3].x > inputs[3].x:
    if D16_inputs[3].x != 0:
        res_16 = res_16 + ( ( float(inputs[3].x)  / D16_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_16 = res_16 + 10
else:
    if inputs[3].x != 0:
        res_16 = res_16 + ( ( float(D16_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D16_inputs[3].x == 0:
            res_16 = res_16 + 10
if D16_inputs[4].x > inputs[4].x:
    if D16_inputs[4].x != 0:
        res_16 = res_16 + ( ( float(inputs[4].x)  / D16_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_16 = res_16 + 10
else:
    if inputs[4].x != 0:
        res_16 = res_16 + ( ( float(D16_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D16_inputs[4].x == 0:
            res_16 = res_16 + 10
if D16_inputs[0].y > inputs[0].y:
    if D16_inputs[0].y != 0:
        res_16 = res_16 + ( ( float(inputs[0].y)  / D16_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_16 = res_16 + 10
else:
    if inputs[0].y != 0:
        res_16 = res_16 + ( ( float(D16_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D16_inputs[0].y == 0:
            res_16 = res_16 + 10
if D16_inputs[1].y > inputs[1].y:
    if D16_inputs[1].y != 0:
        res_16 = res_16 + ( ( float(inputs[1].y)  / D16_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_16 = res_16 + 10
else:
    if inputs[1].y != 0:
        res_16 = res_16 + ( ( float(D16_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D16_inputs[1].y == 0:
            res_16 = res_16 + 10
if D16_inputs[2].y > inputs[2].y:
    if D16_inputs[2].y != 0:
        res_16 = res_16 + ( ( float(inputs[2].y)  / D16_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_16 = res_16 + 10
else:
    if inputs[2].y != 0:
        res_16 = res_16 + ( ( float(D16_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D16_inputs[2].y == 0:
            res_16 = res_16 + 10
if D16_inputs[3].y > inputs[3].y:
    if D16_inputs[3].y != 0:
        res_16 = res_16 + ( ( float(inputs[3].y)  / D16_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_16 = res_16 + 10
else:
    if inputs[3].y != 0:
        res_16 = res_16 + ( ( float(D16_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D16_inputs[3].y == 0:
            res_16 = res_16 + 10
if D16_inputs[4].y > inputs[4].y:
    if D16_inputs[4].y != 0:
        res_16 = res_16 + ( ( float(inputs[4].y)  / D16_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_16 = res_16 + 10
else:
    if inputs[4].y != 0:
        res_16 = res_16 + ( ( float(D16_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D16_inputs[4].y == 0:
            res_16 = res_16 + 10
# if D16_x >= inputs_x :
#     per16_x = ( inputs_x * 50 ) / D16_x
# else:
#     per16_x = ( D16_x * 50 ) / inputs_x
# if per16_x > 50 :
#     per16_x = 50
# if D16_y >= inputs_y :
#     per16_y = ( inputs_y * 50 ) / D16_y
# else:
#     per16_y = ( D16_y * 50 ) / inputs_y
# if per16_y > 50 :
#     per16_y = 50
# per16 = per16_x + per16_y
print "[ 16 ] Sheath blight : "+str(res_16) + " %"
map['[ 16 ] Sheath blight : '] = res_16

D17_x = 0
D17_y = 0
for i in D17_inputs:
    D17_x = D17_x + int(i.x)
    D17_y = D17_y + int(i.y)
print "17"
res_17 = 0
if D17_inputs[0].x > inputs[0].x:
    if D17_inputs[0].x != 0:
        res_17 = res_17 + ( ( float(inputs[0].x)  / D17_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_17 = res_17 + 10
else:
    if inputs[0].x != 0:
        res_17 = res_17 + ( ( float(D17_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D17_inputs[0].x == 0:
            res_17 = res_17 + 10
if D17_inputs[1].x > inputs[1].x:
    if D17_inputs[1].x != 0:
        res_17 = res_17 + ( ( float(inputs[1].x)  / D17_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_17 = res_17 + 10
else:
    if inputs[1].x != 0:
        res_17 = res_17 + ( ( float(D17_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D17_inputs[1].x == 0:
            res_17 = res_17 + 10
if D17_inputs[2].x > inputs[2].x:
    if D17_inputs[2].x != 0:
        res_17 = res_17 + ( ( float(inputs[2].x)  / D17_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_17 = res_17 + 10
else:
    if inputs[2].x != 0:
        res_17 = res_17 + ( ( float(D17_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D17_inputs[2].x == 0:
            res_17 = res_17 + 10
if D17_inputs[3].x > inputs[3].x:
    if D17_inputs[3].x != 0:
        res_17 = res_17 + ( ( float(inputs[3].x)  / D17_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_17 = res_17 + 10
else:
    if inputs[3].x != 0:
        res_17 = res_17 + ( ( float(D17_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D17_inputs[3].x == 0:
            res_17 = res_17 + 10
if D17_inputs[4].x > inputs[4].x:
    if D17_inputs[4].x != 0:
        res_17 = res_17 + ( ( float(inputs[4].x)  / D17_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_17 = res_17 + 10
else:
    if inputs[4].x != 0:
        res_17 = res_17 + ( ( float(D17_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D17_inputs[4].x == 0:
            res_17 = res_17 + 10
if D17_inputs[0].y > inputs[0].y:
    if D17_inputs[0].y != 0:
        res_17 = res_17 + ( ( float(inputs[0].y)  / D17_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_17 = res_17 + 10
else:
    if inputs[0].y != 0:
        res_17 = res_17 + ( ( float(D17_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D17_inputs[0].y == 0:
            res_17 = res_17 + 10
if D17_inputs[1].y > inputs[1].y:
    if D17_inputs[1].y != 0:
        res_17 = res_17 + ( ( float(inputs[1].y)  / D17_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_17 = res_17 + 10
else:
    if inputs[1].y != 0:
        res_17 = res_17 + ( ( float(D17_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D17_inputs[1].y == 0:
            res_17 = res_17 + 10
if D17_inputs[2].y > inputs[2].y:
    if D17_inputs[2].y != 0:
        res_17 = res_17 + ( ( float(inputs[2].y)  / D17_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_17 = res_17 + 10
else:
    if inputs[2].y != 0:
        res_17 = res_17 + ( ( float(D17_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D17_inputs[2].y == 0:
            res_17 = res_17 + 10
if D17_inputs[3].y > inputs[3].y:
    if D17_inputs[3].y != 0:
        res_17 = res_17 + ( ( float(inputs[3].y)  / D17_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_17 = res_17 + 10
else:
    if inputs[3].y != 0:
        res_17 = res_17 + ( ( float(D17_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D17_inputs[3].y == 0:
            res_17 = res_17 + 10
if D17_inputs[4].y > inputs[4].y:
    if D17_inputs[4].y != 0:
        res_17 = res_17 + ( ( float(inputs[4].y)  / D17_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_17 = res_17 + 10
else:
    if inputs[4].y != 0:
        res_17 = res_17 + ( ( float(D17_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D17_inputs[4].y == 0:
            res_17 = res_17 + 10
# if D17_x >= inputs_x :
#     per17_x = ( inputs_x * 50 ) / D17_x
# else:
#     per17_x = ( D17_x * 50 ) / inputs_x
# if per17_x > 50 :
#     per17_x = 50
# if D17_y >= inputs_y :
#     per17_y = ( inputs_y * 50 ) / D17_y
# else:
#     per17_y = ( D17_y * 50 ) / inputs_y
# if per17_y > 50 :
#     per17_y = 50
# per17 = per17_x + per17_y
print "[ 17 ] Sheath rot : "+str(res_17) + " %"
map['[ 17 ] Sheath rot : '] = res_17

D18_x = 0
D18_y = 0
for i in D18_inputs:
    D18_x = D18_x + int(i.x)
    D18_y = D18_y + int(i.y)
print "18"
res_18 = 0
if D18_inputs[0].x > inputs[0].x:
    if D18_inputs[0].x != 0:
        res_18 = res_18 + ( ( float(inputs[0].x)  / D18_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_18 = res_18 + 10
else:
    if inputs[0].x != 0:
        res_18 = res_18 + ( ( float(D18_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D18_inputs[0].x == 0:
            res_18 = res_18 + 10
if D18_inputs[1].x > inputs[1].x:
    if D18_inputs[1].x != 0:
        res_18 = res_18 + ( ( float(inputs[1].x)  / D18_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_18 = res_18 + 10
else:
    if inputs[1].x != 0:
        res_18 = res_18 + ( ( float(D18_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D18_inputs[1].x == 0:
            res_18 = res_18 + 10
if D18_inputs[2].x > inputs[2].x:
    if D18_inputs[2].x != 0:
        res_18 = res_18 + ( ( float(inputs[2].x)  / D18_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_18 = res_18 + 10
else:
    if inputs[2].x != 0:
        res_18 = res_18 + ( ( float(D18_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D18_inputs[2].x == 0:
            res_18 = res_18 + 10
if D18_inputs[3].x > inputs[3].x:
    if D18_inputs[3].x != 0:
        res_18 = res_18 + ( ( float(inputs[3].x)  / D18_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_18 = res_18 + 10
else:
    if inputs[3].x != 0:
        res_18 = res_18 + ( ( float(D18_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D18_inputs[3].x == 0:
            res_18 = res_18 + 10
if D18_inputs[4].x > inputs[4].x:
    if D18_inputs[4].x != 0:
        res_18 = res_18 + ( ( float(inputs[4].x)  / D18_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_18 = res_18 + 10
else:
    if inputs[4].x != 0:
        res_18 = res_18 + ( ( float(D18_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D18_inputs[4].x == 0:
            res_18 = res_18 + 10
if D18_inputs[0].y > inputs[0].y:
    if D18_inputs[0].y != 0:
        res_18 = res_18 + ( ( float(inputs[0].y)  / D18_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_18 = res_18 + 10
else:
    if inputs[0].y != 0:
        res_18 = res_18 + ( ( float(D18_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D18_inputs[0].y == 0:
            res_18 = res_18 + 10
if D18_inputs[1].y > inputs[1].y:
    if D18_inputs[1].y != 0:
        res_18 = res_18 + ( ( float(inputs[1].y)  / D18_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_18 = res_18 + 10
else:
    if inputs[1].y != 0:
        res_18 = res_18 + ( ( float(D18_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D18_inputs[1].y == 0:
            res_18 = res_18 + 10
if D18_inputs[2].y > inputs[2].y:
    if D18_inputs[2].y != 0:
        res_18 = res_18 + ( ( float(inputs[2].y)  / D18_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_18 = res_18 + 10
else:
    if inputs[2].y != 0:
        res_18 = res_18 + ( ( float(D18_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D18_inputs[2].y == 0:
            res_18 = res_18 + 10
if D18_inputs[3].y > inputs[3].y:
    if D18_inputs[3].y != 0:
        res_18 = res_18 + ( ( float(inputs[3].y)  / D18_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_18 = res_18 + 10
else:
    if inputs[3].y != 0:
        res_18 = res_18 + ( ( float(D18_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D18_inputs[3].y == 0:
            res_18 = res_18 + 10
if D18_inputs[4].y > inputs[4].y:
    if D18_inputs[4].y != 0:
        res_18 = res_18 + ( ( float(inputs[4].y)  / D18_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_18 = res_18 + 10
else:
    if inputs[4].y != 0:
        res_18 = res_18 + ( ( float(D18_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D18_inputs[4].y == 0:
            res_18 = res_18 + 10
# if D18_x >= inputs_x :
#     per18_x = ( inputs_x * 50 ) / D18_x
# else:
#     per18_x = ( D18_x * 50 ) / inputs_x
# if per18_x > 50 :
#     per18_x = 50
# if D18_y >= inputs_y :
#     per18_y = ( inputs_y * 50 ) / D18_y
# else:
#     per18_y = ( D18_y * 50 ) / inputs_y
# if per18_y > 50 :
#     per18_y = 50
# per18 = per18_x + per18_y
print "[ 18 ] Stem rot : "+str(res_18) + " %"
map['[ 18 ] Stem rot : '] = res_18

D19_x = 0
D19_y = 0
for i in D19_inputs:
    D19_x = D19_x + int(i.x)
    D19_y = D19_y + int(i.y)
print "19"
res_19 = 0
if D19_inputs[0].x > inputs[0].x:
    if D19_inputs[0].x != 0:
        res_19 = res_19 + ( ( float(inputs[0].x)  / D19_inputs[0].x ) * 10 )
    else:
        if inputs[0].x == 0:
            res_19 = res_19 + 10
else:
    if inputs[0].x != 0:
        res_19 = res_19 + ( ( float(D19_inputs[0].x)  / inputs[0].x ) * 10 )
    else:
        if D19_inputs[0].x == 0:
            res_19 = res_19 + 10
if D19_inputs[1].x > inputs[1].x:
    if D19_inputs[1].x != 0:
        res_19 = res_19 + ( ( float(inputs[1].x)  / D19_inputs[1].x ) * 10 )
    else:
        if inputs[1].x == 0:
            res_19 = res_19 + 10
else:
    if inputs[1].x != 0:
        res_19 = res_19 + ( ( float(D19_inputs[1].x)  / inputs[1].x ) * 10 )
    else:
        if D19_inputs[1].x == 0:
            res_19 = res_19 + 10
if D19_inputs[2].x > inputs[2].x:
    if D19_inputs[2].x != 0:
        res_19 = res_19 + ( ( float(inputs[2].x)  / D19_inputs[2].x ) * 10 )
    else:
        if inputs[2].x == 0:
            res_19 = res_19 + 10
else:
    if inputs[2].x != 0:
        res_19 = res_19 + ( ( float(D19_inputs[2].x)  / inputs[2].x ) * 10 )
    else:
        if D19_inputs[2].x == 0:
            res_19 = res_19 + 10
if D19_inputs[3].x > inputs[3].x:
    if D19_inputs[3].x != 0:
        res_19 = res_19 + ( ( float(inputs[3].x)  / D19_inputs[3].x ) * 10 )
    else:
        if inputs[3].x == 0:
            res_19 = res_19 + 10
else:
    if inputs[3].x != 0:
        res_19 = res_19 + ( ( float(D19_inputs[3].x)  / inputs[3].x ) * 10 )
    else:
        if D19_inputs[3].x == 0:
            res_19 = res_19 + 10
if D19_inputs[4].x > inputs[4].x:
    if D19_inputs[4].x != 0:
        res_19 = res_19 + ( ( float(inputs[4].x)  / D19_inputs[4].x ) * 10 )
    else:
        if inputs[4].x == 0:
            res_19 = res_19 + 10
else:
    if inputs[4].x != 0:
        res_19 = res_19 + ( ( float(D19_inputs[4].x)  / inputs[4].x ) * 10 )
    else:
        if D19_inputs[4].x == 0:
            res_19 = res_19 + 10
if D19_inputs[0].y > inputs[0].y:
    if D19_inputs[0].y != 0:
        res_19 = res_19 + ( ( float(inputs[0].y)  / D19_inputs[0].y ) * 10 )
    else:
        if inputs[0].y == 0:
            res_19 = res_19 + 10
else:
    if inputs[0].y != 0:
        res_19 = res_19 + ( ( float(D19_inputs[0].y)  / inputs[0].y ) * 10 )
    else:
        if D19_inputs[0].y == 0:
            res_19 = res_19 + 10
if D19_inputs[1].y > inputs[1].y:
    if D19_inputs[1].y != 0:
        res_19 = res_19 + ( ( float(inputs[1].y)  / D19_inputs[1].y ) * 10 )
    else:
        if inputs[1].y == 0:
            res_19 = res_19 + 10
else:
    if inputs[1].y != 0:
        res_19 = res_19 + ( ( float(D19_inputs[1].y)  / inputs[1].y ) * 10 )
    else:
        if D19_inputs[1].y == 0:
            res_19 = res_19 + 10
if D19_inputs[2].y > inputs[2].y:
    if D19_inputs[2].y != 0:
        res_19 = res_19 + ( ( float(inputs[2].y)  / D19_inputs[2].y ) * 10 )
    else:
        if inputs[2].y == 0:
            res_19 = res_19 + 10
else:
    if inputs[2].y != 0:
        res_19 = res_19 + ( ( float(D19_inputs[2].y)  / inputs[2].y ) * 10 )
    else:
        if D19_inputs[2].y == 0:
            res_19 = res_19 + 10
if D19_inputs[3].y > inputs[3].y:
    if D19_inputs[3].y != 0:
        res_19 = res_19 + ( ( float(inputs[3].y)  / D19_inputs[3].y ) * 10 )
    else:
        if inputs[3].y == 0:
            res_19 = res_19 + 10
else:
    if inputs[3].y != 0:
        res_19 = res_19 + ( ( float(D19_inputs[3].y)  / inputs[3].y ) * 10 )
    else:
        if D19_inputs[3].y == 0:
            res_19 = res_19 + 10
if D19_inputs[4].y > inputs[4].y:
    if D19_inputs[4].y != 0:
        res_19 = res_19 + ( ( float(inputs[4].y)  / D19_inputs[4].y ) * 10 )
    else:
        if inputs[4].y == 0:
            res_19 = res_19 + 10
else:
    if inputs[4].y != 0:
        res_19 = res_19 + ( ( float(D19_inputs[4].y)  / inputs[4].y ) * 10 )
    else:
        if D19_inputs[4].y == 0:
            res_19 = res_19 + 10
# print "PP"+str(res_19)
# if D19_x >= inputs_x :
#     per19_x = ( inputs_x * 50 ) / D19_x
# else:
#     per19_x = ( D19_x * 50 ) / inputs_x
# if per19_x > 50 :
#     per19_x = 50
# if D19_y >= inputs_y :
#     per19_y = ( inputs_y * 50 ) / D19_y
# else:
#     per19_y = ( D19_y * 50 ) / inputs_y
# if per19_y > 50 :
#     per19_y = 50
# per19 = per19_x + per19_y
print "[ 19 ] Tungroc : "+str(res_19) + " %"
map['[ 19 ] Tungroc : ']=res_19

print "================================================"
import operator
print map
print map.keys()
print map.values()
map_x = sorted(map.items(), key=operator.itemgetter(1), reverse=True)

file = open('result.txt', 'r+')
file.seek(0)
file.truncate()

for i in map_x: 
    y = str(i)+''
    file.write(y+"\n")
file.close()

print '====================Result======================='
# print map_x
for i in map_x:
    print i
print "================================================"