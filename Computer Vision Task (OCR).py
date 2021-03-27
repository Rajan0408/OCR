#!/usr/bin/env python
# coding: utf-8

# In[1]:


#IMPORT REQUIRED MODULES
import cv2
import pytesseract
import re
#location of tesseract executable file
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# In[2]:


#for rotating the image
def rotate(image, center = None, scale = 1.0):
    angle=360-int(re.search('(?<=Rotate: )\d+', pytesseract.image_to_osd(image)).group(0))
    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    # Perform the rotation
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated


# In[3]:


#reading the image
path = r'C:\Users\LENOVO\Desktop\OCR\3657993.jpg'
image = cv2.imread(path)


# In[4]:


img = rotate(image)


# In[5]:


#grayscaling
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#extracting every text from image using pytesseract
out = pytesseract.image_to_string(gray)
out = out.split()
#print(out)


# In[6]:


#list to store output
output = []


# In[7]:


#using regex module to find PAN-NUMBER from out and storing in output
for i in range(len(out)):
    x = re.search("[A-Za-z]{5}\d{4}[A-Za-z]{1}",out[i])
    if(x):
        output.append(out[i])


# In[8]:


#using regex module to find DOB from out and storing in output
for i in range(len(out)):
    x = re.search("(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$",out[i])
    if(x):
        output.append(out[i])


# In[9]:


#printing required details
print("PAN CARD NUMBER : ", output[0])
print("DATE OF BIRTH : ", output[1])


# In[ ]:





# In[ ]:




