import operator
from osgeo import gdal

import os
import cv2
import numpy as np

from PIL import Image

from random import randint
from skimage.transform import resize
from scipy.ndimage import gaussian_filter

def rotate(img, degrees):
    return (np.rot90(img, k=int(degrees / 90)))

def flip(img, direction):
    if (direction == "vertical"):
        return (img[::-1, ::])
    elif (direction == "horizontal"):
        return (img[::, ::-1])
    elif (direction == "both"):
        return (img[::-1, ::-1])

def trim(img, top=0, bottom=0, left=0, right=0):
    return (img[top:-bottom, right:-left])

def crop(img, right=0, top=0, left=100, bottom=100):
    return (img[top:bottom, right:left])

def blur(img, sigma=1):
    return(gaussian_filter(img, sigma=sigma))

def rescale(img, ratio):
    return (resize(img, (int(img.shape[1] * ratio), int(img.shape[0] * ratio))))

def binary(img, threshold=120, inv=False, bw=True):
    if (inv == False):
        method = cv2.THRESH_BINARY
    else:
        method = cv2.THRESH_BINARY_INV

    if (bw == True):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return(cv2.threshold(img, threshold, 255, method)[1])

def trunc(img, threshold=120, max=255):
    return (cv2.threshold(img, threshold, max, cv2.THRESH_TRUNC)[1])

def edgy(img, threshold=120, max=255, aperture=3, mask=True):

    if(img.dtype != "uint8"): img = img.astype('uint8')

    edges = cv2.Canny(img, threshold, max, aperture)

    if (mask == True):
        return (cv2.bitwise_and(img, img, mask=cv2.bitwise_not(edges)))

    return(edges)

def augmentate(img, name, chunks=100, invert=3, rotations=3, blur_sigmas=5):
    
    res = dict()
    labelImg = dict()
    areas = []

    while (len(areas) != chunks):
        x = randint(0, img.shape[1] - chunks)
        y = randint(0, img.shape[0] - chunks)
        if ((x, y) not in areas):
            areas.append((x, y))
    count = 1
    for i, coords in enumerate(areas):
        nimg = crop(img, coords[0], coords[1], coords[0] + chunks, coords[1] + chunks)
        nm1 = (name+"_"+str(i)).upper()

        for idx, x in enumerate([nimg, flip(nimg, "vertical"), flip(nimg, "horizontal"), flip(nimg, "both")][:invert + 1]):
            nm1 += "_" + str(idx)
            res[nm1] = dict()

            for idx2, y in enumerate([0, 90, 180, 270][:rotations + 1]):
                nm2 = ("_ROTATE_" + str(y)).upper()
                _img = rotate(x, y)

                if(np.count_nonzero(_img) == 0): continue

                res[nm1][nm1 + nm2] = dict()
                res[nm1][nm1 + nm2]['name'] = nm1 + nm2

                labelImg[nm1 + nm2] = _img

                count+=1

                for idx3, s in enumerate(range(1, blur_sigmas + 1)):
                    nm3 = ("_BLUR_" + str(s)).upper()
                    _img = rotate(blur(x, sigma=s), y)

                    if(np.count_nonzero(_img) == 0): continue

                    res[nm1][nm1 + nm2 + nm3] = dict()
                    res[nm1][nm1 + nm2 + nm3]['name'] = nm1 + nm2 + nm3

                    labelImg[nm1 + nm2 + nm3] = _img
                    count+=1


    return res, labelImg, count

def cloud(img):
    # Opening the primary image (used in background)
    img1 = Image.fromarray(img)
        
    # Opening the secondary image (overlay image)
    png_path = os.path.abspath(os.path.join(os.path.split(__file__)[0], "..", "img", "cloud_template.png"))
    img2 = Image.open(png_path)

    # resize the image
    size = img1.size
    img2 = img2.resize(size,Image.ANTIALIAS)

    img1 = np.asarray(img1)
    img2 = np.asarray(img2)

    # creating cloud mask
    cloud_mask = img2[:,:,0]

    res = np.where(cloud_mask == 0, img1, cloud_mask)

    return res

def gdalDecreaseResolution(dataset, src, limiar=3, dst="/tmp/decrease.tif"):

    xres, yres = operator.itemgetter(1,5)(dataset.GetGeoTransform())  

    xres*=limiar
    yres*=limiar

    gdal.Warp(dst, src, xRes=xres, yRes=yres)

    res = gdal.Open(dst)
    res_b = res.GetRasterBand(1)
    res_arr = res_b.ReadAsArray()

    return res_arr