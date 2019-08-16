#IMPORTS
import pickle
import numpy as np
import pandas as pd
from Constats import Strings


def runProgram(comment):
    #INITIALIZING
    loaded_model = pickle.load(open(Strings.kmean_model_location, 'rb'))
    loaded_selector = pickle.load(open(Strings.selectK_best_model_location+"_cluster", 'rb'))
    count_vectorizer = pickle.load(open(Strings.count_vectorizer_model_location+"_cluster", 'rb'))

    #PREPROCESS INPUT DATA
    extracted_feature = np.asarray(count_vectorizer.get_feature_names())[loaded_selector.get_support()]
    transformed_vector = count_vectorizer.transform([comment])
    dataframe = pd.DataFrame(transformed_vector.toarray(), columns=count_vectorizer.get_feature_names())
    dataframe_filtered = dataframe[extracted_feature]

    #PREDICTION
    predictions = loaded_model.predict(dataframe_filtered)
    print(predictions)
    if predictions[0].round(0) == 0.0:
        return 'CLUSTER 1'
    else:
        return 'CLUSTER 2'
