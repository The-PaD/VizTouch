#!/user/bin env python

import embedding.embed as veusz

importPath = "/Users/craigbrown/Documents/SummerResearch/Viztouch"

class DataPlot:
	
	def __init__(self, gSize = True, data = "data"):
		self.gridSize = gSize
		self.myData = data
		self.name = "filename"
		self.g = veusz.Embedded('Plot')
		self.g.AddImportPath(u'%s' % importPath)
		self.g.ImportFileCSV(u'%s' % self.myData, linked=True)

	def plotGraph(self):
	
		self.minx = 0
		self.maxx = 5
		self.miny = 0
		self.maxy = 5
		self.lmarg = '0'
		self.rmarg = '6.277531%'
		self.tmarg = '6.277531%'
		self.bmarg = '0'		
			
		#add page1 to Root and go to page1
		self.g.To(self.g.Add('page', name='page1', autoadd=False))
		
		#Add graph1 to page1 and go to graph1
		self.g.To(self.g.Add('graph', name='graph1', autoadd=False))
		self.g.Set('leftMargin', u'%s' % self.lmarg)
		self.g.Set('rightMargin', u'%s'% self.rmarg)
		self.g.Set('topMargin', u'%s' % self.tmarg)
		self.g.Set('bottomMargin', u'%s' % self.bmarg)
		self.g.Set('Border/hide', True)	

		#Set dataset vars
		self.g.To(self.g.Add('xy', name='xy1', autoadd=False))
		self.g.Set('xData', u'col1')
		self.g.Set('yData', u'col2')
		self.g.Set('markerSize', u'3pt')
		self.g.Set('hide', False)
		self.g.Set('PlotLine/width', u'6pt')
		self.g.Set('MarkerLine/color', u'black')
		self.g.Set('MarkerLine/hide', True)
		self.g.Set('MarkerFill/style', u'solid')
		self.g.Set('MarkerFill/hide', True)
		
		if self.gridSize:
			#Single Quadrant
			self.g.To('..')
			#Set X Axis vars
			self.g.To(self.g.Add('axis', name='x', autoadd=False))
			self.g.Set('hide', True)
			self.g.Set('min', self.minx)
			self.g.Set('max', self.maxx)

			#Set Y Axis vars
			self.g.To('..')
			self.g.To(self.g.Add('axis', name='y', autoadd=False))
			self.g.Set('hide', True)
			self.g.Set('min', self.miny)
			self.g.Set('max', self.maxy)
			self.g.Set('direction', 'vertical')

			#save file
			self.g.Export(importPath+"/Q.svg")
			
		else:
			num = 0,1,2,3
			for n in num:
				if n == 0:
					# quadrant 1
					self.minx = 0
					self.maxx = 5
					self.miny = 0
					self.maxy = 5
					self.lmarg = '0'
					self.rmarg = '6.277531%'
					self.tmarg = '6.277531%'
					self.bmarg = '0'
					
					#Add graph1 to page1 and go to graph1
					self.g.To('..')
					self.g.Set('leftMargin', u'%s' % self.lmarg)
					self.g.Set('rightMargin', u'%s'% self.rmarg)
					self.g.Set('topMargin', u'%s' % self.tmarg)
					self.g.Set('bottomMargin', u'%s' % self.bmarg)
					self.g.Set('Border/hide', True)	

					#Set X Axis vars
					self.g.To(self.g.Add('axis', name='x', autoadd=False))
					self.g.Set('hide', True)
					self.g.Set('min', self.minx)
					self.g.Set('max', self.maxx)

					#Set Y Axis vars
					self.g.To('..')
					self.g.To(self.g.Add('axis', name='y', autoadd=False))
					self.g.Set('hide', True)
					self.g.Set('min', self.miny)
					self.g.Set('max', self.maxy)
					self.g.Set('direction', 'vertical')

					#save file
					self.g.Export(importPath+"/Q.svg")	
					
				elif n == 1:
					# quadrant 2
					self.minx = -5
					self.maxx = 0
					self.miny = 0
					self.maxy = 5
					self.lmarg = '6.277531%'
					self.rmarg = '0'
					self.tmarg = '6.277531%'
					self.bmarg = '0'
					
					self.g.To('..')
					
					#adjust graph1 to page1 and go to graph1
					self.g.Set('leftMargin', u'%s' % self.lmarg)
					self.g.Set('rightMargin', u'%s'% self.rmarg)
					self.g.Set('topMargin', u'%s' % self.tmarg)
					self.g.Set('bottomMargin', u'%s' % self.bmarg)
					self.g.Set('Border/hide', True)	

					#Set X Axis vars
					self.g.To('x')
					self.g.Set('hide', True)
					self.g.Set('min', self.minx)
					self.g.Set('max', self.maxx)

					#Set Y Axis vars
					self.g.To('..')
					self.g.To('y')
					self.g.Set('hide', True)
					self.g.Set('min', self.miny)
					self.g.Set('max', self.maxy)
					self.g.Set('direction', 'vertical')

					#save file
					self.g.Export(importPath+"/Q2.svg")	
				elif n == 2:
					# quadrant 3
					self.minx = -5
					self.maxx = 0
					self.miny = -5
					self.maxy = 0
					self.lmarg = '6.277531%'
					self.rmarg = '0'
					self.tmarg = '0'
					self.bmarg = '6.277531%'
					
					self.g.To('..')
					
					#adjust graph1 to page1 and go to graph1
					self.g.Set('leftMargin', u'%s' % self.lmarg)
					self.g.Set('rightMargin', u'%s'% self.rmarg)
					self.g.Set('topMargin', u'%s' % self.tmarg)
					self.g.Set('bottomMargin', u'%s' % self.bmarg)
					self.g.Set('Border/hide', True)	

					#Set X Axis vars
					self.g.To('x')
					self.g.Set('hide', True)
					self.g.Set('min', self.minx)
					self.g.Set('max', self.maxx)

					#Set Y Axis vars
					self.g.To('..')
					self.g.To('y')
					self.g.Set('hide', True)
					self.g.Set('min', self.miny)
					self.g.Set('max', self.maxy)
					self.g.Set('direction', 'vertical')

					#save file
					self.g.Export(importPath+"/Q3.svg")	
				else:
					# quadrant 4
					self.minx = 0
					self.maxx = 5
					self.miny = -5
					self.maxy = 0
					self.lmarg = '0'
					self.rmarg = '6.277531%'
					self.tmarg = '0'
					self.bmarg = '6.277531%'
					
					self.g.To('..')
										#adjust graph1 to page1 and go to graph1
					self.g.Set('leftMargin', u'%s' % self.lmarg)
					self.g.Set('rightMargin', u'%s'% self.rmarg)
					self.g.Set('topMargin', u'%s' % self.tmarg)
					self.g.Set('bottomMargin', u'%s' % self.bmarg)
					self.g.Set('Border/hide', True)	

					#Set X Axis vars
					self.g.To('x')
					self.g.Set('hide', True)
					self.g.Set('min', self.minx)
					self.g.Set('max', self.maxx)

					#Set Y Axis vars
					self.g.To('..')
					self.g.To('y')
					self.g.Set('hide', True)
					self.g.Set('min', self.miny)
					self.g.Set('max', self.maxy)
					self.g.Set('direction', 'vertical')

					#save file
					self.g.Export(importPath+"/Q4.svg")
		
		self.g.Close()




