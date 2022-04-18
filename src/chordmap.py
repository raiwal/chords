import jetson.utils

radius = 8
notecolor = (0, 0, 0, 200)
no_play_line_width = 2

# Open string
fretless = 38
# Note pattern here after fretless. Each semitone is 30 px
fret_1 = 70
fret_2 = 100
fret_3 = 130

E_string = 10
A_string = 42
D_string = 74
G_string = 106
B_string = 138
e_string = 170

# positions for X which indicates that note / string is not played (not played)
E_string_x1 = 8
E_string_x2 = 14
E_string_y1 = 34
E_string_y2 = 42

# positions for play marks    
open_E_string = (E_string, fretless)
open_A_string = (A_string, fretless)
open_D_string = (D_string, fretless)
open_G_string = (G_string, fretless)
open_B_string = (B_string, fretless)
open_e_string = (e_string, fretless)
# E-string notes
F_from_E_string = (E_string, fret_1)
G_from_E_string = (E_string, fret_3)
# A-string notes
B_from_A_string = (A_string, fret_2)
C_from_A_string = (A_string, fret_3)
# D-string notes
E_from_D_string = (D_string, fret_2)
F_from_D_string = (D_string, fret_3)
# G-string notes
A_from_G_string = (G_string, fret_2)
# B-string notes
C_from_B_string = (B_string, fret_1)
D_from_B_string = (B_string, fret_3)
# high e-string notes
F_from_e_string = (e_string, fret_1)
G_from_e_string = (e_string, fret_3)

font = jetson.utils.cudaFont()
chord_info_x = 10
chord_info_y = 10

def draw_A_minor(frame):
    jetson.utils.cudaDrawCircle(frame, E_from_D_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, A_from_G_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, C_from_B_string, radius, notecolor)   
    font.OverlayText(frame, frame.width, frame.height, "A-minor", chord_info_x, chord_info_y, font.Black, font.Gray40)


def draw_C_major(frame):
    jetson.utils.cudaDrawCircle(frame, C_from_A_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, E_from_D_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, C_from_B_string, radius, notecolor)   
    font.OverlayText(frame, frame.width, frame.height, "C-major", chord_info_x, chord_info_y, font.Black, font.Gray40)

def draw_D_minor(frame):
    jetson.utils.cudaDrawCircle(frame, A_from_G_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, D_from_B_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, F_from_e_string, radius, notecolor)   
    jetson.utils.cudaDrawLine(frame, (E_string_x1, E_string_y1), (E_string_x2, E_string_y2), notecolor, no_play_line_width) # E-is not part of D-minor so we draw cross here
    jetson.utils.cudaDrawLine(frame, (E_string_x1, E_string_y2), (E_string_x2, E_string_y1), notecolor, no_play_line_width) # E-is not part of D-minor so we draw cross here
    font.OverlayText(frame, frame.width, frame.height, "D-minor", chord_info_x, chord_info_y,  font.Black, font.Gray40)
 
def draw_E_minor(frame):
    jetson.utils.cudaDrawCircle(frame, B_from_A_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, E_from_D_string, radius, notecolor)   
    font.OverlayText(frame, frame.width, frame.height, "E-minor", chord_info_x, chord_info_y, font.Black, font.Gray40)

def draw_F_major(frame):
    jetson.utils.cudaDrawCircle(frame, F_from_E_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, C_from_A_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, F_from_D_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, A_from_G_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, C_from_B_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, F_from_e_string, radius, notecolor)   
    font.OverlayText(frame, frame.width, frame.height, "F-major", chord_info_x, chord_info_y,  font.Black, font.Gray40)

def draw_G_major(frame):
    jetson.utils.cudaDrawCircle(frame, G_from_E_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, B_from_A_string, radius, notecolor)   
    jetson.utils.cudaDrawCircle(frame, G_from_e_string, radius, notecolor)   
    font.OverlayText(frame, frame.width, frame.height, "G-major", chord_info_x, chord_info_y,  font.Black, font.Gray40)