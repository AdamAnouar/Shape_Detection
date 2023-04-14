"""
    Contours detection by colors using OpenCV, numpy, matplolib libraries and compas framework
    This python file will be run remotely from the gh file and therefore should be stored 
    in the same folder as the gh file.
"""


import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from compas.geometry import Polyline, Point, Curve


#Define the function to get the contours
def get_contours(path):
    frame = cv.imread(path)

    #Resize the image with respect to the initial proportions
    scale = 0.25
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    resized = cv.resize(frame, (dimensions), interpolation= cv.INTER_AREA)

    #Remove a bit of noise
    blurred_frame = cv.GaussianBlur(resized, (5, 5), 0)

    #Convert colors from bgr to hsv
    hsv = cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)

    #Find contours using the bounds of the defined color range (lower, upper) the blue color in this case
    lower = np.array([90, 50, 70])
    upper = np.array([120,255,255])
    mask = cv.inRange(hsv, lower, upper)
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    
    pts = []

    #Loop over the contours to get only those that have a specific size and filter the rest
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 800:
            pts.append([Point(p[0][0], p[0][1], 0) for p in contour])

    #Return a nested list of x,y,z coordinates
    return pts

