#selecting participants who meet the criteria (i.e. no neurological or psychological disorders)

selected_columns = eid + additional_columns + icd10_cols + icd9_cols + diabetes + long_illness + chronic_pain_cols + acute_pain_cols + all_img

ukb_data = pd.read_csv('ukb674571.csv', usecols=selected_columns)

#icd9 - icd10 positive 
matched_icd9_icd10=[]

for j in range (ukb_data.shape[0]):
    for i in range (47):   #icd9
    
        column=ukb_data.columns.get_loc("41271-0." + str(i))
        if (ukb_data.iloc[j,column] in icd9_codes):
            if j not in matched_icd9_icd10:
                matched_icd9_icd10.append(j) #index of row to exclude
        


for z in range (ukb_data.shape[0]):
    for k in range (83):   #icd10   from 0 to 213 rest is NANs
    
        column=ukb_data.columns.get_loc("41270-0." + str(k))
        if (ukb_data.iloc[z,column] in icd10):
            if z not in matched_icd9_icd10:
                matched_icd9_icd10.append(z)



#chronic pain positive
matched_chronic_pain=[]  
for c in range(data.shape[0]):
    for b in chronic_pain_cols:
        column=data.columns.get_loc(b)
        if (data.iloc[c,column] ==1):
            if c not in matched_chronic_pain:
                matched_chronic_pain.append(c)    #index of row to exclude
      
            
#acute pain positive
matched_acute_pain=[]  
for e in range(data.shape[0]):
    for d in acute_pain_cols:
           
        column=data.columns.get_loc(d)
        if ( data.iloc[e,column] == 3 or data.iloc[e,column] == 4  or data.iloc[e,column] == 6 or data.iloc[e,column] == 7 ):
            if e not in matched_acute_pain: #data.iloc[e,column] == 1 or data.iloc[e,column] == 2 or or data.iloc[e,column] == 5 or data.iloc[e,column] == 8
                matched_acute_pain.append(e)




#selecting healthy subjects
healthy_subjects= np.zeros((ukb_data.shape[0],ukb_data.shape[1]), dtype='object')
h=0
for i in range (ukb_data.shape[0]):
    if (i not in matched_chronic_pain and i not in matched_acute_pain and i not in matched_icd9_icd10 and data.iloc[i,diabetes]==0.0 and data.iloc[i,nolongstandingillness]==0): 
        healthy_subjects[h,:]=ukb_data.iloc[i,:]
        
        h=h+1
healthy_subjects_clean=healthy_subjects[0:h, :]

#selecting chronic pain subjects
chronic_pain_subjects= np.zeros((ukb_data.shape[0],ukb_data.shape[1]), dtype='object')
h=0
for i in range (ukb_data.shape[0]):
    if (i in matched_chronic_pain and i not in matched_icd9_icd10 and data.iloc[i,diabetes]==0.0 and data.iloc[i,nolongstandingillness]==0): 
        chronic_pain_subjects[h,:]=ukb_data.iloc[i,:]
        
        h=h+1
chronic_pain_subjects=chronic_pain_subjects[0:h, :]

#selecting acute pain subjects
acute_pain_subjects= np.zeros((ukb_data.shape[0],ukb_data.shape[1]), dtype='object')
h=0
for i in range (ukb_data.shape[0]):
    if (i not in matched_chronic_pain and i in matched_acute_pain and i not in matched_icd9_icd10 and data.iloc[i,diabetes]==0.0 and data.iloc[i,nolongstandingillness]==0): 
        acute_pain_subjects[h,:]=ukb_data.iloc[i,:]
        
        h=h+1
acute_pain_subjects=acute_pain_subjects[0:h, :]

np.savetxt('healthy_controls_data.csv', healthy_subjects_clean, delimiter=',')
np.savetxt('chronic_pain_data.csv', chronic_pain_subjects, delimiter=',')
np.savetxt('acute_pain_data.csv', acute_pain_subjects, delimiter=',')
