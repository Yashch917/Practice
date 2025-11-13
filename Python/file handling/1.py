#file handling
#by the end of this chapter, students will be able to:
#understand what files are and why they are used
#open, read, write, and close files using Python
#work with text and CSV files
#use files modes(r,w,a,etc.)
#Handle file-related exceptions safely
#Filehandling allows a program to store data permanently on disk

# Example of file handling in Python
#Saving robot names, movements, or sensor data in a file.
#Reading that data later when the program restarts.
#in python, we use the built-in open() function to work with files.

#the open() Function
#file = open("filename.txt", "mode")

# File modes:
# "r" - Read mode (default): Opens a file for reading.
# "w" - Write mode: Opens a file for writing (creates a new file or truncates an existing file).
# "a" - Append mode: Opens a file for appending (adds data to the end of the file).