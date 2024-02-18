# Stereo Camera Setup & Calibration

<p align="center">
  <img src="data/project_title.png" alt="data/project_title" width="1500"/>
</p>

---------------------------------------------

## About this Project:
This project delves into the realm of Computer Vision with a focus on setting up and calibrating a stereo camera system using OpenCV, a leading open-source computer vision library. Stereo camera calibration is crucial for accurate depth estimation and 3D reconstruction, as it corrects for lens distortion and aligns the two cameras to a common viewpoint. The calibration process involves capturing images of a known pattern, such as a checkerboard, from different angles and then using these images to find the camera's internal and external parameters.

In the second phase, the project applies the calibration data to rectify the stereo images, aligning them to the same plane and making them suitable for computer vision tasks like object detection and ranging. This is an essential step in preparing the system for complex applications such as autonomous navigation, robotic manipulation, and 3D scanning. The use of Python alongside OpenCV provides a powerful and flexible development environment, enabling the creation of sophisticated computer vision applications. The project's success in stereo camera setup and calibration paves the way for further exploration and implementation of advanced computer vision capabilities.

<p align="center">
  <img src="data/project_logo.png" alt="data/project_title" width="1500"/>
</p>

---------------------------------------------

## Lens Distortions:

<p align="center">
  <img src="data/types_of_Dist.png" alt="2" width="1500"/>
</p>

---------------------------------------------

## Project Guide:

<p align="center">
  <img src="data/step1.png" alt="2" width="1500"/>
</p>

<p align="center">
  <img src="data/step2.png" alt="2" width="1500"/>
</p>

<p align="center">
  <img src="data/step3.png" alt="2" width="1500"/>
</p>

<p align="center">
  <img src="data/step4.png" alt="2" width="1500"/>
</p>

---------------------------------------------

## How to use my code?

The Python scripts provided are twofold: one for capturing images for calibration and the other for calibrating the camera. The scripts also output the camera parameters and save them in a text file.

`image_captures.py` → Captures images from the camera and saves them.

`stereo_camera_calibration.py` → Calibrates the camera using the captured images from both the left and right cameras.

To use this code:

1. Ensure that OpenCV and NumPy are installed in your Python environment.
2. Clone my repository.
3. Set up the camera; ensure it remains immobile after the calibration process.
4. Modify the path in both scripts to your own.
5. Run `image_captures.py` to capture and save the images.
6.Using the captured images, execute `stereo_camera_calibration.py` to begin calibrating both camera's.
7. This will save your camera parameters in a text file.

---------------------------------------------

## My Project Video Demonstration:

<p align="center">
  
  <a href="https://www.linkedin.com/posts/tvharikrishna_cameracalibration-computervision-opencv-activity-7126272257726799872-sEbZ?utm_source=share&utm_medium=member_desktop">
  <img src="https://img.shields.io/badge/Video-Watch Stereo Camera Calibration in Action-blue" alt="Video"/>
  </a>
</p>

---------------------------------------------
