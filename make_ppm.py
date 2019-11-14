def make_ppm():
    f = open('test.ppm', 'w')
    f.write("P3\n")
    f.write("1000 1000\n")
    f.write("255\n")
    for i in range(1000**2):
        if (i % 3 == 0):
            f.write("200 0 0   ")
        elif (i % 3 == 1):
            f.write("0 200 0   ")
        elif (i % 3 == 2):
            f.write("0 0 200   ")
        if ((i + 1) % 1000 == 0):
            f.write("\n")
    f.close()

make_ppm()
