🧠 Brain Age Analysis: A Machine Learning Framework

📚 Background

Brain age, derived from structural Magnetic Resonance Imaging (MRI) and Diffusion Tensor Imaging (DTI) scans using Deep Learning (DL) or Machine Learning (ML) models, serves as a biomarker that provides insights into an individual's brain health relative to their chronological age.
This measure captures deviations in brain structure and white matter integrity, which may indicate accelerated aging or early signs of neurodegenerative diseases.
By comparing predicted brain age to actual chronological age, researchers can assess the impact of factors such as disease, lifestyle, and genetics on brain health.

🎯 Aim of the Project

This project aims to establish a framework for the preprocessing of various MRI sequences, specifically DTI and T1-weighted (T1w) images. The framework includes a feature extraction pipeline, followed by the application of ML models to predict brain age and evaluate discrepancies from chronological age. The proposed brain age framework is applied to three cohorts—healthy controls, individuals with acute pain, and those with chronic pain—to predict brain age, examine differences in brain age delta (predicted age minus chronological age), and explore associations with lifestyle and biomedical variables.

⚙️ Methods and Pre-processing Techniques Implemented

DTI and T1w data pre-processing
Feature extraction from pre-processed sequences to describe structural brain volumes (from T1w) and white matter tracts (from DTI)
ML model development to predict brain age
Age bias calculation and correction
Brain Age Gap (BAG) computation after bias correction (defined as the difference between predicted and chronological age)
Use of BAG to: assess the impact of lifestyle, socioeconomic, and genetic factors, evaluate differences between case and control groups (or other experimental groupings)

🛠️ Tools, Techniques, and Programming Languages

Programming Languages:
R
Python
Software and Libraries:
FMRIB Software Library (FSL) for imaging pre-processing
Big Data analysis: dataset including ~500,000 participants
Machine Learning Models:
Support Vector Regression (SVR)
Lasso Regression
Linear Regression
Random Forest Regression
Statistical Analysis: statistical methods for age bias correction, BAG correlation with other variables, and group comparisons

Abstract presented at the Society of Neuroscience 2024, Washington DC, USA  ---> M. Cannistra, V. Sacca, G. Tradigo, P. Veltri, T. Ge, J. Kong; Evaluation of musculoskeletal pain’s impact on brain age in UK Biobank cohorts using multimodality neuroimaging: a Machine Learning study. Society of Neuroscience (SfN), 2023, Washington D.C. 11-15 November.
