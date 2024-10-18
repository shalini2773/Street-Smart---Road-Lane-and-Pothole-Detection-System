# Street Smart: Road Lane and Pothole Detection System

## Overview

**Street Smart** is a road lane and pothole detection system that leverages the power of computer vision and YOLOv5 models to provide real-time detection of lanes and potholes. The project includes a graphical user interface (GUI) that allows users to initiate lane or pothole detection using a webcam, as well as upload images for processing.

## Features

- **Lane Detection**: Real-time lane detection using a live webcam feed.
- **Pothole Detection**: Real-time pothole detection with an alert system using a webcam feed.
- **Image Upload**: Upload an image to display it in grayscale for basic processing.
- **Alert System**: Sound alerts for pothole or speedbreaker detection.

## Project Structure
StreetSmart/ │ ├── main.py                        # GUI for lane and pothole detection 
               ├── detection.py                   # Detection logic for lanes and potholes
               ├──image_upload.py                # Image upload and  processing
               ├── utils.py                       # Utility functions (e.g., email alerts) 
               ├──requirements.txt                # List of dependencies
            └── README.md                      # Project documentation

  ## Installation
  1. **Clone the repository**:
   ```
   git clone
   https://github.com/shalini2773/Street-Smart---Road-Lane-and-Pothole-Detection-System.git
   ```
  2. **Navigate to the Project Directory**
     ```
     cd ProjectFiles
     ```
  3. **Install the required dependencies:**
      Install all the dependencies listed in the requirements.txt file.
     
  4. **Download YOLOv5 Models:** Ensure that you have the YOLOv5 model files (best.pt for lane detection and pothole detection) in the appropriate paths as specified in detection.py.
     
     For example:
     yolov5/runs/train/exp6/weights/best.pt for lane detection.

     yolov5/runs/train/exp8/weights/best.pt for pothole detection.

   5. **Set up Alert Sound:**
       Ensure you have the alert.wav file in the project directory for sound alerts on pothole detection.

# Usage

  1. **Run the application:** To start the graphical user interface (GUI), run the main.py file:

  python main.py


 2. **Features:**

  Lane Detection: Click on the "Lane Detection" button to start lane detection using your webcam.

  Pothole Detection: Click on the "Pothole Detection" button to start detecting potholes with sound alerts.

  Upload Image: Click the "Upload Image" button to upload an image and view it in grayscale.

# Configuration

Email Notifications (Optional)

If you want to enable email alerts for certain detections, you need to set up email credentials.

1. Set your email password as an environment variable:

For Windows:

set EMAIL_PASSWORD=your_email_password

For Linux/Mac:

export EMAIL_PASSWORD=your_email_password

2. Modify utils.py to retrieve the password from the environment variable:

In utils.py, replace "sample_password" with:

import os
email_password = os.environ.get("EMAIL_PASSWORD")

Now the email alerts will use the password securely from your environment variable.

# Dependencies

The following Python libraries are required for this project:

OpenCV: For video and image processing.

PyTorch: For using the YOLOv5 models.

NumPy: For numerical operations.

Tkinter: For the graphical user interface.

Winsound: For playing sound alerts (for Windows systems).

# Troubleshooting

Model Not Found: If you're seeing errors related to model loading, ensure that the paths to the YOLOv5 models are correct in detection.py. You can modify the paths to match your local setup.

Sound Alert Not Working: If the sound alert (alert.wav) is not playing, ensure that the file exists in the project directory and that the path is correct in the code.

# Contribution

Contributions are welcome! Please submit a pull request or open an issue if you encounter any problems or have suggestions for new features.

# License

This project is licensed under the MIT License. See the LICENSE file for more details.


Thank you for visiting and checking out Street Smart: Road Lane and Pothole Detection System. Your interest and support mean a lot! If you find this project helpful, please feel free to contribute, suggest improvements, or raise any issues. Together, we can make our roads safer!






