>>> dnsRequest = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname='www.facebook.com'))  

>>> dnsResponse = sr1(dnsRequest)   

# Begin emission:
# Finished sending 1 packets.
# .*
# Received 2 packets, got 1 answers, remaining 0 packets
>>> print(dnsResponse[DNS].summary())                                                          
# DNS Ans "b'star-mini.c10r.facebook.com.'" 
