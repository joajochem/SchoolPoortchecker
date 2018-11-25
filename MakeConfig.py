#!/usr/bin/python
import inspect

#def main():
print "\neinde klaar!\n"
intLaagstepoort = 1
intHoogstepoort = 20
intPoortteller = intLaagstepoort

bufPart1 = ""
bufPart2 = ""

while intPoortteller <= intHoogstepoort:
    print "poort= [" , intPoortteller , "]\n"
    bufPart1 = bufPart1 + "#Port " + str(intPoortteller) + "\nListen " + str(intPoortteller) + "\n"
    bufPart2 = bufPart2 + "<VirtualHost *:" + str(intPoortteller) + ">\n    ServerName 192.168.178.36\n    DocumentRoot /var/www/html/test" + str(intPoortteller) + "\n</VirtualHost>\n\n"
    intPoortteller = intPoortteller + 1
#       bufPart2 =

print bufPart1
fout = open("test17.conf", 'w')
fout.write (bufPart1 + "\n\n" + bufPart2)
fout.close()








