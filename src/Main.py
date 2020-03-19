#!/usr/bin/env python

import slowobot
import argparse
from getpass import getpass

defaultlogin = "kochamslowotok@gmail.com"
defaultpass = "niemampomyslu"

parser = argparse.ArgumentParser()

parser.add_argument('-q', '--quiet',
        action='store_true', dest='training',
        help='Quiet mode. No words are going to be selected on the grid, but the dictionary is still going to be updated', default=False )

parser.add_argument('-l', '--login',
        action='store_true', dest='credentials',
        help='Use custom login credentials', default=False )

parser.add_argument('--firefox',
        action='store_true', dest='firefox',
        help='Use Firefox (Chrome/Chromium is the default browser)', default=False )

arguments = parser.parse_args()

if arguments.credentials:
    login = input("Login (E-mail): ")
    password = getpass("Haslo: ")
    slowobot.start(arguments.training, arguments.firefox, login, password)
else:
    slowobot.start(arguments.training, arguments.firefox, defaultlogin, defaultpass)
