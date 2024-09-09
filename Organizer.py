from os import scandir, rename
from os.path import exists, join, splitext
from shutil import move
import logging


source_dir = r"C:\Users\dgsy2\Downloads"
musicDestination = r"C:\Users\dgsy2\Music"
videoDestination = r"C:\Users\dgsy2\Videos"
documentDestination = r"C:\Users\dgsy2\Documents\WordDocuments"
PDFDestination = r"C:\Users\dgsy2\Documents\PDF"
spreadsheetDestination = r"C:\Users\dgsy2\Documents\Spreadsheet"
imageDestination = r"C:\Users\dgsy2\Pictures"
miscellaneousDestination = r"C:\Users\dgsy2\Documents\Misc"

all_extensions = []

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

document_extensions = [".doc", ".docx", ".odt", ".ppt", ".pptx"]

pdf_extensions = [".pdf"]

spreadsheet_extensions = [".xls", ".xlsx"]

    
def create_unique_file(location, name):
    filename, extension = splitext(name)
    counter = 1
    
    while exists(f"{location}/{name}"):
        name = f"{filename}_{counter}{extension}"
        counter += 1
    return name

def move_file(location, entry, name):
    print(f"{location}/{name}")
    if exists(f"{location}/{name}"):
        uniqueName = create_unique_file(location, name)
        oldName = join(location,name)
        newName = join(location, uniqueName)
        rename(oldName, newName)
    move(entry, location)
    
def cleanerFunction():
    with scandir(source_dir) as entries:
        for entry in entries:
            print(f"{entry.name}")
            name = entry.name
            checkIfAudio(entry, name)
            checkIfVideo(entry, name)
            checkIfImage(entry, name)
            checkIfDocument(entry, name)
            checkIfPDF(entry, name)
            checkIfSpreadsheet(entry, name)
            checkIfMisc(entry, name)

def checkIfAudio(entry, name):
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                move_file(musicDestination, entry, name)
                logging.info(f"Moved audio file: {name} to {musicDestination}")
                
def checkIfVideo(entry, name):
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(videoDestination, entry, name)
                logging.info(f"Moved video file: {name} to {videoDestination}")
    
def checkIfImage(entry, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(imageDestination, entry, name)
                logging.info(f"Moved image file: {name} to {imageDestination}")
    
def checkIfDocument(entry, name):
        for document_extension in document_extensions:
            if name.endswith(document_extension) or name.endswith(document_extension.upper()):
                move_file(documentDestination, entry, name)
                logging.info(f"Moved document file: {name} to {documentDestination}")
    
def checkIfPDF(entry, name):
        for pdf_extension in pdf_extensions:
            if name.endswith(pdf_extension) or name.endswith(pdf_extension.upper()):
                move_file(PDFDestination, entry, name)
                logging.info(f"Moved PDF file: {name} to {PDFDestination}")
    
def checkIfSpreadsheet(entry, name):
        for spreadsheet_extension in spreadsheet_extensions:
            if name.endswith(spreadsheet_extension) or name.endswith(spreadsheet_extension.upper()):
                move_file(spreadsheetDestination, entry, name)
                logging.info(f"Moved spreadsheet file: {name} to {spreadsheetDestination}")
    
def checkIfMisc(entry, name):
        newExtensionCheck(name)
        for all_extension in all_extensions:
            if (name.endswith(all_extension) or name.endswith(all_extension.upper())) != True :
                move_file(miscellaneousDestination, entry, name)
                logging.info(f"Moved miscellaneious file: {name} to {miscellaneousDestination}")
                continue

def newExtensionCheck(name):
    filename, extension = splitext(name)
    ##for extension in all_extensions:
    if any(extension in all_extension for all_extension in [image_extensions, video_extensions, audio_extensions, document_extensions, pdf_extensions, spreadsheet_extensions]):
        print(f"found Extension {extension}")
    else:
        if extension not in all_extensions:
            all_extensions.append(extension)
    

def main():
    cleanerFunction()
    
if __name__ == "__main__":
    main()