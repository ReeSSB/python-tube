from pytube import YouTube


def download_video(link):
    """this function will help download video."""
     youtube_object = YouTube(link)
      youtube_object = youtube_object.streams.get_highest_resolution()
       try:
            youtube_object.download()
        except:
            print("There has been an error in downloading video.")
        print("Video download has been completed.")


link = input("put your youtube link here... URL: ")
download_video(link)
