#!/usr/bin/env python
import socket, sys

usage = "EchoServer.py <serverip> <port>"
HOST = sys.argv[1]
PORT = sys.argv[2]

def banner():
   print "------------------------------------------------"
   print "--------        Basic Echo Server. p 34   ------"
   print "  Don't be fancy.  serverip == localhost     "

def echosrv(HOST, PORT)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	conn, addr = s.accept()
	print 'Connected by', addr
	while 1:
	        data = conn.recv(1024)
	        if not data: break
	        conn.send(data)
	conn.close()

def main():
	if sys.argv == 2:
		banner()
		echosrv(HOST, PORT)
	else:
		usage

if __name__ = "__main__":
	main()

