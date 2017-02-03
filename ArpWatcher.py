#!/usr/bin/env python


from scapy.all import sniff, ARP
from signal import signal, SIGINT
import sys

def banner():
   print "---------------------------------------------------"
   print "###### ARP Watcher.  Chapter 4, Page 39   #########"
   print ""

usage = "./UNHarpatk <target> <spoof ip>"

   sys.exit(0)

def main():
    if not len(sys.argv[1:]):
        usage()

	arp_watcher_db_file = "/Users/kenyadoit/Desktop/arpwatcher.db"
	ip_mac = {}

	def sig_int_handler(signum, frame):								#Save ARP table on shutdown
		print "Got SIGINT.  Saving ARP dtabase..."
		try:
			f = open(arp_watcher_db_file, "w")

			for (ip, mac) in ip_mac.items():
				f.write(ip + " " + mac + "\n")

			f.close()
			print "Done."
		except IOError:
			print "Cannot write file.  COME ON SERIOUSLY DUDE! " +_watcher_db_file
			sys.exit(1)

	def watch_arp(pkt):
		#got is-at pkt (ARP resposne)
		if pkt[ARP].op == 2:
			print pkt[ARP].hwsrc + " " + pkt[ARP].psrc

		#Remember new device
		if ip_mac.get(pkt[ARP].psrc) == None:
			print "Found new device " + \
				pkt[ARP].hwsc + " " + \
				pkt[ARP].psrc
			ip_mac[pkt[ARP].psrc] = pkt[ARP].hwsrc

		#Known device but different IP
		elif ip_mac.get(pkt[ARP].psrc) and ip_mac[pkt[ARP].psrc] != pkt[ARP].hwsrc:
			print pkt[ARP].hwsrc + \
			" has got new ip " + \
			" (old " + ip_mac[pkt[ARP].psrc] + ")"
			ip_mac[pkt[ARP].psrc] = pkt[ARP].hwsrc

	signal(SIGINT, sig_int_handler)

	if len(sys.argv) < 2:
		print sys.argv[0] + " <iface>"
		sys.exit(0)

	try:
		fh = open(arp_watcher_db_file, "r")
	except IOError:
		print "Cannot read file " + arp_watcher_db_file
		sys.exit(1)

	for line in fh:
		line.chomp()
		(ip, mac) = line.split (" ")
		ip_mac[ip] = mac

	sniff(prn = watch_arp, filter="arp", iface=sys.argv[1], store= 0)

if __name__ = "__main__":
	main()

