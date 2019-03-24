import urllib.request
import json



def YouTube_API(search,KEY):
    url = f'https://www.googleapis.com/youtube/v3/search?q={search}&type=video&key={KEY}&part=snippet&maxResults=10'
    info = urllib.request.urlopen(url)
    result = json.load(info)
    ret = []
    for video in sorted(result['items'], key = lambda item : item['snippet']['publishedAt'], reverse = True):
        ret.append(video['snippet']['title'])
        date = video['snippet']['publishedAt']
        ret.append(f'Date of Publication: {date[5:7]}-{date[8:10]}-{date[0:4]}')
        link = 'https://www.youtube.com/watch?v=' + video['id']['videoId']
        ret.append(link)
    return ret