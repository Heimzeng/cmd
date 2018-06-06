import os
import cv2

path = './'
filenames = os.listdir(path)
for filename in filenames:
    portion = os.path.splitext(filename)
    if portion[1] == '.jpg':
        img = cv2.imread(path + filename, 1)
        # cv2.imshow(filename, img)
        cv2.imwrite(path + portion[0] + '.png', img)
        print('change ' + filename + ' to ' + portion[0] + '.png')
        os.remove(path + filename)