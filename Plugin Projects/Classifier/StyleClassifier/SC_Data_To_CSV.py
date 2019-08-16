import os
import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from pandas import Series, DataFrame
from sklearn.pipeline import Pipeline
from sklearn.utils import shuffle

import Helper_Method
from Constats import Strings, Preferences, Status

pd.options.mode.chained_assignment = None  # default='warn'

def runProgram() -> object:

      #READ positive COMMENTS
      file_data = np.empty([0,0])
      positive_count = 0
      for filename in os.listdir(Strings.positive_dataset_location):
            text = open(Strings.positive_dataset_location_file + filename, 'r', encoding="utf8")
            file_data = np.append(file_data,Helper_Method.stylometryFilter(text.read()))
            positive_count += 1

      #READ negative COMMENTS
      for filename in os.listdir(Strings.negative_dataset_location):
            text = open(Strings.negative_dataset_location_file + filename, 'r', encoding="utf8")
            file_data = np.append(file_data,Helper_Method.stylometryFilter(text.read()))

      #CREATE CSV
      count_vectorizer = CountVectorizer(analyzer='char',ngram_range=(1, Status.vector_analyser_range))
      transformed_vector = count_vectorizer.fit_transform(file_data)
      dataframe = pd.DataFrame(transformed_vector.toarray(), columns=count_vectorizer.get_feature_names())

      #SAVING COUNT VECTORIZER
      f = open(Strings.count_vectorizer_model_location+"_style", 'wb')
      pickle.dump(count_vectorizer, f)
      f.close()

      #SETTING KNOWN GENDER OUTPUT VECTOR
      dataframe['gender'] = Series('negative', index=dataframe.index)
      dataframe.gender.iloc[0:positive_count] = 'positive'

      #SHUFFLE DATASET AND SAVE TO CSV
      dataframe = shuffle(dataframe)
      dataframe.to_csv(Strings.data_location, encoding='utf-8', index=False)
