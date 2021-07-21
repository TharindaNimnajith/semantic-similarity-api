# importing utilities for preprocessing sequence data from
# keras library
from keras.preprocessing.sequence import pad_sequences

# importing Tokenizer from keras library
# keras is a high-level api of tensorflow
# keras.preprocessing.text provides keras data preprocessing utils
# to pre-process datasets with textual data before they are fed to the
# machine learning model
from keras.preprocessing.text import Tokenizer

# Tokenizer allows to vectorize a text corpus, by turning each text into
# either a sequence of integers (each integer being the index of a token
# in a dictionary) or into a vector where the coefficient for each token
# could be binary, based on word count, based on tf-idf
tokenizer = Tokenizer()

# defining a maximum sequence length based on the distribution
# plot observations
maximum_sequence_length = 30


def transform_text(text):
    # transforming text to a sequence of integers
    sequence = tokenizer.texts_to_sequences([text])[0]

    # pad_sequences pads sequences to the same length
    # padding='post' to pad after each sequence
    sequence = pad_sequences([sequence],
                             maxlen=maximum_sequence_length,
                             padding='post')

    return sequence[0]
