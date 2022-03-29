from feed_reader import feed_read

if __name__ == '__main__':
    '''Takes in user input and maps space separated the urls to list'''
    urls = list(map(str,input('Enter RSS URL(s):').split()))

    for url in urls:
        '''Passes the RSS feed url as parameter in feed_read()'''
        feed_read(url)