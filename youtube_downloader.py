import youtube_dl
from requests import get
import validators
from youtube_dl import YoutubeDL
import os
from os import system
import platform
import time

# Prajnadeep

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
song_title = ''

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'noplaylist': True,
    'flatplaylist': True,
    'nocheckcertificate': True,
    'source_address': '0.0.0.0',
    'default_search': 'auto'
}


def checkURL(url):
    global song_title

    if validators.url(url):
        urlInfo = YoutubeDL(YDL_OPTIONS).extract_info(url, download=False)

        song_title = urlInfo.get('title')

        return url
    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            try:
                get(url)
            except:
                video = ydl.extract_info(f"ytsearch:{url}", download=False)['entries'][0]
            else:
                video = ydl.extract_info(url, download=False)

        video_result = str(video.get('webpage_url'))

        video_result = video_result.replace("'", "")
        video_result = video_result.replace('"', "")

        song_title = video.get('title')

    return video_result


def downloadSong(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    system('clear') if platform.system() == 'Linux' else system('cls')  # CLEAR SCREEN
    print("Downloaded " + song_title)
    print('')
    print('@https://github.com/Prajnadeep/')
    inp = input("Press Y to download another video or Press any key to quit: ")
    time.sleep(3)

    if inp == 'Y' or inp == 'y':
        main()
    else:
        exit()


def searchAgain():
    main()


def main():
    system('clear') if platform.system() == 'Linux' else system('cls')  # CLEAR SCREEN
    print("======== Youtube to MP3 Downloader =========")
    print('')
    query = input('Enter a youtube URL or search: ')
    if query == '':
        print('')
        print('Please enter a search query or URL')
        time.sleep(3)
        system('clear') if platform.system() == 'Linux' else system('cls')  # CLEAR SCREEN
        main()
    else:
        try:
            finalUrl = checkURL(query)
            system('clear') if platform.system() == 'Linux' else system('cls')  # CLEAR SCREEN
            print('Fetched Song : ' + song_title)
            print('')
            print("Press Y to Download")
            print("Press N to search again")
            download = input()

            if download == 'Y' or download == 'y':
                downloadSong(finalUrl)
            elif download == 'N' or download == 'n':
                system('clear') if platform.system() == 'Linux' else system('cls')  # CLEAR SCREEN
                searchAgain()
            else:
                print("Invalid input")
                system('clear') if platform.system() == 'Linux' else system('cls')  # CLEAR SCREEN
                main()
        except:
            print("Error ! Please check your internet connection !")

if __name__ == "__main__":
    main()
