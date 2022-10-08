import cv2, random, os, sys
import numpy as np
import multiprocessing as mp
from copy import deepcopy
from skimage.metrics import mean_squared_error as compare_mse

img = cv2.imread('imgname')
height, width, channels = img.shape

nofg = 50 #number of first genes
noggp = 50 #number of gene groups pergeneration
pomo = 0.01 #probability of mutation occurrence
poaaciagg = 0.3 #probability of adding a circle in a gene group
potdoaciagg = 0.2 #Probability of the disappearance of a circle in a gene group

circle_min, circle_max = 2, 10
image_storage_cycle = 100