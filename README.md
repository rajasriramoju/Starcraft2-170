# AINeedUnits

This library of tools provides the functions to convert observed data into intervals which can be fitted into Neural Network. The Neural Networks then can be saved into h5 files which can be reloaded to predict which unit is the most desirable to produce.

GData and Intervals contain sample datas as the orginal files are larger than github's limit.

## DistributionGraphs

Images of distribution for neural network population. The configuration values are in the title. These values can be inserted getInterval.py to separate a total dataset into interval datasets with corresponding size to the distribution.

## GData

GData stands for Game Data. The game datas are obtained through the use of PySC2's observer tools to gather players' information such as unit types and their counts, resource rates and numbers, and also total cumulative score of the game.

The data we used were imported from the [MSC](https://github.com/wuhuikai/MSC). Specifically we used the global features dataset that can be downloaded from the MSC's markdown readme file. MSC has  The format of GData can be found in the mark down of the linked repository.

GData elements are the raw data of this project. They will be processed by dataExtract to retrieve necessary features and calculate desire classifcation output.

## Intervals

The folder "Intervals" contains total extracted total data that are split into segments of various sizes depending on the distribution to split them by.

## Trained Models

"Trained Models" contains h5 extension typed files which essentially are saved neural network models. To utilized these models, simply use `` model = load_model(ex.h5) `` from Keras. Thus you can predict new values from the loaded model.

## Utilities 

"Utilities" contains the tools to parse the GData, Intervals. The folder also contains tools to train and test the intervals for model extraction which will be saved into "Trained Models"

### dataExtract.py

DataExtract goes into the protoss path to find all the replay games' npz files for processing. The "Most Beneficial Unit" which is a new dimension of data is calculated through using the next frame's friendly unit types and their corresponding counts to subtract the current frame. The max of those differences will indicate the need to create this unit to converge to the next frame which has the future optimal army formation. The new column will then have the correspond unit names encoding into a value using the unit-value dictionary at the top of the file. All replay games' frame will then be appended into one single npy file for process.

The dimensions of the resulting npy file are:

| Cumulative | Frame ID | Minerals | Vespene | Food Cap | Food Used | Food Army | Food Worker | Idle Worker Count | Army Count | Warp Gate Count | 19 Friendly Protoss Units | 19 Enemy Protoss Units | Most Beneficial Unit |
|------------|----------|----------|---------|----------|-----------|-----------|-------------|-------------------|------------|-----------------|---------------------------|------------------------|----------------------|

Please see the list call [unit](https://github.com/rajasriramoju/Starcraft2-170/blob/master/Utilities/dataExtract.py) for friendly and enemy protoss unit orders. 

### extractModel.py

ExtractModel loads the the data parsed and combined by the dataExtract script. The extractModel fits the data into the pandas dataframe and train test split by 75-25 percents ratio.

##### Main(input_file)

- input_file: A string typed file name within the current directory of where extractModel is located.

### getIntervals.py and gameIntervals.py

This script contains the the code transform the npy file from dataExtract.py to intervals based on the specified distributions that can be tweaked and defined on the top of the page. Default setting is at 20 neural networks with uniform distribution. 

GameIntervals.py is a similar script to getIntervals.py, but instead of a collection game frames it runs on a single game to split it into correspondly intervals of time stamped data for neural network training and testing.

### modelTemplate.py

This script contains the initialization and configuration of a neural network. Specifically in the NeuralNetwork function.

##### NeuralNetwork(train, test, file)

- Dependencies: Pandas, Numpy, Keras

- train: A pandas dataframe containing same number of columns or features and output as the combined input and output dimensions of neural network.

- test: Same as the train variable.

- file: A string typed file name within the current directory of where modelTemplate is located.

Configurations of the neural network can be adjusted. Please see the documentation of the Keras framework.

### visual.py

This script loads saved neural network models from extractModel.py. Predict method then executes after loading to utilize and demonstrate the functionality of the loaded model.
