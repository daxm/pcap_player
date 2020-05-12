#!/usr/bin/env python3

from scapy.all import *
import sys

for sniffed_packet in sniff(offline=sys.argv[1]):
    # print(sniffed_packet)
    sendp(sniffed_packet)

