import keras
from keras.models import Sequential
from keras.models import model_from_json
import os
import numpy as np

# loading model from json file and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights("model-weights.h5")

# reading accuracies
file = open('accuracy.txt', 'r')
accuracy_scores = []
for line in file.readlines():
    accuracy_scores.append(float(line.replace('\n', '')))

training_acc = accuracy_scores[0]
testing_acc = accuracy_scores[1]

def predict_class(conv_systolic, conv_diastolic, conv_avg_bp, conv_heart_rate, conv_glucose, conv_spo2, conv_weight, conv_height, conv_imc):
    # reading max values
    f = open('max_values.txt', 'r')
    max_values = []
    for line in f.readlines():
        max_values.append(float(line.replace('\n','')))

    # scaling new data from computed max values
    conv_systolic = conv_systolic/max_values[0]
    conv_diastolic = conv_diastolic/max_values[1]
    conv_avg_bp = conv_avg_bp/max_values[2]   
    conv_heart_rate = conv_heart_rate/max_values[3]
    conv_glucose = conv_glucose/max_values[4]
    conv_spo2 = conv_spo2/max_values[5]
    conv_weight = conv_weight/max_values[6]
    conv_height = conv_height/max_values[7]
    conv_imc = conv_imc/max_values[8]

    # Creating a vector array for feeding into the Neural Network
    test_values = [[conv_systolic, conv_diastolic, conv_avg_bp, conv_heart_rate, conv_glucose, conv_spo2, conv_weight, conv_height, conv_imc]]
    
    #Compiling the loaded model 
    loaded_model.compile(loss = 'categorical_crossentropy', optimizer='adamax', metrics=['accuracy'])
    
    # This function will predict the class for the new given values
    result = loaded_model.predict_classes(test_values, verbose=1)

    return result



def get_training_acc():
    return training_acc

def get_testing_acc():
    return testing_acc