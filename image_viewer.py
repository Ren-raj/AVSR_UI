import cv2



def photo_view(dir):

	img = cv2.imread(dir)

	screen_res = 1280, 720
	scale_width = screen_res[0] / img.shape[1]
	scale_height = screen_res[1] / img.shape[0]
	scale = min(scale_width, scale_height)
	window_width = int(img.shape[1] * scale)
	window_height = int(img.shape[0] * scale)
	
	cv2.namedWindow('AVSR- FRAME', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('AVSR- FRAME', window_width, window_height)

	cv2.imshow('AVSR- FRAME', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return 2
