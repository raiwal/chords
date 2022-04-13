import jetson.utils

def draw_A_minor(frame):
    jetson.utils.cudaDrawCircle(frame, (42, 38), 8, (0, 0, 100, 200))              # Open A-string
    jetson.utils.cudaDrawCircle(frame, (74, 100), 8, (0, 0, 100, 200))             # E-from D-string
    jetson.utils.cudaDrawCircle(frame, (106, 100), 8, (0, 0, 100, 200))             # A-from D-string
    jetson.utils.cudaDrawCircle(frame, (138, 70), 8, (0, 0, 100, 200))          # C-from B-string
    jetson.utils.cudaDrawCircle(frame, (170, 38), 8, (0, 0, 100, 200))             # Open high E-string

def draw_C_major(frame):
    jetson.utils.cudaDrawCircle(frame, (42, 130), 10, (0, 0, 100, 200))            # C-from A-string
    jetson.utils.cudaDrawCircle(frame, (105, 100), 10, (0, 0, 100, 200))           # E-from D-string
    jetson.utils.cudaDrawCircle(frame, (138, 70), 10, (0, 0, 100, 200))            # C-from B-string
    jetson.utils.cudaDrawCircle(frame, (170, 38), 5, (0, 0, 100, 200))             # Open high E-string

def draw_D_minor(frame):
    jetson.utils.cudaDrawCircle(frame, (42, 38), 8, (0, 0, 100, 200))       # Open A-string
    jetson.utils.cudaDrawCircle(frame, (74, 38), 8, (0, 0, 100, 200))              # Open D-string
    jetson.utils.cudaDrawCircle(frame, (106, 100), 8, (0, 0, 100, 200))   # A-from G-string
    jetson.utils.cudaDrawCircle(frame, (138, 130), 8, (0, 0, 100, 200))   # D-from B-string
    jetson.utils.cudaDrawCircle(frame, (170, 70), 8, (0, 0, 100, 200))   # F-from e-string

def draw_E_minor(frame):
    jetson.utils.cudaDrawCircle(frame, (10, 38), 8, (0, 0, 100, 200))              # Open E-string
    jetson.utils.cudaDrawCircle(frame, (42, 100), 8, (0, 0, 100, 200))  # B-from A-string
    jetson.utils.cudaDrawCircle(frame, (74, 100), 8, (0, 0, 100, 200))    # E-from D-string
    jetson.utils.cudaDrawCircle(frame, (106, 38), 8, (0, 0, 100, 200))             # Open G-string
    jetson.utils.cudaDrawCircle(frame, (137, 38), 8, (0, 0, 100, 200))             # Open B-string
    jetson.utils.cudaDrawCircle(frame, (170, 38), 8, (0, 0, 100, 200))             # Open high E-string

def draw_F_major(frame):
    jetson.utils.cudaDrawCircle(frame, (10, 70), 8, (0, 0, 100, 200))    # F from E-string
    jetson.utils.cudaDrawCircle(frame, (42, 130), 8, (0, 0, 100, 200)) # C-from A-string
    jetson.utils.cudaDrawCircle(frame, (74, 130), 8, (0, 0, 100, 200))    # F-from D-string
    jetson.utils.cudaDrawCircle(frame, (106, 100), 8, (0, 0, 100, 200))  # A-from G-string
    jetson.utils.cudaDrawCircle(frame, (137, 70), 8, (0, 0, 100, 200))   # C-from B-string
    jetson.utils.cudaDrawCircle(frame, (170, 70), 8, (0, 0, 100, 200))    # F-from high E-string

def draw_G_major(frame):
    jetson.utils.cudaDrawCircle(frame, (10, 130), 8, (0, 0, 100, 200))   # G from E-string
    jetson.utils.cudaDrawCircle(frame, (42, 100), 8, (0, 0, 100, 200))    # B-from A-string
    jetson.utils.cudaDrawCircle(frame, (74, 38), 8, (0, 0, 100, 200))              # open D-string
    jetson.utils.cudaDrawCircle(frame, (106, 38), 8, (0, 0, 100, 200))            # open G-string
    jetson.utils.cudaDrawCircle(frame, (137, 38), 8, (0, 0, 100, 200))             # open B-string
    jetson.utils.cudaDrawCircle(frame, (170, 130), 8, (0, 0, 100, 200)) # G-from high e-string


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
