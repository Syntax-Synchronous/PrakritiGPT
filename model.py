
## Importing Packages

import pandas as pd
import json
import tensorflow 
from tensorflow import keras
from sklearn.feature_extraction.text import CountVectorizer
from joblib import dump
import numpy as np

with open('./intents.json', 'r') as f:
    intents=json.load(f)
intents = intents['intent']

tags=[]
xy=[]
for intent in intents:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = pattern
        xy.append((w,tag))
df = pd.DataFrame(xy)
df.rename(columns = {0:"Sentence", 1:"Target"}, inplace = True)
named_y = df['Target']

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
df['Target'] = lb.fit_transform(df['Target'])

X_train = df.Sentence
y_train = df.Target
labels = {}
for i in range(30):
    labels[y_train[i]] = named_y[i]

vec = CountVectorizer(min_df=1)
X_train_count = vec.fit_transform(X_train.values)

df_bow = pd.DataFrame(X_train_count.toarray(), columns=vec.get_feature_names_out())


X_train = df_bow
X_train = X_train.to_numpy()

model = keras.Sequential([
    keras.layers.Dense(1000, input_shape=(44,),activation='relu',),
    keras.layers.Dense(100,activation='relu',),
    keras.layers.Dense(7,activation='sigmoid',)
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(X_train, y_train, epochs=100)

from joblib import dump 
dump(model, './nlm')

