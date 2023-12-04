import json
import random
import os
from video_maker import video_maker

#path
imagesPath = "./assets/images/"
audioPath = "./assets/audio/"
quotesPath = "./assets/quotes/"

# load a random quote
f = open(f"{quotesPath}{random.choice(os.listdir(quotesPath))}")
data = json.load(f)
text = (data['quotes'][random.randint(0,(len(data['quotes'])-1))]['quote'])

# load a random audio
audio = f"{audioPath}{random.choice(os.listdir(audioPath))}"

# load a random image
image = f"{imagesPath}{random.choice(os.listdir(imagesPath))}"

video_maker(image, text, audio)




