from flask import Flask, flash, jsonify, render_template, request, redirect, url_for
from flask.templating import render_template
import tensorflow as tf
import numpy #as np
import os
import csv
import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import sklearn.preprocessing
from sklearn.preprocessing import LabelBinarizer
import pickle
import nltk
nltk.download('punkt')
from newspaper import Article

app = Flask(__name__)

def model_input(input_text):
    vocab_size = 10000
    embedding_dim = 16
    max_length = 100
    trunc_type = 'post'
    padding_type = 'post'
    oov_tok = "<OOV>"
    training_size = 20000

    with open('train_text.txt') as file:
        train_texts = file.readlines()
        file.close()
    with open('test_text.txt') as file:
        test_texts = file.readlines()
        file.close()
    with open('train_labels.txt') as file:
        train_labels = file.readlines()
        file.close()
    with open('test_labels.txt') as file:
        test_labels = file.readlines()
        file.close()
    print(len(train_texts))
    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
    tokenizer.fit_on_texts(train_texts)

    word_index = tokenizer.word_index

    train_sequences = tokenizer.texts_to_sequences(train_texts)
    train_padded = pad_sequences(train_sequences, maxlen=max_length,
                                 padding=padding_type,
                                 truncating=trunc_type)

    test_sequences = tokenizer.texts_to_sequences(test_texts)
    test_padded = pad_sequences(test_sequences, maxlen=max_length,
                                padding=padding_type,
                                truncating=trunc_type)

    train_padded = numpy.array(train_padded)
    train_labels = numpy.array(train_labels)
    test_padded = numpy.array(test_padded)
    test_labels = numpy.array(test_labels)

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

    text = [input_text]
    sequences = tokenizer.texts_to_sequences(text)
    padded = pad_sequences(sequences, maxlen=max_length,
                           padding=padding_type, truncating=trunc_type)

    model.load_weights("model_python_weights.h5")
    prediction = model.predict(padded)
    print(prediction)
    return prediction



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=['POST'])
def result():
    news_link = request.form['news_link']
    #url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
    article = Article(news_link)
    article.download()
    article.parse()
    input_text = article.text
    prediction = model_input(input_text)
    return render_template("result.html", model_prediction = prediction)


if __name__ == "__main__":
    app.run(debug=True)