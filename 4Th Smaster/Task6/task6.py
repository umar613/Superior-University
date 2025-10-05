import os
import urllib.request

# Download YOLOv3 weights if not present
weights_url = "https://pjreddie.com/media/files/yolov3.weights"
weights_path = "yolov3.weights"
if not os.path.exists(weights_path):
    print("Downloading yolov3.weights...")
    urllib.request.urlretrieve(weights_url, weights_path)
    print("Download complete.")

import cv2
import numpy as np

# Make sure the paths to the weights and config files are correct
net = cv2.dnn.readNet(r"yolov3.weights", r"yolov3.cfg")
# If the files are in a different directory, provide the full path, e.g.:
# net = cv2.dnn.readNet(r"e:\Task PAI lab 4A\Task6\yolov3.weights", r"e:\Task PAI lab 4A\Task6\yolov3.cfg")

with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]

animal_classes = ['dog', 'cat', 'horse', 'cow']

def detect_animals(image_path, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Image '{image_path}' not found or cannot be opened.")
        return []

    height, width, _ = img.shape

    blob = cv2.dnn.blobFromImage(img, 1/255.0, (416,416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5 and classes[class_id] in animal_classes:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x,y,w,h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    detected_animals = []

    for i in indexes.flatten():
        x, y, w, h = boxes[i]
        label = classes[class_ids[i]]
        confidence = confidences[i]

        color = (0,255,0)
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        cv2.putText(img, f"{label} {int(confidence*100)}%", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        detected_animals.append(label)

    cv2.imwrite(output_path, img)

    return detected_animals

if __name__ == "__main__":
    image_path = "your_image.jpg"
    output_path = "result_image.jpg"

    animals = detect_animals(image_path, output_path)
    print("Detected Animals:", animals)
    print(f"Result image saved as {output_path}")