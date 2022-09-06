import os
from PIL import Image
from exif import Image
import time

if __name__ == '__main__':
    processes = []
    for file in os.listdir():
        if (file.endswith(('.JPG','.jpg')) and  "__" in file):
            print(file)
            new_file = file.rsplit("__")[1]
            os.rename(file,new_file)
            time.sleep(0.01)
            print(file + " -----> " + new_file)




