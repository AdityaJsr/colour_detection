
#This is a personal project for in-depth understanding of python and its packages like openCV,pandas,numpy.
#In this project i am trying create a color detector using python.
import pandas as pd
import numpy as np
import cv2
import argparse

#We are using argparse library to create an argument parser. We can directly give an image path from the command prompt:
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

#Reading image with openCV
img = cv2.imread(img_path)
imgS = cv2.resize(img,(720,480))

# print(imgS.shape)
click = False
r =g=b = xpos =ypos = 0 

#Reading CSV file with pandas and coloumn manipulation(renaming)
index = ["color","color_name","hex","R","G","B"]
csv = pd.read_csv('datasets/colors.csv', names = index, header = None)


#Draw function
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,click
        click = True
        xpos = x
        ypos = y
        b,g,r = imgS[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

#Mouse callbacks
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)


#Get color name defination
def get_color_name(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R-int(csv.loc[i,"R"])) + abs(G-int(csv.loc[i,"G"])) + abs(B-int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

while(1):
    cv2.imshow("image",imgS)
    if(click == True):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness) -1 thickness fills rectangle entirely
        cv2.rectangle(imgS,(20,20), (600,60), (b,g,r), -1)

        #Creating text string to display ( Color name and RGB values )
        text = get_color_name(r,g,b) + ' R='+ str(r) + ' G='+ str(g) + ' B='+ str(b)
        #cv2.putText(img,text,start,font(0-7), fontScale, color, thickness, lineType, (optional bottomLeft bool) )
        cv2.putText(imgS, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
 #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(imgS, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        click=False
    #Break the loop when user hits 'esc' key 
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()