from pytube import YouTube
from colorama import Fore
import re
import sys
import os


def youtube_url_validation(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return youtube_regex_match

    return youtube_regex_match


def stream_size(stream):
    return str(stream.filesize // 1_000_000) + "mb"


def take_input():
    urls = []
    print(Fore.WHITE + "Enter Url {q to quit}")
    url_input = input()
    while url_input not in ['q', 'Q']:
        if youtube_url_validation(url_input):
            urls.append(url_input)
            print(Fore.WHITE + "Url Added! Add another one: ")
        else:
            print(Fore.RED + "This input did not match YouTube Url Validation")
            print(Fore.WHITE + "Enter Url {q to quit}:")
        url_input = input()
    return urls


def arrange_videos(urls):
    videos = []
    try:
        for url in urls:
            video = YouTube(url, on_progress_callback=None)
            stream = video.streams.filter(progressive=True, file_extension="mp4", res="720p").first()
            videos.append(stream)
            print(Fore.BLUE + 'The video '
                  + Fore.YELLOW + stream.title
                  + Fore.BLUE + ' weigh: '
                  + Fore.YELLOW + stream_size(stream))
        print(Fore.GREEN + str(len(videos)) + ' videos has been fetched')
        return videos
    except Exception as e:
        print(Fore.RED + 'An error accrued: ' + str(e))
        raise Exception('Error raised during video fetching')


def download_stream(stream):
    try:
        stream.download(output_path='C:\\Users\\ADMIN\\Downloads')
        return 1
    except Exception as e:
        return 0  # TODO


def downloader(videos):
    try:
        print(Fore.GREEN + 'Downloading...')
        download_count = 0
        for v in videos:
            print(Fore.BLUE + "Starting with: "
                  + Fore.YELLOW + v.title
                  + Fore.BLUE + ", at the size "
                  + Fore.YELLOW + stream_size(v))
            download_count += download_stream(v)
            print(Fore.BLUE + "finished with: " + v.title)
        print(Fore.GREEN + 'Downloaded ' + str(download_count) + ' out of ' + str(len(videos)))

    except Exception as e:
        print(Fore.RED + 'An error accrued: ' + str(e))
        raise Exception('Error raised during video downloading')


def main():
    print(Fore.BLUE + "Hopefully, YouTube Downloader!")
    while True:
        choice = input(Fore.BLUE + 'Choose Your Download Method: ')
        if choice == 'url':
            urls = take_input()
            if len(urls) < 1:
                print(Fore.WHITE + "Not enough Urls")
                continue
            print(Fore.WHITE + "********************")
            videos = arrange_videos(urls)
            downloader(videos)
        elif choice == 'file':
            # TODO
            pass
        else:
            print(Fore.RED + "That's not a valid option.")
        end = input("Do you want to go again ? (y/n): ")
        while end != 'y' and end != 'n':
            end = input("Please enter correct input (y/n): ")
        if end == 'n':
            break
        else:
            continue


if __name__ == "__main__":
    main()
