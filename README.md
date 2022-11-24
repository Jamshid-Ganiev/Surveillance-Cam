# Counting-People-in-Real-Tme-Using-OpenCV
The use case of this project is to count the number of visitors who are heading in or out in a particular store/ building/ shopping mall/ class room in real-time.

This project is done as the final IoT project for "Iot Apllication System Class"(Professor: Vijay Kakani) by the 'GiGa' team consisted of 4 undergraduate students majoring in ISE(Integrated System Engineering) department. (Fall semester in 2022).

## Simple Theory
**SSD detector:**
- We used a SSD (Single Shot Detector) in the project. Generally, it only takes a single shot to detect whatever is in an image.
- Compared to other 2 shot detectors such as R-CNN, SSD is quite fast.
---
**Centroid tracker:**
- Centroid tracker is one of the most reliable trackers out there.
- To be straightforward, the centroid tracker computes the centroid of the bounding boxes.
- That is, the bounding boxes are (x, y) co-ordinates of the objects in an image. 
- Once the co-ordinates are obtained by our SSD, the tracker computes the centroid (center) of the box. In other words, the center of an object.
- Then an unique ID is assigned to every particular object deteced, for tracking over the sequence of frames.

## Running the code in Raspberry Pi(worked well with Pi3 model B)
-First of all, install OpenCV-Python Environment in Raspberry Pi:
    - Usually takes around 3-4 hours.
    $ https://pimylifeup.com/raspberry-pi-opencv/
- Install all the required Python dependencies:
'''
pip install -r requirements.txt

'''
    -Highly advised to install dependencies in python virtual Environment:
      -more on : '''https://docs.python.org/3/library/venv.html'''
