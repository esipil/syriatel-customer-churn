# SYRIA TEL CUSTOMER CHURN

Syria Tel is one of the three telecommunication company in Syria. It is a mobile network provider in Syria. Syria Tel needs competitive edge against its competitors including data driven insights on how to improve their business. 

### PROBLEM STATEMENT
Syria Tel has discovered that their customers have started to churn, discontinue their services. This poses a major risk to the company. The challenge is to Build a classifier to predict whether a customer will ("soon") stop doing business with SyriaTel, a telecommunications company

#### OBJECTIVES
1. Determine what features will indicate if a customer will discontinue their services. 
2. To build a predictive model that forecast the likelihood of customer churn in the telecom industry.

## DATA UNDERSTANDING
This project uses data from [Churn in Telcom Dataset](https://www.kaggle.com/datasets/becksddf/churn-in-telecoms-dataset/code).   
The data has 3333 rows of different customer information, with 21  columns representing the different customer information and whether the customer left the  company or not.    
The company is  interested in reducing how much money is lost because of customers who don't stick around very long.

##  MODELLING
The results for the best model: 
Training accuracy: 0.9938574938574939     
Test accuracy: 0.9508196721311475    
F1 score: 0.7999999999999999    
Training AUC : 0.9938574938574939    
Test AUC : 0.8745779202197677    
Test Recall : 0.7722772277227723   

The model test  accuracy score is 0.9546.
The model training AUC is 0.99 while the test AUC is 0.87  
This is a good metric , however, there is an indication of overfitting the training data.  
We could try hyperparameter tune the XGBoost to try and reduce the overfitting and improve model performance

## EVALUATION
I evaluate the models using recall and AUC.    
Recall explains how many of the actual positive cases we were able to predict correctly with our model. This is a good metric to look at because we are concerned of false negatives more than false positives. If we fail to predict a customer will churn, we risk loosing money spent on that customer. We want a model with the best precision.   
AUC measures the ability of a model to distinguish between classes. We want the model that will distinguish the two classes best.    
 
XGBoost model has the best .  
Additionally, it has the best scores for the other metrics, score
XGBoost will be our final model.  
Our best model distinguished between retained and churned customers with an 87% success rate. 
Moreover, it correctly classified  77% of the customers who churned correctly.



