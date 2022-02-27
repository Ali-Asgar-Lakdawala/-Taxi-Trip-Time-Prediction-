# Taxi trip time Prediction
## Introduction
The competition dataset is based on the 2016 NYC Yellow Cab trip record data made available in Big Query on Google Cloud Platform. The data was originally published by the NYC Taxi and Limousine Commission (TLC). The data was sampled and cleaned for the purposes of this playground competition. Based on individual trip attributes, participants should predict the duration of each trip in the test set.

The studied dataset contains weather information which are the features (Trip duration, pickup and dropoff location in terms of latitudea and logtitude, number of passengers and datatime of puckup and dropoff etc), the target is time required for trip to complete. The dataset presents the company's data between janurary and june 2016

We started with loading the data, then we did Exploratory Data Analysis (EDA), null values treatment, feature selection, encoding of categorical columns, and then model building. In all of these models, our r2 ranges from 0.60 to 0.73, which can be said to be good for such a large dataset. This performance could be due to various reasons like the proper pattern of data, large data, or because of the relevant features.
 
We performed variable importance analysis to find the most significant variables for all the models developed with the given data sets. We are getting the best results from xgboost.

## Problem Statement
Your task is to build a model that predicts the total ride duration of taxi trips in New York City. Your primary dataset is one released by the NYC Taxi and Limousine Commission, which includes pickup time, geo-coordinates, number of passengers, and several other variables.

## Data Description
The dataset is based on the 2016 NYC Yellow Cab trip record data made available in Big Query on Google Cloud Platform. The data was originally published by the NYC Taxi and Limousine Commission (TLC). The data was sampled and cleaned for the purposes of this project. Based on individual trip attributes, you should predict the duration of each trip in the test set.
NYC Taxi Data.csv - the training set (contains 1458644 trip records)
Data fields
* id - a unique identifier for each trip
* vendor_id - a code indicating the provider associated with the trip record
* pickup_datetime - date and time when the meter was engaged
* dropoff_datetime - date and time when the meter was disengaged
* passenger_count - the number of passengers in the vehicle (driver entered value)
* pickup_longitude - the longitude where the meter was engaged
* pickup_latitude - the latitude where the meter was engaged
* dropoff_longitude - the longitude where the meter was disengaged
* dropoff_latitude - the latitude where the meter was disengaged
* store_and_fwd_flag - This flag indicates whether the trip record was held in vehicle memory before sending to the vendor because the vehicle did not have a connection to the server - Y=store and forward; N=not a store and forward trip
* trip_duration - duration of the trip in seconds

## Steps involved:

### Exploratory Data Analysis
After loading the dataset we compared our target variable that is the trip_duration with other independent variables. This process helped us figure out various aspects and relationships among the dependent and the independent variables. It gave us a better idea of which feature behaves in which manner compared to the dependent variable.
![](https://github.com/Ali-Asgar-Lakdawala/-Taxi-Trip-Time-Prediction-/blob/main/photos/eda.JPG)
###Null values Treatment
Our dataset didn’t have any null values to be treated.

###Outliers treatment 
This data set contained tons of outliers as some of the locations had some pickup and drop-off locations or had distances less than 200 meters and time more than an hour.

###Feature engineering
Datetime feature was converted into bins and then to binary values by one-hot encoding 

###Feature Selection
In these steps, we used correlation, VIF analysis to check the results of each feature i.e which feature is more important compared to our model and which is of less importance.

###Standardization of features
Our main motive through this step was to scale our data into a uniform format that would allow us to utilize the data in a better way while performing fitting and applying different algorithms to it.
The basic goal was to enforce a level of consistency or uniformity to certain practices or operations within the selected environment.


### Fitting different models
For modeling, we tried various classification algorithms like:
* Linear Regression
* Desision Tree Regression
* Random Forest Regression
* XGBoost Regression
* LightGBM Regression

### Tuning the hyperparameters for better accuracy
Tuning the hyperparameters of respective algorithms is necessary for getting better accuracy and to avoid overfitting in the case of tree-based models like Random Forest Classifier and XGBoost classifier.

### Features Explainability 
We have applied SHAP on the XGBoost and CatBoost model to determine the features that were most important while predicting an instance
And also build a feature importance graph to find out which features were important and which were redundant in a model

### Performance Metrics
![](https://github.com/Ali-Asgar-Lakdawala/-Taxi-Trip-Time-Prediction-/blob/main/photos/performance%20metrics.JPG)


## Deployment of Streamlit WebApp in Heroku and Streamlit

We have created front-end using Streamlit for the webapp. whose deployments link are as follows 

| Website | Link |
| ------ | ------ |
| Github | https://github.com/Ali-Asgar-Lakdawala/my-ml-deployment-2 |
| Heroku | https://my-ml-deployment-2.herokuapp.com/ |
| Streamlit | https://share.streamlit.io/ali-asgar-lakdawala/my-ml-deployment-2/main/app.py|

## Conclusion
* we got the best fit model as lightGBM whith MAPE of 0.38 and adjusted R2 of 0.70.
* We were successfull in deploying the strealit app on heruko .

