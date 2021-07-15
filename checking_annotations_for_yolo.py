# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:49:11 2021

@author: ridvan.ozdemir
"""

import os
import glob

#path = 'D:/ridvan_2020/01_gelisim/python_ornekleri/furkan'
#path = 'E:/Yolo_v4/darknet/build/darknet/x64/data/obj'
path='E:\\ridvan_2021\\07_eti\\iade_depo\\DIVK_yolov4'
root='E:\\ridvan_2021\\07_eti\\iade_depo\\DIVK'
#D:\ridvan_2020\05_PhD\YOLO\tik_2\yedekler\R_F_D_Bigger_v2_09
#D:\ridvan_2020\05_PhD\YOLO\tik_2\yedekler\First_Plus_07

# set all object number's value to zero 
Gonlubol=0
FormPatlak=0
Gong=0
PopkekMuzlu=0
PopkekLimonlu=0
FormKepekli=0
BenimO=0
BrowniGoldVisne=0
PufKakaolu=0
AntepFistikli=0
AskTadinda=0
Crax=0
KaramGurme=0
Petito=0
Sutlu =0

labels = ["Gonlubol","FormPatlak","Gong","PopkekMuzlu","PopkekLimonlu","FormKepekli","BenimO","BrowniGoldVisne","PufKakaolu",
             "AntepFistikli","AskTadinda","Crax","KaramGurme","Petito","Sutlu"]

urunler_isaret={}

i=0    

# read all YOLOv4 format labeling text files in the dataset folder and count object's number    
for filename in glob.glob(os.path.join(path, '*.txt')):
   with open(filename, 'r') as f: # open in readonly mode
       for satır in f:
           sinif = satır.split(' ')[0]
           print(sinif)
           i+=1
           urunler_isaret[filename[44:-4]]=labels[int(sinif)]
           if (sinif == "0"):
               Gonlubol+=1
           elif (sinif == "1"):
               FormPatlak+=1
           elif (sinif == "2"):
               Gong+=1
           elif (sinif == "3"):
               PopkekMuzlu+=1
           elif (sinif == "4"):
               PopkekLimonlu+=1
           elif (sinif == "5"):
               FormKepekli+=1
           elif (sinif == "6"):
               BenimO+=1
           elif (sinif == "7"):
               BrowniGoldVisne+=1
           elif (sinif == "8"):
               PufKakaolu+=1
           elif (sinif == "9"):
               AntepFistikli+=1
           elif (sinif == "10"):
               AskTadinda+=1       
           elif (sinif == "11"):
               Crax+=1
           elif (sinif == "12"):
               KaramGurme+=1
           elif (sinif == "13"):
               Petito+=1
           elif (sinif == "14"):
               Sutlu+=1
    
print(i, "number of total object")
print(len(urunler_isaret), "işaretli ürün sayıldı")


#read sub folders in the main folder
urunler_klasor={}
filenames=[]
for foldername in os.listdir(root):
    filenames.append(foldername)
    sub=os.path.join(root, foldername)
    for name in os.listdir(sub):
        urunler_klasor[name[:-4]]=foldername
print(len(urunler_klasor), "klasorlü ürün sayıldı")

j=0
k=0
wrong_annotations=[]
for image_file in urunler_klasor:
    if (urunler_klasor[image_file]==urunler_isaret[image_file]):
        j+=1
    else:
        wrong_annotations.append(image_file)
        k+=1

print(k, " number of wrong annotation")        
        
    