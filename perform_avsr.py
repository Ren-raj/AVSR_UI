from tensorflow import keras
import pandas as pd
import numpy as np


def perform_avsr():

    x_vid=pd.read_csv("feature_video.csv")

    x=pd.read_excel('feature_audio.xlsx')

    X=np.array(x).reshape(87*20)

    X=pd.DataFrame(X)

    X=pd.concat([X,x_vid],axis=1)

    model=keras.models.load_model("recognizer.h5")

    label=model.predict_classes(X)[0]

    return label





