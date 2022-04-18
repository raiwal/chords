import jetson.utils


radius = 8 # for note head
notecolor = (0, 0, 0, 200) # black
staff_color =  (0, 0, 0, 200)  # black
# positions for staff in base image
staff_x = 285
# note positions for staff in background image. Whole note distance is nine pixel.
# Scientific notation used: https://en.wikipedia.org/wiki/Scientific_pitch_notation
staff_G5 = 74
staff_F5 = 83
staff_E5 = 92
staff_D5 = 102
staff_C5 = 111
staff_B4 = 120
staff_A4 = 129
staff_G4 = 138
staff_F4 = 147
staff_E4 = 156
staff_D4 = 165
staff_C4 = 174
staff_B3 = 183
staff_A3 = 192
staff_G3 = 201
staff_F3 = 210
staff_E3 = 219
# lower note support line width settings 
staff_support_line_start = staff_x - 10
staff_support_line_end = staff_x + 10
staff_support_line_thickness = 1


def draw_A_minor(frame):
    jetson.utils.cudaDrawCircle(frame,(staff_x, staff_A3), radius, notecolor)   
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_C4), (staff_support_line_end, staff_C4), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_A3), (staff_support_line_end, staff_A3), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_E4), radius, notecolor)  
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_A4), radius, notecolor)  
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_C5), radius, notecolor)  
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_E5), radius, notecolor)  


def draw_C_major(frame):
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_C4), (staff_support_line_end, staff_C4), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_C4), radius, notecolor)  
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_E4), radius, notecolor)  
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_G4), radius, notecolor)  
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_C5), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_E5), radius, notecolor)     


def draw_D_minor(frame):
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_A4), radius, notecolor)  
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_D4), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_A4), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_D5), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_F5), radius, notecolor)   


def draw_E_minor(frame):
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_F3), (staff_support_line_end, staff_F3), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_A3), (staff_support_line_end, staff_A3), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_C4), (staff_support_line_end, staff_C4), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_E3), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_B3), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_E4), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_G4), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_B4), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_E5), radius, notecolor)  


def draw_F_major(frame):
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_F3), (staff_support_line_end, staff_F3), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_A3), (staff_support_line_end, staff_A3), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_C4), (staff_support_line_end, staff_C4), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_F3), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_C4), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_F4), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_A4), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_C5), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_F5), radius, notecolor)   


def draw_G_major(frame):
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_F3), (staff_support_line_end, staff_F3), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_A3), (staff_support_line_end, staff_A3), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_C4), (staff_support_line_end, staff_C4), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_G3), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_B3), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_D4), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_G4), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_B4), radius, notecolor)      
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_G5), radius, notecolor)      