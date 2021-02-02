def get_database():
    import requests

    url = 'https://gitlab.com/wireshark/wireshark/-/raw/master/manuf/'
    text = requests.get(url).text

    with open('wireshark_database.txt', 'w') as dbase:
        dbase.write(text)