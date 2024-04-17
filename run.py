from ultralytics import YOLO
from PIL import Image
from os import listdir
from os.path import isfile, join

source_dir = input("Enter path to directory containing files to run on: ")
dest_dir = input("Enter path to directory to store results: ")
model_path = input("Enter path to model: ")

onlyfiles = [f for f in listdir(source_dir) if isfile(join(source_dir, f))]

model = YOLO(model_path)

for file in onlyfiles:
    results = model(source_dir + "/" + file)
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.save(dest_dir + "/" + file)  # save image
