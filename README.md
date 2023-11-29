# public_backup_to_usb

This Python script helps you automate the backup of folders listed in a text file to an external USB drive. The program reads folder paths from a specified text file, with the first line representing the destination USB drive path. It then proceeds to copy each folder to the USB drive, overwriting existing folders if necessary.

How to Use:

Prepare Text File:

Create a text file (folder_paths.txt) containing folder paths, one per line.
The first line should specify the destination USB drive path.

example:

E:\BackupDestination  <=== where to back up
C:\Users\YourUsername\Documents\ImportantFiles <=== what to back up
D:\Projects\ProjectFolder <=== what to back up
F:\Photos\VacationPics <=== what to back up


Run the Script:

Execute the script by running python main.py in the terminal or if you want to completely automate the process make it so the script runs in specific time intervals.
The program will display constant updates on its actions, including the copying of each folder.

Important Notes:

Ensure that the USB drive is accessible and correctly specified in the text file and on the first line of the txt file.
!!!caution, as existing folders on the USB drive with the same names as source folders will be overwritten.!!!
Feel free to customize and extend the script to suit your specific needs and hopefully this helps you keep youre data more secure and fault proof! stars are allways apriciated tough :D
