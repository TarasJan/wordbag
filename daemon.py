#!/usr/bin/env python

import asyncio
import multiprocessing
import signal
import sys


import text_capture
from bag import Bag
from mouse_handler import MouseHandler

# disabling KeyboardInterrupt
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

# setting log
sys.stdout = open("wordbag.log", "w")

def wordbag():
    print('Daemon scraper starting...')
    bag = Bag.from_file_or_new('phrases.bag')
    exit_signal = None
    while exit_signal is None:
        try:
            handler = MouseHandler()
            with handler.listener as listener:
                listener.join()
                captured_text = text_capture.capture_text()
                bag.elements.append(captured_text)
                bag.dump_to_file('result.txt')
                bag.marshall('phrases.bag')
        except InterruptedError as error:
            exit_signal = True
    print('Daemon scraper shutting down...')

if __name__ == '__main__':
     p = multiprocessing.Process(target=wordbag)
     p.start()
     p.join()
