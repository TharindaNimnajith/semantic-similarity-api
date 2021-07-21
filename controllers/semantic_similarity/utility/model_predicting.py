# importing tensorflow library
# it is a free and open-source software library for machine learning
# used across a range of machine learning related tasks
# focus on training and inference of deep neural networks
import tensorflow as tf
# importing model_from_json function from models module in keras package
from keras.models import model_from_json
# importing roc_auc_score from metrics package of scikit-learn library
# roc_auc_score computes area under the receiver operating characteristic
# curve (roc auc) from prediction scores
from sklearn.metrics import roc_auc_score

# importing preprocess_text function from text_preprocessing module
from text_preprocessing import preprocess_text
# importing transform_text function from text_transforming module
from text_transforming import transform_text


# predicting the relatedness of the two texts
def predict_score(student_answer, model_answer):
    student_answer_preprocessed = preprocess_text(student_answer)
    model_answer_preprocessed = preprocess_text(model_answer)

    student_answer_sequence = transform_text(student_answer_preprocessed)
    model_answer_sequence = transform_text(model_answer_preprocessed)

    similarity_score = loaded_model.predict([student_answer_sequence, model_answer_sequence],
                                            verbose=1)

    return similarity_score


# py_function wraps a python function into a tensorflow op that executes it eagerly
# py_function allows expressing computations in a tensorflow graph as Python functions
# auroc - area under the receiver operating characteristic curve
def auroc(y_true, y_pred):
    return tf.py_function(roc_auc_score,
                          (y_true, y_pred),
                          tf.double)


# reading and loading json file
json_file = open('models/siamese_network_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

# parsing a json model configuration string and returning a model instance
loaded_model = model_from_json(loaded_model_json)

# loading weights into loaded model
loaded_model.load_weights('models/siamese_network_model.h5')

# compiling model
# configuring the model for training
loaded_model.compile(optimizer='adam',
                     loss='binary_crossentropy',
                     metrics=['acc', auroc])
