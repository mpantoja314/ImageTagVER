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
# import the necessary packages
import Tkinter as tk
from PIL import Image
from PIL import ImageTk
import os

def image_concrete():
	os.system('python ImageTagGUI.py')
def images_own():
	os.system('python ImageTagOwn.py')
def review_image():
	os.system('python ReviewTag.py')
def stats():
	os.system('python histConcLabels.py')
def select_crop_image():
	os.system('python crop.py')


#Main Window Code   
root = tk.Tk()
root.title("V.E.R. Visual Earthquake Reconnaissance");

verlogo=tk.PhotoImage(file= "verlogo.png")
calpolylogo=tk.PhotoImage(file= "mustang.png")

cv=tk.Canvas(width=360, height=360)
cv.create_image(10,10,image=verlogo, anchor='nw')
cv.create_image(10,200,image=calpolylogo, anchor='nw')
cv.pack(pady=12, side='left', fill='both', expand='yes')




#instructions

label=tk.Label(root, width=50, text="Instructions:",font=("Italic",10, "bold"))
label1=tk.Label(root, text="This Software is created to easily annotate images taken after earthquake damages to Civil Infrastructure") 
label2=tk.Label(root, text="Tag Concrete Image: Specific Tags for concrete damges") 
label3=tk.Label(root, text="Tag Images Add your own label: User create their own two files with structure type and Damages.") 
label4=tk.Label(root, text="Review Tagged Images: Load Image and the tags so they can be reviewed/modified") 
label5=tk.Label(root, text="Create Statistics: Generates basic statistics about the data already tagged") 
label6=tk.Label(root, text="Crop All Pictures: Select an Image file folder and crops all the images to a desired size") 
label7=tk.Label(root, text="Owners: MAria & Anahid Calpoly. More info on Menu:Help") 


label.pack(pady=8, anchor='w')
label1.pack( anchor='w')
label2.pack( anchor='w')
label3.pack( anchor='w')
label4.pack( anchor='w')
label5.pack( anchor='w')
label6.pack( anchor='w')
label7.pack( anchor='w')


button = tk.Button(root, text="Tag Concrete Image", command=image_concrete)
button.pack(pady=8,padx=8,fill="both", expand="no")

button = tk.Button(root, text="Tag Image Add Your Own Labels", command=images_own)
button.pack(pady=8,padx=8,fill="both", expand="no")

button = tk.Button(root, text="Review Tagged Image", command=review_image)
button.pack(pady=8,padx=8,fill="both", expand="no")

button = tk.Button(root, text="Create Statistics", command=stats)
button.pack(pady=8,padx=8,fill="both", expand="no")

button = tk.Button(root, text="Crop All Pictures in Folder to Same Size", command=select_crop_image)
button.pack(pady=8,padx=8,fill="both", expand="no")

# kick off the GUI
root.mainloop()
