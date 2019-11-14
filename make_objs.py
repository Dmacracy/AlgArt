import numpy as np
import sys

class Color:
  '''Basic '''
  def __init__(self, r=0, g=0, b=0):
   self.r = r
   self.g = g
   self.b = b

class Point:
  def __init__(self, x=0.0, y=0.0, z=0.0, col=Color()):
   self.x = x
   self.y = y
   self.z = z
   self.col = col

class Face:
  def __init__(self, p1, p2, p3, col=Color()):
    self.p1 = p1
    self.p2 = p2
    self.p3 = p3


class Tetra:
  

  def __init__(self):
    self.p1 = Point(-1.0, 0.0, -1.0/np.sqrt(2))
    self.p2 = Point(1.0, 0.0, -1.0/np.sqrt(2))
    self.p3 = Point(0.0, -1.0, 1.0/np.sqrt(2))
    self.p4 = Point(0.0, 1.0, 1.0/np.sqrt(2))

    self.f1 = Face(1,2,3)
    self.f2 = Face(2,3,4)
    self.f3 = Face(1,2,4)
    self.f4 = Face(1,3,4)

  def write_to_file(self, filename):
    with open(filename, 'a') as sceneFile:
      sceneFile.write("v " + str(self.p1.x) + " " + str(self.p1.y) + " " + str(self.p1.z) + "\n")
      sceneFile.write("v " + str(self.p2.x) + " " + str(self.p2.y) + " " + str(self.p2.z) + "\n")
      sceneFile.write("v " + str(self.p3.x) + " " + str(self.p3.y) + " " + str(self.p3.z) + "\n")
      sceneFile.write("v " + str(self.p4.x) + " " + str(self.p4.y) + " " + str(self.p4.z) + "\n")
      sceneFile.write("f " + str(self.f1.p1) + " " + str(self.f1.p2) + " " + str(self.f1.p3) + "\n")
      sceneFile.write("f " + str(self.f2.p1) + " " + str(self.f2.p2) + " " + str(self.f2.p3) + "\n")
      sceneFile.write("f " + str(self.f3.p1) + " " + str(self.f3.p2) + " " + str(self.f3.p3) + "\n")
      sceneFile.write("f " + str(self.f4.p1) + " " + str(self.f4.p2) + " " + str(self.f4.p3) + "\n")

if __name__ == "__main__":
  tet = Tetra()
  filename = sys.argv[1]
  tet.write_to_file(filename)
  
