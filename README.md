# Project-Hermes

# Machine Learning

## Road Quality Measurement

Using the Canny edge detector we are able to quantify how irregular the road is, how much bumps/potholes/defects it has. The objective quantification of the road quality is done using the following Key Indicators:

1) Amount of edges detected, defining the indicator as:

$\frac{\sum_{i=0,j=0}^{width, height} edges(i,j)}{width*height}, \text{  where } width, height \in \R$


2) Number of detected contours (closed-form edges)
3) Size of detected contours

From these three indicators, the number 2 shown a better correlation with the quality of the road as evaluated by a human. For roads in a bad situation are detected on average 400 contours per frame, while for roads in a good condition are detected on average 200 contours per frame.

![img](images/canny1.png)

![img](images/canny2.png)

## Road lanes identification
Using the Hough Transform we can detect the lane lines, allowing our system to detect whenever the driver sways of the road

![img](images/hough1.png)

## Road segmentation

can we do it, or just cite some paper?

## Cars and people detection

YoloV3

## Pothole detection

can we find a model?

# Mobile
We are using the Framework Kivy (Python language) to develop a minimum viable app.

The visualization dashboard was developed using Infrogram platform.
