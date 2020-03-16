from noisereduce import *
import noisereduce as nr
import scipy.io.wavfile
import tkMessageBox

def noise_reducer():

	# load data
	rate, data = scipy.io.wavfile.read("appaudio.wav")
	# select section of data that is noise
	noisy_part = data
	# perform noise reduction
	reduced_noise = nr.reduce_noise(audio_clip=data,noise_clip=noisy_part, verbose=False)

	scipy.io.wavfile.write('clean_appaudio.wav', rate, reduced_noise)

	return


