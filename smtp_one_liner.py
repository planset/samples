import telnetlib as T;from sys import argv as A;A[0]='localhost';A.insert(3,A[1]);T.Telnet(A[0],25).write("HELO %s\nMAIL FROM: %s\nRCPT TO: %s\nDATA\nFrom: %s\nSubject: %s\n%s\n.\n"%(tuple(A)))

#import smtplib as L;from sys import argv as A;L.SMTP('localhost','25').sendmail(A[1],A[2],'From<%s>\nTo<%s>\nSbuject:%s\n\n%s'%tuple(A[1:5]))

