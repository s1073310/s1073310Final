import requests
from pytube import YouTube


key_url = 'https://www.googleapis.com/youtube/v3/'
api_key = 'AIzaSyCBfoEmlDAYh4M7wo0RMlD30V5fL47BXpc'
channel_id = 'UC355gFBb1J4fKuDmRW4uqJw'


def download_video():

    part = 'snippet'
    for video_id in video_ids:

        url = key_url + 'videos?part=' + part + '&id=' + video_id + '&key=' + api_key
        r = requests.get(url)

        # Check request success or fail
        if r.status_code != requests.codes.ok:
            print('Request video_info Fail!')
            return 1

        # print(r.text)
        data = r.json()
        # print(data)
        video_url = 'https://www.youtube.com/watch?v=' + video_id

        # Print title and author(ChannelID)
        print('========================================')
        print(video_url)
        print('Title: ' + data['items'][0]['snippet']['title'])
        print('Channel: ' + data['items'][0]['snippet']['channelTitle'])
        print('Downloading...')
        yt = YouTube(video_url)
        yt.streams.filter(only_audio=True).first().download(r'C:\Users\Owner\Desktop\music')
        print('Complete')


def get_video_id():

    # Check if playlist is empty
    if int(playlist['pageInfo']['totalResults']) == 0:
        print('Playlist is empty')
        return 1

    videoID = []

    for item in playlist['items']:
        videoID.append(item['contentDetails']['videoId'])
    # print(ids)
    return videoID


def get_playlist_info():

    part = 'contentDetails'
    url = key_url + 'playlistItems?part=' + part + '&playlistId=' + playlist_id + '&key=' + api_key
    r = requests.get(url)

    # Check request success or fail
    if r.status_code == requests.codes.ok:
        # print(r.text)
        return r.json()
    else:
        print('Request playlist_info Fail!')
        return 1


def get_playlist_id():

    part = 'snippet'
    url = key_url + 'playlists?part=' + part + '&channelId=' + channel_id + '&key=' + api_key
    r = requests.get(url)

    # Check request success or fail
    if r.status_code != requests.codes.ok:
        print('Request playlist_id Fail!')
        return 1

    # print(r.text)
    data = r.json()
    # print(data)
    length = int(data['pageInfo']['totalResults'])
    pos = 0

    for i in range(length):
        title = data['items'][i]['snippet']['title']
        if title == 'finalProject':
            pos = i
            break
    playlistID = data['items'][pos]['id']
    return playlistID


if __name__ == "__main__":

    playlist_id = get_playlist_id()
    playlist = get_playlist_info()
    video_ids = get_video_id()
    download_video()
