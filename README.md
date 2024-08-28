# Brain-Age-prediction
Background: Brain age, derived from structural Magnetic Resonance Imaging (MRI) and diffusion tensor imaging (DTI) scans using Deep Learning (DL) or Machine Learning (ML) models, is a biomarker that provides insights into an individual's health relative to their chronological age. This measure captures deviations in brain structure and white matter integrity, which can indicate accelerated aging or early signs of neurodegenerative diseases. By comparing the models' predicted brain age to actual chronological age, researchers assess the impact of various factors such as disease, lifestyle, and genetics on brain health.


In this project, pipeline is implemented to:

-apply pre-processing procedures to the DTI and MRI sequences
-extract features describing structural volumes (derived from T1w MRI) and white matter tracts (derived from DTI)
-these features are then used into a ML model to predict the brain age
-predicted age, as identified in previous studies, suffer from age bias, a statistical trend that brings biases model to underestimate the predicted
-Brain Age Gap (BAG), defined as the delta between the predicted age and chronological age, is then extracted
-BAG can then be used to assess the impact of lifestyle, socioeconomic or genetic factors
-BAG can also be used to test for differences between case/controls or, in general, between groups, defined according to the experimental settings

