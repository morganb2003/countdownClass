# Name: Blaine Morgan
# Date: 4/24/2022
# Project: Countdown Timer using GitHub


import time

usertime = input('Please enter the time in seconds: ')

def timercountdown(usertime):
    while usertime:
        min, secs = divmod(usertime, 60)

        timer = '{:02d} : {:02d}' .format(min, secs)

        print('\r', timer, end='')

        time.sleep(1)

        usertime -= 1

        print('\n Timer completed')

timercountdown(int(usertime))
