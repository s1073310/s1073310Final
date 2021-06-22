 # Download YouTub playlist video using YouTube data api and Pytube
 ## 一. 動機與簡介
 會寫這個程式的動機是因為實習的公司沒有提供Wi-Fi, 所以用手機聽音樂會耗費自己的流量, 因此在電腦上把想聽的音樂先下載下來並存在手機, 就可以聽喜歡的歌, 也不會耗費手機的流量了.
 
 首先需要和Google申請一組YouTube Data API v3的API Key, 在之後提出的每一次Requests都需要用到. 還需要自己Youtube的ChannelID, 可以在YoutTube->設定->查看進階設定裡看自己的ChannelID
 還需要使用Pytube套件來下載音樂或影片. 方法是傳Request給Youtube並從回傳的內容取得自己的PlaylistID, 並從Playlist裡找到每一個影片的videoID, 有了videoID就可以知道影片的連結, 
 再用Pytube下載影片.
 
 ## 二. Requirement
 - YouTube Data API v3 API Key
 - Pytube 10.8.5
 
 ## 三. 步驟說明
 向YouTube提出Request的網址都是由https://www.googleapis.com/youtube/v3/ + 要搜尋的部分 + API Key組成, \
 part = 'snippet'代表Request所有屬性的資料, 一開始還需要自己的channelId
 ```python
 def get_playlist_id():

    part = 'snippet'
    url = key_url + 'playlists?part=' + part + '&channelId=' + channel_id + '&key=' + api_key
    r = requests.get(url)

    # Check request success or fail
    if r.status_code != requests.codes.ok:
        print('Request playlist_id Fail!')
        return 1
    # print(r.text)
 ```
    

 提出Request後, 開頭回傳的格式如下, totalResults代表會有3個撥放清單, 會接在後面
 ```
 {
  "kind": "youtube#playlistListResponse",
  "etag": "qFbdxTlQQrXON3WeJJ9usTupXB0",
  "pageInfo": {
    "totalResults": 3,
    "resultsPerPage": 5
  },
 ```
 接下來撥放清單的格式如下:
 ```
 {
      "kind": "youtube#playlist",
      "etag": "CB_m3YavOYmfk86aNsik3-ckyPw",
      "id": "PLckf5jsQmF0UwSUFFTthsI7OAO1DkVc6e",
      "snippet": {
        "publishedAt": "2021-06-13T07:15:32Z",
        "channelId": "UC355gFBb1J4fKuDmRW4uqJw",
        "title": "finalProject",
        "description": "",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/g4_nRpHotMo/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/g4_nRpHotMo/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/g4_nRpHotMo/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/g4_nRpHotMo/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "maxres": {
            "url": "https://i.ytimg.com/vi/g4_nRpHotMo/maxresdefault.jpg",
            "width": 1280,
            "height": 720
          }
        },
        "channelTitle": "Jimmy Huang",
        "localized": {
          "title": "finalProject",
          "description": ""
        }
      }
    },
 ```
 這邊只需要用到id, title兩個參數
 - id代表playlistID
 - title代表撥放清單的名稱
 
 先檢查Request是否有問題, 再轉成json格式使用, 用迴圈從頭到尾找到title為finalProject的清單, 並回傳該清單的playlistID.
 ```python
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
 ```
 接著要從清單內找出vedio的videoID, 這次的Request需要用到剛剛找到的playlistID來找清單裡的videoID 
 ```python
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
  ```
 回傳的內容
 ```
 {
  "kind": "youtube#playlistItemListResponse",
  "etag": "OaoqTZfdWp3D8eYpLuJFXSbaOmo",
  "items": [
    {
      "kind": "youtube#playlistItem",
      "etag": "9OnJ9x4ScbM4xDuoMPaNA-aB0yg",
      "id": "UExja2Y1anNRbUYwVXdTVUZGVHRoc0k3T0FPMURrVmM2ZS4wMTcyMDhGQUE4NTIzM0Y5",
      "contentDetails": {
        "videoId": "g4_nRpHotMo",
        "videoPublishedAt": "2019-11-15T09:00:14Z"
      }
    },
    {
      "kind": "youtube#playlistItem",
      "etag": "ZRvUlzdGx8lqpFyN-CNb-yTGxls",
      "id": "UExja2Y1anNRbUYwVXdTVUZGVHRoc0k3T0FPMURrVmM2ZS41MjE1MkI0OTQ2QzJGNzNG",
      "contentDetails": {
        "videoId": "fuM1aVCGR8c",
        "videoPublishedAt": "2012-09-17T08:41:36Z"
      }
    },
    {
      "kind": "youtube#playlistItem",
      "etag": "-J8RNSHqD9cRNa1Cyg5CzNJ2ZQM",
      "id": "UExja2Y1anNRbUYwVXdTVUZGVHRoc0k3T0FPMURrVmM2ZS4wOTA3OTZBNzVEMTUzOTMy",
      "contentDetails": {
        "videoId": "SviE5fHCV0c",
        "videoPublishedAt": "2016-11-17T13:52:18Z"
      }
    }
  ],
  "pageInfo": {
    "totalResults": 3,
    "resultsPerPage": 5
  }
}
```
把contentDetails底下的videoID先存進list裡, 並檢查playlist是不是空的
```python
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
```
 因為YouTube影片網址都是由https://www.youtube.com/watch?v= + videoID 所組成, \
 所以用videoID就可以找到原始上傳影片的網頁. \
 提出Request得到影片channelID和title等資訊, 會存在items的snippet底下
```
"items": [
    {
      "kind": "youtube#video",
      "etag": "6RgV8Gc8_8moFxkFgGQnj79OGJ0",
      "id": "g4_nRpHotMo",
      "snippet": {
        "publishedAt": "2019-11-15T09:00:14Z",
        "channelId": "UCkB8HnJSDSJ2hkLQFUc-YrQ",
        "title": "King Gnu - 傘  OFFICIAL AUDIO",
```
 並用pytube下載, 由於只下載音樂所以在fileter()內加上only_audio=True, 在download()內加上下載的路徑
```python
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
```
 
 ## 四. 測試與結果
 測試的playlist\
 ![image](https://user-images.githubusercontent.com/85933578/122643693-e4688080-d143-11eb-92b2-8809d9c26f26.png)
 https://www.youtube.com/playlist?list=PLckf5jsQmF0UwSUFFTthsI7OAO1DkVc6e  
 
 後面PLckf5jsQmF0UwSUFFTthsI7OAO1DkVc6e就是playlistID\
 ![image](https://user-images.githubusercontent.com/85933578/122643792-6658a980-d144-11eb-93e8-10666a4faa6f.png)
 
 可以看到"id": "PLckf5jsQmF0UwSUFFTthsI7OAO1DkVc6e", "title": "finalProject"\
 這三個影片的連結 \
 https://www.youtube.com/watch?v=g4_nRpHotMo \
 https://www.youtube.com/watch?v=fuM1aVCGR8c \
 https://www.youtube.com/watch?v=SviE5fHCV0c \
 ![image](https://user-images.githubusercontent.com/85933578/122643927-14645380-d145-11eb-89b4-767e84703a54.png)
 
 可以看到對應的videoID
 ![image](https://user-images.githubusercontent.com/85933578/122643976-470e4c00-d145-11eb-9094-d658bc102723.png)
 執行的結果, 在資料夾內可以找到下載的影片
 ![image](https://user-images.githubusercontent.com/85933578/122644001-64dbb100-d145-11eb-859e-cc981a59ebfa.png)
 
  ## 五. References
  
 https://developers.google.com/youtube/v3/docs
 
 https://pytube.io/en/latest/

 https://blog.jiatool.com/posts/youtube_spider_api/




 

