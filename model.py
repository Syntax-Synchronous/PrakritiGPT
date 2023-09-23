
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
len_dict=0
for intent in intents:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        len_dict=len_dict + 1
        w = pattern
        xy.append((w,tag))
df = pd.DataFrame(xy)
df.rename(columns = {0:"Sentence", 1:"Target"}, inplace = True)
named_y = df['Target']

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
print(df['Target'])
df['Target'] = lb.fit_transform(df['Target'])

df.set_index('Sentence')
df.reset_index(drop=True)
df.to_csv('./datasets/sentences_intent.csv')

X_train = df.Sentence
y_train = df.Target
labels = {}
for i in range(len_dict):
    labels[y_train[i]] = named_y[i]


vec = CountVectorizer(min_df=1)
X_train_count = vec.fit_transform(X_train.values)
bag_len = len(X_train_count.toarray()[0])

df_bow = pd.DataFrame(X_train_count.toarray(), columns=vec.get_feature_names_out())


X_train = df_bow
X_train = X_train.to_numpy()

model = keras.Sequential([
    keras.layers.Dense(1000, input_shape=(bag_len,),activation='relu',),
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
dump(model, './models/nlm')

