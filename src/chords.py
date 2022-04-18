import staff
import chordmap


def chord_drawing(chord_name, frame):
    
    if chord_name == 'Am':
        chordmap.draw_A_minor(frame)
        staff.draw_A_minor(frame)

    if chord_name == 'C':
        chordmap.draw_C_major(frame)
        staff.draw_C_major(frame)

    if chord_name == 'Dm':
        chordmap.draw_D_minor(frame)
        staff.draw_D_minor(frame)

    if chord_name == 'Em':
        chordmap.draw_E_minor(frame)
        staff.draw_E_minor(frame)

    if chord_name == 'F':
        chordmap.draw_F_major(frame)
        staff.draw_F_major(frame)

    if chord_name == 'G':
        chordmap.draw_G_major(frame)
        staff.draw_G_major(frame)

    if chord_name == 'Background':
        pass
