# update-digital-photo-file-name
Simple python script to extract digital photo EXIF info and rename file accordingly
This useful when creating digital album using photo taken with multiple devices. It makes following timeline easier. 

Usage: 
1. copy the scripts to your digital photo folder 
2. Run the needed script
3. Script will rename all you JPG photos according to their EXIF content, if avalible 
4. No command line arguments needed
5. Tested on MAC, Python3 and neccesry packages.  

add_datetime_loc.py 
-------------------
Add original timedate and location to file name: 
DATE    _ TIME _ PLUS CODE __ FILENAME.jpg 
20180316_172502_93GGM5RP+QR__DSC02457.jpg

add_datetime.py 
---------------
Add original timedate to file name: 
DATE    _ TIME __ FILENAME.jpg 
20180316_172502__DSC02457.jpg

undo_photo_rename
-----------------
Undo rename by removing add prefix fields sperated by double underscore 
20180316_172502_93GGM5RP+QR__DSC02457.jpg --> DSC02457.jpg
20180316_172502__DSC02457.jpg --> DSC02457.jpg

