from tkinter import Tk
from tkinter.filedialog import askopenfilename

root = Tk()
ftypes = [('htm file',"*.htm")]
ttl  = "Title"
dir1 = 'C:\\'
root.fileName = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
print (root.fileName)