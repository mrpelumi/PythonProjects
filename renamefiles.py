#The code below renames batch txt files in windows.
from pathlib import Path
import fnmatch
from dotenv import load_dotenv
import os

load_dotenv()

directory = os.getenv('directory')

newfile_name = ['nysc_1.jpg','nysc_2.jpg','nysc_3.jpg','nysc_4.jpg','nysc_5.jpg',
                'nysc_6.jpg','nysc_7.jpg','nysc_8.jpg','nysc_9.jpg','nysc_10.jpg'
                'nysc_11.jpg','nysc_12.jpg']

try:
    with Path(directory) as path_obj:
        index = 0
        for filename in path_obj.iterdir():
            if filename.is_file():
                if fnmatch.fnmatch(filename,'*.jpg'):
                    new_name = directory + newfile_name[index]
                    filename.rename(new_name)
                    index += 1
except FileExistsError as fe:
    print(f'{new_name.name}: Exists already')