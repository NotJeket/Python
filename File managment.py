# basicly it separates different file formats in separate folders for eaze of acces

import logging
from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#directory config:

source_dir = "C:\\Users\\Is_Not_NotJeket.DESKTOP-D2BOUE5\\Desktop\\test"
dest_dir_audio = "C:\\Users\\Is_Not_NotJeket.DESKTOP-D2BOUE5\\Desktop\\audio\\"
dest_dir_video = "C:\\Users\\Is_Not_NotJeket.DESKTOP-D2BOUE5\\Desktop\\video\\"
dest_dir_image = "C:\\Users\\Is_Not_NotJeket.DESKTOP-D2BOUE5\\Desktop\\img\\"
dest_dir_docs = "C:\\Users\\Is_Not_NotJeket.DESKTOP-D2BOUE5\\Desktop\\doc\\"

#extensions:

audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",".k25",
".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

docs_extensions = [".doc", ".docx", ".odt",".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

#commands

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    #if it exists it makes copy instead of overwrite
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

#file recognition

class MoverHandler(FileSystemEventHandler):
    #this will run everytime there is change in "source_dir"/.upper is in case there are uppercase extensions
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_docs_files(entry, name)

    def check_audio_files(self, entry, name):
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                move_file(dest_dir_audio, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video_files(self, entry, name):
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_docs_files(self, entry, name):
        for docs_extension in docs_extensions:
            if name.endswith(docs_extension) or name.endswith(docs_extension.upper()):
                move_file(dest_dir_docs, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_image_files(self, entry, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved audio file: {name}")

#dont change it works

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()