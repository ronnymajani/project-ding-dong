/**
@title: Project Ding Dong encasing
@author: Ronny Majani
**/

chassis_outer_width = 3;
chassis_outer_height = 4.8;
chassis_outer_depth = 2.3;

/* Module Definitions */
/*
Creates a block in the dimensions of the chassis
This module uses the globally defined width, height, and depth variables
*/
module chassis_fill() {
    chassis_outer_dimensions = [
        chassis_outer_width,
        chassis_outer_depth,
        chassis_outer_height
    ];
    cube(chassis_outer_dimensions);
}

/*
Creates the chassis' hull which is a an outer shell with empty space inside
@param thickness: the thickness of the chassis' inner walls
@param depth: the depth of the inner space
*/
module chassis_hull(thickness, depth) {
    offset_fix = 0.1;
    inner_dimensions = [
        chassis_outer_width - thickness*2,
        depth + offset_fix,
        chassis_outer_height - thickness*2
    ];
    difference() {
        chassis_fill();
        translate([thickness, -offset_fix, thickness])resize(inner_dimensions) chassis_fill();
    }
}



/* Generate Chassis */
chassis_hull(thickness=0.1, depth=1);


/* Test */
