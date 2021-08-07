#########pip install tensorflowjs

import tensorflowjs as tfjs
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
import csv
import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

data = []
labels = []
fake_csv_path = "data/archive-2/Fake.csv"
real_csv_path = "data/archive-2/True.csv"

with open(real_csv_path) as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        train_string = row[0] + " " + row[1]
        data.append(train_string)
        labels.append("True")

with open(fake_csv_path) as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        train_string = row[0] + " " + row[1]
        data.append(train_string)
        labels.append("False")
        
print(len(data))
print(len(labels))



import sklearn.preprocessing
from sklearn.preprocessing import LabelBinarizer

lb = LabelBinarizer()
labels = lb.fit_transform(labels)
print(lb.classes_)



training_size = 33675

train_text = data[0:training_size]
with open('train_text.txt', 'w') as f:
    for item in train_text:
        f.write("%s\n" % item)

test_text = data[training_size:]
with open('test_text.txt', 'w') as f:
    for item in test_text:
        f.write("%s\n" % item)

train_labels = labels[0:training_size]

with open('train_labels.txt', 'w') as f:
    for item in train_labels:
        f.write("%s\n" % item)


test_labels = labels[training_size:]

with open('test_labels.txt', 'w') as f:
    for item in test_labels:
        f.write("%s\n" % item)

vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
#training_size = 20000

tokenizer = Tokenizer(num_words = vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(train_text)

word_index = tokenizer.word_index

train_sequences = tokenizer.texts_to_sequences(train_text)
train_padded = pad_sequences(train_sequences, maxlen = max_length, 
                             padding = padding_type, 
                             truncating = trunc_type)


test_sequences = tokenizer.texts_to_sequences(test_text)
test_padded = pad_sequences(test_sequences, maxlen=max_length,
                            padding=padding_type,
                            truncating=trunc_type)



import numpy as np
import tensorflow as tf
train_padded = np.array(train_padded)
train_labels = np.array(train_labels)
test_padded = np.array(test_padded)
test_labels = np.array(test_labels)


model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy',optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), metrics=['accuracy'])

num_epochs = 25

model.summary()

