#!/usr/bin/python

import aiml
k = aiml.Kernel()
k.learn("thudiniska-startup.xml")
k.respond("load aiml b")
while True: print(k.respond(input("> ")))
