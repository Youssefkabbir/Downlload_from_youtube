
from pytube import Playlist
path="Y:\CoursesUniversity\Big_Data"
playlist = Playlist('https://www.youtube.com/watch?v=zez2Tv-bcXY&list=PL9ooVrP1hQOFrYxqxb0NJCdCABPZNo0pD')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Loop through all videos in the playlist and download them
for video in playlist.videos:
    print('le nom de videoest:',video)
    video.streams.first().download(path)