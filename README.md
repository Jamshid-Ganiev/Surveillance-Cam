# Counting-People-in-Real-Tme-Using-OpenCV-Python-in-Raspberry-Pi3-modelB
The use case of this project is to count the number of visitors who are heading in or out in a particular store/ building/ shopping mall/ class room in real-time.

This project is done as the final IoT project for "Iot Apllication System Class"(Professor: Vijay Kakani) by the 'GiGa' team consisted of 4 undergraduate students majoring in ISE(Integrated System Engineering) department. (Fall semester in 2022).

## Simple Theory
**SSD detector:**
- We used a SSD (Single Shot Detector) with a MobileNet architecture in the project. Generally, it only takes a single shot to detect whatever is in an image.
- Compared to other 2 shot detectors such as R-CNN, SSD is quite fast.
- - For more info:
'''
SD paper: https://arxiv.org/abs/1512.02325
MobileNet paper: https://arxiv.org/abs/1704.04861
'''
---
**Centroid tracker:**
- Centroid tracker is one of the most reliable trackers out there.
- Then an unique ID is assigned to every particular object deteced, for tracking over the sequence of frames.
- For more info:
'''
https://towardsdatascience.com/review-ssd-single-shot-detector-object-detection-851a94607d11
'''

## Running the code in Raspberry Pi(worked well with Pi3 model B)
- First of all, install OpenCV-Python Environment in Raspberry Pi:(Usually takes around 3-4 hours.)
'''
https://pimylifeup.com/raspberry-pi-opencv/
'''

-Install all the required Python dependencies:
```
pip install -r requirements.txt
```
>    -Highly advised to install dependencies in python virtual Environment:
      -more on : '''https://docs.python.org/3/library/venv.html'''

-To run the code in real-time video , use the following command:
```
python start.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel
```

>  (works with both raspberry pi camera oo usb camera connected to raspberry pi.


## Features
**Real-time Alert via email address
- sender's email address and password is changed in "mylib/mailer.py" and receiver's email address can be changed in "my_lib/config.py" easily.

**Scheduler
- Automatic scheduler to start the software. Configure to run at every second, minute, day, or Monday to Friday.

**Timer
- All you have to do is set your desired time and run the script. (inside start.py)

**Automatic data saver
-saves all the date in ".csv" format in "mylib/log.csv" after the program ended.

## Refernces
- Mainly this project was actually motivated from:
"""
https://github.com/saimj7/People-Counting-in-Real-Time 
"""
- which was motivated from:
"""
https://www.pyimagesearch.com/2018/07/23/simple-object-tracking-with-opencv/
"""
-Special thanks to :  <a href="http://saimj7.github.io" target="_blank">Sai_Mj</a>.
