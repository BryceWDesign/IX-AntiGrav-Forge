// casimir_plate_array.scad  
// OpenSCAD model for Casimir plate cavity — IX-AntiGrav-Forge  
// Author: Bryce Wooster 
// License: Open-source, non-military use only

/*  
    This file models a high-precision, adjustable plate mount system
    for use in vacuum-based Casimir interaction studies. The plates
    are held in parallel alignment via nanoscale-resolution piezo
    actuators (not modeled here) and enclosed in a vacuum shell.
*/

$fn = 200;  // smooth curvature

//---------------------------------------------
// PARAMETERS

plate_diameter = 30;         // mm
plate_thickness = 1.5;       // mm
plate_spacing_min = 0.02;    // mm (20 µm)
plate_spacing_max = 2;       // mm
support_ring_diameter = 50;  // mm
support_height = 8;          // mm
alignment_pin_diameter = 2;  // mm
alignment_pin_depth = 4;     // mm

//---------------------------------------------
// MODULES

module casimir_plate(z_offset = 0) {
    translate([0, 0, z_offset])
        cylinder(d=plate_diameter, h=plate_thickness);
}

module support_ring() {
    difference() {
        cylinder(d=support_ring_diameter, h=support_height);
        translate([0, 0, -1])
            cylinder(d=plate_diameter + 2, h=support_height + 2);
    }
}

module alignment_pins() {
    for (angle = [0, 180]) {
        rotate([0, 0, angle])
            translate([plate_diameter/2 - 3, 0, 0])
                cylinder(d=alignment_pin_diameter, h=alignment_pin_depth);
    }
}

//---------------------------------------------
// ASSEMBLY

// Lower support ring
support_ring();

// Lower plate
casimir_plate(z_offset = support_height);

// Alignment pins (to interface with top structure)
alignment_pins();

// Optional: top plate preview (not physically rendered with spacing logic here)
// Uncomment below to preview both plates in visual mockup
/*
casimir_plate(z_offset = support_height + plate_spacing_min);
*/

