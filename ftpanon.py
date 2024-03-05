#!/usr/bin/python2

#Este script testa se o servico FTP alvo possui a configuracao de login anonimo ativa, enviando as credenciais
#ftp:ftp e anonymous:anonymous para isto

import socket
import sys

#Explicacao de uso da ferramenta

if len(sys.argv) != 3:
        print "Exemplo de Uso: ./ftpanon.py [IP] [PORT]"
        sys.exit()

#Criacao de socket para fazer a conexao com o alvo

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((str(sys.argv[1]), int(sys.argv[2])))

#Coleta de banner

banner = socket.recv(1024)
print "\nBanner do Servico: "+banner

#Envio de credenciais ftp:ftp

print "Enviando Usuario --> ftp"
socket.send("USER ftp\r\n")
userresp = socket.recv(1024)

print "Enviando Senha --> ftp"
socket.send("PASS ftp\r\n")
passresp = socket.recv(1024)

#Verificacao de login com credenciais ftp:ftp

if "logged" in passresp:
        print "\n[+] LOGIN ANONIMO ATIVO (ftp:ftp)"
else:
#Envio de credenciais anonymous:anonymous
        print "\nEnviando Usuario --> anonymous"
        socket.send("USER anonymous\r\n")
        userresp2 = socket.recv(1024)

        print "Enviando Senha --> anonymous"
        socket.send("PASS anonymous\r\n")
        pwdresp2 = socket.recv(1024)
#Verificacao de login com credenciais anonymous:anonymous
        if "logged" in pwdresp2:
                print "\n[+] LOGIN ANONIMO ATIVO (anonymous:anonymous)"
        else:
                print "\n[-] LOGIN ANONIMO DESATIVADO"
