# Download YouTub playlist video using YouTube data api and pytube
## 一. 動機與簡介
 會寫這個程式的動機是因為實習的公司沒有提供Wi-Fi, 所以用手機聽音樂會耗費自己的流量, 因此在電腦上把想聽的音樂先下載下來並存在手機, 就可以聽喜歡的歌, 也不會耗費手機的流量了.
 
 首先需要和Google申請一組YouTube Data API v3的API Key, 在之後提出的每一次Requests都需要用到. 還需要自己Youtube的ChannelID可以在, 設定->查看進階設定裡看自己的ChannelID
 
 實作的方法是傳Request給Youtube並從回傳的內容取得自己的PlaylistID, 並從Playlist裡找到每一個影片的videoID, 有了videoID就可以知道影片的連結, 再用pytube套件的功能下載影片
 
 ## 二. 
 向YouTube提出Request的網址都是由https://www.googleapis.com/youtube/v3/ + 要搜尋的細節 + API Key組成, 一開始需要自己的channelId, 提出Request後, 回傳的結果如下:
 
 回傳後, 需要轉成json格式才能使用, 接著要從撥放清單內找到finalProject這個撥放清單, 用迴圈從頭到尾找到title為finalProject的清單, 並回傳該清單的playlistID.
 
 接著要從清單內找出vedio的videoID, 這次的Request需要用到剛剛找到的playlistID來找清單裡的videoID, 找到後先存在list裡. YouTube影片網址都是由https://www.youtube.com/watch?v= + videoID 
 所組成, 所以用videoID就可以找到原始上傳影片的網站, 提出Request得到影片channelID和title等資訊, 接著用pytube下載影片就完成
