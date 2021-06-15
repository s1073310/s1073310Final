# Download YouTub playlist video using YouTube data api and pytube
## 一. 動機與簡介
 會寫這個程式的動機是因為實習的公司沒有提供Wi-Fi, 所以用手機聽音樂會耗費自己的流量, 因此在電腦上把想聽的音樂先下載下來並存在手機, 就可以聽喜歡的歌, 也不會耗費手機的流量了.
 
 首先需要和Google申請一組YouTube Data API v3的API Key, 在之後提出的Requests都需要用到. 還需要自己Youtube的ChannelID可以在, 設定->查看進階設定裡看自己的ChannelID
 
 實作的方法是傳Request給Youtube並從回傳的內容取得自己的PlaylistID, 並從Playlist裡找到每一個影片的videoID, 有了videoID就可以知道影片的連結, 再用pytube套件的功能下載影片
 
 ## 二. 
