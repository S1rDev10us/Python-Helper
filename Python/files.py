from json import loads, dumps, dump

#region
def read(filen)->str:
	"""
		Reads a text file and returns it
	"""
	f = open(filen, "r")
	filecont = (f.read())
	f.close()
	return filecont

def readjs(filen) -> dict:
	"""
		Reads a Json file and returns it as a dictionary
	"""
	f = open(filen, "r")
	filecont = loads(f.read())
	f.close()
	return filecont
#endregion

#region Write
def write(content,filen)->None:
	"""
		Writes a string to a file
	"""
	f = open(filen, "w")
	f.write(content)
	f.close()

def writejs(jsonf,filen)->None:
	"""
		Write a Dictionary to a JSON file
	"""
	f = open(filen, "w")
	f.write(dumps(jsonf))
	f.close()

#Wojiee's weird overwrite function that does almost the same thing as the regular write function
def overwritejs(json, file):
	"""
		Does, something? Maybe... I think?
	"""
	file.seek(0)
	dump(json, file, indent=4)

#endregion


#region File Picker
from tkinter import Tk
from tkinter.filedialog import askopenfilename
def FilePicker(*,Extension='.json',Extensions=[('Json','.json')],Force=True,Title='Open')->str:
	"""
		Pulls up a default system file picker and returns a string representing the file location


		Extension	-> The default extension for the file

		Extensions	-> A list of tuples of strings of which the first item represents a label and the second represents the actual extension

		Force		-> A boolean representing whether to force the user to pick a file before returning to the main code

		Title		-> The string to show at the top of the window

	"""
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	while True:
		temp=askopenfilename(defaultextension=Extension,filetypes=Extensions,title=Title) # show an "Open" dialog box and return the path to the selected file
		if((temp !=''or temp is not None) or not Force):break
	return temp
