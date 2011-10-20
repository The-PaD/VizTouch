//for apporopriate alignment of the grid
xoff = 17;
yoff = 17;
zoff = 2;
plat = 167;
scaleFac = 25.4;

//remove excess grid/plot
difference() {
	//align and union the grid and plot
	translate(v = [xoff, yoff, zoff]) { 
		union() {
			linear_extrude(file = "cleanGrid1.dxf", height = 3, center = false);
			linear_extrude(file = "newgridnum.dxf", height = 5, center = false);
			linear_extrude(file = "DataAQuad.dxf", height = 5, center = false);
			linear_extrude(file = "DataBQuad.dxf", height = 7, center = false);
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
translate(v=[plat/2,plat+8,zoff]) linear_extrude(file = "one.dxf", height = 5 , center = false);		

