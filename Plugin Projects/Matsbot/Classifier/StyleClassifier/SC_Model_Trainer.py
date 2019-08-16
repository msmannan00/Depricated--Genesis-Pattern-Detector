#IMPORTS
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.pipeline import Pipeline

import Helper_Method
from Constats import Strings, Status


def runProgram():

    #INITIALIZATION
    dataFrame = pd.read_csv(Strings.data_location, sep =",")
    dataFrame['gender'] = Helper_Method.encode_data('gender',dataFrame)
    tokens_list = dataFrame.columns.values

    #SPLIT TEST TRAIN
    data = dataFrame[tokens_list[0:len(tokens_list)-1]]
    label = dataFrame['gender']
    train_features, test_features, train_labels, test_labels = train_test_split(data, label, test_size = 0.4,shuffle=False)

    #CREATE MODEL
    model = RandomForestClassifier()

    #TRAIN MODEL
    trainedModel = model.fit(train_features, train_labels);

    #PREDICTION
    predictions = trainedModel.predict(test_features)

    #SHOW PREDICTIONS
    print("PREDICTION : ")
    print(predictions.round(0))

    #TRAINNING ENTIRE DATASET
    model = RandomForestRegressor()
    trainedModel = model.fit(data, label)

    #SAVE PICKLE FILE
    f = open(Strings.stylometry_model_location, 'wb')
    pickle.dump(trainedModel, f)
    f.close()

    #SHOW ACCURACY
    Helper_Method.popupmsg("Model Accuracy : " + repr(accuracy_score(test_labels, predictions).round(2)))
    Status.is_app_waiting = False
