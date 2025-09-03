# YouTube Video Combiner with Audio

This Python script provides a convenient way to combine multiple video files and overlay them with audio downloaded directly from a YouTube video. It's particularly useful for creating compilations or adding background music to silent video clips.

---



## What it Does

This script automates the process of:

1.  **Downloading Audio from YouTube**: It uses `yt-dlp` to download the best available audio stream from a specified YouTube URL. The downloaded audio is saved as a temporary file.
2.  **Concatenating Videos**: It takes a list of video files (e.g., `video1.mp4`, `video2.mp4`, `video3.mp4`), removes their original audio tracks, and then concatenates them into a single video.
3.  **Overlaying Audio**: The downloaded YouTube audio is then overlaid onto the combined video. The audio is automatically trimmed to match the duration of the concatenated video.
4.  **Saving the Final Video**: The final video, with the new audio track, is saved as `final_video_with_music.mp4`.

This tool is ideal for content creators, video editors, or anyone looking to quickly merge video clips and add a custom audio track from YouTube without manual editing.

---



## Installation

To run this script, you need to have Python installed on your system. Additionally, you'll need the following Python libraries:

*   `moviepy`: For video editing and manipulation.
*   `yt-dlp`: For downloading YouTube videos and audio.

You can install these libraries using `pip`:

```bash
pip install moviepy yt-dlp
```

**Note**: `moviepy` depends on `ffmpeg`. If you don't have `ffmpeg` installed, `moviepy` will prompt you to download it, or you can install it manually from [ffmpeg.org](https://ffmpeg.org/download.html).

---



## Usage

1.  **Save the script**: Save the provided Python code as a `.py` file (e.g., `video_combiner.py`).

2.  **Prepare your video files**: Place the video files you want to combine in the same directory as the script, or provide their full paths. Update the `video_list` variable in the script with the names of your video files:

    ```python
    video_list = ["your_video1.mp4", "your_video2.mp4", "your_video3.mp4"]
    ```

3.  **Specify the YouTube URL**: Change the `youtube_url` variable to the URL of the YouTube video from which you want to extract audio:

    ```python
    youtube_url = "https://www.youtube.com/watch?v=YOUR_YOUTUBE_VIDEO_ID"
    ```

4.  **Run the script**: Open a terminal or command prompt, navigate to the directory where you saved the script, and run it using Python:

    ```bash
    python video_combiner.py
    ```

5.  **Output**: The script will download the audio, combine the videos, and save the final output as `final_video_with_music.mp4` in the same directory.

---



## Customization

You can easily customize the script by modifying the following variables:

*   `youtube_url`: Change this to any YouTube video URL to use its audio.
*   `video_list`: Add or remove video filenames from this list to combine different sets of videos. Ensure these video files are accessible by the script.
*   `output_filename`: Modify this string to change the name of the final output video file.

---

## Troubleshooting

*   **`moviepy` or `yt-dlp` not found**: Ensure you have installed the required libraries using `pip install moviepy yt-dlp`.
*   **`ffmpeg` error**: `moviepy` requires `ffmpeg`. If you encounter errors related to `ffmpeg`, make sure it's correctly installed and accessible in your system's PATH. Refer to the [ffmpeg.org](https://ffmpeg.org/download.html) website for installation instructions.
*   **Video or audio download issues**: Check your internet connection and ensure the YouTube URL is valid and the video is publicly accessible. Some videos might have restrictions that prevent downloading.
*   **Video files not found**: Make sure the video files listed in `video_list` are in the same directory as the script, or provide their full, correct paths.

---

