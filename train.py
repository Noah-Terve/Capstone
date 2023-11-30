from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

# add a new data file here to train on different datay
results = model.train(data='coco128.yaml', epochs=100, imgsz=640)
