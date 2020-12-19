#!/usr/bin/env python

import multiprocessing
import signal
import sys

from app import App
from bag import Bag

# disabling KeyboardInterrupt
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

# # setting log
# sys.stdout = open("wordbag.log", "w")
   
def wordbag():
    print('Wordbag starting')
    bag = Bag.from_file_or_new('phrases.bag')
    app = App(bag)
    app.mainloop()

if __name__ == '__main__':
     p = multiprocessing.Process(target=wordbag)
     p.start()
     p.join()
