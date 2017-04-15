import cv2
import numpy as np
import math
import sys

def blue(hsv):
    blue = cv2.inRange(hsv,np.array((100,100,100)),np.array((120,255,255)))
    return blue

def green(hsv):
    green = cv2.inRange(hsv,np.array((60,100,100)),np.array((80,255,255)))
    return green

def purple(hsv):
    purple = cv2.inRange(hsv,np.array((130,100,100)),np.array((150,255,255)))
    return purple

def red(hsv):
    red = cv2.inRange(hsv,np.array((0,100,100)),np.array((20,255,255)))
    return red

def yellow(hsv):
    yellow = cv2.inRange(hsv,np.array((30,100,100)),np.array((50,255,255)))
    return yellow

path = sys.argv[1]
print "Path",path
c = cv2.imread(path)
height, width, channels = c.shape
print "Frame width : ", width
print "Frame height : ",height

def draw_center(f):
    w_W = int(width/2)
    h_H = int(height/2)
    cv2.circle(f,(w_W,h_H),10,[255,255,255],2)

def write_text(f,x,y):
    x_s = int(x-width/2)
    y_s = int(y-height/2)
    # cv2.putText(f,"x:"+str(x_s)+"y"+str(y_s),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0))

def write_file(cc,f,x,y):
    class Green(object):
        c = str(cc)
        cx = str(x)
        cy = str(y)
    temp = Green()
    greens.append(temp)

Frame_Max_Y = width #ubuntu
Frame_Max_X = height #ubuntu

file = open(sys.argv[2], 'r+')
file.seek(0)
file.truncate()
file.write('Start\n')

while(1):

    f = c
    blur = cv2.medianBlur(f,5)
    hsv = cv2.cvtColor(f,cv2.COLOR_BGR2HSV)
    draw_center(f)

    greens = []
    blues = []
    both_blue = blue(hsv)
    erode_blue = cv2.erode(both_blue,None,iterations = 3)
    dilate_blue = cv2.dilate(erode_blue,None,iterations = 10)
    contours_blue,hierarchy_blue = cv2.findContours(dilate_blue,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours_blue:
        x,y,w,h = cv2.boundingRect(cnt)
        cx,cy = x+w/2, y+h/2
	if 100 < hsv.item(cy,cx,0) < 120:
            cv2.rectangle(f,(x,y),(x+w,y+h),[255,0,0],2)
            print "Blue :"
            print "Center : (", str((x+w)/2) , "," , str((y+h)/2) , ")"
            # file.write("Blue :","\n")
            # file.write("Center : (",str((x+w)/2),",",str((y+h)/2),")","\n")
            # class Blue(object):
            #     x = str((x+w)/2)
            #     y = str((y+h)/2)
            # temp = Blue()
            # blues.append(temp)
	    write_text(f,cx,cy)
        write_file("BLUE",f,cx,cy)
    
    
    both_green = green(hsv)
    erode_green = cv2.erode(both_green,None,iterations = 3)
    dilate_green = cv2.dilate(erode_green,None,iterations = 10)
    contours_green,hierarchy_green = cv2.findContours(dilate_green,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours_green:
        x,y,w,h = cv2.boundingRect(cnt)
        cx,cy = x+w/2, y+h/2
	if 60 < hsv.item(cy,cx,0) < 80:
            cv2.rectangle(f,(x,y),(x+w,y+h),[0,255,0],2)
            print "GREEN :"
            print "Center : (", str((x+w)/2) , "," , str((y+h)/2) , ")"
            first = "Green :" + "\n"
            second = "Center : (" + str((x+w)/2) + "," + str((y+h)/2) + ")" + "\n"
	    write_text(f,cx,cy)
        write_file("GREEN",f,cx,cy)

    both_purple = purple(hsv)
    erode_purple = cv2.erode(both_purple,None,iterations = 3)
    dilate_purple = cv2.dilate(erode_purple,None,iterations = 10)
    contours_purple,hierarchy_purple = cv2.findContours(dilate_purple,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours_purple:
        x,y,w,h = cv2.boundingRect(cnt)
        cx,cy = x+w/2, y+h/2
	if 130 < hsv.item(cy,cx,0) < 150:
            cv2.rectangle(f,(x,y),(x+w,y+h),[255,0,165],2)
            print "Purple :"
            print "Center : (", str((x+w)/2) , "," , str((y+h)/2) , ")"
	    write_text(f,cx,cy)
        write_file("PURPLE",f,cx,cy)

    both_red = red(hsv)
    erode_red = cv2.erode(both_red,None,iterations = 3)
    dilate_red = cv2.dilate(erode_red,None,iterations = 10)
    contours_red,hierarchy_red = cv2.findContours(dilate_red,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours_red:
        x,y,w,h = cv2.boundingRect(cnt)
        cx,cy = x+w/2, y+h/2
	if 0 < hsv.item(cy,cx,0) < 20:
            cv2.rectangle(f,(x,y),(x+w,y+h),[0,0,255],2)
            print "Red :"
            print "Center : (", str((x+w)/2) , "," , str((y+h)/2) , ")"
	    write_text(f,cx,cy)
        write_file("RED",f,cx,cy)
    
    both_yellow = yellow(hsv)
    erode_yellow = cv2.erode(both_yellow,None,iterations = 3)
    dilate_yellow = cv2.dilate(erode_yellow,None,iterations = 10)
    contours_yellow,hierarchy_yellow = cv2.findContours(dilate_yellow,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours_yellow:
        x,y,w,h = cv2.boundingRect(cnt)
        cx,cy = x+w/2, y+h/2
	if 30 < hsv.item(cy,cx,0) < 50:
            cv2.rectangle(f,(x,y),(x+w,y+h),[0,255,255],2)
            print "Yellow :"
            print "Center : (", str((x+w)/2) , "," , str((y+h)/2) , ")"
	    write_text(f,cx,cy)
        write_file("YELLOW",f,cx,cy)
    
    # cv2.imshow('RESULT',f)

    
    # if cv2.waitKey(25) == 27:
    #     file.write('Finish\n')
    #     break
    if True:
        cv2.imwrite(sys.argv[3],f)
        break

print "out"
for g in greens:
    file.write(g.c+": ")
    print g.cx
    file.write(g.cx+",")
    print g.cy
    file.write(g.cy+"\n")
file.write("Finish\n")


file.write("Diagnosis : \n")
file.write("01 [ Bacterial blight ] : \n")
file.write("02 [ Bacterial leaf streak ] : \n")
file.write("03 [ Bacterial sheath brown rot ] : \n")
file.write("04 [ Bakanae ] : \n")
file.write("05 [ Blast leaf and collar ] : \n")
file.write("06 [ Blast node and neck ] : \n")
file.write("07 [ Brown spot ] : \n")
file.write("08 [ False smut ] : \n")
file.write("09 [ Blast node and neck ] : \n")
file.write("10 [ Narrow brown spot ] : \n")
file.write("11 [ Red stripe ] : \n")
file.write("12 [ Rice grassy stunt ] : \n")
file.write("13 [ Rice ragged stunt ] : \n")
file.write("14 [ Rice stripe virus disease ] : \n")
file.write("15 [ Rice yellow mottle virus ] : \n")
file.write("16 [ Sheath blight ] : \n")
file.write("17 [ Sheath rot ] : \n")
file.write("18 [ Stem rot ] : \n")
file.write("19 [ Tungroc ] : \n")


file.close()
cv2.destroyAllWindows()
# c.release()


