import os
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow, cyan
import time
from tqdm import tqdm

d = "repos"


for dirpath, dirnames, filenames in tqdm(os.walk(d)):
    for f in filenames:
        fullpath = os.path.join(dirpath,f)
        # print(fullpath)

        if fullpath.endswith(".py"):
            #print(green(f"Keeping ... {fullpath}"))
            print(f.os.stat.st_size)    
            pass
            break
        else:
            #print(red(f"Deleting ... {fullpath}"))
            if d in fullpath:
                os.remove(fullpath)
            else:
                print(yellow("Something is wrong"))
                time.sleep(60)



        


