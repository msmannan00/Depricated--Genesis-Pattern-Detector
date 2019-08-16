import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from Constats import Strings, Preferences, Status

pd.options.mode.chained_assignment = None  # default='warn'

def runProgram():

      #READ Comments COMMENTS
      dataset = np.loadtxt(Strings.merged_dataset_location, dtype=np.str, delimiter=':', usecols=range(3))

      #SHUFFLE DATASET AND SAVE TO CSV
      dataframe_filtered = shuffle(dataset[1:])
      dataframe_filtered = np.insert(dataframe_filtered, 0, dataset[0], axis=0)

      pd.DataFrame(dataframe_filtered, dtype=np.str).to_csv(Strings.data_location,index=False,index_label =False,header=False)
      print(dataset)

