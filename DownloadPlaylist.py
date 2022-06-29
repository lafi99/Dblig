import time
import pafy

# youtube API key
pafy.set_api_key("AIzaSyCtU2gIKBhRU5Ofa_9EwTFNr3glBxCNJkM")

# ###### playlist ##########
# getting playlist
# url of playlist
url = "https://www.youtube.com/playlist?list=PLqM7alHXFySGqCvcwfqqMrteqWukz9ZoE"

playlist = pafy.get_playlist2(playlist_url=url)

# printing playlist
print(playlist)

for item in range(len(playlist)):
    url = playlist[item].getbestaudio()
    url.download(filepath=r"C:\Users\bushr\PycharmProjects\Blagin\videos")
    time.sleep(3)