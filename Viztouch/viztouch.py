#!/usr/bin/env python

from Tkinter import *
import tkSimpleDialog, tkFileDialog
import subprocess
import sys
import string
import embedding.embed as veusz
from functionPlot import FunctionPlot 
from dataPlot import DataPlot

# Function var
myFunc = ""
# Data set var
myData = ""
# gridType = True for a 5x5, single quadrant grid, and False for a 10x10 4 quadrant grid.
gridSize = False
# function or dataset boolean
plotType = False
# font boolean
braille = False
# save file name (stl)
saveAsName = ""
# graph title for OpenSCAD
graphTitle = ""
# for accessing letters and numbers in OpenSCAD
folder = ""
font = ""
# directories
opendir="/Applications/OpenSCAD.app/Contents/MacOS/"
inkdir=""

#open dialog to inferface with the user

class MyDialog(tkSimpleDialog.Dialog):
		
	def body(self, master):
	
		self.type = BooleanVar()
		self.size = BooleanVar()
		self.font = BooleanVar()
		self.filename = ""
		self.savename = ""
		self.func = StringVar()
		self.dat = StringVar()
		self.dat.set("No File Selected")
		self.sav = StringVar()
		self.sav.set("No File Name")
		self.title = StringVar()

        	Label(master, text="Please define your graph:").grid(row=0,columnspan=2)
        	Label(master, text="Title:").grid(row=1, column=0, sticky=W)
    		self.t = Entry(master)
    		self.t.grid(row=1, column=1)
    		
    		Label(master, text="Font:").grid(row=2, sticky=W)
        	self.brailleb = Radiobutton(master, text="Braille", variable = self.font, value = True).grid(row=3,column=0,sticky=W)
        	self.alphab = Radiobutton(master, text="Alphanumeric", variable = self.font, value = False).grid(row=3,column=1,sticky=W)
    		
		Label(master, text="Type:").grid(row=4, sticky=W)
        	self.funcb = Radiobutton(master, text="Function", variable = self.type, value = True).grid(row=5,column=0,sticky=W)
        	self.datab = Radiobutton(master, text="Data set", variable = self.type, value = False).grid(row=5,column=1,sticky=W)
    	
    		Label(master, text="Size").grid(row=6, columnspan=2, sticky=W)
    		self.quadb = Radiobutton(master, text="5X5 (prints 1 quad)", variable = self.size, value = True).grid(row=7,column=0,sticky=W)
        	self.fullb = Radiobutton(master, text="10X10 (prints 4 quads)", variable = self.size, value = False).grid(row=7,column=1,sticky=W)
    
    		Label(master, text="Function:").grid(row=8, column=0, sticky=W)
    		self.f = Entry(master)
    		self.f.grid(row=8, column=1)
        

        	Label(master, text="Data set:").grid(row=9, column=0, sticky=W)	
        	Label(master, textvariable=self.dat).grid(row=10, column=0, columnspan=2,sticky=W)	      	
		Label(master, text="Save as file name (no extension)").grid(row=11, column=0,sticky=W)
		Label(master, textvariable=self.sav).grid(row=12, column=0, columnspan=2,sticky=W)
        	
   		Button(master, text='Select', command=self.askopenfilename).grid(row=9,column=1)
		Button(master, text='Select', command=self.asksaveasfilename).grid(row=11,column=1)
         
	def askopenfilename(self):   
        	# get filename
       		self.filename = tkFileDialog.askopenfilename()
       		self.dat.set(self.filename)
       		
	def asksaveasfilename(self):
		# get save as file name
		self.savename = tkFileDialog.asksaveasfilename()       		
		self.sav.set(self.savename)
    
	def apply(self):
        	self.func = self.f.get()
	   	self.title = self.t.get()
	
# run program		
root = Tk()
root.title("Viztouch")
d = MyDialog(root)

# collect vars
graphTitle = d.title
myFunc = d.func
myData = d.filename
gridSize = d.size.get()
plotType = d.type.get()
braille = d.font.get()
saveAsName = d.savename

# convert graphTitle to 4 separate title variables (openSCAD is goofy with arrays). Then define the folder
graphArray = list(graphTitle.upper())
t0 = graphArray[0]
t1 = graphArray[1]
t2 = graphArray[2]
t3 = graphArray[3]
folderArray = ["","","",""]
j = 0
f0 = ""
f1 = ""
f2 = ""
f3 = ""
for l in graphArray:
	if l in string.ascii_uppercase:
		folderArray[j] = "Letters/"
	elif l in string.digits:
		folderArray[j] = "Numbers/"
	else:
		print "Error: invalid character"
		sys.exit()
	j += 1
	
f0 = folderArray[0]
f1 = folderArray[1]
f2 = folderArray[2]
f3 = folderArray[3]

# determine font 
if braille:
	font = "_braille.dxf"
else:
	font = "_alpha.dxf"


# Build appropriate plot
if plotType:
	plot = FunctionPlot(gridSize, myFunc)
	plot.plotGraph()
else:
	plot = DataPlot(gridSize, myData)
	plot.plotGraph()


#Clean in Inkscape and send to OpenSCAD for conversion
if gridSize: 
	subprocess.call(inkdir+"inkscape Q.svg --verb=EditSelectAll "
	"--verb=SelectionUnGroup --verb=EditDeselect --select=g8 --verb=EditDelete "
	"--verb=EditSelectAll --verb=SelectionUnGroup --verb=EditSelectAll --verb=SelectionUnGroup "
	"--verb=EditSelectAll --verb=StrokeToPath --verb=ToolNode --verb=EditSelectAll "
	"--verb=FileSave --verb=FileClose", shell=True)
	
	#convert to eps - for some reason this fails inline with the command above...maybe due to needing 
	#to save and close the file as an SVG before saving as eps... 
	subprocess.call(inkdir+"inkscape Q.svg --export-ps=Q.ps", shell=True)

	# Save as dxf
	subprocess.call("pstoedit -dt -f dxf:-polyaslines Q.ps Q.dxf", shell=True)

	# convert to STL, via Openscad
	subprocess.call(opendir+"openscad -s "+saveAsName+".stl -D 't0="+'"'+t0+'"'+"' "
	"-D 't1="+'"'+t1+'"'+"' "
	"-D 't2="+'"'+t2+'"'+"' "
	"-D 't3="+'"'+t3+'"'+"' "
	"-D 'f0="+'"'+f0+'"'+"' "
	"-D 'f1="+'"'+f1+'"'+"' "
	"-D 'f2="+'"'+f2+'"'+"' "
	"-D 'f3="+'"'+f3+'"'+"' "
	"-D 'braille="+str(braille).lower()+"' "
	"-D 'font="+'"'+font+'"'+"' QSingle.scad", shell=True)
	
	subprocess.call("rm Q.ps Q.svg Q.dxf")
	
else:
	names = saveAsName+"1", saveAsName+"2", saveAsName+"3", saveAsName+"4"
	scadFiles = ["Q","Q2","Q3","Q4"]
	i = 0	

	for n in names:
		subprocess.call(inkdir+"inkscape " + scadFiles[i] +".svg --verb=EditSelectAll "
		"--verb=SelectionUnGroup --verb=EditDeselect --select=g8 --verb=EditDelete "
		"--verb=EditSelectAll --verb=SelectionUnGroup --verb=EditSelectAll --verb=SelectionUnGroup "
		"--verb=EditSelectAll --verb=StrokeToPath --verb=ToolNode --verb=EditSelectAll "
		"--verb=FileSave --verb=FileClose", shell=True)
		
		#convert to eps - for some reason this fails inline with the command above...maybe due to needing 
        	#to save and close the file as an SVG before saving as eps...
        	subprocess.call(inkdir+"inkscape "+scadFiles[i]+".svg --export-ps="+scadFiles[i]+".ps", shell=True)

		# Save as dxf
		subprocess.call("pstoedit -dt -f  dxf:-polyaslines "+scadFiles[i]+".ps "+scadFiles[i]+".dxf", shell=True)
		
		# convert to STL, via Openscad
		subprocess.call(opendir+"openscad -s "+ n +".stl -D 't0="+'"'+t0+'"'+"' "
		"-D 't1="+'"'+t1+'"'+"' "
		"-D 't2="+'"'+t2+'"'+"' "
		"-D 't2="+'"'+t3+'"'+"' "
		"-D 'f0="+'"'+f0+'"'+"' "
		"-D 'f1="+'"'+f1+'"'+"' "
		"-D 'f2="+'"'+f2+'"'+"' "
		"-D 'f3="+'"'+f3+'"'+"' "
		"-D 'braille="+str(braille).lower()+"' "
		"-D 'font="+'"'+font+'"'+"' "+ scadFiles[i] +".scad", shell=True)

		i+=1
		
	subprocess.call("rm Q.ps Q.svg Q.dxf Q2.ps Q2.svg Q2.dxf Q3.ps Q3.svg Q3.dxf Q4.ps Q4.svg Q4.dxf")
 
