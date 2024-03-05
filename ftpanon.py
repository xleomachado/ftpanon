#!/usr/bin/python3

import socket
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((str(sys.argv[1]), int(sys.argv[2])))

print("Coletando Banner")
banner = socket.recv(1024)
print(banner)

print("Enviando usuario: ftp")
socket.send(b"USER ftp\r\n")
userresp = socket.recv(1024)

print("Enviando senha: ftp")
socket.send(b"PASS ftp\r\n")
pwdresp = socket.recv(1024)

x = b"logged in"

if x in pwdresp:
	print("\r\n------------------- LOGIN ANONIMO ATIVO -------------------")
else:
	print("\r\nEnviando usuario: anonymous")
	socket.send(b"USER anonymous\r\n")
	userresp2 = socket.recv(1024)

	print("Enviando senha: anonymous")
	socket.send(b"PASS anonymous\r\n")
	pwdresp2 = socket.recv(1024)
	if x in pwdresp2:
		print("\r\n------------------- LOGIN ANONIMO ATIVO -------------------")
	else:
		print("\r\nxxxxxxxxxxxxxxxx LOGIN ANONIMO DESATIVADO xxxxxxxxxxxxxxxx")
