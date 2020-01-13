#!/usr/bin/python3

import sys
import os
import xml.etree.ElementTree as ET

def bb_intersection_over_union(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
 
    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
 
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
    
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)
 
    # return the intersection over union value
    return iou

def main():
    if len(sys.argv) != 4:
        print("Usage:\n\tscore.py <teams_folder> <results_xml_folder> <soln_xml_folder>")
        sys.exit(1)

    teams_folder = sys.argv[1]
    results_xml_folder = sys.argv[2]
    soln_xml = os.path.normpath(sys.argv[3])

    teams = [ item for item in os.listdir(teams_folder) if os.path.isdir(os.path.join(teams_folder, item)) ]
    # teams = [f.path for f in os.scandir(teams_folder) if f.is_dir()]    
    for team in teams:        
        score_group(os.path.join(results_xml_folder, team, "results.xml"), soln_xml)
        print("")

def score_group(group_xml, soln_xml):
    group = group_xml.split(os.sep)[-2]
    print("Scoring group", group)

    # Parse tree
    if not os.path.isfile(group_xml):
        print("Missing results:", group_xml)
        return
    root = ET.parse(group_xml).getroot()

    # Print runtime
    runtime = float(root.find('runtime').text)
    print("Runtime (s):", round(runtime,1))

    # Print energy
    energy = float(root.find('energy').text)
    print("Energy (J):", round(energy,1))

    # Print power
    power = energy / runtime
    print("Avg Power (W):", round(power,3))

    # Score object detection
    ious = []
    # img = root.find('image')
    for img in root.findall('image'):        
        filename = img.find('filename').text
        filenum = filename.split(".")[0]        
        # print(filenum)

        # User box
        user_box = []
        xmin = int(img.find('object/bndbox/xmin').text)
        ymin = int(img.find('object/bndbox/ymin').text)
        xmax = int(img.find('object/bndbox/xmax').text)
        ymax = int(img.find('object/bndbox/ymax').text)
        user_box.append(min(xmin, xmax))
        user_box.append(min(ymin, ymax))
        user_box.append(max(xmin, xmax))
        user_box.append(max(ymin, ymax))
        # print(user_box)

        # Soln box
        soln_root = ET.parse(os.path.join(soln_xml, str(filenum) + ".xml")).getroot()
        soln_box = []
        soln_box.append(int(soln_root.find('object/bndbox/xmin').text))
        soln_box.append(int(soln_root.find('object/bndbox/ymin').text))
        soln_box.append(int(soln_root.find('object/bndbox/xmax').text))
        soln_box.append(int(soln_root.find('object/bndbox/ymax').text))
        # print(soln_box)

        iou = bb_intersection_over_union(user_box, soln_box)
        ious.append(iou)
    print("# images:", len(ious))
    # print("iou min:", round(min(ious), 2))
    # print("iou max:", round(max(ious), 2))
    print("iou avg:", round(sum(ious) / len(ious), 3))

    fps = len(ious) / runtime
    print("fps: ", round(fps, 2))  


if __name__ == "__main__":
    main()
