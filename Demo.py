import serial
import pickle
import keyboard
import time
import numpy as np
import warnings
import os

clear = os.system('cls')

displayString = ''

currentLetter = None
lastLetter = 'Rest'

warnings.filterwarnings('ignore') 

lastTime = time.time()
currentTime = None
elapsedTime = None

alphabet = ['A','B','C','D','E','F','Fuck U','G','H','I','J','K','L','M','N','O','P','Q','R','Rest','S','T','U','V','W','X','Y','Z']

def updateDisplay():
    os.system('cls')
    print("Current Letter: " + currentLetter)
    print("Phrase: " + displayString)

serialBus = serial.Serial(
    port="com6",
    baudrate=9600,
    timeout=1
)

with open('Model.pkl', 'rb') as f:
    model = pickle.load(f)

while not keyboard.is_pressed('q'):
    currentTime = time.time()
    elapsedTime = currentTime - lastTime

    data = serialBus.readline()
    sample = data.decode('utf', errors='ignore').strip()
    sample = sample.split(',')

    if len(sample) == 5:
        #os.system('cls')
        #qqprint(sample)
        sample = np.reshape(sample, (1,-1))

        pred = model.predict(sample)
        #prob = model.predict_proba(sample)[0][alphabet.index(predictedLetter)]
        currentLetter = alphabet[pred[0]]

        if lastLetter == currentLetter and not currentLetter == 'Rest':
            if elapsedTime > 2:

                lastLetter = currentLetter
                displayString = displayString + currentLetter

                lastTime = currentTime
                updateDisplay()
            
        else:
            lastLetter = currentLetter
            lastTime = currentTime
            updateDisplay()
        

