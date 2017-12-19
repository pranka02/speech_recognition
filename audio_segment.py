import os 
from pydub import AudioSegment
from pydub.utils import make_chunks

root = os.path.dirname(os.path.realpath(__file__))
path_name = r'train\audio\silence'
direc_name= os.path.join(root, path_name)
files = os.listdir(direc_name)
print(len(files))
chunk_length_ms = 1000 # pydub calculates in millisec

for i, file in enumerate(files):
	myaudio = AudioSegment.from_file(os.path.join(direc_name,file) , "wav") 
	chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec
	for j, chunk in enumerate(chunks):
		chunk_name = "silence-{}-{}.wav".format(i,j)
		print ("exporting", chunk_name)
		chunk.export(os.path.join(direc_name,chunk_name), format="wav")