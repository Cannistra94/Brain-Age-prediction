#this script select the columns of interest from the UK BIOBANK dataset, 
#as the dataset contains around 500,000 participants and hundred of thousands of variables
#we want to remove any neurological or psychological disorders to avoid confounds 
#then we select chronic pain, acute pain and healthy controls participants
import pandas as pd
import numpy as np


eid = ['eid']
#selecting icd10 and icd9 columns to exclude
icd10_cols = [f'41270-0.{idx}' for idx in range(83)]
icd9_cols = [f'41271-0.{idx}' for idx in range(47)]
diabetes = [f'2443-{idx}.0' for idx in range(2)]
long_illness = [f'2188-{idx}.0' for idx in range(2)]
#select additional columns of interests
date_assessment_1=[f'53-0.0']
date_assessment_2=[f'53-1.0']
date_assessment_3=[f'53-2.0']
age=[f'21003-0.0']
gender=[f'31-0.0']
additional_columns = date_assessment_1 + date_assessment_2 + date_assessment_3 + age + gender

# ICD10 and ICD9 exclusion criteria

# ICD10 
# Tuberculosis + Acute poliomyelitis
icd10_A = ['A' + str(idx) for idx in range(15,20)] + ['A80'] 

# Benign neoplasms
icd10_D = ['D' + str(idx) for idx in range(10,37)]

# Organic, including symptomatic, mental disorders 
icd10_F = ['F' + f"{idx:02d}" for idx in range(10)]

# Schizophrenia, schizotypal and delusional disorders 
icd10_F += ['F' + str(idx) for idx in range(20,30)]

# Manic episode + Bipolar affective disorder 
# Obsessive-compulsive disorder 
# Depressive episode
# Recurrent depressive disorder
# Phobic anxiety disorders
# Other anxiety disorders
# Reaction to severe stress, and adjustment disorders
# Other neurotic disorders 
# Eating disorders
# Mental disorder, not otherwise specified
icd10_F += ['F30','F31', 'F32', 'F33', 'F40', 'F41', 'F42','F43','F48','F50','F99']

# Mental retardation
# Disorders of psychological development
icd10_F += ['F' + str(idx) for idx in range(70,90)]

# Diseases of the nervous system
icd10_G = ['G' + f"{idx:02d}" for idx in range(100)]

# Cerebral infarction
# Stroke, not specified as haemorrhage or infarction
icd10_I = ['I63', 'I64']

# Injuries to the head
icd10_Stemp = ['S' + f"{idx:02d}" for idx in range(10)]
icd10_S = icd10_Stemp + [code+str(idx) for idx in range(10) for code in icd10_Stemp]

# Spina bifida
icd10_Q = ['Q05']

# Append all and add last character codes from 0-9
codes = icd10_A + icd10_D + icd10_F + icd10_G + icd10_I + icd10_S + icd10_Q
icd10_codes = set()
for code in codes:
    icd10_codes.add(code)
    for idx in range(10):
        icd10_codes.add(code+str(idx))


# ICD9 
icd9_codes = []
# Cellulitis and abscess of face
icd9_codes += ['6820']

# Anxiety 
#icd9_codes += ['3000']

# Depressive disorder
icd9_codes += ['3119']

# Psychosis
icd9_codes += [str(idx) for idx in range(2900,2990)]

# Mental retardation
#icd9 += [str(idx) for idx in range(31700,32000)]
icd9_codes += ['31999'] # there is only this from 31700 to 31999

# Other and unspecified injury of face and neck
icd9_codes += ['9590']

# Fracture of skull
# Fracture of neck and trunk
# Fracture of upper limb
# Fracture of lower limb
# Dislocation
# Sprains/strains shoulder/upper arm - acromioclavicular (joint)(ligament)
icd9_codes += [str(idx) for idx in range(8000,8401)]

# Intracranial injury, excluding those with skull fracture
# (Thalia: yours run to 8540, not 8541)
icd9_codes += [str(idx) for idx in range(8500,8542)]

# Congenital anomalies - Nervous system
icd9_codes += [str(idx) for idx in range(74199,74300)]

# Occlusion of cerebral arteries
icd9_codes += [str(idx) for idx in range(4340,4350)]

# Obsessive-compulsive disorders
icd9_codes += ['3003']

icd9_codes = set(icd9_codes).union(set([code+'.0' for code in icd9_codes]))

#selecting pain-related columns
chronic_pain_cols = []
acute_pain_cols=[]
for col in data.columns:
    #if f'6159-2.0' in col:
     #    chronic_pain_cols.append(col)
    if '3571-0.0' in col:     #back pain 3+months
        chronic_pain_cols.append(col)       
    if f'2956-{ins_id}' in col:     #general pains 3+months
        chronic_pain_cols.append(col)
    if '3414-0.0' in col:     #hip pain 3+months
        chronic_pain_cols.append(col)
    if '3773-0.0' in col:     #knee pain 3+months
        chronic_pain_cols.append(col)
    if '3404-0.0' in col:     #neck/shoulder pain 3+months
        chronic_pain_cols.append(col)
    

for col in data.columns:
    if f'6159-0.0' in col:
        acute_pain_cols.append(col)
    if f'6159-0.1' in col:
        acute_pain_cols.append(col)
    if f'6159-0.2' in col:
        acute_pain_cols.append(col)
    if f'6159-0.3' in col:
        acute_pain_cols.append(col)
    if f'6159-0.4' in col:
        acute_pain_cols.append(col)
    if f'6159-0.5' in col:
        acute_pain_cols.append(col)
    if f'6159-0.6' in col:
        acute_pain_cols.append(col)

