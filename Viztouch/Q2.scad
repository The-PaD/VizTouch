//for apporopriate alignment of the grid
xoff = 30.5;
yoff = 0.5;
zoff = 2;
plat = 150;
plotXOff = -178;
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
qxoff = 30;
qyoff = 8;

//remove excess grid/plot
difference() {
	//align and union the grid and plot
	translate(v = [xoff,yoff,zoff]) { 
		union() {
			linear_extrude(file = "Grid/cleanGrid2.dxf", height = 3, center = false);
			if (braille) {
				translate(v=[-1*xoff,0,0]) linear_extrude(file = "Grid/gridNumQ2.dxf", height = 5, center = false);
			} else { 
				translate(v=[-1*xoff,0,0]) linear_extrude(file = "Grid/gridNumQ2_alpha.dxf", height = 5, center = false);
			}		
			translate(v=[plotXOff,0,0]){
				scale(v = [scaleFac,scaleFac,0]) linear_extrude(file = "Q2.dxf", height = 5, center = false);
			}	
			
		}
	}
	
	//blocks to remove excess
	union() {
		translate(v=[2.5,-5,0]) cube(size = [20,175,10], center=false);
		translate(v=[-170,-20,0]) cube(size = [175,20,10], center=false);
	}
}

//grid platform
translate(v=[-1*(plat-2.5),0,0]) cube(size = [plat,plat+20,3], center = false);
//title bar
first = -10;
translate(v=[first-45,plat+qyoff,zoff]) linear_extrude(file = str(f0,t0,font), height = 5 , center = false);
translate(v=[first-30,plat+qyoff,zoff]) linear_extrude(file = str(f1,t1,font), height = 5 , center = false);
translate(v=[first-15,plat+qyoff,zoff]) linear_extrude(file = str(f2,t2,font), height = 5 , center = false);
translate(v=[first,plat+qyoff,zoff]) linear_extrude(file = str(f3,t3,font), height = 5 , center = false);	
if (braille) {
	translate(v=[-1*(plat-qxoff),plat+qyoff,zoff]) linear_extrude(file = "Grid/two.dxf", height = 5, center = false);	
} else {
	translate(v=[-1*(plat-qxoff),plat+qyoff,zoff]) linear_extrude(file = "Grid/two_alpha.dxf", height = 5 , center = false);
}


