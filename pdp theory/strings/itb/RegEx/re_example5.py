#program to remove leading zeros from an IP address
import re
ip = "216.008.094.196"
string = re.sub('\.[0]+', '.', ip)
print(string)