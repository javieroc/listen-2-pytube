from pytube import YouTube


def download(url):
    filename = None
    try:
        yt = YouTube(url)
        filename = yt.streams.filter(progressive=True).first().default_filename
        yt.streams.filter(progressive=True).first().download(output_path='data')
    except Exception as e:
        print('Something went wrong')
        print(e)

    return filename
