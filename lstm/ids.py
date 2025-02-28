import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import time
# For LSTM model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.callbacks import EarlyStopping
from keras import optimizers
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

# Load dataset
train = pd.read_csv("https://raw.githubusercontent.com/ayaafathy/Deep-Learning-based-IDS-for-In-Vehicle-Network/main/Datasets/FinalDataset2.csv")
test = pd.read_csv("https://raw.githubusercontent.com/ayaafathy/Deep-Learning-based-IDS-for-In-Vehicle-Network/main/Datasets/testdataset.csv")

train_proccessed = train.iloc[:, 0:13]
test_procecssed = test.iloc[:, 0:13]

features_set=train_proccessed.drop(['Label'],axis=1)
labels=train_proccessed['Label']
labels=np.matrix(labels).reshape((393763,1))

test_set=test_procecssed.drop(['Label'],axis=1)
testlabels=test_procecssed['Label']
testlabels=np.matrix(testlabels).reshape((403858,1))

features_set, labels = np.array(features_set), np.array(labels)
test_set, testlabels = np.array(test_set), np.array(testlabels)

features_set = np.reshape(features_set, (features_set.shape[0], features_set.shape[1], 1))
test_set = np.reshape(test_set, (test_set.shape[0], test_set.shape[1], 1))

# Initialize LSTM model
model = Sequential()
model.add(LSTM(128, return_sequences=False,  activation='sigmoid', input_shape=(features_set.shape[1], 1)))
model.add(Dense(4, activation='softmax'))
opt = optimizers.Adam(lr=0.0001)
model.compile(optimizer = opt , loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(features_set, labels, epochs=250, batch_size=512)