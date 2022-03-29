from lib2to3.pgen2.parse import ParseError
from msilib.schema import Error
from urllib import request
import requests
import xml.etree.ElementTree as ET

def feed_read(link):
    try:
        res = requests.get(link)
    except:
        print('An error occured while parsing ' + link +', kindly check your RSS url')
    else:
        try:
            root = ET.fromstring(res.content)
        except ET.ParseError:
            print('An error occured while parsing ' + link +', kindly check your RSS url')
        else:
            items = root[0].findall('item')
            print(root[0].find('title').text.upper())
            print()
            for item in items[:2]:
                print('Title - ',item.find('title').text)
                print('Description - ',item.find('description').text)
                print('link - ',item.find('link').text)
                print('\n--------------------------------------------------------------\n')

    