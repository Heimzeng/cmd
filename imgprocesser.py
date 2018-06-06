import cv2
import sys
import numpy as np

if __name__ == '__main__':
    argv = sys.argv
    imgName = argv[1]
    op = argv[2]

    input_img = cv2.imread(imgName, 1)
    if op == 'scale':
        scale = 1.0
        size = [np.size(input_img,0),np.size(input_img,1)]
        output_size = (int(size[1] * scale), int(size[0] * scale))
        output_img = cv2.resize(input_img, output_size)
        cv2.imshow('res', output_img)
        cv2.waitKey()
    elif op == 'resize':
        #print(argv[3], argv[4])
        #output_size = (int(argv[3].split(',')[0].split('(')[1]), int(argv[3].split(',')[1].split(')')[0]))
        #output_size = (output_size[1], output_size[0])
        output_img = cv2.resize(input_img, (int(argv[4]), int(argv[3])))
        cv2.imwrite('res.png', output_img)
    else :
    	print("Op error")