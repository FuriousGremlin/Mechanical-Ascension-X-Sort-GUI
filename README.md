# Mechanical-Ascension-X-Sort-GUI

The script was made in python, so make sure to use an IDE that supports it, I use Spyder.

## Set up
To set up the script, open the "Mechanical Ascension X Sort GUI.py" file in your IDE.
You will need to manually enter a directory to where your text files will be stored where it says [Filepath]. Ex. C:/Users/Yourname/Documents
Once you have done that, make two text files named all_items and current_items. If you wish to call them something else, make sure to change the name in the script.

## How to use
Once you have set it up, hit run in your IDE and a GUI with a blue feather icon should now pop up.

This GUI has 3 fields and 5 buttons.

"Name:" is where you enter the name of the item.
"MPU:" is where you enter the mpu of the item, currently you have to enter both values with a different name if the item has a base and max value.
The third field is the item list, this will show the name and the mpu, you can scroll down so dont worry if it looks like an item wasnt added. 
Ex. Nonexistent Atomizer - 2.0

#### Add items: 
Adds an item with the name from "Name:" and mpu from "MPU:" in a "Name - MPU" format to the item list field, in the text file it will be Name,MPU format. If an item you are trying to add to the current items list already exists in the all items list, you only need to enter the name and not the MPU as it will grab it from there, likewise an item that is added to the current items list will not be duplicated in the all items list if it already exists there.

#### Save Current Items: 
Saves current items list, redundant as switching item lists also does this.

#### Reset Current Items: 
Wipes the current items list.

#### Show Current Items / Show All Items: 
Switches between the list shown in the third field.

#### Quit: 
Crashes the program, just hit the X instead once youve saved as there is no reason to hit quit at the moment.

## Known bugs

Having a blank line in your txt file will cause the program to not run and spit out the error:
ValueError: not enough values to unpack (expected 2, got 1)

Quit button causes the program to crash rather than quit.

## End notes

This program was made using ChatGPT in my spare time, I do not work as a developer or programmer so if there are any bugs I may not be able to fix them.
If there are any issues with the program, feel free to let me know either on discord ( Furious Gremlin#3927 ) or on github.
