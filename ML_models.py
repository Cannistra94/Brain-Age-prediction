import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import RepeatedKFold, KFold, cross_val_score, GridSearchCV
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from scipy import stats

#reading csv generated with imaging data

traindata=pd.read_csv("healthy.csv", header=0)
testdata1=pd.read_csv("acutepain.csv",header=0)
testdata2=pd.read_csv("chronicpain.csv",header=0)

x_train=traindata.iloc[:,:]
y_train_=traindata['Age']
x_test_1=testdata1.iloc[:,:]
y_test_1=testdata1['Age']
x_test_2=testdata2.iloc[:,:]
y_test_2=testdata2['Age']

# Fit scaler on training data and transform both training and test data
X_train_scaled = scaler.fit_transform(x_train_forcv.iloc[:,0:165]) #first 165 columns are t1w
x_test_1_scaled = scaler.transform(x_test_1.iloc[:,0:165])
x_test_2_scaled = scaler.transform(x_test_2.iloc[:,0:165])

#initializating models and parameters to be optimized

# Define the Random Forest model
rf = RandomForestRegressor(random_state=42)

# Define the hyperparameters to tune
rf_param_grid = {
    'n_estimators': [100, 200, 300],        
    'max_depth': [10, 20, 30],              
    'min_samples_split': [2, 5, 10],        
    'min_samples_leaf': [1, 2, 4]            
}

# Define the Support Vector Regression model
svr = SVR()

# Define the hyperparameters to tune
svr_param_grid = {
    'kernel': ['linear', 'rbf'],            # Type of kernel function
    'C': [0.1, 1, 10, 100],                 # Regularization parameter
    'epsilon': [0.01, 0.1, 0.2],            # Epsilon in the epsilon-SVR model
    'gamma': ['scale', 'auto']              # Kernel coefficient (for ‘rbf’ and others)
}

#other models
lasso=Lasso(alpha=1) #lasso
resnet=Lasso(alpha=0.5) #res-net
linear_regression=Lasso(alpha=0.01) #LR

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=rf, param_grid=rf_param_grid, cv=5, n_jobs=-1, verbose=2)

# Fit the model on the entire training set
grid_search.fit(X_train_scaled, y_train_)

# Get the best model
best_model = grid_search.best_estimator_

best_model.fit(X_train_scaled, y_train_)

# Fit the model on the entire training set


# Make predictions on the test set
prediction_test_1 = best_model.predict(x_test_1_scaled)
prediction_test_2 = best_model.predict(x_test_2_scaled)

# Assuming testdata_y and prediction are your arrays
correlation_real_pred_test, p_value = pearsonr(y_test_1, prediction_test_1)
print(f"Pearson correlation coefficient on Test 1: {correlation_real_pred_test}")
print(f"P-value: {p_value}")

correlation_real_pred_test_2, p_value_2 = pearsonr(y_test_2, prediction_test_2)
print(f"Pearson correlation coefficient on Test 2: {correlation_real_pred_test_2}")
print(f"P-value: {p_value_2}")

#extracting delta
delta_1=prediction_test_1-y_test_1
delta_2=prediction_test_2-y_test_2
print('delta on AP:', np.mean(delta_1))
print('delta on CP:', np.mean(delta_2))


#assess age-bias
correlation_real_pred_test_delta_1, p_value_delta_1 = pearsonr(y_test_1, delta_1)
print(f"Age bias on Test 1: {correlation_real_pred_test_delta_1}")
print(f"P-value: {p_value_delta_1}")

correlation_real_pred_test_delta_2, p_value_delta_2 = pearsonr(y_test_2, delta_2)
print(f"Age bias on Test 2: {correlation_real_pred_test_delta_2}")
print(f"P-value: {p_value_delta_2}")

# Mean Absolute Error for Test 1 and Test 2
mae_test_1 = mean_absolute_error(y_test_1, prediction_test_1)
mae_test_2 = mean_absolute_error(y_test_2, prediction_test_2)
print(f"Mean Absolute Error on Test 1: {mae_test_1}")
print(f"Mean Absolute Error on Test 2: {mae_test_2}")

# R-squared for Test 1 and Test 2
r2_test_1 = r2_score(y_test_1, prediction_test_1)
r2_test_2 = r2_score(y_test_2, prediction_test_2)
print(f"R-squared on Test 1: {r2_test_1}")
print(f"R-squared on Test 2: {r2_test_2}")


# store predictions and corresponding Ids for both test sets
predictions_test_1_df = pd.DataFrame({
    'eid': x_test_1['eid'],            
    'RF_T1': prediction_test_1,
    'Age': y_test_1,                 
    'Delta': delta_1                 # Including the delta (prediction error)
})

predictions_test_2_df = pd.DataFrame({
    'eid': x_test_2['eid'],            # Assuming 'Id' is the column name in x_test_2
    'RF_T1': prediction_test_2,
    'Age': y_test_2,                 # Including actual Age for reference
    'Delta': delta_2                 # Including the delta (prediction error)
})

# Save the predictions to CSV files if needed
predictions_test_1_df.to_csv('predictions_AP_randomforest_T1.csv', index=False)
predictions_test_2_df.to_csv('predictions_CP_randomforest_T1.csv', index=False)
