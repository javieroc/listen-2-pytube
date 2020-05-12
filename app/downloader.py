from pytube import YouTube

def download_music(url):
    filename = None
    try:
        yt = YouTube(url)
        filename = yt.streams.filter(progressive=True).first().default_filename
        yt.streams.filter(only_audio=True).first().download(output_path='data')
    except Exception as e:
        print('Something went wrong')
        print(e)

    return filename

def download_video(url):
    filename = None
    try:
        yt = YouTube(url)
        filename = yt.streams.filter(progressive=True).first().default_filename
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path='data')
    except Exception as e:
        print('Something went wrong')
        print(e)

    return filename
