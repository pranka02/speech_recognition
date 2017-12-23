# Speech Recognition

This project aims to do the first step towards building a simple speech detector using Speech Commands Dataset relased by TensorFlow.

---------------------------
## Dataset

The dataset used in this project is the Speech Commands Dataset by TensorFlow. The dataset contains 65,000 one-second long utterances of 30 short words and a separate folder with backgound noise audio clips. These clips were broken into one-second chunks and separated into a folder named 'silence', for classification.

---------------------------
## Features

Short Time Fourier Transform (STFT) was performed on the .wav audio clips and the coefficients were used as the features. Mel-Frequency Cepstral Coefficients (MFCC), Chroma and Contrast features were also used as features.

---------------------------
## Preprocessing

The features were normalized and PCA was performed on them to reduce dimension.

---------------------------
## Learning Models

### Deep Neural Network 
A 3 layer deep neural network was implemented in TensorFlow to do the classification. 


