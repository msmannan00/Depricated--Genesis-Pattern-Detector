import os
import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from pandas import Series
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.utils import shuffle
from Constats import Strings, Preferences, Status

pd.options.mode.chained_assignment = None  # default='warn'

def runProgram():

      #READ positive COMMENTS
      file_data = np.empty([0,0])
      positive_count = 0
      for filename in os.listdir(Strings.positive_dataset_location):
            text = open(Strings.positive_dataset_location_file + filename, 'r', encoding="utf8")
            file_data = np.append(file_data,text.read())
            positive_count += 1

      #READ negative COMMENTS
      for filename in os.listdir(Strings.negative_dataset_location):
            text = open(Strings.negative_dataset_location_file + filename, 'r', encoding="utf8")
            file_data = np.append(file_data,text.read())

      #CREATE CSV
      count_vectorizer = CountVectorizer(analyzer=Status.vector_analyser_type,ngram_range=(1, Status.vector_analyser_range),max_features=Status.kbest_threshhold)
      transformed_vector = count_vectorizer.fit_transform(file_data)
      dataframe = pd.DataFrame(transformed_vector.toarray(), columns=count_vectorizer.get_feature_names())

      #SETTING KNOWN GENDER OUTPUT VECTOR

      output_array = np.full((1, len(dataframe)), 1)
      output_array[0][0:positive_count] = 0
      output_array = output_array[0]

      selector = SelectKBest(score_func=chi2, k=Status.kbest_threshhold)
      selector.fit(dataframe,output_array)
      extracted_data = selector.transform(dataframe)
      extracted_feature = np.asarray(count_vectorizer.get_feature_names())[selector.get_support()]

      #SHUFFLE DATASET AND SAVE TO CSV
      dataframe['_!gender!_'] = Series('negative', index=dataframe.index)
      dataframe['_!gender!_'].iloc[0:positive_count] = 'positive'
      dataframe_filtered = shuffle(dataframe)
      dataframe_filtered.to_csv(Strings.data_location, encoding='utf-8', index=False)

      #SAVING COUNT VECTORIZER
      f = open(Strings.count_vectorizer_model_location+"_cluster", 'wb')
      pickle.dump(count_vectorizer, f)
      f.close()

      #SAVING SelectKBest
      f = open(Strings.selectK_best_model_location+"_cluster", 'wb')
      pickle.dump(selector, f)
      f.close()
