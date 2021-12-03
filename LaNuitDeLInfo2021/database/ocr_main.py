import sys
import os
import re

import cv2 
import numpy as np

import pytesseract

from PIL import Image

def image_remove_shadows(img):
    dilated_img = cv2.dilate(img, np.ones((7,7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(img, bg_img)

    _, thr_img = cv2.threshold(diff_img, 230, 0, cv2.THRESH_TRUNC)
    return cv2.normalize(diff_img, thr_img, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)

def image_sharpening(img):
    blur_img = cv2.GaussianBlur(img, (0, 0), 5)
    return cv2.addWeighted(img, 1.5, blur_img, -0.5, 0)

def preprocessing(filepath):
    img = cv2.imread(filepath, 0)
    
    img = image_remove_shadows(img)
    img = image_sharpening(img)
    
    # Return PIL image
    return Image.fromarray(img)

def remove_empty_lines(text):
    # Text cleaning
    # Count the first empty lines
    idx_start = 0
    lines = text.splitlines()
    for line in lines:
        if len(line) > 1:
            break
        idx_start += 1
    # Count empty lines at the end
    idx_end = 0
    for line in lines[::-1]:
        if len(line) > 1:
            break
        idx_end += 1
    idx_end = len(lines)-idx_end
    # Remove lines with less than 2 characters 
    text = ""
    for line in lines[idx_start:idx_end]:
        if len(line) < 2:
            text += "\n"
        else:
            text += line.strip() + '\n'
    # Remove mutliple line breaks
    clean = re.sub(r'(\n\s*)+\n', '\n\n', text)
    clean = clean.replace('\n', '<br>')
    
    return clean

def main(filepath):
    if os.path.exists(filepath):
        img = preprocessing(filepath)
        img.save("preprocessing.png")
        custom_config = r'--oem 3 --psm 1'
        ocr_text = pytesseract.image_to_string(img, config=custom_config, lang="fra")

        final_text = remove_empty_lines(ocr_text)
        print(final_text)
        return final_text
    else:
        return "File does not exist"

if __name__ == '__main__':
    assert len(sys.argv) == 2
    filepath = sys.argv[1]
    main(filepath)
