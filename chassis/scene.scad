include <globals.scad>
use <chassis.scad>


/** Main Scene **/
chassis_hull(chassis_outer_width,
            chassis_outer_height,
            chassis_outer_depth,
            chassis_inner_depth,
            chassis_thickness);;




/** Support Objects **/
/*
Used only as a guide to show how the chassis will be mounted
*/
module mount_grips() {
    width = 5;
    height = 11;
    inner_depth = chassis_outer_depth;
    top_thickness = 2;
    depth = inner_depth + top_thickness;
    side_thickness = 3;
    inner_width = width - side_thickness;

    mirror()translate([-inner_width, -top_thickness, 0]) {
        difference() {
            cube([width, depth, height]);  // outer cube
            translate([-0.2, top_thickness
    , -0.2]) {  // inner cube (cut out)
                cube([inner_width + 0.2, inner_depth+0.2, height + 0.4]);
            }
        }
    }
}

%translate([0, 0, 21]) {
    mount_grips();   

    mirror() translate([-chassis_outer_width, 0, 0]){
        mount_grips();
    }
}