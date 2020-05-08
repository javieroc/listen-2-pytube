from pytube import YouTube

url = 'https://www.youtube.com/watch?v=vmlSAAxnoSE'

try:
    yt = YouTube(url)
except exception:
    print('Something went wrong')
    print(exception)
    exit('Exiting app ...')

yt.streams.filter(progressive=True).first().download('./data')
