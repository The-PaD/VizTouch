//for apporopriate alignment of the grid
xoff = 28;
yoff = 29;
zoff = 2;
plat = 150;
plotXOff = -177.5;
plotYOff = -178.8;
scaleFac = 25.4;
t0 = "O";
t1 = "N";
t2 = "E";
t3 = "1";
f0 = "Letters/";
f1 = "Letters/";
f2 = "Letters/";
f3 = "Numbers/";
font = "_alpha.dxf";
braille = false;
//quadrant title offsets
qxoff = 40;
qyoff = 6;

//remove excess grid/plot
difference() {
	//align and union the grid and plot
	translate(v = [xoff,yoff,zoff]) { 
		union() {
			linear_extrude(file = "Grid/cleanGrid3.dxf", height = 3, center = false);
			if (braille) {
				translate(v=[-1*xoff,-1*yoff,0]) linear_extrude(file = "Grid/gridNumQ3.dxf", height = 5, center = false);
			} else { 
				translate(v=[-1*xoff,-1*yoff,0]) linear_extrude(file = "Grid/gridNumQ3_alpha.dxf", height = 5, center = false);
			}		
			translate(v=[plotXOff,plotYOff,0]){
				scale(v = [scaleFac,scaleFac,0]) linear_extrude(file = "Q3.dxf", height = 5, center = false);
			}
			
		}
	}
	
	//blocks to remove excess
	union() {
		translate(v=[0,-170,0]) cube(size = [20,180,10], center=false);
		translate(v=[-170,0,0]) cube(size = [175,20,10], center=false);
	}
}

//grid platform
translate(v=[-1*plat,-1*(plat+20),0]) cube(size = [plat,plat+20,3], center = false);
// title bar
first = -10;
translate(v=[first-45,-1*(plat+qyoff),zoff]) linear_extrude(file = str(f0,t0,font), height = 5 , center = false);
translate(v=[first-30,-1*(plat+qyoff),zoff]) linear_extrude(file = str(f1,t1,font), height = 5 , center = false);
translate(v=[first-15,-1*(plat+qyoff),zoff]) linear_extrude(file = str(f2,t2,font), height = 5 , center = false);
translate(v=[first,-1*(plat+qyoff),zoff]) linear_extrude(file = str(f3,t3,font), height = 5 , center = false);	
if (braille) {	
	translate(v=[-1*(plat-qxoff),-1*(plat+qyoff),zoff]) linear_extrude(file = "Grid/three.dxf", height = 5, center = false);
}else {
	translate(v=[-1*(plat-qxoff),-1*(plat+qyoff),zoff]) linear_extrude(file = "Grid/three_alpha.dxf", height = 5, center = false);
}