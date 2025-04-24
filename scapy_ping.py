from scapy.all import *
import sys

target_ip = sys.argv[1]
icmp_pkt = IP(dst=target_ip, ttl=1) / ICMP()

reply = sr1(icmp_pkt, timeout=2)

if reply is not None:
 reply.show()
else:
 print("No reply received.")
