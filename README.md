# Download YouTub playlist video using YouTube data api and pytube
## 一. 動機與簡介
 會寫這個程式的動機是因為實習的公司沒有提供Wi-Fi, 所以用手機聽音樂會耗費自己的流量, 因此在電腦上把想聽的音樂先下載下來並存在手機, 就可以聽喜歡的歌, 也不會耗費手機的流量了.
 
 首先需要和Google申請一組YouTube Data API v3的API Key, 在之後提出的每一次Requests都需要用到. 還需要自己Youtube的ChannelID可以在, 設定->查看進階設定裡看自己的ChannelID
 
 實作的方法是傳Request給Youtube並從回傳的內容取得自己的PlaylistID, 並從Playlist裡找到每一個影片的videoID, 有了videoID就可以知道影片的連結, 再用pytube套件的功能下載影片
 
 ## 二. 
 向YouTube提出Request的網址都是由https://www.googleapis.com/youtube/v3/ + 要搜尋的部分 + API Key組成, 一開始需要自己的channelId, 提出Request後, 回傳的結果如下:
 ![image](https://user-images.githubusercontent.com/85933578/122627509-835c9080-d0e2-11eb-902e-49399830a801.png)
 totalResults = 清單的數量
 ![image](https://user-images.githubusercontent.com/85933578/122627991-e56ac500-d0e5-11eb-8c3a-eaba9e155910.png)
 回傳後, 先檢查Request是否有問題, 再轉成json格式使用, 用迴圈從頭到尾找到title為finalProject的清單, 並回傳該清單的playlistID.
 接著要從清單內找出vedio的videoID, 這次的Request需要用到剛剛找到的playlistID來找清單裡的videoID 
 ![image](https://user-images.githubusercontent.com/85933578/122628036-3ed2f400-d0e6-11eb-906a-891096c608de.png)
 回傳的內容
 ![image](https://user-images.githubusercontent.com/85933578/122627775-51e4c480-d0e4-11eb-8b1c-c728fbe35740.png)
 找到videoID後先存在list裡.
 ![image](https://user-images.githubusercontent.com/85933578/122628084-a2f5b800-d0e6-11eb-9a7d-1e66d9db940f.png)
 因為YouTube影片網址都是由https://www.youtube.com/watch?v= + videoID 
 所組成, 所以用videoID就可以找到原始上傳影片的網頁, 並對
 提出Request得到影片channelID和title等資訊, 接著用pytube下載影片就完成
