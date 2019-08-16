#IMPORTS
import pickle
import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

import Helper_Method
from Constats import Strings, Status


def runProgram():

    #INITIALIZATION
    dataFrame = pd.read_csv(Strings.data_location, sep =",")
    dataFrame['_!gender!_'] = Helper_Method.encode_data('_!gender!_',dataFrame)
    tokens_list = dataFrame.columns.values

    #SPLIT TEST TRAIN
    data = dataFrame[tokens_list[0:len(tokens_list)-1]]
    label = dataFrame['_!gender!_']
    train_features, test_features, train_labels, test_labels = train_test_split(data, label, test_size = 0.4,shuffle=False)

    #CREATE AND TRAIN MODEL
    agglomerative_clustering = AgglomerativeClustering(n_clusters=2).fit(train_features,train_labels)

    #PREDICTION
    predictions = agglomerative_clustering.fit_predict(test_features)

    #SHOW ACCURACY
    agglomerative_clustering = KMeans(n_clusters=2).fit(data,label)
    Helper_Method.popupmsg("Model Accuracy : " + repr(accuracy_score(test_labels, predictions).round(2)))
    Status.is_app_waiting = False

    #SAVE PICKLE FILE
    f = open(Strings.agglomerative_model_location, 'wb')
    pickle.dump(agglomerative_clustering, f)
    f.close()
    Status.is_app_waiting = False
