import os, time
from PIL import Image
from exif import Image
from openlocationcode import openlocationcode as olc


def decimal_coords(coords, ref):
 decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
 if ref == 'S' or ref == 'W':
     decimal_degrees = -decimal_degrees
 return decimal_degrees

def image_loc(img_path):
    with open(img_path, 'rb') as src:
        img = Image(src)
    if not img.has_exif:
        #print(img_path + ' no EXIF information')
        return ""
    try:
            img.gps_longitude
            coords = (decimal_coords(img.gps_latitude,
                      img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                      img.gps_longitude_ref))
            img_loc = olc.encode(decimal_coords(img.gps_latitude,
                      img.gps_latitude_ref),decimal_coords(img.gps_longitude,
                      img.gps_longitude_ref))
    except AttributeError:
           #print(img_path + ' No Coordinates')
           return ""
    #print(coords)
    #print(img_loc)
    return img_loc



def image_timedate(img_path):
    with open(img_path, 'rb') as src:
        img = Image(src)
    if not img.has_exif:
        print(img_path + ' no EXIF information')
        return ""
    try:
        img.datetime_original
        img_timedate = img.datetime_original.replace(":","")
        img_timedate = img_timedate.replace(" ","_")
    except AttributeError:
        print(img_path+ ' No timedate')
        return ""
    return img_timedate

if __name__ == '__main__':
    for file in os.listdir():
        if (file.endswith(('.JPG','.jpg')) and  "__" not in file):

            img_time = image_timedate(file)
            img_place = image_loc(file)


            #print(file)
            #print(img_time)
            #print(img_place)

            if img_time != "":
                new_name = img_time + '_'
                #if img_place != "":
                #    new_name = new_name + img_place + '_'
                new_name = new_name + '_' + file

            os.rename(file,new_name)
            time.sleep(0.01)
            print(file + " -----> " + new_name)
