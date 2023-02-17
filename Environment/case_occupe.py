from Map.generation import *
from Environment.statistic import *

#Condition dans l'environnement
def test_case_occupe(image):
    global FEED
    position  = [image.x,image.y]
    if position in nourriture:
        FEED = FEED+1
        nourriture.remove(position)


