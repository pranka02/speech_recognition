# Speech Recognition

This project aims to do the first step towards building a simple speech detector using Speech Commands Dataset relased by TensorFlow.

---------------------------
## Dataset

The dataset used in this project is the Speech Commands Dataset by TensorFlow. The dataset contains 65,000 one-second long utterances of 30 short words and a separate folder with backgound noise audio clips. These clips were broken into one-second chunks and separated into a folder named 'silence', for classification.

---------------------------
## Features

Mel-Frequency Cepstral Coefficients (MFCC), Chroma and Contrast features were extracted and used as features.

---------------------------
## Preprocessing

The features were normalized and PCA was performed on them to reduce dimension.

---------------------------
## Learning Models

### Deep Neural Network 
A 3 layer deep neural network was implemented in TensorFlow to do the classification. 
After experimneting with a few combinations I chose the hidden layer units as 700, 700 and 100.
The output of each hidden layer passes through a RELU activation. 
Score - 0.63

### Random Forest Ensemble
A Random Forest model was fit with the default parameters.
Score - 0.64

### K Nearest Neighbor 
kNN was used to fit the data with the default parameters.
Score - 0.65



