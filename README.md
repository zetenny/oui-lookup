It's an OUI lookup tool written in Python3.
This tool uses the Wireshark's publicly available manufacturer database.
link: https://gitlab.com/wireshark/wireshark/-/raw/master/manuf

Install dependencie:
pip3 install requests

Usage:
./lookup -m, --mac [MAC]      oui lookup
./lookup -u, --update         update database
./lookup -c, --clear          clear history file
