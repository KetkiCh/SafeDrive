# SafeDrive

# Requirements
Install:
pymysql,
tkinter,
pillow,
numpy

# SafeDrive Applicattion 
Designed using python. For vehicle fleet managers to help manage their respective drivers' statistics. It detects drowsiness upon a login of a driver.

# Employee Database
Uses a MySQL database to add,modify and access data entries.
Note: you need to setup a MySQL server to use this

# Login Frontend
Uses tkinter to design a GUI for new employee registration or manual login

# Drowsiness Detection
Uses OpenCV library to detect drowsiness and yawn and sounds an alarm upon detection. Uses haar cascade classifiers for face, eyes and mouth detection. However, it has functions that can be used to calculate eye aperture ratio and mouth aperture ratio from the ROI data obtained using dlib.