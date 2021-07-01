# PCAP Player
Have a pcap file you wish to re-transmit onto the wire?  Here is a Python script and Docker image that help you do 
that.

## How to use
1. Install python packages via requirements.txt file: `pip install -r requriements.txt`
1. Run pcap_player.py either taking the defaults or passing variable changes via CLI: `./pcap_player.py -h`

The result will be to *play* the infile.pcap contents onto the network.

##  Docker how to use
1. ```docker pull dmickels/pcap_player:latest```
1. ```docker run --rm --net=host -v "<path and filename to pcap>":"/app/infile.pcap" dmickels/pcap_player```
    * This shows you all the arguments you can pass.  Remove the "-h" and add any options you want.
    * The defaults will expect an "infile.pcap" for the filename of the PCAP file.

## Example
Let's say you have a PCAP file named "twinkie.pcap", and it is in the "/home/user/pcaps" directory.
The command would then be:  ```docker run --rm --net=host -v "/home/user/pcaps":"/app" dmickels/pcap_player -i twinkie.pcap```
