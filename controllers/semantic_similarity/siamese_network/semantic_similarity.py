# importing sys module
# used to access objects used or maintained by the interpreter and to functions
# that interact strongly with the interpreter
# import sys

# appending a relative path to the top package to the search path
# sys.path.append('../')

# importing predict_score function from model_predicting module in utility package
from ..utility.model_predicting import predict_score


# function to return the predicted similarity score between the two input texts
def get_semantic_similarity(student_answer, model_answer):
    return predict_score(student_answer, model_answer)
