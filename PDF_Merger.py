
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileMerger


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

root = Tk()
ftypes = [('All files','*.*')]
ttl  = "Select the file"
dir1 = desktop
root.fileName = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl,multiple=True)
naming = str(root.fileName)


# print(type(naming))
# print(naming)

pdfs = naming.split("'")
for x in pdfs:
    if len(x)<10:
        pdfs.remove(x)

# print(splitting)
# print(root.tk.splitlist(naming))

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(desktop +r"\merged_file.pdf")
merger.close()