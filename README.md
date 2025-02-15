## youtube-music-dl

### Requirements

- brave browser
- yt-dlp
- ffmpeg

### Usage

```bash
# run the script to generate the cookies.txt file
uv run app.py

# download the video
yt-dlp -F --cookies cookies.txt https://music.youtube.com/watch?v=2XxA6YNBG7I

# for video with black background
ffmpeg -f lavfi -i color=c=black:s=1280x720:r=30 -i revolutionary.m4a -c:v libx264 -c:a aac -shortest output.mp4

# for video with image background
ffmpeg -loop 1 -i image.jpg -i audio.m4a -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -c:a aac -shortest output.mp4
```

### Notes

- When using an image as background, make sure the image dimensions are even numbers (divisible by 2). If not, use the `-vf "scale=trunc(iw/2)*2:trunc(ih/2)*2"` option to automatically adjust the dimensions.

