from pytube import YouTube
from tkinter import *

URL_X = 160
URL_Y = 60
LINK_ENTRY_WIDTH = 70
LINK_ENTRY_X = 32
LINK_ENTRY_Y = 90
DOWNLOADED_X = 180
DOWNLOADED_Y = 210
BUTTON_X = 180
BUTTON_Y = 220
TEXTBOX_H = 5
TEXTBOX_W = 55


def create_display_window():
    """
    create Tkinter display window.
    :return: the new display window
    """
    window = Tk()
    window.geometry('500x300')
    window.resizable(0, 0)
    window.title("Hopefully, YouTube downloader")
    return window


def download_stream(stream):
    try:
        stream.download(output_path='C:\\Users\\ADMIN\\Downloads')
        return 1
    except Exception:
        return 0


def stream_size(stream):
    return str(stream.filesize // 1_000_000) + "mb"


def fetcher():
    try:
        header.set('Arranging...')
        root.update()
        urls = take_input()

        videos = []
        for url in urls:
            root.update()
            video = YouTube(url, on_progress_callback=None)
            stream = video.streams.filter(progressive=True, file_extension="mp4", res="720p").first()
            videos.append(stream)
        print('videos has been fetched')

        header.set('Downloading...')
        download_count = 0
        for v in videos:
            print("Starting with: " + v.title + ", at the size " + stream_size(v))
            root.update()
            download_count += download_stream(v)
            print("finished with: " + v.title)
        header.set('Downloaded ' + str(download_count) + ' out of ' + str(len(urls)))
        root.update()
        input_txt.delete("1.0", "end")

    except Exception as e:
        print(e)
        header.set("An error accrued")
        root.update()


def take_input():
    urls = input_txt.get("1.0", "end-1c")
    print(urls)
    return urls.splitlines()


if __name__ == '__main__':
    root = create_display_window()

    link = StringVar()
    header = StringVar()
    button_text = StringVar()
    header.set('Enter URLs:')
    button_text.set('GET\'EM')

    Label(root, text='Youtube Downloader', font='calibre 20 bold').pack(pady=10)
    Label(root, textvariable=header, font='calibre 10 bold').place(x=URL_X, y=URL_Y)
    input_txt = Text(root, height=TEXTBOX_H, width=TEXTBOX_W, bg="pale violet red")
    input_txt.place(x=LINK_ENTRY_X, y=LINK_ENTRY_Y)

    Button(root, textvariable=button_text, font='calibre 15 bold', bg='pale violet red', padx=2, command=fetcher).place(
        x=BUTTON_X, y=BUTTON_Y)

    root.mainloop()
