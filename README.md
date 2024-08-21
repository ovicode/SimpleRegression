This repository contains a Python script that implements a simple linear regression model to analyze biomechanical data. The script performs data splitting, statistical calculations, and evaluates the model's performance using Root Mean Square Error (RMSE). This readme file will guide you through the functionality, usage, and structure of the script.

**Overview**
This script is designed to perform simple linear regression on a given dataset, specifically motion data. The primary objective is to split the dataset into training and testing sets, calculate key statistical metrics, build the regression model, and evaluate its performance using RMSE.

**Dependencies**
The script requires the following Python libraries:

'random'
'math'
These libraries are used for data manipulation, mathematical computations, and random selection during the data splitting process.

**Dataset**
The dataset used in this script is expected to be in a CSV file named motion_data.csv. The CSV file should contain two columns representing the features (independent variables) and the target values (dependent variables). The data is loaded and processed within the script.

**Functions**

**Data Splitting**
split_dataset(list_, ratio): This function splits the dataset into training and testing sets based on the specified ratio. It randomly selects data points for the training set and uses the remaining data for testing.

**Statistical Calculations**
sumList(list_): Calculates the sum of elements in a list.
meanList(list_): Computes the mean (average) of the list elements.
stdevList(list_): Determines the standard deviation of the list elements.
variancelist(list_): Calculates the variance of the list elements.
covariance(x, y): Computes the covariance between two lists, representing the relationship between the independent and dependent variables.

**Regression Model**
coefficientlist(traindata): Calculates the coefficients (intercept and slope) for the linear regression model using the training data.
simple_linear_regression(trainlist, testlist): Predicts the output for the test data using the linear regression model built from the training data.

**Model Evaluation**
root_mean_square(testResult_list): Evaluates the model's performance by calculating the Root Mean Square Error (RMSE) between the predicted and actual values.

**Usage**
To use this script, follow these steps:

Place the motion_data.csv file in the same directory as the script.
Run the script to execute the data splitting, model training, and evaluation processes.
The training and testing datasets will be printed in the console, followed by the model's RMSE value.

**Results**
The script will output the following:

The training and testing datasets after the split.
The RMSE value that indicates the model's performance. Lower RMSE values indicate better performance.

