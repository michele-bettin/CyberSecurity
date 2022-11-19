#!/usr/bin/env python3
import random
import sys
import time

cur_time = str(time.time()).encode('ASCII')
random.seed(cur_time)

msg = input('Your message: ').encode('ASCII')
key = [random.randrange(256) for _ in msg]

c = [print(k) for (m,k ) in zip(msg + cur_time, key + [0x88]*len(cur_time))]

with open("C:/Users/miche/Desktop/CyberSecurity/Lez5-CryptoTool/Exercises/3_top/enc.txt", "wb") as f:
    f.write(bytes(c))
