"""Asking CLI — cleanroom's stdin-lane demo.

Every answer comes from input(). In the cleanroom live runner, type each
answer in the terminal box (one line per Enter) before running — the VM
queues those lines and this script reads them like a real stdin. On a real
PC it reads your keyboard exactly like any other script.
"""

import sys


def verdict(name, color, number):
    print("")
    print("so, %s: you like %s" % (name, color))
    if number is None:
        print("and you could not give me a number — noted, gently")
    elif number == 7:
        print("and %d is the statistically favorite number — good taste" % number)
    else:
        print("and %d is a fine number" % number)


def main():
    print("the asking-quiz — three questions, then a verdict")
    name = input("your name? ")
    color = input("favorite color? ")
    raw = input("a number between 1 and 10? ")
    try:
        number = int(raw)
    except ValueError:
        number = None
    verdict(name, color, number)
    again = input("ask someone else? y/n ")
    if again.strip().lower() == "y":
        main()
    else:
        print("done — thanks for playing")


if __name__ == "__main__":
    main()
