from detector import *
from tests.test import *
import json
import time

#detected_cars = action()
#print(test1(detected_cars, '/correct/test1.json'))
#video_capture, model = load_model()
#places, frame = start_action()
#
def get_jsons(mode):
	#places = [[508, 937, 632, 1133], [303, 634, 379, 783], [375, 769, 464, 916], [334, 693, 418, 859], [265, 596, 338, 732], [236, 540, 308, 673], [444, 1126, 554, 1280], [201, 506, 275, 661], [28, 241, 59, 320], [74, 329, 122, 418], [520, 349, 673, 621], [122, 126, 168, 242], [60, 230, 111, 277], [146, 161, 205, 282], [23, 143, 77, 224], [396, 300, 482, 536], [135, 847, 169, 897], [66, 157, 116, 208], [108, 362, 160, 466], [177, 194, 230, 335], [187, 855, 231, 902], [148, 418, 204, 537], [131, 806, 211, 901], [182, 471, 234, 609], [115, 92, 149, 145], [401, 451, 347, 264], [360, 427, 301, 249], [308, 410, 252, 241], [527, 556, 464, 334]]
	places=[[338, 553, 460, 779], 
[382, 648, 514, 865], 
[223, 370, 318, 561], 
[285, 496, 396, 692], 
[262, 429, 355, 619], 
[186, 583, 270, 731], 
[478, 300, 715, 560], 
[204, 654, 301, 817], 
[170, 517, 244, 651], 
[213, 335, 286, 469], 
[130, 170, 183, 279], 
[409, 773, 583, 1001], 
[133, 417, 202, 554], 
[166, 973, 231, 1077], 
[207, 70, 277, 138], 
[247, 745, 343, 892], 
[77, 86, 103, 142], 
[140, 925, 206, 1026], 
[33, 519, 76, 610], 
[136, 204, 216, 359], 
[51, 494, 84, 561], 
[265, 854, 396, 1025], 
[136, 863, 190, 958], 
[112, 134, 156, 188], 
[190, 276, 248, 368], 
[105, 353, 129, 429], 
[175, 37, 241, 97], 
[256, 94, 328, 166], 
[248, 1224, 332, 1280], 
[527, 1055, 719, 1259], 
[269, 113, 417, 244], 
[113, 359, 168, 488], 
[346, 1027, 456, 1148], 
[118, 625, 85, 580] ]
	(free_places, bisy_places) = action(places)
	
	if mode == 1:
		if len(free_places) == 0:
			return 0

		out = "{ \"free_places\":[ "
		for tmp in free_places:
			out += str(tmp) + ", "
		out = out[:-2]
		out += "]}"

	elif mode == 0:
		if len(bisy_places) == 0:
			return 0
		out = "{ \"bisy_places\":[ "
		for tmp in bisy_places:
			out += str(tmp) + ", "
		out = out[:-2]
		out += "]}"
	return out

if __name__ == "__main__":
	while(1):
		#places, frame = start_action()
		s1 = get_jsons(1)
		s0 = get_jsons(0)
		text_file = open("good.txt", "w")
		n = text_file.write(s1)
		text_file.close()
		text_file = open("bad.txt", "w")
		n = text_file.write(s0)
		text_file.close()
		time.sleep(60*5)  

