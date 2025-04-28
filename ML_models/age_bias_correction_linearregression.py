#age bias correction using linear regression
#only training data is used in the model
import statsmodels.api as sm

data=pd.read_csv("imaging1_hc_allmod_ovhealthrating.csv", header=0)

# Add a constant to the model (intercept)
X = sm.add_constant(data[['Age', 'Sex']])
y = data['LR_ALL']

# Fit the model
model = sm.OLS(y, X).fit()

# Extract coefficients and intercept
intercept = model.params['const']
age_coeff = model.params['Age']
gender_coeff = model.params['Sex']

print(f'Intercept: {intercept}')
print(f'Coefficient for Age: {age_coeff}')
print(f'Coefficient for Gender: {gender_coeff}')

#bias correction for test sets using the coefficients previosly extracted

data_AP=pd.read_csv("predictions_AP_randomforest_T1.csv", header=0)
data_CP=pd.read_csv("predictions_CP_randomforest_T1.csv", header=0)

delta_1=data_AP['RF_T1']-data_AP['Age']
delta_2=data_CP['RF_T1']-data_CP['Age']

print('delta on AP:', np.mean(delta_1))
print('delta on AP:', np.mean(delta_2))

corrected_PAD_1= data_AP['RF_T1'] - intercept - age_coeff * data_AP['Age'] - gender_coeff * data_AP['Sex']
corrected_PAD_2= data_CP['RF_T1'] - intercept - age_coeff * data_CP['Age'] - gender_coeff * data_CP['Sex']

data_AP['RF_T1_corrected'] = corrected_PAD_1 + data_AP['Age']
data_CP['RF_T1_corrected'] = corrected_PAD_1 + data_CP['Age']

delta_1_corrected=data_AP['RF_T1_corrected']-data_AP['Age']
delta_2_corrected=data_CP['RF_T1_corrected']-data_CP['Age']
print('delta on AP after correction:', np.mean(delta_1_corrected))
print('delta on CP after correction:', np.mean(delta_2_corrected))

#assessing age bias again
correlation_real_pred_test_delta_1, p_value_delta_1 = pearsonr(data ['Age'], delta_1)
print(f"Age bias on Test 1: {correlation_real_pred_test_delta_1}")
print(f"P-value: {p_value_delta_1}")

data_AP.to_csv("predictions_AP_randomforest_T1.csv", index=False)
data_CP.to_csv("predictions_CP_randomforest_T1.csv", index=False)
