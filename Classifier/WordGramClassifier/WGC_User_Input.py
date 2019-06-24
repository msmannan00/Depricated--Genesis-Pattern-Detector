#IMPORTS
import pickle
import numpy as np
import pandas as pd
from Constats import Strings
from Constats import Status
import glob, os


def runProgram(comment):
    #INITIALIZING
    loaded_model = pickle.load(open(Strings.wordgram_model_location, 'rb'))
    loaded_selector = pickle.load(open(Strings.selectK_best_model_location+"_wordgram", 'rb'))
    count_vectorizer = pickle.load(open(Strings.count_vectorizer_model_location+"_wordgram", 'rb'))

    #PREPROCESS INPUT DATA
    extracted_feature = np.asarray(count_vectorizer.get_feature_names())[loaded_selector.get_support()]

    if(Status.is_report_prediction == False):
        f = open("C:\\xampp\\htdocs\\desim\\visualization\\\mvisual.txt", "w")
        f.write("")
        f.close

        root = "C:\\xampp\\htdocs\\desim\\Extracted_Source\\Software"
        content = ""
        list = []
        for path, subdirs, files in os.walk(root):
            for name in files:
                list.append(path+"\\"+name)

        for i in list:

            f = open(i, "r", encoding="utf-8",errors='ignore')
            f_contents = f.read()

            transformed_vector = count_vectorizer.transform([f_contents])
            dataframe = pd.DataFrame(transformed_vector.toarray(), columns=count_vectorizer.get_feature_names())
            dataframe_filtered = dataframe[extracted_feature]

            #PREDICTION
            predictions = loaded_model.predict(dataframe_filtered)

            if predictions[0].round(0) == 0.0:
                content += i + " | " + "NEGATIVE"+"-newstart-\n"
            else:
                content += i + " | " + "POSITIVE"+"-newstart-\n"
            f.closed

        f = open("C:\\xampp\\htdocs\\desim\\visualization\\\mvisual.txt", "w+")
        f.write(content)
        f.close
        return 'PREDICTION REPORTED TO DASHBOARD'
    else:
        transformed_vector = count_vectorizer.transform([comment])
        dataframe = pd.DataFrame(transformed_vector.toarray(), columns=count_vectorizer.get_feature_names())
        dataframe_filtered = dataframe[extracted_feature]

        #PREDICTION
        predictions = loaded_model.predict(dataframe_filtered)
        print(predictions)

        if predictions[0].round(0) == 0.0:
            return 'NEGATIVE'
        else:
            return 'POSITIVE'
