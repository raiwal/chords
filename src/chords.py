
# ➜  src git:(circle_of_fifth) ✗ cat chordlayout.py
import jetson.utils
radius = 8
notecolor = (0, 100, 100, 200)
extension_color = (0, 200, 100, 200)
staff_color =  (0, 0, 100, 200)


fretless = 38
# Note pattern here after fret 0. Each semitone is 30 px
fret_1 = 70
fret_2 = 100
fret_3 = 130

E_string = 10
A_string = 42
D_string = 74
G_string = 106
B_string = 138
e_string = 170

# positions for play marks    
open_E_string = (E_string, fretless)
open_A_string = (A_string, fretless)
open_D_string = (D_string, fretless)
open_G_string = (G_string, fretless)
open_B_string = (B_string, fretless)
open_e_string = (e_string, fretless)

F_from_E_string = (E_string, fret_1)
G_from_E_string = (E_string, fret_3)

B_from_A_string = (A_string, fret_2)
C_from_A_string = (A_string, fret_3)

E_from_D_string = (D_string, fret_2)
F_from_D_string = (D_string, fret_3)

A_from_G_string = (G_string, fret_2)

C_from_B_string = (B_string, fret_1)
D_from_B_string = (B_string, fret_3)

F_from_e_string = (e_string, fret_1)
G_from_e_string = (e_string, fret_3)

# positions for staff in image
staff_x = 285
# note positions for staff in background image
staff_G5 = 74
staff_F5 = 83
staff_E5 = 92
staff_D5 = 102
staff_C5 = 111
staff_B4 = 120
staff_A4 = 129
staff_G4 = 138
staff_F4 = 148
staff_E4 = 157
staff_D4 = 166
staff_C4 = 178
staff_B3 = 187
staff_A3 = 196
staff_G3 = 205
staff_F3 = 214
staff_E3 = 223

staff_support_line_start = staff_x - 10
staff_support_line_end = staff_x + 10
staff_support_line_thickness = 1
def draw_A_minor_to_staff(frame):
    jetson.utils.cudaDrawCircle(frame,(staff_x, staff_A3), radius, notecolor)   # A3 Open A  
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_C4), (staff_support_line_end, staff_C4), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawLine(frame, (staff_support_line_start, staff_A3), (staff_support_line_end, staff_A3), (staff_color), staff_support_line_thickness) 
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_E4), radius, notecolor)  # E4
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_A4), radius, notecolor)  # A4
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_C5), radius, notecolor)  # C5    
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_E5), radius, notecolor)  # E5 Open E   


def draw_A_minor(frame):
    jetson.utils.cudaDrawCircle(frame, open_A_string, radius, notecolor)     # Open A-string
    jetson.utils.cudaDrawCircle(frame, E_from_D_string, radius, notecolor)   # E-from D-string
    jetson.utils.cudaDrawCircle(frame, A_from_G_string, radius, notecolor)   # A-from G-string
    jetson.utils.cudaDrawCircle(frame, C_from_B_string, radius, notecolor)   # C-from B-string
    jetson.utils.cudaDrawCircle(frame, open_e_string, radius, notecolor)     # Open high E-string


def draw_C_major(frame):
    jetson.utils.cudaDrawCircle(frame, C_from_A_string, radius, notecolor)   # C-from A-string
    jetson.utils.cudaDrawCircle(frame, E_from_D_string, radius, notecolor)   # E from D-string
    jetson.utils.cudaDrawCircle(frame, open_G_string, radius, notecolor)     # open G-string
    jetson.utils.cudaDrawCircle(frame, C_from_B_string, radius, notecolor)   # C-from B-string
    jetson.utils.cudaDrawCircle(frame, open_e_string, radius, notecolor)     # Open high E-string


def draw_D_minor(frame):
    jetson.utils.cudaDrawCircle(frame, open_A_string, radius, notecolor)     # Open A-string
    jetson.utils.cudaDrawCircle(frame, open_D_string, radius, notecolor)     # Open D-string
    jetson.utils.cudaDrawCircle(frame, A_from_G_string, radius, notecolor)   # A-from G-string
    jetson.utils.cudaDrawCircle(frame, D_from_B_string, radius, notecolor)   # D-from B-string
    jetson.utils.cudaDrawCircle(frame, F_from_e_string, radius, notecolor)   # F-from e-string


def draw_E_minor(frame):
    jetson.utils.cudaDrawCircle(frame, open_E_string, radius, notecolor)     # Open E-string
    jetson.utils.cudaDrawCircle(frame, B_from_A_string, radius, notecolor)   # B-from A-string
    jetson.utils.cudaDrawCircle(frame, E_from_D_string, radius, notecolor)   # E-from D-string
    jetson.utils.cudaDrawCircle(frame, open_G_string, radius, notecolor)     # Open G-string
    jetson.utils.cudaDrawCircle(frame, open_B_string, radius, notecolor)     # Open B-string
    jetson.utils.cudaDrawCircle(frame, open_e_string, radius, notecolor)     # Open high E-string


def draw_F_major(frame):
    jetson.utils.cudaDrawCircle(frame, F_from_E_string, radius, notecolor)   # F from E-string
    jetson.utils.cudaDrawCircle(frame, C_from_A_string, radius, notecolor)   # C-from A-string
    jetson.utils.cudaDrawCircle(frame, F_from_D_string, radius, notecolor)   # F-from D-string
    jetson.utils.cudaDrawCircle(frame, A_from_G_string, radius, notecolor)   # A-from G-string
    jetson.utils.cudaDrawCircle(frame, C_from_B_string, radius, notecolor)   # C-from B-string
    jetson.utils.cudaDrawCircle(frame, F_from_e_string, radius, notecolor)   # F-from high E-string


def draw_G_major(frame):
    jetson.utils.cudaDrawCircle(frame, G_from_E_string, radius, notecolor)   # G from E-string
    jetson.utils.cudaDrawCircle(frame, B_from_A_string, radius, notecolor)   # B-from A-string
    jetson.utils.cudaDrawCircle(frame, open_D_string, radius, notecolor)     # open D-string
    jetson.utils.cudaDrawCircle(frame, open_G_string, radius, notecolor)     # open G-string
    jetson.utils.cudaDrawCircle(frame, open_B_string, radius, notecolor)     # open B-string
    jetson.utils.cudaDrawCircle(frame, G_from_e_string, radius, notecolor)   # G-from high e-string


def draw_staff(frame):
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_G4), 5, notecolor)
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_F4), 5, notecolor)
    jetson.utils.cudaDrawCircle(frame, (staff_x, staff_E3), 5, notecolor)

def chord_drawing(chord_name, frame, chord_extension):
    
    if chord_name == 'Am':
        draw_A_minor(frame)
        draw_A_minor_to_staff(frame)

    if chord_name == 'C':
        draw_C_major(frame)

    if chord_name == 'Dm':
        draw_D_minor(frame)

    if chord_name == 'Em':
        draw_E_minor(frame)

    if chord_name == 'F':
        draw_F_major(frame)

    if chord_name == 'G':
        draw_G_major(frame)

    if chord_name == 'Background':
        pass
