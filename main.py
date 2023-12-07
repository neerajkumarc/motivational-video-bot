import json
import random
import os, time
from video_maker import video_maker

#path
imagesPath = "./assets/images/"
audioPath = "./assets/audio/"
quotesPath = "./assets/quotes/"
outputPath = "./exports/"

#create a output directory
if not (os.path.exists(outputPath)):
    os.mkdir(outputPath)



print("\n",45*"-","\n \tWelcome To Motivational Video Bot","\n","-"*45,"\n")

while True:
    num_of_vid = int(input("Enter the number of videos you want to create (1-10): "))
    if num_of_vid >= 1 and num_of_vid <= 10:
        break
    else:
        print("Invalid input. Please enter a value between 1 and 10.")

v_timeStart = time.time()
for i in range(num_of_vid):
    # load a random quote
    f = open(f"{quotesPath}{random.choice(os.listdir(quotesPath))}")
    data = json.load(f)
    text = (data['quotes'][random.randint(0,(len(data['quotes'])-1))]['quote'])

    # load a random audio
    audio = f"{audioPath}{random.choice(os.listdir(audioPath))}"

    # load a random image
    image = f"{imagesPath}{random.choice(os.listdir(imagesPath))}"

    #vide creation
    video_maker(image, text, audio, f'{outputPath}/video{i+1}.mp4')

v_timeEnd = time.time()
v_timeTotal =v_timeEnd-v_timeStart
print(f"{num_of_vid} videos created successfully (finished in {(v_timeTotal):.2f}s)")


