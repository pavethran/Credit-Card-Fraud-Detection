# Import libraries  
import pandas as pd  
from sklearn.model_selection import train_test_split  
from imblearn.over_sampling import SMOTE  
from xgboost import XGBClassifier  
from sklearn.metrics import classification_report  

# Load dataset  
data = pd.read_csv('data/Financial_Transactions.csv')  

# EDA  
print(data.isnull().sum())  
print(data['isFraud'].value_counts())  

# Split data  
X = data.drop('isFraud', axis=1)  
y = data['isFraud']  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  

# Handle imbalance with SMOTE  
smote = SMOTE(random_state=42)  
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)  

# Train XGBoost  
model = XGBClassifier()  
model.fit(X_train_res, y_train_res)  

# Evaluate  
y_pred = model.predict(X_test)  
print(classification_report(y_test, y_pred))  
