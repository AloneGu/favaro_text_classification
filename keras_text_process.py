#!/usr/bin/env python
# encoding: utf-8

"""
@author: Jackling Gu
@file: keras_text_process.py
@time: 2017-05-19 14:32
"""
import numpy as np
from keras.preprocessing.text import text_to_word_sequence,Tokenizer

texts = ['hello world','hello python','hello hello hello']

print(text_to_word_sequence(texts[0]))
print(text_to_word_sequence(texts[1]))
print(text_to_word_sequence(texts[2]))

# ['hello', 'world']
# ['hello', 'python']
# ['hello', 'hello', 'hello']


tok = Tokenizer(num_words=10)
tok.fit_on_texts(texts)

print(tok.texts_to_sequences(texts))
# [[1, 3], [1, 2], [1, 1, 1]]

print(tok.texts_to_matrix(texts,mode='binary'))
# [[ 0.  1.  1.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  1.  0.  1.  0.  0.  0.  0.  0.  0.]
#  [ 0.  1.  0.  0.  0.  0.  0.  0.  0.  0.]]


print(tok.texts_to_matrix(texts,mode='count'))
# [[ 0.  1.  1.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  1.  0.  1.  0.  0.  0.  0.  0.  0.]
#  [ 0.  3.  0.  0.  0.  0.  0.  0.  0.  0.]]

rd_seq = [[1,2,1,1],[2,1,3,3],[4,5,6]]
new_tok = Tokenizer(num_words=10)
print(new_tok.sequences_to_matrix(rd_seq))
# [[ 0.  1.  1.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  1.  1.  1.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  1.  1.  1.  0.  0.  0.]]
