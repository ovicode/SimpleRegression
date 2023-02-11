#!/usr/bin/env python
# coding: utf-8

# In[29]:


#Created on 10/18/2022

#author: Ifeoluwa Olawore

#lab9

#Task
#import relevant libraries
import random as rd
import math

#define function to split dataset from list of data given
def split_dataset(list_,ratio):
    train_ = round(len(list_) * ratio)
    train_set = []
    test_set = []
    while len(train_set) < train_:
            ind = rd.randint(0,len(list_)-1)
            train_set.append(list_[ind])
            list_.pop(ind) #delete values selected in train set
    test_set = list_
    return train_set,test_set

#define function for summing up
def sumList(list_):
    sum_ = 0
    for values in list_:
        sum_ += values
    return sum_
#define mean using sum method
def meanList(list_):
    length = len(list_)
    mean_ = sumList(list_)/length
    return mean_
#define standard deviation method
def stdevList(list_):
    deviation = 0
    for val in list_: 
        deviation += (val-meanList(list_))**2
        standard_dev = math.sqrt(deviation/len(list_))
    return standard_dev
#function to calculate the variance of the list
def variancelist(list_):
    deviation = 0
    for val in list_: 
        deviation += (val-meanList(list_))**2
        variance = deviation/len(list_)
    return variance
#function to calculate the covariance of the two lists using the formular provided
def covariance(x,y): 
    cov = 0.0
    mean_x = meanList(x)
    mean_y = meanList(y)
    for val in range(len(x)):
        cov += (x[val]-mean_x) * (y[val]-mean_y)
    return cov/len(x)-1
        
#function to calculate coefficients of the input training set list  
def coefficientlist(traindata):
    x_list = [val[0] for val in traindata]
    y_list = [val[0] for val in traindata]
    b1 = covariance(x_list,y_list)/variancelist(x_list)
    b0 = meanList(y_list)-b1 * meanList(x_list)
    return b0,b1

#function for regression model and testing it
def simple_linear_regression(trainlist,testlist): 
    b0,b1 = coefficientlist(trainlist)
    test_result = []
    for item in testlist:
        y_predict = b0 +b1*item[0]
        test_result.append([item[1],y_predict])
    return test_result

#function to evaluate the performance using root mean square
def root_mean_square(testResult_list): 
    error_ = 0
    for val in testResult_list: 
        error_ += (val[0]-val[1])**2
    final = math.sqrt((error_ /len(testResult_list)))
    return final

data = []
#open file from source
with open ("salary.csv","r") as f: 
    for values in f.readlines():
        col1 = values.strip()
        col2 = col1.split(",")
        data.append(col2)# apend split data into list

#call splitdata function to separate train from test        
train_set,test_set = split_dataset(data,0.75)
print(f"The training data is {train_set}") 
print(f"The test data is {test_set}")
for val in train_set: 
    val[0]= float(val[0])
    val[1]= float(val[1])
for val in test_set: 
    val[0]= float(val[0])
    val[1]= float(val[1])

#call the regression function to test the model
regression = simple_linear_regression(train_set,test_set)
#call the rmse function to evaluate performance
rmse = root_mean_square(regression)
print(f"The model performance root mean square values is {rmse:.2f}")
       

