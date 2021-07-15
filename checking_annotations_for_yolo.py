# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:49:11 2021

@author: ridvan.ozdemir
"""

import os
import glob

path='E:\\ridvan_2021\\07_***\\*****\\****_yolov4' #your annoted images folder
root='E:\\ridvan_2021\\07_***\\*****\\****' #your iamges in subfolders with class name

# set all object number's value to zero 
# you can give your class names but don't need to
class_name=0
class_name=0
class_name=0
class_name=0
class_name=0
class_name=0
class_name=0
class_name=0
class_name=0
class_name=0
class_name=0
class_name=0
class_name=0
class_name=0
class_name=0

#write your class names in a list as in yolo classes file
labels = ["class_name","class_name","class_name","class_name","class_name","class_name","class_name","class_name","class_name",
             "class_name","class_name","class_name","class_name","class_name","class_name"]

classes_annoted={}

i=0    

# read all YOLOv4 format labeling text files in the dataset folder and count object's number    
for filename in glob.glob(os.path.join(path, '*.txt')):
   with open(filename, 'r') as f: # open in readonly mode
       for satır in f:
           sinif = satır.split(' ')[0]
           print(sinif)
           i+=1
           classes_annoted[filename[44:-4]]=labels[int(sinif)]
           if (sinif == "0"):
               class_name+=1
           elif (sinif == "1"):
               class_name+=1
           elif (sinif == "2"):
               class_name+=1
           elif (sinif == "3"):
               class_name+=1
           elif (sinif == "4"):
               class_name+=1
           elif (sinif == "5"):
               class_name+=1
           elif (sinif == "6"):
               class_name+=1
           elif (sinif == "7"):
               class_name+=1
           elif (sinif == "8"):
               class_name+=1
           elif (sinif == "9"):
               class_name+=1
           elif (sinif == "10"):
               class_name+=1       
           elif (sinif == "11"):
               class_name+=1
           elif (sinif == "12"):
               class_name+=1
           elif (sinif == "13"):
               class_name+=1
           elif (sinif == "14"):
               class_name+=1
    
print(i, "number of total object")
print(len(classes_annoted), "annoted object count")


#read sub folders in the main folder
classes_folder={}
filenames=[]
for foldername in os.listdir(root):
    filenames.append(foldername)
    sub=os.path.join(root, foldername)
    for name in os.listdir(sub):
        classes_folder[name[:-4]]=foldername
print(len(classes_folder), "object count in folder")

j=0
k=0
wrong_annotations=[]
for image_file in classes_folder:
    if (classes_folder[image_file]==classes_annoted[image_file]):
        j+=1
    else:
        wrong_annotations.append(image_file)
        k+=1

print(k, " number of wrong annotation")        
        
    
