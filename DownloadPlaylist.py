"""
install dependencies first:
pip install pafy
pip install youtube-dl==2020.12.2
"""
import time
import pafy

# youtube API key
pafy.set_api_key("<YOUTUBE_API_KEY>")


def writeVideoInfo(video, path=""):
    # open file to write vide info
    videoInfoFile = open(file=path+str(video.title).replace("|", "") + ".txt", mode="w")
    # write video info
    videoInfoFile.write(f"title: {video.title}\n")
    videoInfoFile.write(f"author: {video.author}\n")
    videoInfoFile.write(f"category: {video.category}\n")
    videoInfoFile.write(f"published: {video.published}\n")
    videoInfoFile.write(f"description: {video.description}\n")
    videoInfoFile.write(f"keywords: {video.keywords}\n")
    videoInfoFile.write(f"videoid: {video.videoid}\n")
    videoInfoFile.write(f"bigthumb: {video.bigthumb}\n")
    videoInfoFile.write(f"viewcount: {video.viewcount}\n")
    videoInfoFile.write(f"likes: {video.likes}\n")
    videoInfoFile.write(f"dislikes: {video.dislikes}\n")
    videoInfoFile.write(f"rating: {video.rating}\n")
    videoInfoFile.write(f"duration: {video.duration}\n")
    videoInfoFile.write(f"length: {video.length}\n")
    # close the file
    videoInfoFile.close()


# ###### playlist ##########
# url of playlist
url = "<PLAYLIST_URL>"

# getting playlist
playlist = pafy.get_playlist2(playlist_url=url)

for item in range(len(playlist)):
    url = playlist[item].getbestaudio()
    path =r"<PATH_TO_SAVE_PLAYLIST_IN>"
    writeVideoInfo(playlist[item], path)
    url.download(filepath=path)
    print("video", playlist[item].title, "done.")
    time.sleep(3)
