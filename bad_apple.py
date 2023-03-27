import os
import time
from time import sleep

import numpy as np
import cv2


def get_frame_size():
    term_height = int(os.popen('tput lines').read())
    term_width = int(os.popen('tput cols').read())

    return term_height, term_width

def render_frame(frame, term_height, term_width):
    h_step = int(360/term_height)
    w_step = int(480/term_width)

    ascii_frame = ''

    for h in range(term_height):
        for w in range(term_width):
            if frame[h_step*h][w_step*w] > 128:
                ascii_frame += '*'
            else:
                ascii_frame += ' '

        ascii_frame += '\n'

    return ascii_frame


def main():
    cap = cv2.VideoCapture('bad_apple.mp4')
    assert cap.isOpened(), "Can't open the video"

    while True:
        start_time = time.time()

        ret, frame = cap.read()
        if not ret:
            print('Thanks for watching!')
            break

        term_height, term_width = get_frame_size()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        ascii_frame = render_frame(frame, term_height, term_width)
        print(ascii_frame, end='')

        elapsed_time = time.time() - start_time
        sleep(0.03333 - elapsed_time if elapsed_time < 0.03333 else 0)


if __name__ == '__main__':
    main()
