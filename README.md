# autometa
Adds XPKeywords to jpg images based on file name. [LINUX]

**About**
I had thousands of digital images that I have accumulated over the years. Most of these pictures were taken at a time before
I knew what metadata was let alone being able to properly tag the images. So, I essentially started tagging the images by useing one-word 
descriptors in the file name. Each discriptor was separated by an underscore with some random number at the end of the file name. 

In order to make my life easier when updating these image file with their keywords, I developed this python app to loop through all of the images 
and add the appropriate keyswords to a file based of the keyword in the file name. Though it is still a work in progress. It has made my life a lot
easier. 

**How to use**

1. Update line 9 of the code so that path = "/Your/Path/*.jpg"
2. Ensure that all of the images that you want to tag have the following name format:
    example file name: family_brother_sister_mom_dad_77yeww.jpg
           (Note:
               A. the random number at the end of the file name will be not be added to the keywords.
               B. Do not place any descriptors after the random number. )
3. Place all images in the designated file from step 1.
4. Run python autometa.py in your linux command line. 
