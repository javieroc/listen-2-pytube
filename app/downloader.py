from pytube import YouTube


def download(url):
    data = None
    try:
        yt = YouTube(url)
        data = yt.streams.filter(progressive=True).first().download(output_path='./data')
    except Exception as e:
        print('Something went wrong')
        print(e)

    return data
