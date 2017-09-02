# Copyright 2017 The ImageTAgVER Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import PIL
from PIL import Image, ImageTk # for windows is this option , ImageGrab
import tkFileDialog
import os

# open a file chooser dialog and allow the user to select an input
opts = {}
opts['filetypes'] =[('Supported types',('.jpeg','.jpg','.JPG','.JPEG')),
                             ('EEG files','.eeg'),('all files','.*')]
        
path1 = tkFileDialog.askdirectory(title = "Select Input Folder")
#if path1 == '': return
print path1    

path2 = tkFileDialog.askdirectory(title = "Select Output Folder")
#if path2 == '': return
print path2  

basewidth= int(input("Please enter reduction factor for your image (100-half size, 200-quarter size, 300...): "))

listing = os.listdir(path1)  
print listing  
for file in listing:
    img = Image.open(path1 +'/' +file) 
    #basewidth=100  
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    img.save(path2 +'/crop'+ file)

#basewidth = 300
#img = Image.open('SLOLogo.jpeg')
#wpercent = (basewidth/float(img.size[0]))
#hsize = int((float(img.size[1])*float(wpercent)))
#img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
#img.save('sompic.jpg') 




#from multiprocessing import Pool
#import os

#path1 = "some/path"
#path2 = "some/other/path"

#listing = os.listdir(path1)    

#p = Pool(5) # process 5 images simultaneously

#def process_fpath(path):
#    im = Image.open(path1 + path)    
#    im.resize((50,50))                # need to do some more processing here             
#    im.save(os.path.join(path2,path), "JPEG")

#p.map(process_fpath, listing)

