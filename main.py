# Import necessary libraries
import os
import time
import urllib.request

# Replace with your YouTube stream key
youtube_stream_key = "yxys-x4qa-rbv6-rsub-2j2d"

# List of video URLs from Bitrix24
video_urls = [
    "https://hanuman.s3.us-south.cloud-object-storage.appdomain.cloud/0002.mp4",
]

# Infinite loop to cycle through videos
while True:
    for idx, video_url in enumerate(video_urls):
        # Download the video to a temporary location
        temp_video_path = f"/tmp/video_{idx}.mp4"
        print(f"Downloading {video_url} to {temp_video_path}")
        urllib.request.urlretrieve(video_url, temp_video_path)

        # Construct the FFmpeg command for the current video
        ffmpeg_command = f"ffmpeg -re -i {temp_video_path} -c:v libx264 -preset veryfast -b:v 3000k -c:a aac -b:a 192k -f flv rtmp://a.rtmp.youtube.com/live2/{youtube_stream_key}"

        # Stream the current video to YouTube
        os.system(ffmpeg_command)

        # Wait a moment before moving to the next video if the stream ends
        print(f"Stream for {temp_video_path} ended. Restarting the next video in 7 seconds...")
        time.sleep(7)
