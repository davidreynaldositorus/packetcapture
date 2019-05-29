import subprocess
import time
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)

try:
	from scapy.all import *
except ImportError:
	sys.exit()

interface = 'wlo1'
subprocess.call(["ifconfig",interface,"promisc"],stdout=None,stderr=None,shell=False)
print ('Capturing packet....')

totalpackets=0
sniffingtime=10
protocols=0
infinite=1

def timenow():
	currenttime=time.strftime("%m%d%y-%H%M%S")
	return currenttime
	
def export():
	p = sniff(iface='wlo1',timeout=sniffingtime,count=0)
	wrpcap('pcap' + timenow() + '.pcap',p);

while infinite==1 :
	export()

