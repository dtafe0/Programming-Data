

f = open("textfile.txt", "r")

if f.mode == 'r':
    # contents = f.read()
    # print(contents)
    fl = f.readlines()
    for x in fl:
        print(x)


# for i in range(10):
#     f.write("This is line " + str(i) + "\r\n")

f.close()
