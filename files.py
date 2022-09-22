# Import the latest files from https://github.com/s1rdev10us/PythonFiles/blob/main/Python/files.py (link may change)
from json import loads, dumps, dump

"""
A Files management module designed for ease of use and simplicity rather than control
"""


#region
def read(filen:str)->str:
	"""
		Reads a text file and returns it
	"""
	f = open(filen, "r")
	filecont = (f.read())
	f.close()
	return filecont

def readjs(filen:str) -> dict:
	"""
		Reads a Json file and returns it as a dictionary
	"""
	f = open(filen, "r")
	filecont = loads(f.read())
	f.close()
	return filecont
#endregion

#region Write
def write(content:str,filen:str)->None:
	"""
		Writes a string to a file
	"""
	f = open(filen, "w")
	f.write(content)
	f.close()

def writejs(jsonf:dict|list,filen:str)->None:
	"""
		Write a Dictionary to a JSON file
	"""
	f = open(filen, "w")
	f.write(dumps(jsonf,indent=4))
	f.close()

#Wojiee's weird overwrite function that does almost the same thing as the regular write function
def overwritejs(json, file):
	"""
		Does, something? Maybe... I think?
	"""
	file.seek(0)
	#I had an issue where not putting this in added an extra } at the end of the file
	file.truncate()

	dump(json, file, indent=4)

#endregion

#region File Picker

def FilePicker(*,Extension='.json',Extensions=[('Json','.json')],Force=True,Title='Open')->str:
	"""
		Pulls up a default system file picker and returns a string representing the file location


		Extension	-> The default extension for the file

		Extensions	-> A list of tuples of strings of which the first item represents a label and the second represents the actual extension

		Force		-> A boolean representing whether to force the user to pick a file before returning to the main code

		Title		-> The string to show at the top of the window

	"""
	from tkinter import Tk
	from tkinter.filedialog import askopenfilename
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	while True:
		temp=askopenfilename(defaultextension=Extension,filetypes=Extensions,title=Title) # show an "Open" dialog box and return the path to the selected file
		if((temp !=''and temp is not None) or not Force):break
	return temp


def FolderPicker(*,Force=True,Title='Open')->str:
	"""
		Pulls up a default system file picker and returns a string representing the file location


		Extension	-> The default extension for the file

		Extensions	-> A list of tuples of strings of which the first item represents a label and the second represents the actual extension

		Force		-> A boolean representing whether to force the user to pick a file before returning to the main code

		Title		-> The string to show at the top of the window

	"""
	from tkinter import Tk
	from tkinter.filedialog import  askdirectory
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	while True:
		temp=askdirectory(initialdir='./',title=Title) # show an "Open" dialog box and return the path to the selected file
		if((temp !=''and temp is not None) or not Force):break
	return temp
if(__name__=="__main__"):
	writejs({"test":"test","notTest":{"a":0}},'test')