#!/usr/bin/env python
# -*- coding: latin-1 -*-

import time
import pigpio
import vw

BPS=2000 
pi = pigpio.pi()
tx = vw.tx(pi, 25, BPS)
compteur = 0
start = time.time()
while (time.time()-start) < 2:

   compteur += 2

   while not tx.ready():
      time.sleep(0.1)

   time.sleep(0.2)

   while not tx.ready():
      time.sleep(0.1)

   time.sleep(0.2)

   tx.put("0")
   exit()

tx.cancel()
pi.stop()
