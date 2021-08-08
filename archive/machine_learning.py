#########pip install tensorflowjs

import csv

data = []
labels = []

with open("data/fake_or_real_news.csv") as csvfile:
  datareader = csv.reader(csvfile)
  for row in datareader:
    if row[3] != 'label':
      article_body = row[2]
      article_label = row[3]
      data.append(article_body)
      labels.append(article_label)


print(len(data))
print(len(labels))
print(data[1])
print(labels[1])
print(data[3500])
print(labels[3500])


import sklearn.preprocessing
from sklearn.preprocessing import LabelBinarizer

lb = LabelBinarizer()
labels = lb.fit_transform(labels)
print(lb.classes_)



import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(oov_token='<OOV>')
tokenizer.fit_on_texts(data)
word_index = tokenizer.word_index


sequences = tokenizer.texts_to_sequences(data)
padded = pad_sequences(sequences, padding='post')


training_size = 4835

train_texts = data[0:training_size]

with open('train_text.txt', 'w') as f:
    for item in train_texts:
        item = item.replace("\n","" )
        f.write(item + "\n")

test_texts = data[training_size:]
with open('test_text.txt', 'w') as f:
    for item in test_texts:
        item = item.replace("\n","" )
        f.write(item + "\n")

train_labels = labels[0:training_size]
with open('train_labels.txt', 'w') as f:
    for item in train_labels:
        f.write("%s\n" % item)

test_labels = labels[training_size:]
with open('test_labels.txt', 'w') as f:
    for item in test_labels:
        f.write("%s\n" % item)

print(len(train_texts))
print(len(test_texts))

print(len(train_labels))
print(len(test_labels))


vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
training_size = 20000

tokenizer = Tokenizer(num_words = vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(train_texts)

word_index = tokenizer.word_index

train_sequences = tokenizer.texts_to_sequences(train_texts)
train_padded = pad_sequences(train_sequences, maxlen = max_length, 
                             padding = padding_type, 
                             truncating = trunc_type)


test_sequences = tokenizer.texts_to_sequences(test_texts)
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
    #tf.keras.layers.Dense(20, activation='relu'),
    #tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy',optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), metrics=['accuracy'])

num_epochs = 150

model.summary()




