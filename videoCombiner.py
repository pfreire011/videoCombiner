from moviepy import VideoFileClip, concatenate_videoclips, AudioFileClip
from yt_dlp import YoutubeDL

youtube_url = "https://www.youtube.com/watch?v=9jK-NcRmVcw"

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "youtube_audio.%(ext)s",
}

try:
    with YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading audio from: {youtube_url}")
        info = ydl.extract_info(youtube_url, download=True)
        downloaded_audio_file = ydl.prepare_filename(info)
        print(f"Audio saved as: '{downloaded_audio_file}'")
except Exception as e:
    print(f"Error downloading audio: {e}")
    exit()

video_list = ["video1.mp4", "video2.mp4", "video3.mp4"]
output_filename = "final_video_with_music.mp4"

print("\nStarting process...")

videos_with_no_audio = []

for video_name in video_list:
    try:
        print(f"loading video: {video_name}")
        clip = VideoFileClip(video_name).without_audio()
        videos_with_no_audio.append(clip)
    except Exception as e:
        print(f"error loading video {video_name}: {e}")
        for c in videos_with_no_audio:
            c.close()
        exit()

if videos_with_no_audio:
    print("Combining the videos (without audio)…")
    final_video_with_no_audio = concatenate_videoclips(videos_with_no_audio, method="chain")

    try:
        audioclip = AudioFileClip(downloaded_audio_file)
        audioclip_cut = audioclip.subclip(0, final_video_with_no_audio.duration)
        final_video_with_no_audio.audio = audioclip_cut
        print(f"Saving video as: '{output_filename}'...")
        final_video_with_no_audio.write_videofile(
            output_filename,
            codec="libx264",
            audio_codec="aac"
        )

        audioclip.close()
        audioclip_cut.close()
        final_video_with_no_audio.close()
        for clip in videos_with_no_audio:
            clip.close()

        print(f"Your video'{output_filename}' was successfully created.")

    except Exception as e:
        print(f"Error processing {downloaded_audio_file}: {e}")
        final_video_with_no_audio.close()
        for clip in videos_with_no_audio:
            clip.close()
else:
    print("video list is empty.")
