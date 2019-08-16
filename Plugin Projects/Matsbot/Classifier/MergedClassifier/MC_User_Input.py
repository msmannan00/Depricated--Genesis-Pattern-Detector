#IMPORTS
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

import Helper_Method
from Constats import Strings


def runProgram(comment):
    #INITIALIZING
    loaded_model = pickle.load(open(Strings.wordgram_model_location, 'rb'))
    tokens_list = pd.read_csv(Strings.data_location, sep =",").columns.values

    #PREPROCESS INPUT DATA
    comment = comment.replace('\n', '')
    dataFrame = comment.split(",")
    dataFrame = np.array(dataFrame)

    dataframe = pd.DataFrame([dataFrame],columns=tokens_list[0:2])

    #PREDICTION
    predictions = loaded_model.predict(dataframe)
    print(predictions)
    if predictions[0].round(0) == 0.0:
        return 'THIS PRICE BOND NUMBER ['+ dataFrame[0] +'] WILL NOT WORK'
    else:
        return 'THIS PRICE BOND NUMBER ['+ dataFrame[0] +'] WILL WORK'
