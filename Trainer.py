import pandas as pd
import numpy as np
import keyboard
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import pickle

# = ['A','B','C','D','E','F','Fuck U','G','H','I','J','K','L','M','N','O','P','Q','R','Rest','S','T','U','V','W','X','Y','Z']
#alphabet = ['A','B','C','D','E','Rest']
alphabet = ['H','E','L','O','W','R','D','Rest']

def get_numerical(categorical):
    numerical = []

    for index in range(0,len(categorical)):
        letter = categorical[index]
        num = alphabet.index(letter)
        numerical.append(num)

    return numerical

trainData = pd.read_csv('letterDirectory/trainData.csv') #Add file name to path

testData = pd.read_csv('letterDirectory/testData.csv')

col_numerical = get_numerical(trainData['Letter'])
trainData.insert(loc=0, column='Label',value=col_numerical)

col_numerical = get_numerical(testData['Letter'])
testData.insert(loc=0, column='Label',value=col_numerical)

X_train = trainData.drop(labels=['Label','Letter', 'File Name'], axis='columns')

X_test = testData.drop(labels=['Label','Letter', 'File Name'], axis='columns')

Y_train = trainData['Label']     #X refers to data / Y refers to labels

Y_test = testData['Label']

model = KNeighborsClassifier(n_neighbors = 4, metric = 'minkowski', weights='distance', p = 2)
model.fit(X_train, Y_train)

train_acc = model.score(X_train, Y_train)
test_acc = model.score(X_test, Y_test)
#predLetter = model.predict(X_test)
#pred_acc = accuracy_score(Y_test, pred)

print("Training Accuracy: " + str(train_acc))
print("Testing Accuracy: " + str(test_acc))
#print("Model Accuracy: " + str(pred_acc))

#model_name = "Model_" +  str(round(test_acc, 4)) + ".pkl"
model_name = "Hello.pkl"

with open(model_name,'wb') as f:
     pickle.dump(model,f)