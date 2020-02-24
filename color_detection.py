#This is a personal project for indept understanding of python and its packages like openCV,pandas,numpy.
#In this project i am trying create a color detector using python.
import pandas as pd
import numpy as np
import cv2
import argparse

#We are using argparse library to create an argument parser. We can directly give an image path from the command prompt:
ap = argparse.ArgumentParser()
ap.add_argument('-i','--images',required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
#Reading image with openCV
img = cv2.imr(img_path)
