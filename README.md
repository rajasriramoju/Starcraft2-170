# AINeedUnits

This library of tools provides the functions to convert observed data into intervals which can be fitted into Neural Network.

## GData

GData stands for Game Data. The game datas are obtained through the use of PySC2's observer tools to gather players' information such as unit types and their counts, resource rates and numbers, and also total cumulative score of the game.

The data we used were imported from the [MSC](https://github.com/wuhuikai/MSC). Specifically we used the global features dataset that can be downloaded from the MSC's markdown readme file. The format of GData can be found in the mark down of the linked repository.

GData elements are the raw data of this project. They will be processed by dataExtract to retrieve necessary features and calculate desire classifcation output.

## Intervals

The folder "Intervals" contains total extracted total data that are split into segments of various sizes depending on the distribution to split them by.

## Trained Models

"Trained Models" contains 

## Utilities 

"Utilities" contains the tools to parse the GData, Intervals. The folder also contains tools to train and test the intervals for model extraction which will be saved into "Trained Models"

### dataExtract.py


### extractModel.py

extractModel loads the 

##### Main(input_file)

- input_file:

### getIntervals.py

This script contains the 

### modelTemplate.py

This script contains the initialization and configuration of a neural network.

##### NeuralNetwork(train, test, file)

- Dependencies: Pandas, Numpy, Keras

- train: A pandas dataframe containing same number of columns or features and output as the combined input and output dimensions of neural network.

- test: Same as the train variable.

- file: A string typed file name within the current directory of where modelTemplate is located.

Configurations of the neural network can be adjusted. Please see the documentation of the Keras framework.
