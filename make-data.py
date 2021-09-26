import os
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow, cyan
import time
from tqdm import tqdm

directory = "repos"

MAX_CHAR_LENGTH = 512
MIN_CHAR_LENGTH = 400

NEW_LINE_CHAR = "<N>"

full_paths = []

for dirpath, dirnames, filenames in tqdm(os.walk(directory)):
    for f in filenames:
        full_path = os.path.join(dirpath,f)
        full_paths.append(full_path)
print(len(full_paths))
#44615 

with open("data1.txt" , "a") as f:
    try:
        for fpath in tqdm(full_paths):
            d= open(fpath,"r" , encoding='latin-1').read()
            fd = d.replace("\n",NEW_LINE_CHAR)
            # print(d)
            if  100 < len(d) <= MAX_CHAR_LENGTH :
                f.write(fd+'\n')
                
            else:
                sd = fd.split(f"{NEW_LINE_CHAR}{NEW_LINE_CHAR}")
                substring = ""
                for split in sd:
                    substring += split + f"{NEW_LINE_CHAR}{NEW_LINE_CHAR}"
                    if MIN_CHAR_LENGTH< len(d) <= MAX_CHAR_LENGTH :
                        f.write(fd+'\n')            
                        substring = ""
    except Exception as e:
        print(red(str(e)))
                        
            
