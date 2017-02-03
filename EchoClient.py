#!/usr/bin/env python
import socket, sys

usage = "EchoClient.py <target> <port> <message>"
HOST = sys.argv[1]
PORT = sys.argv[2]
msg = sys.argv[3]

def banner():
  print "---------------------------------"
  print "---- Basic Echo client p 34 -----"

def echocli(HOST, PORT, msg)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello World')
data = s.recv(1024)
s.close()
print 'Received', repr(data)

def main():
  if len(sys.argv[3:]):
    echocli(HOST, PORT, msg)
  else:
    usage

if __name__ = "__main__":
  main()