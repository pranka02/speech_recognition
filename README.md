# Speech Recognition

This project aims to do the first step to build a simple speech detector using Speech Commands Dataset relased by TensorFlow.

## Dataset

The dataset used in this project is teh Speech Commands Dataset by TensorFlow. The dataset contains folders with .wav files of 30 different words and a backgound noise.
The background noise audio clips were broken into 1 second chunks and separated into a separate folder named 'silence', for classification.

## Features

Short Time Fourier Transform was performed on the .wav audio clips and the coefficients were used as the features.

---------------------------
## Learning Models

With cleaned data, we are now able to build multiple different models to predict the PM 2.5 Level

Final Result:

| Model        | Normalized RSS | 
| :---         |     :---:      |
| Simple first-order linear regression   | 0.542290     |
| Third-order linear regression     | 0.417474       |
| Third-order linear regression with LASSO L1 Regularization     | 0.417535       |
| Neural Network with 10 hidden-units     | 0.404074       |
| Neural Network with 20 hidden-units     | 0.391214       |
| Neural Network with 40 hidden-units     | 0.393047       |
| Neural Network with 80 hidden-units     | 0.406128       |

