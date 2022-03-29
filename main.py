from feed_reader import feed_read

if __name__ == '__main__':
    urls = list(map(str,input('Enter RSS URL(s):').split()))
    for url in urls:
        feed_read(url)