import jetson.utils

def draw_C_major(frame):
    jetson.utils.cudaDrawCircle(frame, (42, 130), 10, (0, 0, 100, 200))            # C-from A-string
    jetson.utils.cudaDrawCircle(frame, (105, 100), 10, (0, 0, 100, 200))           # E-from D-string
    jetson.utils.cudaDrawCircle(frame, (138, 70), 10, (0, 0, 100, 200))            # C-from B-string
    jetson.utils.cudaDrawCircle(frame, (170, 38), 5, (0, 0, 100, 200))             # Open high E-string
