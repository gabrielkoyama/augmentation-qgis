import sys
import subprocess

try:
    import cv2
except:
    print('installing opencv2')
    subprocess.call([sys.exec_prefix + '/python', "-m", 'pip', 'install', 'opencv-python'])
    import cv2
    print('installation opencv2')

try:
    import skimage
except:
    print('installing scikit-image')
    subprocess.call([sys.exec_prefix + '/python', "-m", 'pip', 'install', 'scikit-image'])
    import skimage
    print('installation scikit-image')