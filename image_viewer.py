import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tkMessageBox



def photo_view(dir):

	try:

		img = mpimg.imread(dir)
		imgplot = plt.imshow(img)
		plt.title("AVSR- FRAME")
		plt.show()

		return
	except:
		tkMessageBox.showinfo(title="Exception !", message="Delay Expected \n Try Again.. :)")
		return
