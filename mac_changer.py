#!/usr/bin/env python
import subprocess
import optparse

def mac_changer(interface,mac_addr):
	subprocess.call(["ifconfig", interface ,"down"])
	subprocess.call(["ifconfig" , interface , "hw","ether" , mac_addr])
	subprocess.call(["ifconfig" , interface , "up"])
	print("[+] Changed the MAC address of " + interface + " to " + mac_addr)

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface",dest="interface",help="Network interface you wants to change")
	parser.add_option("-m","--mac_addr",dest="mac_addr",help="new mac address you wants to replace")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specify the interface, use --help for more information")
	elif not options.mac_addr:
		parser.error("[-] Please specify the MAC address, use --help for more information")
	return options

	
options = get_arguments()
mac_changer(options.interface, options.mac_addr)
