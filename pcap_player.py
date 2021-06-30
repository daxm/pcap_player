#!/usr/bin/env python3
"""Generate traffic by playing a PCAP file onto the network."""

from scapy.all import *
import argparse
import sys

# User modifiable variables
source_pcap_file = "infile.pcap"

parser = argparse.ArgumentParser()
parser.add_argument(
    "-i",
    "--infile",
    help="Path and filename of source pcap file to play.",
    default=source_pcap_file,
)
parser.add_argument(
    "-v",
    "--verbose",
    help="Display additional detail while running.",
    action="store_true",
)
parser.parse_args()
args = parser.parse_args()


def main():
    for sniffed_packet in sniff(offline=args.infile):
        if args.verbose:
            print(sniffed_packet)
        sendp(sniffed_packet)


if __name__ == "__main__":
    main()
