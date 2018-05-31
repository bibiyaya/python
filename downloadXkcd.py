#! python3 
#DownloadXkcd.py - download every single skcd comic

import requests, os, bs4

url = 'http://xkcd.com'  #starting url
os.makedirs('xkcd', exist_ok=True)  #store commics in ./xkcd
while not url.endswith('#'):
    #Todo :download the page
    print('Downloading the page %s...' %url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    #Tode : find the rul of the commic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('could not find commic image')
    else:
        comicUrl = comicElem[0].get('src')
        
    #Todo : download the image
        print('Downloading image %s...' %(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    #Todp : save the image to ./xkcd 
        imageFile = open(os.path.join('skcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    #Todo : get th prev button's url
    preLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+preLink.get('href')
print('Done.')
