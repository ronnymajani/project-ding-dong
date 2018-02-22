/**
@title: Project Ding Dong encasing
@author: Ronny Majani
**/
/* Module Definitions */
/*
Creates a block in the dimensions of the chassis
This module uses the globally defined width, height, and depth variables
*/
module chassis_fill(width, height, depth) {
    dimensions = [
        width,
        depth,
        height
    ];
    cube(dimensions);
}

/*
Creates the chassis' hull which is a an outer shell with empty space inside
@param thickness: the thickness of the chassis' inner walls
@param depth: the depth of the inner space
*/
module chassis_hull(width, height, outer_depth, inner_depth, thickness) {
    offset_fix = 0.1;
    inner_dimensions = [
        width - thickness*2,
        inner_depth + offset_fix,
        height - thickness*2
    ];
    difference() {
        chassis_fill(width, height, outer_depth);
        translate([thickness, -offset_fix, thickness]) {
            resize(inner_dimensions) chassis_fill();
        }
    }
}



/* Generate Chassis */
chassis_outer_width = 30;
chassis_outer_height = 48;
chassis_outer_depth = 23;
chassis_inner_depth = 20;
chassis_thickness = 2;
chassis_hull(chassis_outer_width,
            chassis_outer_height,
            chassis_outer_depth,
            chassis_inner_depth,
            chassis_thickness);
