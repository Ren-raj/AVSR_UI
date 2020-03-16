
import cv2
import dlib
import numpy
import  csv
import pandas as pd

import glob


print("...........................PROCESSING FRAMES..............................\n\n\n")

def videp_feature_extraction(screen, END):
    count = 0
    for frame in glob.glob('frames/frame*.jpg'):

        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        image = cv2.imread(frame)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        rects = detector(gray)

        lis = []
        l = []

        for rect in rects:

            landmarks = predictor(gray, rect)

            for n in range(48, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
                e = numpy.array((x, y))
                for k in range(48, 68):
                    if (k > n):
                        a = landmarks.part(k).x
                        b = landmarks.part(k).y
                        o = numpy.array((a, b))
                        dist = numpy.linalg.norm(e - o)
                        l.append(dist)
            lis.append(l)
            l = []

        cv2.imwrite('pframes/pframe%d.jpg' % count, image)

        with open('pcsv/ccsv_video.csv', 'a') as f:
            wtr = csv.writer(f, delimiter=',')
            wtr.writerows(lis)

        lis = []
        l = []

        cv2.destroyAllWindows()
        print('FRAME %d processed' % count)
        screen.insert(END, "FRAME %d PROCESSED\n" %count)
        screen.see(END)
        count = count + 1

    df = pd.read_csv("pcsv/ccsv_video.csv")
    from openpyxl import load_workbook

    writer = pd.ExcelWriter('feature_video.xlsx', engine='openpyxl')
    writer.book = load_workbook('feature_video.xlsx')
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    reader = pd.read_excel(r'feature_video.xlsx')
    df.to_excel(writer, index=False, header=False, startrow=len(reader) + 2)
    writer.close()
    print("\n\n\n...........................ALL FRAMES PROCESSED..............................\n\n\n")
    screen.insert(END, "ALL FRAMES PROCESSED\n")
    screen.see(END)

    print("\n\n\n...........................GENERATING VIDEO FEATURE SET..............................\n\n\n")
    fil = pd.read_csv('pcsv/ccsv_video.csv')
    fil = list(fil.mean())
    print(fil)
    print('\n\n\nLength of feature set')
    print(len(fil))
    print('feature saved')

    with open('feature_video.csv', 'a') as f:
        wtr = csv.writer(f, delimiter=',')
        wtr.writerow(fil)

    print("\n\n\n...........................VIDEO FEATURE SET GENERATED..............................\n\n\n")
    screen.insert(END, "VIDEO FEATURE GENERATED\n")
    screen.see(END)

    return 1
