import librosa
import librosa.display
from librosa import feature as ft
import matplotlib.pyplot as plt
import os 
import numpy as np
import csv
import ntpath

root = os.path.dirname(os.path.realpath(__file__))
path_name = r'test'
direc_name = os.path.join(root,path_name)
train_path = r'test/audio'
csv_file = os.path.join(direc_name,'features_test.csv')
folders = os.listdir(path_name)
features = []

with open(csv_file, "w", newline= '') as output:
	audio_class_folder = os.path.join(root,train_path)
	files = os.listdir(audio_class_folder)
	for file in files:
			print(file)
			features = []
			X, samp_rate = librosa.load(os.path.join(audio_class_folder,file))
			stft = np.array(np.abs(librosa.stft(X)))
			mfcc = np.array(np.mean(librosa.feature.mfcc(y=X, sr=samp_rate, n_mfcc=40).T,axis=0))
			chroma = np.array(np.mean(librosa.feature.chroma_stft(S=stft, sr=samp_rate).T,axis=0))
			contrast = np.array(np.mean(librosa.feature.spectral_contrast(S=stft, sr=samp_rate).T,axis=0))
			features.append(mfcc)
			features.append(chroma)
			features.append(contrast)
			writer = csv.writer(output, delimiter=',')
			writer.writerow(features)
print('Yay')
