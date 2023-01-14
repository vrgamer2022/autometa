#!/usr/bin/env python3

import os
import glob
import piexif


# Enter the complete file path of your jpg location between the quotations.
path = "/media/sf_sharedfolder/myimages/*.jpg"

# Returns an intereator which will
# print simultaneously.
drfiles = glob.iglob(path, recursive=True)

#List of file names
filelist = []

#key words to be placed as meta data in jpg file
kword = []
k = []


for dfiles in drfiles:
    (head, tail) = os.path.split(dfiles)
    filelist.append(dfiles)

#Parses filename and puts keywords into kword lst
for file in filelist:
    (head, tail) = os.path.split(file)
    x = tail.split(".")
    y = x.pop(0)
    z = y.split("_")
    kword.append(z)

#removes the last numeric item in the list; joins list separted by semicolon;
#and appends to new list.
for i in range(len(kword)):
    kword[i].pop()
    s = ";".join(kword[i])
    k.append(s)

#prints the filename with each keyword.
#for y in range(len(filelist)):
    #print(filelist[y], k[y])


#prints metadata to file.
for y in range(len(filelist)):
    file = filelist[y]
    exif_dict = piexif.load(file)
    print(exif_dict)
    exif_dict["0th"][piexif.ImageIFD.XPKeywords] = k[y].encode("utf-16le")
    print(exif_dict)
    piexif.insert(piexif.dump(exif_dict), file)



        
    









