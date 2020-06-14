import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import imutils
import argparse

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Convert color image into grayscale
    canny = cv2.Canny(gray, 10, 40)
    return canny

def region_of_interest(image):
    height = image.shape[0]
    width = image.shape[1]
    margin = 500
    polygons = np.array([ # FillPoly takes a polygon, therefore you must make a polygon
        [(0, height), (width, height), (width, height-margin), (0, height-margin)]
        ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask) # Taking the bitwise & of the two images, essitally getting rid of anything outside of the area of 

    return masked_image

# def apply_contor(cropped_image, image):
#     ret, threshold = cv2.threshold(cropped_image, 127, 255, 0)
#     contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#     sorted_contours = max(self.contours, key=cv2.contourArea)
#     area = cv2.contourArea(sorted_contours)

#     cv2.drawContours(image, contours, -1, (0, 255, 0), 2) # Draw Contors


def apply_contour(cropped_image, image):
    copy = np.copy(image)
    ret, threshold = cv2.threshold(cropped_image, 127, 255, 0)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)       
    image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)


    # print("Number of contors = " + str(len(contours)))
    # print(contours[0])

# image =  cv2.imread('test_media\pothole_test.jpg')
# copy_image = np.copy(image)
# pothole_image = np.copy(image) # Make copy to ensure that OG does not get affected 
# canny_image= canny(pothole_image)
# cropped_image = region_of_interest(canny_image)
# contor_image = apply_contour(cropped_image, copy_image)

# cv2.imshow('result', copy_image)
# cv2.waitKey(0)

cap = cv2.VideoCapture("test_media\pothole_sample_clips\statistics 00005652.mov")
while(cap.isOpened()):
    _, frame = cap.read() # Getting the current frame
    pothole_image = np.copy(frame) # Make copy to ensure that OG does not get affected 
    canny_image = canny(pothole_image)
    cropped_image = region_of_interest(canny_image)
    shape = cropped_image.shape 
    print(cropped_image.mean()/(shape[0]*shape[1]))

    cv2.imshow('result', cropped_image)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# cap = cv2.VideoCapture(" test_media\pothole_sample_clips\pothole_clip00006135.mp4")
# while(cap.isOpened()):
#     _, frame = cap.read() # Getting the current frame
#     pothole_image = np.copy(frame) # Make copy to ensure that OG does not get affected 
#     canny_image= canny(pothole_image)
#     cropped_image = region_of_interest(canny_image)
#     contour_image = apply_contour(cropped_image, frame)
#     cv2.imshow('result', canny_image)
#     cv2.waitKey(1)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

#Good: 
#   1e-6
#   9e-7

#Bad:
#   5e-7

# Video names:
#   Good:
#   test_media\pothole_sample_clips\pothole_clip00002549.mp4
#   New Good: test_media\pothole_sample_clips\statistics 00005652.mov
#   Bad:
#   test_media\pothole_sample_clips\pothole_clip00006135.mp4
#   New Bad: test_media\pothole_sample_clips\statistics 00006047.mov


#For Bad Video: (8, 35) for canny -> noisey edge detection
#For Bad Video: (10, 40) for less noisey, easy to see holes