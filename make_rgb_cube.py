def make_cube(bitdepth):
  print("ply")
  print("format ascii 1.0")
  print("element vertex ", 2**(bitdepth*3))
  print("property float x")
  print("property float y")
  print("property float z")
  print("property uchar red")
  print("property uchar green")
  print("property uchar blue")
  print("end_header")
  for r in range(2**bitdepth):
    for g in range(2**bitdepth):
      for b in range(2**bitdepth):
        print(float(r), float(g), float(b), r, g, b)

make_cube(8)
