# -*- coding: utf-8 -*-
"""way of data loading.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x2jdIJ1_zTbvLRkd0l16-cTVcQ3Hr6Iy

# Data loading methods

# load documents like csv and xlsx
"""

# load data from local system
import pandas as pd
data = "path"
pd.read_csv(data)
pd.read_excel(data)

"""# load image as single and multiple"""

# single file
    file_path = ""
    # use read function to read the above file
    file_path.load()

# folder
import glob
import os
folder_path = ""
data_path = os.path.join(folder_path,'*g')
files = glob.glob(data_path)

# data generator
from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_path = ''
test_path = ''

train_datagen = ImageDataGenerator(rescale=1./255,shear_range= 0.2,zoom_range=0.2,horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(train_path,target_size=(150,150),batch_size=128,class_mode='binary')
test_set = test_datagen.flow_from_directory(test_path,target_size=(150,150),batch_size=128,class_mode='binary')