# Download YouTub playlist video using YouTube data api and Pytube
## 一. 動機與簡介
 會寫這個程式的動機是因為實習的公司沒有提供Wi-Fi, 所以用手機聽音樂會耗費自己的流量, 因此在電腦上把想聽的音樂先下載下來並存在手機, 就可以聽喜歡的歌, 也不會耗費手機的流量了.
 
 首先需要和Google申請一組YouTube Data API v3的API Key, 在之後提出的每一次Requests都需要用到. 還需要自己Youtube的ChannelID, 可以在YoutTube->設定->查看進階設定裡看自己的ChannelID
 還需要使用Pytube套件來下載音樂或影片. 方法是傳Request給Youtube並從回傳的內容取得自己的PlaylistID, 並從Playlist裡找到每一個影片的videoID, 有了videoID就可以知道影片的連結, 
 再用Pytube下載影片.
 
 ## 二. 詳細步驟
 向YouTube提出Request的網址都是由https://www.googleapis.com/youtube/v3/ + 要搜尋的部分 + API Key組成, 一開始需要自己的channelId, 提出Request後, 回傳的結果如下: totalResults = 清單的數量
 ![image](https://user-images.githubusercontent.com/85933578/122627509-835c9080-d0e2-11eb-902e-49399830a801.png)
 part = 'snippet'代表YouTube API會回傳網頁的所有屬性的資料
 ![image](https://user-images.githubusercontent.com/85933578/122627991-e56ac500-d0e5-11eb-8c3a-eaba9e155910.png)
 先檢查Request是否有問題, 再轉成json格式使用, 用迴圈從頭到尾找到title為finalProject的清單, 並回傳該清單的playlistID.
 接著要從清單內找出vedio的videoID, 這次的Request需要用到剛剛找到的playlistID來找清單裡的videoID 
 ![image](https://user-images.githubusercontent.com/85933578/122628036-3ed2f400-d0e6-11eb-906a-891096c608de.png)
 回傳的內容
 ![image](https://user-images.githubusercontent.com/85933578/122627775-51e4c480-d0e4-11eb-8b1c-c728fbe35740.png)
 找到videoID後先存在list裡.
 ![image](https://user-images.githubusercontent.com/85933578/122628084-a2f5b800-d0e6-11eb-9a7d-1e66d9db940f.png)
 
 因為YouTube影片網址都是由https://www.youtube.com/watch?v= + videoID 所組成, 所以用videoID就可以找到原始上傳影片的網頁. 
 提出Request得到影片channelID和title等資訊, 並列印在終端機上, 並用pytube下載由於只下載音樂所以在fileter()內加上only_audio=True, 在download()內加上下載的路徑
 ![image](https://user-images.githubusercontent.com/85933578/122643620-54c2d200-d143-11eb-8170-ecbbec3e34f3.png)
 
 ## 三. 測試與結果
 測試的playlist
 
 ![image](https://user-images.githubusercontent.com/85933578/122643693-e4688080-d143-11eb-92b2-8809d9c26f26.png)

 https://www.youtube.com/playlist?list=PLckf5jsQmF0UwSUFFTthsI7OAO1DkVc6e  
 
 後面PLckf5jsQmF0UwSUFFTthsI7OAO1DkVc6e就是playlistID
 
 ![image](https://user-images.githubusercontent.com/85933578/122643792-6658a980-d144-11eb-93e8-10666a4faa6f.png)
 
 可以看到"id": "PLckf5jsQmF0UwSUFFTthsI7OAO1DkVc6e", "title": "finalProject"
 
 這三個影片的連結 https://www.youtube.com/watch?v=g4_nRpHotMo https://www.youtube.com/watch?v=fuM1aVCGR8c https://www.youtube.com/watch?v=SviE5fHCV0c
 
 ![image](https://user-images.githubusercontent.com/85933578/122643927-14645380-d145-11eb-89b4-767e84703a54.png)
 
 可以看到對應的videoID
 ![image](https://user-images.githubusercontent.com/85933578/122643976-470e4c00-d145-11eb-9094-d658bc102723.png)
 執行的結果, 在資料夾內可以找到下載的影片
 ![image](https://user-images.githubusercontent.com/85933578/122644001-64dbb100-d145-11eb-859e-cc981a59ebfa.png)
 
  ## 四. References
  
 https://developers.google.com/youtube/v3/docs
 
 https://pytube.io/en/latest/





 

