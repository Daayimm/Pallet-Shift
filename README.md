# Pallet-Shift

PaletteShift
                                                                                                 
  A Python command-line tool that transfers the colour grading of a reference image onto a target
   image.

  It works by analysing the colour statistics (mean and standard deviation) of each LAB channel  
  in the reference image, then applying those statistics to the target image — shifting its      
  overall tone, warmth, and mood to match the reference while preserving its original structure  
  and composition.

  Usage
  python cli.py reference.jpg target.jpg --output result.jpg

  Requirements
  pip install opencv-python numpy
