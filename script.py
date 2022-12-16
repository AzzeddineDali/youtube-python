
# Import pytube package or install if not exist
from pytube import YouTube

#Function to download a video from youtube
def download_video(link):
    """
    Function to download vedio from youtube
    args :
        link : Video URL
    """
    # Create instance youtube
    youtube_object = YouTube(link)

    # Get video title before downloading
    video_title = youtube_object.title

    # Get video object
    youtube_object = youtube_object.streams.get_highest_resolution()

    # Try to download the video
    try:
        youtube_object.download()
    except:
        print("There has been an error in downloading your video")
    print("Download has completed!")


if __name__ == "__main__":
    """
    This will not be running in case of imort module
    """
    video_link = input("Set Your video link: " )
    download_video(video_link)