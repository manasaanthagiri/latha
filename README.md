## crop.py
# Library used in it #
import os
import os is a Python statement that imports the os module, which provides a way to interact with the operating system.
import csv
A CSV is a comma-separated values file, which allows data to be saved in a tabular format
from PIL import Image, ImageDraw
 PIL is an additional, free, open-source library for the Python programming language that provides support for opening, manipulating, and saving many different image file formats.
```
import os
import csv
from PIL import Image, ImageDraw


csv_file = "/home/manasa-anthagiri/Downloads/7622202030987_bounding_box.csv"
image_dir = "/home/manasa-anthagiri/Downloads/7622202030987"
output_dir = "/home/manasa-anthagiri/Downloads/7622202030987_with_boxes"


os.makedirs(output_dir, exist_ok=True)


def draw_boxes(image, boxes):
    draw = ImageDraw.Draw(image)
    for box in boxes:
        left = int(box['left'])
        top = int(box['top'])
        right = int(box['right'])
        bottom = int(box['bottom'])
        draw.rectangle([left, top, right, bottom], outline="red")
    return image


def crop_image(image, boxes):
    cropped_images = []
    for box in boxes:
        left = int(box['left'])
        top = int(box['top'])
        right = int(box['right'])
        bottom = int(box['bottom'])
        cropped_img = image.crop((left, top, right, bottom))
        cropped_images.append(cropped_img)
    return cropped_images


with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        image_name = row['filename']
        image_path = os.path.join(image_dir, image_name)
        output_path = os.path.join(output_dir, image_name)
        image = Image.open(image_path)
        boxes = [{'left': row['xmin'], 'top': row['ymin'], 'right': row['xmax'], 'bottom': row['ymax']}]
        cropped_images = crop_image(image, boxes)
        for i, cropped_img in enumerate(cropped_images):
            cropped_img.save(os.path.join(output_dir, f"{i}_{image_name}"))  
        full_image_with_boxes = draw_boxes(image, boxes)
        full_image_with_boxes.save(os.path.join(output_dir, f"full_{image_name}"))
```

## histo.py

# HISTOGRAM #
A histogram is the graphical representation of data where data is grouped into continuous number ranges and each range corresponds to a vertical bar.
The horizontal axis displays the number range.
The vertical axis (frequency) represents the amount of data that is present in each range.
The number ranges depend upon the data that is being used.

# Library used in it #
```
import numpy as np
```
 In numpy library, np. mean() is a function used to calculate arithmetic mean of the given array along with the axis.
```
import cv2 as cv
```
 The statement import cv2 as cv imports the OpenCV library in Python.. OpenCV (Open Source Computer Vision Library) is a widely used library for computer vision tasks such as image and video processing
```
from matplotlib import pyplot as plt
```
 Matplotlib is a popular data visualization library in Python. It's often used for creating static, interactive, and animated visualizations in Python.

 # CODE EXPLANATION
 ```
 img = cv.imread('/home/manasa-anthagiri/teddy.jpg')
```

![graph](https://github.com/manasaanthagiri/latha/assets/169051455/0c3a4661-8812-4e44-80c5-c521b4e223f0)


   This line states that read the image file named "teddy.jpg" located at the specified path /home/manasa-anthagiri/teddy.jpg by using opencv library
   ```
cv.imwrite("/home/manasa-anthagiri/Desktop/manasa/graph.png",img)
```
 This line states that it will store the image using open cv function in specified folder.
 ```
assert img is not None, "file could not be read, check with os.path.exists()"
```
 ```
color = ('b','g','r')
```
Each character represents a color channel: 'b' for blue, 'g' for green, and 'r' for red
```
for i,col in enumerate(color):
```
The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object. col will represent the color ('b', 'g', or 'r').
```
 histr = cv.calcHist([img],[i],None,[256],[0,256])
```
 the cv2.calcHist() function to calculate the image histograms.It also calculate color channels (blue, green, and red) of the image.
 ```
plt.plot(histr,color = col)
```
 This command plots the histogram data.
 ```
plt.xlim([0,256])
```
 This function is used to set the limits for the x-axis of the plot.
 ```
plt.show()
```
This command is used to display the plot that has been created using Matplotlib's plotting functions.
```

# iterate.py #

# Iteration
Iteration is the process of repeating a set of operations or steps.The essence of iteration is cyclical in nature

```
num = list(range(10))
```
This line creates a list of numbers from first 10 integers
```
previousNum = 0
```
The line seems as previousNum starts with the value of 0.
```
for i in num:
    sum = previousNum + i
    ```
    It calculates the sum of the current value i and the previous value stored in the  previousNum.
    ```
    print('Current Number '+ str(i) + 'Previous Number ' + str(previousNum) + 'is ' + str(sum)) # <- This is the issue.
    previousNum=i
    ```
    printing out the current number (i), the previous number (previousNum), and their sum (sum).


## video.py
```
import the opencv library 
import cv2 
  
  
# define a video capture object 
vid = cv2.VideoCapture(0) 
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
  
    # Display the resulting frame 
    cv2.imshow('frame', frame) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
```

