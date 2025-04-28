# Brain Age analysis: a Machine Learning Study
Background: 
Brain age, derived from structural Magnetic Resonance Imaging (MRI) and Diffusion Tensor Imaging (DTI) scans using Deep Learning (DL) or Machine Learning (ML) models, serves as a biomarker that provides insights into an individual's brain health relative to their chronological age. This measure captures deviations in brain structure and white matter integrity, which may indicate accelerated aging or early signs of neurodegenerative diseases. By comparing predicted brain age to actual chronological age, researchers can assess the impact of factors such as disease, lifestyle, and genetics on brain health.

Aim of the project: 
Chronic pain is known to alter brain structure and functionality, potentially accelerating neurodegenerative processes. The aim of this project was to investigate the extent to which chronic pain affects brain aging by using brain age as a quantitative biomarker. Specifically, we assessed whether individuals with chronic pain exhibited increased brain age compared to healthy controls, providing insights into the impact of chronic pain on brain health and aging.

Methods and pre-processing techniques implemented:
-DTI and MRI (T1 weighted) data pre-processing
-Features extraction from pre-processed sequences to describe structural volumes (derived from T1-weighted MRI) and white matter tracts (derived from DTI)
-ML model building to predict brain age
-Age bias (a statistical trend that can skew age predictions) calculation and correction using different statistical approaches
-Brain Age Gap (BAG) computation (after bias correction), defined as the difference between the predicted age and chronological age
-Utilize BAG to assess the impact of lifestyle, socioeconomic, or genetic factors
-Employ BAG to test for differences between case/control groups or other experimental groupings

