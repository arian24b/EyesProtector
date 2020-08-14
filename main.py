#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Arian -> https://arianomrani.ir - ["https://t.me/s/devdon","https://t.me/arianomrani"]

import time

"""It takes your Name and Working time and Reminds you at the End of working time to REST A BIT."""

name = input("Enter your Name:\n")
st = int(input("Announce your working hours so that at the end of this time, I can remind you to rest:\n"))


def main(name, st):
    while True:
        starttime = int(time.time())
        time.sleep(st)
        alarmtime = int(time.time())

        if alarmtime-starttime == st:
            print(f"{name}! stop using computer and relaxing")
            print(st)


if __name__ == '__main__':
    main(name, st)
