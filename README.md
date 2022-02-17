# Taxi trip time Prediction

## Introduction
The competition dataset is based on the 2016 NYC Yellow Cab trip record data made available in Big Query on Google Cloud Platform. The data was originally published by the NYC Taxi and Limousine Commission (TLC). The data was sampled and cleaned for the purposes of this playground competition. Based on individual trip attributes, participants should predict the duration of each trip in the test set.

The studied dataset contains weather information which are the features (Trip duration, pickup and dropoff location in terms of latitudea and logtitude, number of passengers and datatime of puckup and dropoff etc), the target is time required for trip to complete. The dataset presents the company's data between janurary and june 2016

We started with loading the data, then we did Exploratory Data Analysis (EDA), null values treatment, feature selection, encoding of categorical columns, and then model building. In all of these models, our r2 ranges from 0.60 to 0.73, which can be said to be good for such a large dataset. This performance could be due to various reasons like the proper pattern of data, large data, or because of the relevant features.
 
We performed variable importance analysis to find the most significant variables for all the models developed with the given data sets. We are getting the best results from xgboost.

## Problem Statement
Your task is to build a model that predicts the total ride duration of taxi trips in New York City. Your primary dataset is one released by the NYC Taxi and Limousine Commission, which includes pickup time, geo-coordinates, number of passengers, and several other variables.

## Models used 
* Linear Regression
* Desision Tree Regression
* Random Forest Regression
* XGBoost Regression
* LightGBM Regression

## Deployment of Streamlit WebApp in Heroku and Streamlit

We have created front-end using Streamlit for the webapp. whose deployments link are as follows 

| Website | Link |
| ------ | ------ |
| Github | https://github.com/Ali-Asgar-Lakdawala/my-ml-deployment-2 |
| Heroku | https://my-ml-deployment-2.herokuapp.com/ |
| Streamlit | https://share.streamlit.io/ali-asgar-lakdawala/my-ml-deployment-2/main/app.py|

## Conclusion

* In all of these models, our MAPE revolves in the range of 0.32 TO 0.42.with the best fit model as LightGBM
* We were successfull in deploying the strealit app on heruko .

