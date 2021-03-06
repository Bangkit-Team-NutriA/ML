# -*- coding: utf-8 -*-
"""Resnet50.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mz7JYQ39KCImU8ItL-M05BdB-zAfwU44
"""

from google.colab import drive
drive.mount('/content/drive',force_remount=True)

!unzip "/content/drive/MyDrive/datasetFoodImage/images.zip" -d "/content/sample_data/data"

import json
import os
import tensorflow as tf
from google.colab import files
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout, BatchNormalization
from tensorflow.keras import Sequential, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, Callback
from tensorflow_hub import KerasLayer
from tensorflow.keras.metrics import Precision,Recall

import math

Resnet50Path = 'https://tfhub.dev/google/imagenet/resnet_v2_50/feature_vector/5'

modelCNN = KerasLayer(Resnet50Path, trainable = False, input_shape = (250,250,3), name = 'Resnet50')

def build_model(modelCNN):
  model = Sequential([
    Input(shape=(250,250,3)),
    modelCNN,   
    Dense(108, activation="softmax")
  ])
  model.compile(optimizer='Adam', loss="categorical_crossentropy", metrics=["accuracy", Precision(), Recall()])
  return model

model = build_model(modelCNN[0])

model.summary()

datagen = ImageDataGenerator(
    rescale = 1./255,
    validation_split=0.1)

train_data_generator = datagen.flow_from_directory(
    "/content/sample_data/data/images",
    target_size=(250,250),
    subset='training'
)

valid_data_generator = datagen.flow_from_directory(
    "/content/sample_data/data/images",
    target_size=(250,250),
    subset='validation'
)

freq = 91064/32

math.ceil(freq)

checkpoint = ModelCheckpoint("/content/sample_data/model/RESNET_{epoch:02d}_{accuracy:.2f}.h5", verbose=1, mode='auto', save_freq=2846)

class myCallback(Callback):
  def on_epoch_end(self, epoch, logs={}):
    path = '/content/sample_data/trainingHistoryResnet.json'
    with open(path) as f:
      data = json.load(f)
    os.remove(path)
    dictLogs = {
        'loss': logs.get('loss'),
        'accuracy': logs.get('accuracy'),
        'val_loss': logs.get('val_loss'),
        'val_accuracy': logs.get('val_accuracy'),
        'val_precision': logs.get('val_precision_4'),
        'val_recall': logs.get('val_recall_4'),
        'recall': logs.get('recall_4'),
        'precision': logs.get('precision_4')
    }
    data.append(dictLogs)
    json_object = json.dumps(data, indent = 4)
    with open(path, "w") as outJson:
      outJson.write(json_object)

callbacks = myCallback()

model.fit(train_data_generator, validation_data=valid_data_generator, epochs=5,callbacks=[checkpoint, callbacks])

model.fit(train_data_generator, validation_data=valid_data_generator, epochs=3,callbacks=[checkpoint, callbacks])

labels = train_data_generator.class_indices

with open('labels.json','w') as f:
  f.write(json.dumps(labels,indent=4))