import struct

f = open('G:/20211122_1.dat', 'rb')
data_bin = f.read()
for each in data_bin[0:10]:
    print(int(each))

f.close()