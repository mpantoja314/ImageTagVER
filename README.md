# ImageTagVER
Earthquake Reconnaissance Tool. Rapid Labeling Damages after earthquake   

Installation Instructions:

Step 1.

Download python2.7 if you don’t already have it
python get-pip
pip install pillow
pip install numpy
pip install matplotlib

Step 4
Download them and put them in a folder.
In a terminal type:
python main.py

you should see this:
![alt text](screenshots/1.jpg "New Screen")

Instruction of how to use ImageTagVER

1. Create the Folders

Recommended to Create the following folders:

images/ Where the original RGB images will be saved. Mist contain the image you want to tag
annotations/ where the xml PASCAL VOC files for tensorflow will be saved, empty at the beginning
out/ where where the tagged images will be saved, empty at the beginning


3. Open terminal

Linux/mac: ctrl+T and then type : python main.py
Window: double click on main.py

1. Tag Concrete Image
![alt text](screenshots/2.jpg "New Screen")

On Top Left corner select File→open file (select the image you want to tag)
On Top Left Conner select File→select output folder (select the folder where you want to save all outputs)

Select one of the Type of Damage radio buttons and a Type of Structure radio button and click/drag on the image selecting the area you are interested on
The labels you select will be shown on the History Console  ListBox

You can create your own labels by entering the names on the top left create new label Input box, the previously created labels will be displayed in the listbox under. You must click on the Done creating new label so it gets saved for future use

If you made a mistake and want to erase some of the lebels click on the button Start Label Erase and then click on the Top Left corner of the rectangle containing the label. Once you are done erasing the mistakes select the Stop  deleting label

Click on Save and exit when done

2. When you click on Tag Image add your own labels you will be ask for the location of the Damages (DM.txt) and then the location of the structures (ST.txt) . After that the functionality is exactly the same  as in 1.
![alt text](screenshots/3.jpg "New Screen")

3. Review ImageTag

If you want to review somebody else’s tag and erase/add some of the labels
1. Select File→open original file NOTE: select the original file not the tagged one, it will add all tags in step 3
2. Select output folder
3. Select Tagged text file (output.txt). This is the file that contains all the tags should be named Output.txt and located on the out folder you selected

After this functionality is as 1
![alt text](screenshots/4.jpg "New Screen")

4. Create Statistics

By now just creates the Histogram of the labels

5. Crop all Images from a folder

Input Folder: contains images
Output folder: Location to save the cropped files

LICENSE

Copyright (C) <2017-2018> Maria Pantoja and Anahid B.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

Reference the work as : M. Pantoja, A. B. ......

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


