import os
import time
from time import sleep

import numpy as np
import cv2


TERM_WIDTH = 203
TERM_HEIGHT = 55


def main():
    cap = cv2.VideoCapture('bad_apple.mp4')
    assert cap.isOpened(), "Can't open the video"

    h_step = int(360/TERM_HEIGHT)
    w_step = int(480/TERM_WIDTH)


    while True:
        start_time = time.time()

        ret, frame = cap.read()
        if not ret:
            print('Thanks for watching!')
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ascii_frame= ''

        for h in range(TERM_HEIGHT):
            for w in range(TERM_WIDTH):
                if frame[h_step*h][w_step*w] > 125:
                    ascii_frame += '*'
                else:
                    ascii_frame += ' '

            ascii_frame += '\n'
                
        print(ascii_frame, end='')

        elapsed_time = time.time() - start_time
        sleep(0.03333 - elapsed_time if elapsed_time < 0.03333 else 0)


if __name__ == '__main__':
    main()
