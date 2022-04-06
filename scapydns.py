from scapy.all import DNS, DNSQR, IP, sr1, UDP
import sys
queryHost=sys.argv[1]

>>> dnsRequest = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname='qname=queryHost'))  

>>> dnsResponse = sr1(dnsRequest)   

>>> print(dnsResponse[DNS].summary())                                                          
