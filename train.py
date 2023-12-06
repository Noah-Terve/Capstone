from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

training_path = input("Enter path to .yaml file for testing data: ")
results = model.train(data=training_path, epochs=100, imgsz=640)
