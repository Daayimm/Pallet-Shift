
# import pandas as pd
import cv2
import numpy as np


def load_lab(path):
    image = cv2.imread(path)
    return cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
    

def image_statistics(lab_image):
    """ LAB: 
            L : Light
            A: green-red axis
            B: blue-yellow axis 
            
            A channel (Green ↔ Red)
            negative values → green
            positive values → red
            
            B channel (Blue ↔ Yellow)
            negative values → blue
            positive values → yellow
            
            """
            
    light_mean = np.mean(lab_image[:,:,0])
    light_std = np.std(lab_image[:,:,0])
    
    
    # green_red_axis mean & std
    a_mean = np.mean(lab_image[:,:,1])
    a_std = np.std(lab_image[:,:,1])
    
    
    # blue_yellow_axis mean & std
    b_mean = np.mean(lab_image[:,:,2])
    b_std = np.std(lab_image[:,:,2])
    
    
    return (light_mean,light_std) , (a_mean,a_std),(b_mean,b_std)
    


def transfer(reference_img,target_img,strength=1.0):
    
    

    reference_stats = image_statistics(reference_img)
    target_stats = image_statistics(target_img)
    
    
    
    ref_l_stats,ref_a_stats,ref_b_stats = reference_stats
    target_l_stats,target_a_stats,target_b_stats = target_stats
    
    
    
    l_shift = np.clip((target_img[:,:,0] - target_l_stats[0]) / target_l_stats[1] * ref_l_stats[1] + ref_l_stats[0],0,255).astype(np.uint8)
    # l_shift = 255 * l_shift

    a_shift = np.clip((target_img[:,:,1] - target_a_stats[0]) / target_a_stats[1] * ref_a_stats[1] + ref_a_stats[0],0,255).astype(np.uint8)
    # a_shift *= 255
    b_shift = np.clip((target_img[:,:,2] - target_b_stats[0]) / target_b_stats[1] * ref_b_stats[1] + ref_b_stats[0],0,255).astype(np.uint8)
    # b_shift *= 255
    
    
    
    shifted = np.stack([l_shift,a_shift,b_shift],axis=-1)
    # target_merged = np.stack([target_img[:,:,0],target_img[:,:,1],target_img[:,:,2]],axis=-1)
    
    # if strength = 0 we get back original image
    # custom_strength = np.clip((target_merged + strength * (shifted - target_merged)),0,255).astype(np.uint8)
    
    return cv2.cvtColor(shifted,cv2.COLOR_LAB2BGR)