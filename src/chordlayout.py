import jetson.utils
radius = 8
notecolor = (0, 100, 100, 200)

open_E_string = (10, 38)
open_A_string = (42, 38)
open_D_string = (74, 38)
open_G_string = (106, 38)
open_B_string = (137, 38)
open_e_string = (170, 38)

F_from_E_string = (10, 70)
G_from_E_string = (10, 130)

B_from_A_string = (42, 100)
C_from_A_string = (42, 130)

E_from_D_string = (74, 100)
F_from_D_string = (74, 130)

A_from_G_string = (106, 100)

C_from_B_string = (138, 70)
D_from_B_string = (138, 130)

F_from_e_string = (170, 70)
G_from_e_string = (170, 130)

def draw_A_minor(frame):
    jetson.utils.cudaDrawCircle(frame, open_A_string, radius, notecolor)    # Open A-string
    jetson.utils.cudaDrawCircle(frame, E_from_D_string, radius, notecolor)   # E-from D-string
    jetson.utils.cudaDrawCircle(frame, A_from_G_string, radius, notecolor)  # A-from G-string
    jetson.utils.cudaDrawCircle(frame, C_from_B_string, radius, notecolor)   # C-from B-string
    jetson.utils.cudaDrawCircle(frame, open_e_string, radius, notecolor)   # Open high E-string


def draw_C_major(frame):
    jetson.utils.cudaDrawCircle(frame, C_from_A_string, radius, notecolor)   # C-from A-string
    jetson.utils.cudaDrawCircle(frame, E_from_D_string, radius, notecolor)   # E from D-string
    jetson.utils.cudaDrawCircle(frame, open_G_string, radius, notecolor)  # open G-string
    jetson.utils.cudaDrawCircle(frame, C_from_B_string, radius, notecolor)   # C-from B-string
    jetson.utils.cudaDrawCircle(frame, open_e_string, radius, notecolor)   # Open high E-string


def draw_D_minor(frame):
    jetson.utils.cudaDrawCircle(frame, open_A_string, radius, notecolor)    # Open A-string
    jetson.utils.cudaDrawCircle(frame, open_D_string, radius, notecolor)    # Open D-string
    jetson.utils.cudaDrawCircle(frame, A_from_G_string, radius, notecolor)  # A-from G-string
    jetson.utils.cudaDrawCircle(frame, D_from_B_string, radius, notecolor)  # D-from B-string
    jetson.utils.cudaDrawCircle(frame, F_from_e_string, radius, notecolor)   # F-from e-string


def draw_E_minor(frame):
    jetson.utils.cudaDrawCircle(frame, open_E_string, radius, notecolor)    # Open E-string
    jetson.utils.cudaDrawCircle(frame, B_from_A_string, radius, notecolor)   # B-from A-string
    jetson.utils.cudaDrawCircle(frame, E_from_D_string, radius, notecolor)   # E-from D-string
    jetson.utils.cudaDrawCircle(frame, open_G_string, radius, notecolor)   # Open G-string
    jetson.utils.cudaDrawCircle(frame, open_B_string, radius, notecolor)   # Open B-string
    jetson.utils.cudaDrawCircle(frame, open_e_string, radius, notecolor)   # Open high E-string


def draw_F_major(frame):
    jetson.utils.cudaDrawCircle(frame, F_from_E_string, radius, notecolor)    # F from E-string
    jetson.utils.cudaDrawCircle(frame, C_from_A_string, radius, notecolor)   # C-from A-string
    jetson.utils.cudaDrawCircle(frame, F_from_D_string, radius, notecolor)   # F-from D-string
    jetson.utils.cudaDrawCircle(frame, A_from_G_string, radius, notecolor)  # A-from G-string
    jetson.utils.cudaDrawCircle(frame, C_from_B_string, radius, notecolor)   # C-from B-string
    jetson.utils.cudaDrawCircle(frame, F_from_e_string, radius, notecolor)   # F-from high E-string


def draw_G_major(frame):
    jetson.utils.cudaDrawCircle(frame, G_from_E_string, radius, notecolor)   # G from E-string
    jetson.utils.cudaDrawCircle(frame, B_from_A_string, radius, notecolor)   # B-from A-string
    jetson.utils.cudaDrawCircle(frame, open_D_string, radius, notecolor)    # open D-string
    jetson.utils.cudaDrawCircle(frame, open_G_string, radius, notecolor)   # open G-string
    jetson.utils.cudaDrawCircle(frame, open_B_string, radius, notecolor)   # open B-string
    jetson.utils.cudaDrawCircle(frame, G_from_e_string, radius, notecolor)  # G-from high e-string


def chord_drawing(chord_name, frame):

    if chord_name == 'Am':
        draw_A_minor(frame)

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
