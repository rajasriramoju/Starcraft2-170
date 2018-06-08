# AINeedUnits

This library of tools provides the functions to convert observed data into intervals which can be fitted into Neural Network.

## GData

GData stands for Game Data. The game datas are obtained through the use of PySC2's observer tools to gather players' 

## Intervals

The folder "Intervals" contains total extracted total data that are split into segments of various sizes depending on the distribution to split them by.

## Trained Models

"Trained Models" contains 

## Utilities 

"Utilities" contains the tools to parse the GData, Intervals. The folder also contains tools to train and test the intervals for model extraction which will be saved into "Trained Models"

### dataExtract.py


### extractModel.py


### getIntervals.py


### modelTemplate.py

This script contains the initialization and configuration of a neural network.

#### NeuralNetwork(train, test, file)

<span style="color:yellow">Dependencies</span>: Pandas, Numpy, Keras

<mark> train </mark>: A pandas dataframe containing same number of columns or features and output as the combined input and output dimensions of neural network.

<mark> test </mark>: Same as the train variable.

<mark> file </mark>: A string typed file name within the current directory of where modelTemplate is located.

Configurations of the neural network can be adjusted. Please see the documentation of the Keras framework.
