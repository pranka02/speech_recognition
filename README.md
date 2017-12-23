# Speech Recognition

This project aims to do the first step to build a simple speech detector using Speech Commands Dataset relased by TensorFlow.

---------------------------
## Dataset

The dataset used in this project is the Speech Commands Dataset by TensorFlow. The dataset contains 65,000 one-second long utterances of 30 short words and a separate folder with backgound noise audio clips. These clips were broken into one-second chunks and separated into a folder named 'silence', for classification.

---------------------------
## Features

Short Time Fourier Transform was performed on the .wav audio clips and the coefficients were used as the features.

---------------------------
## Learning Models

Deep Neural Network --A 3 layer deep neural network in python was implemented to do the classification.


