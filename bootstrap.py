#!/usr/bin/env python3
"""Generate traffic by playing a PCAP file onto the network."""

from scapy.all import *
import sys

verbose = False


def main():
    for sniffed_packet in sniff(offline=sys.argv[1]):
        if verbose:
            print(sniffed_packet)
        sendp(sniffed_packet)


if __name__ == "__main__":
    main()
