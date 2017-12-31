import librosa
import librosa.display
from librosa import feature as ft
import matplotlib.pyplot as plt
import os 
import numpy as np
import csv
import ntpath

# root path
root = os.path.dirname(os.path.realpath(__file__))
path_name = r'train_full\audio'
direc_name = os.path.join(root,path_name)
train_path = r'train_full'
csv_file = os.path.join(train_path,'features_full.csv')
folders = os.listdir(path_name)
print(folders)
features = []

with open(csv_file, "w", newline= '') as output:
	for folder in folders:
		audio_class_folder = os.path.join(direc_name,folder)
		files = os.listdir(audio_class_folder)
		print(folder)
		for file in files:
			features = []
			print(file)
			X, samp_rate = librosa.load(os.path.join(audio_class_folder,file))
			stft = np.array(np.abs(librosa.stft(X)))
			mfcc = np.array(np.mean(librosa.feature.mfcc(y=X, sr=samp_rate, n_mfcc=40).T,axis=0))
			chroma = np.array(np.mean(librosa.feature.chroma_stft(S=stft, sr=samp_rate).T,axis=0))
			contrast = np.array(np.mean(librosa.feature.spectral_contrast(S=stft, sr=samp_rate).T,axis=0))
			features.append(mfcc)
			features.append(chroma)
			features.append(contrast)
			features.append(folder)
			writer = csv.writer(output, delimiter=',')
			writer.writerow(features)
print('Yay!')
