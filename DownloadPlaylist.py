"""
install dependencies first:
pip install pafy
pip install youtube-dl==2020.12.2
"""
import re
import time
import pafy

# youtube API key
pafy.set_api_key("<YOUTUBE_API_KEY>")


def writeVideoInfo(video, path=""):
    # open file to write vide info
    # title = re.sub('[^0-9a-zA-Z()-]+', ' ', video.title)
    title = video.title.replace("|", " ")
    videoInfoFile = open(file=path + title + ".txt", mode="w", encoding="utf-8")
    # write video info
    try:
        videoInfoFile.write(f"title: {video.title}\n")
    except Exception as e:
        videoInfoFile.write(f"title: {title}\n")
        print(e)
    try:
        videoInfoFile.write(f"author: {video.author}\n")
    except Exception as e:
        videoInfoFile.write(f"author: None\n")
        print(e)
    try:
        videoInfoFile.write(f"category: {video.category}\n")
    except Exception as e:
        videoInfoFile.write(f"category: None\n")
        print(e)
    try:
        videoInfoFile.write(f"published: {video.published}\n")
    except Exception as e:
        videoInfoFile.write(f"published: None\n")
        print(e)
    try:
        videoInfoFile.write(f"description: {video.description}\n")
    except Exception as e:
        videoInfoFile.write(f"description: None\n")
        print(e)
    try:
        videoInfoFile.write(f"keywords: {video.keywords}\n")
    except Exception as e:
        videoInfoFile.write(f"keywords: None\n")
        print(e)
    try:
        videoInfoFile.write(f"videoid: {video.videoid}\n")
    except Exception as e:
        videoInfoFile.write(f"videoid: None\n")
        print(e)
    try:
        videoInfoFile.write(f"bigthumb: {video.bigthumb}\n")
    except Exception as e:
        videoInfoFile.write(f"bigthumb: None\n")
        print(e)
    try:
        videoInfoFile.write(f"viewcount: {video.viewcount}\n")
    except Exception as e:
        videoInfoFile.write(f"viewcount: None\n")
        print(e)
    try:
        videoInfoFile.write(f"likes: {video.likes}\n")
    except Exception as e:
        videoInfoFile.write(f"likes: None\n")
        print(e)
    try:
        videoInfoFile.write(f"dislikes: {video.dislikes}\n")
    except Exception as e:
        videoInfoFile.write(f"dislikes: None\n")
        print(e)
    try:
        videoInfoFile.write(f"rating: {video.rating}\n")
    except Exception as e:
        videoInfoFile.write(f"rating: None\n")
        print(e)
    try:
        videoInfoFile.write(f"duration: {video.duration}\n")
    except Exception as e:
        videoInfoFile.write(f"duration: None\n")
        print(e)
    try:
        videoInfoFile.write(f"length: {video.length}\n")
    except Exception as e:
        videoInfoFile.write(f"length: None\n")
        print(e)
    # close the file
    videoInfoFile.close()


# ###### playlist ##########
# url of playlist
url = "<PLAYLIST_URL>"

# getting playlist
playlist = pafy.get_playlist2(playlist_url=url)
path = r"<PATH_TO_SAVE_VIDEOS_IN>"

for item in range(len(playlist)):
    try:
        url = playlist[item].getbest()
        writeVideoInfo(playlist[item], path)
        url.download(filepath=path)
        print("video[", item, " ]", playlist[item].title, "done.")
    except Exception as e:
        print("video[", item, " ] have ", e)
        continue
    time.sleep(3)
