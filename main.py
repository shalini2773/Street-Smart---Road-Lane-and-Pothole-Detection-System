"""
Road Lane Detection Application
This script provides a graphical user interface (GUI) for lane and pothole detection.
Users can initiate detection or upload images for processing.
"""

from tkinter import *
from detection import Camera, Cameral
from image_upload import imgtest

  def main_account_screen():

  """Create and display the main application window."""
  global main_screen
  main_screen = Tk()
  main_screen.title("Road Lane Detection")
  main_screen.geometry("600x600")

  Label(text="Road Lane Detection", width="300", height="5", font=("Calibri", 16)).pack()
  Button(text="Lane Detection", font=('Verdana', 15), height="2", width="30",
  command=Camera).pack(side=TOP)

  Button(text="Pothole Detection", font=('Verdana', 15), height="2", width="30",
  command=Cameral).pack(side=TOP)

  Button(text="Upload Image", font=('Verdana', 15), height="2", width="30",
  command=imgtest).pack(side=TOP)

  main_screen.mainloop()
  if __name__ == "__main__":
  main_account_screen()