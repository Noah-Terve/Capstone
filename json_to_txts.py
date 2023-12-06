import json
import sys

IMAGES_DIRECTORY = "data/"
IMAGES_EXTENSION = ".jpg"


# assumes txt files being created don't already exist


if __name__ == '__main__':

    args = sys.argv[1:]

    if len(args) != 1:
        print("Usage: python json_to_txts.py [json_file]")
        exit()

    try:
        f = open(args[0])
    except IOError:
        print(args[0] + " could not be found")
        exit()
    
    data = json.load(f)

    filtered_annotations = {}

    annotations = data["annotations"]
    images = data["images"]

    # filter annotations
    for a in annotations:
        image_id = str(a["image_id"])

        if image_id in filtered_annotations:
            filtered_annotations[image_id].append({"cat_id": a["category_id"], "bbox": a["bbox"]})
        else:
            filtered_annotations[image_id] = [{"cat_id": a["category_id"], "bbox": a["bbox"]}]
        
    # create txt files
    for image in images:
        width = image["width"]
        height = image["height"]

        fName = image["file_name"].lstrip(IMAGES_DIRECTORY).rstrip(IMAGES_EXTENSION)

        with open(fName + ".txt", "w") as f:
            for a in filtered_annotations[str(image["id"])]:
                bbox = a["bbox"]
                percent_bbox = [x / width if i in [0, 2] else x / height for i, x in enumerate(bbox)]
                f.write(str(a["cat_id"]) + " " + ' '.join(map(str, percent_bbox)) + '\n')
