"""
Image Upload Module
This module handles the uploading of images and displays them in grayscale.
""" 

import cv2
from tkinter import filedialog

  def imgtest():
  """Function to upload and process an image."""

  import_file_path = filedialog.askopenfilename()
  image = cv2.imread(import_file_path)
  filename = 'Test.jpg'

  cv2.imwrite(filename, image)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  cv2.imshow('Gray Image', gray)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  print(f"Image uploaded from: {import_file_path}")