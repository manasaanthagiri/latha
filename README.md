## crop.py

![image](https://github.com/manasaanthagiri/latha/assets/169051455/7cef5eea-bb6a-4195-a7cc-84db6c97c601)


# Library used in it #
```
import os
```
import os is a Python statement that imports the os module, which provides a way to interact with the operating system.

```
import csv
```
A CSV is a comma-separated values file, which allows data to be saved in a tabular format.

```
from PIL import Image, ImageDraw
```
 PIL is an additional, free, open-source library for the Python programming language that provides support for opening, manipulating, and saving many different image file formats.

```
csv_file = "/home/manasa-anthagiri/Downloads/7622202030987_bounding_box.csv"
image_dir = "/home/manasa-anthagiri/Downloads/7622202030987"
output_dir = "/home/manasa-anthagiri/Downloads/7622202030987_with_boxes"
```


os.makedirs(output_dir, exist_ok=True)

```
def draw_boxes(image, boxes):
    draw = ImageDraw.Draw(image)
    for box in boxes:
        left = int(box['left'])
        top = int(box['top'])
        right = int(box['right'])
        bottom = int(box['bottom'])
        draw.rectangle([left, top, right, bottom], outline="red")
    return image
```
This functions takes an image and a list of bounding boxes as input and draws rectangles around the objects specified by the bounding boxes.
It useful for visualizing bounding boxes on images, which is common in object detection

```
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
```
This function, crop_image, takes an image and crops the image based on the bounding box coordinates. It returns a list of cropped images.

```
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
 From a CSV file containing bounding box, images crops them based on the bounding box coordinates.
 Their bounding box  from the CSV file and saves the cropped images and images with bounding boxes drawn in the specified output directory.

 
![image](https://github.com/manasaanthagiri/latha/assets/169051455/df8aee4d-6449-4a4e-9189-ec37e7b2ca8d)

 
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
This line states that read the image file named "teddy.jpg" located at the specified path /home/manasa-anthagiri/teddy.jpg by using opencv library


![graph](https://github.com/manasaanthagiri/latha/assets/169051455/7eee43b8-9ea2-4868-9e96-455844aa2686)


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


![RGB](https://github.com/manasaanthagiri/latha/assets/169051455/1218b532-b612-402f-8726-25a89801e9e7)



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

OUTPUT

Current Number 0Previous Number 0is 0
Current Number 1Previous Number 0is 1
Current Number 2Previous Number 1is 3
Current Number 3Previous Number 2is 5
Current Number 4Previous Number 3is 7
Current Number 5Previous Number 4is 9
Current Number 6Previous Number 5is 11
Current Number 7Previous Number 6is 13
Current Number 8Previous Number 7is 15
Current Number 9Previous Number 8is 17


## video.py
```
import the opencv library 
import cv2 
```
  This statement imports the entire OpenCV library and its functions.

```  
    # define a video capture object 
vid = cv2.VideoCapture(0) 
```
 This line of code creates a VideoCapture object named vid. After executing this line,obj ready to capture video frames

```
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
  ```
  this lines capture a frame from the video stream using the VideoCapture object .This method reads a single frame from the video capture.

```
    # Display the resulting frame 
    cv2.imshow('frame', frame) 
    ```
    This line of code displays the captured frame.
    
     ``` 
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
        ```
        These lines of code wait for a key press after displaying the frame.

  ```
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
```
This function closes all OpenCV windows, useful for cleaning up after displaying frames.
