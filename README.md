🧠 Brain Age Analysis: A Machine Learning Study

📚 Background

Brain age, derived from structural Magnetic Resonance Imaging (MRI) and Diffusion Tensor Imaging (DTI) scans using Deep Learning (DL) or Machine Learning (ML) models, serves as a biomarker that provides insights into an individual's brain health relative to their chronological age.
This measure captures deviations in brain structure and white matter integrity, which may indicate accelerated aging or early signs of neurodegenerative diseases.
By comparing predicted brain age to actual chronological age, researchers can assess the impact of factors such as disease, lifestyle, and genetics on brain health.

🎯 Aim of the Project

Chronic pain is known to alter brain structure and functionality, potentially accelerating neurodegenerative processes.
This project aimed to investigate the extent to which chronic pain affects brain aging by using brain age as a quantitative biomarker.
Specifically, we assessed whether individuals with chronic pain exhibited increased brain age compared to healthy controls, providing insights into the impact of chronic pain on brain health and aging.

⚙️ Methods and Pre-processing Techniques Implemented

DTI and MRI (T1-weighted) data pre-processing
Feature extraction from pre-processed sequences to describe:
Structural brain volumes (from T1-weighted MRI)
White matter tracts (from DTI)
ML model development to predict brain age
Age bias calculation and correction, using different statistical approaches
Brain Age Gap (BAG) computation after bias correction (defined as the difference between predicted and chronological age)
Use of BAG to:
Assess the impact of lifestyle, socioeconomic, and genetic factors
Evaluate differences between case and control groups (or other experimental groupings)

🛠️ Tools, Techniques, and Programming Languages

Programming Languages:
R
Python
Software and Libraries:
FMRIB Software Library (FSL) for imaging pre-processing
Big Data Handling:
Processing and feature extraction from datasets including ~500,000 participants
Machine Learning Models:
Support Vector Regression (SVR)
Lasso Regression
Linear Regression
Random Forest Regression
Statistical Analysis:
Linear regression models used for age bias correction, BAG correlation with other variables, and group comparisons
