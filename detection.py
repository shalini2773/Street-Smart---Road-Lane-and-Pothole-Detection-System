"""
Detection Module
This module contains functions to detect lanes and potholes using YOLOv5.
"""

import cv2
import torch
import numpy as np
import winsound

  def detect_objects(model_path, camera_source=0):

  """
  Detect objects in a video stream using YOLOv5.
  Args:
  model_path (str): Path to the YOLOv5 model weights.
  camera_source (int): Camera index (default is 0 for the primary camera).
  """
  model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
  cam = cv2.VideoCapture(camera_source)

  while True:
  ret, img = cam.read()

  if not ret:
  break

  results = model(img)

  cv2.imshow("Output", np.squeeze(results.render()))

  # List of class names for detection

  class_names = ['lane', 'pothole', 'speedbreaker', 'sign', 'vehicle']
  bounding_boxes = results.xyxy[0]

  class_indices = bounding_boxes[:, -1].int().tolist()
  prediction_names = [class_names[idx] for idx in class_indices]

  # Sound alert for pothole or speedbreaker detection

  if "pothole" in prediction_names or "speedbreaker" in prediction_names:
  winsound.PlaySound("alert.wav", winsound.SND_FILENAME)

  if cv2.waitKey(1) & 0xFF == ord("q"):
  break

  cam.release()
  cv2.destroyAllWindows()

  def Camera():

  """Function for lane detection."""

 detect_objects('yolov5/runs/train/exp6/weights/best.pt')

 def Cameral():

  """Function for pothole detection."""

  detect_objects('yolov5/runs/train/exp8/weights/best.')