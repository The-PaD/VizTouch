translate(v = [17, 17, 5]) { 

union() {

linear_extrude(file = "newgridgrid.dxf", height = 5, center = true);
linear_extrude(file = "newgridnum.dxf", height = 10, center = true);
linear_extrude(file = "Unemp.dxf", height = 10, center = true);

}}

cube(size = [168,168,3], center = false);	

