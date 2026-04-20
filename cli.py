import argparse

import cv2
from palette_shift import load_lab, transfer

parser = argparse.ArgumentParser()
parser.add_argument("reference_image")
parser.add_argument("target_image")
# parser.add_argument("--strength",default=1.0,type=float)
parser.add_argument("--output",default="output.jpg")
args = parser.parse_args()

ref_lab = load_lab(args.reference_image)
target_lab = load_lab(args.target_image)


output = transfer(ref_lab,target_lab)#,args.strength)



cv2.imwrite(args.output,output)

