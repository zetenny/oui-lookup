#!/usr/bin/python3

import update_database
import sys

# convert mac
def main():
    try:
        mac = sys.argv[2]
        parts = mac.split(':')
        oui2 = parts[0] + ':' + parts[1] + ':' + parts[2]
        uppers2 = oui2.upper()
    except:
        print('Invalid MAC address!')
        exit()

    # wireshark database
    with open('wireshark_database.txt', 'r') as macs2:
        lista2 = []
        result02 = ''
        for x in macs2:
            b = x + ':'
            lista2.append(b)
        for l in lista2:
            if uppers2 in l:
                result02 = l

        # print results
        result02.translate({ord(i): None for i in ':'})
        result03= result02.translate({ord(i): None for i in ':'})
        splitted_result = result03.split('\t')
        lista3 = []
        lista3.append(result03)
        print()
        try:
            print(splitted_result[2])
        except:
            print('No manufacturer found!')


    # append history file
    summa = mac + ' --> ' + str(result02)
    with open('history.txt', 'a') as elozmeny:
        elozmeny.write(summa)

try:
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print("""
-m, --mac [MAC]     oui lookup
-u, --update        update database
-c, --clear         clear history file""")

    elif sys.argv[1] == "--mac" or sys.argv[1] == "-m":
        main()

    elif sys.argv[1] == "--update" or sys.argv[1] == "-u":
        update_database.get_database()

    elif sys.argv[1] == "--clear" or sys.argv[1] == "-c":
        rnd = ""
        with open('history.txt', 'w') as hist:
            hist.write(rnd)

    else:
        print("Wrong option!")

except:
    print("Usage: ./lookup --help")
