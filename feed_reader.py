from lib2to3.pgen2.parse import ParseError
from msilib.schema import Error
from urllib import request
import requests
import xml.etree.ElementTree as ET

def feed_read(link):
    '''feed_read() parses the response and prints the blogs from the RSS feed'''

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
            #All the items tags are stored in items
            items = root[0].findall('item')
            N = 5
            if not len(items)>=N:
                N = len(items)

            #prints the title of the RSS feed
            print('~~~~~~~~~ '+root[0].find('title').text.upper()+' ~~~~~~~~~')
            print()

            #iterates through items and prints title, description, link for each item
            #Here only first five posts from each RSS feed are being printed for sake of simplicity
            #and can be changed as per user's requirement by changing N
            for item in items[:N]:
                print('Title - ',item.find('title').text)
                print('Description - ',item.find('description').text)
                print('link - ',item.find('link').text)
                print('\n--------------------------------------------------------------\n')

    