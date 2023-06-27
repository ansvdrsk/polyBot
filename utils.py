from yt_dlp import YoutubeDL


def search_download_youtube_video(video_name, num_results=1):
    ydl_opts = {
        'verbose': True,
        'default_search': f"ytsearch{num_results}: {video_name}",
        'format': 'best',
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_name, download=True)
        video_title = info.get('title', None)

        if video_title:
            return f"{video_title}.mp4"

    return ""
