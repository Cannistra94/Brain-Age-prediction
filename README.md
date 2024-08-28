# Brain-Age-prediction
Background: Brain age, derived from structural Magnetic Resonance Imaging (MRI) and diffusion tensor imaging (DTI) scans using Deep Learning (DL) or Machine Learning (ML) models, is a biomarker that provides insights into an individual's health relative to their chronological age. This measure captures deviations in brain structure and white matter integrity, which can indicate accelerated aging or early signs of neurodegenerative diseases. By comparing the models' predicted brain age to actual chronological age, researchers assess the impact of various factors such as disease, lifestyle, and genetics on brain health.


In this project, a pipeline is implemented to:

-apply pre-processing procedures to the DTI and MRI sequences
-Extract features that describe structural volumes (derived from T1-weighted MRI) and white matter tracts (derived from DTI)
-use these features in a ML model to predict brain age
-Address age bias in the predicted age, a statistical trend that can skew age predictions, by applying an age bias correction algorithm
-Calculate the Brain Age Gap (BAG), defined as the difference between the predicted age and chronological age
-Utilize BAG to assess the impact of lifestyle, socioeconomic, or genetic factors
-BAG can also be used to test for differences between case/controls or, in general, between groups, defined according to the experimental settings
-Employ BAG to test for differences between case/control groups or other experimental groupings

