//for apporopriate alignment of the grid
xoff = 0.55;
yoff = 1.65;
zoff = 2;
plat = 150;
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
			linear_extrude(file = "Grid/cleanGrid1.dxf", height = 3, center = false);
			if (braille) {
				linear_extrude(file = "Grid/gridNum.dxf", height = 5, center = false);
			} else { 
				linear_extrude(file = "Grid/gridNum_alpha.dxf", height = 5, center = false);
			}		
			scale(v = [scaleFac,scaleFac,0])linear_extrude(file = "Q.dxf", height = 5, center = false);
		}
	}
	
	//blocks to remove excess
	union() {
		translate(v=[-20,-10,0]) cube(size = [20,170,10], center=false);
		translate(v=[0,-20,0]) cube(size = [170,20,10], center=false);
	}
}

//grid platform
cube(size = [plat,plat+20,3], center = false);
//title bar
first = 10;
translate(v=[first,plat+qyoff,zoff]) linear_extrude(file = str(f0,t0,font), height = 5 , center = false);
translate(v=[first+15,plat+qyoff,zoff]) linear_extrude(file = str(f1,t1,font), height = 5 , center = false);
translate(v=[first+30,plat+qyoff,zoff]) linear_extrude(file = str(f2,t2,font), height = 5 , center = false);
translate(v=[first+45,plat+qyoff,zoff]) linear_extrude(file = str(f3,t3,font), height = 5 , center = false);
if (braille) {
	translate(v=[plat-qxoff,plat+qyoff,zoff]) linear_extrude(file = "Grid/one.dxf", height = 5 , center = false);		
} else {
	translate(v=[plat-qxoff,plat+qyoff,zoff]) linear_extrude(file = "Grid/one_alpha.dxf", height = 5 , center = false);		
}
