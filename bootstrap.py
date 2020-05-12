#!/usr/bin/env python3

from scapy.all import *
from random import randint, choice
import sys

for sniffed_packet in sniff(offline=sys.argv[1]):
    # print(sniffed_packet)
    sendp(sniffed_packet)

