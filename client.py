#!/usr/bin/env python

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
    bag = Bag('foo')
    app = App(bag)
    app.mainloop()

if __name__ == '__main__':
    wordbag()
