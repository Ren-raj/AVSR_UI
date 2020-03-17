import librosa as lr
import  numpy as np
import  pandas as pd
from openpyxl import *




def audio_feature_extraction():
    audio_path = 'clean_appaudio.wav'
    x, sr = lr.load(audio_path)
    lr.load(audio_path, sr=44100)
    mfccs = lr.feature.mfcc(x, sr=sr)
    mfccs = np.mat(mfccs)
    mfccs = pd.DataFrame(mfccs.T)
    print(mfccs)
    mfccs.to_excel("feature_audio.xlsx", index=False, header=False)
    
    return 1
