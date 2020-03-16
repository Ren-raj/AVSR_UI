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
    writer = pd.ExcelWriter('feature_audio.xlsx', engine='openpyxl')
    writer.book = load_workbook('feature_audio.xlsx')
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    reader = pd.read_excel(r'feature_audio.xlsx')
    mfccs.to_excel(writer, index=False, header=False, startrow=len(reader) + 2)
    writer.close()

    return 1
