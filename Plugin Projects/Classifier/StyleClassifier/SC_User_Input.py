#IMPORTS
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

import Helper_Method
from Constats import Strings


def runProgram(comment):
    #INITIALIZING
    loaded_model = pickle.load(open(Strings.stylometry_model_location, 'rb'))
    count_vectorizer = pickle.load(open(Strings.count_vectorizer_model_location+"_style", 'rb'))

    #PREPROCESS INPUT DATA
    transformed_vector = count_vectorizer.transform([Helper_Method.stylometryFilter(comment)])
    dataframe = pd.DataFrame(transformed_vector.toarray(), columns=count_vectorizer.get_feature_names())

    #PREDICTION
    predictions = loaded_model.predict(dataframe)
    print(predictions)
    if predictions[0].round(0) == 0.0:
        return 'YOU ARE positive'
    else:
        return 'YOU ARE negative'
