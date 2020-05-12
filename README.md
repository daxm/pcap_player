# PCAP Player
Have a pcap file you wish to re-transmit onto the wire?  Here is a docker image that help you do that.

## How to use
```docker pull dmickels/pcap_player:latest```

```docker run -d --net=host -v <dir where pcap file resides>:/pcap -e PCAP_FILE=<name of pcap file> pcap_player```

## Example
Let's say you have a PCAP file named "twinkie.pcap" and it is in the "/home/user/pcaps" directory.
The command would then be:

```docker run -d --net=host -v /home/user/pcaps:/pcap -e PCAP_FILE=twinkie.pcap pcap_player```

