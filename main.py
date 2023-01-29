# leho.dev | github.com/Lehoooo
import sys
import os


def switch(number):
    if number == 1: # port 1
        os.system("ir-ctl -d /dev/lirc0 -S nec:0x0103 -v")
    elif number == 2: # port 2
        os.system("ir-ctl -d /dev/lirc0 -S nec:0x0100 -v")
    elif number == 3: # port 3
        os.system("ir-ctl -d /dev/lirc0 -S nec:0x0107 -v")
    elif number == 4: # port 4
        os.system("ir-ctl -d /dev/lirc0 -S nec:0x0104 -v")
    elif number == 5: # cycling port
        os.system("ir-ctl -d /dev/lirc0 -S nec:0x011F -v")


if __name__ == '__main__':
    switch(int(sys.argv[1]))
    print("done")
