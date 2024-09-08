from os import scandir, rename
from os.path import exists, join, splitext
from shutil import move
import logging


source_dir = "C:\Users\dgsy2\Downloads"
musicDestination = "C:\Users\dgsy2\Music"
videoDestination = "C:\Users\dgsy2\Videos"
documentDestination = "C:\Users\dgsy2\Documents\WordDocuments"
PDFDestination = "C:\Users\dgsy2\Documents\PDF"
spreadsheetDestination = "C:\Users\dgsy2\Documents\Spreadsheet"
imageDestination = "C:\Users\dgsy2\Pictures"
miscellaneousDestination = "C:\Users\dgsy2\Documents\Misc"

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
        name = f"{filename}{str(counter)}{extension}"
        counter += 1
    return name

def move_file(location, entry, name):
    if exists(f"{location}/{name}"):
        uniqueName = create_unique_file(location, name)
        oldName = join(location,name)
        newName = join(location, uniqueName)
        rename(oldName, newName)
    move(entry, location)
    
def cleanerFunction():
    with scandir(source_dir) as entries:
        for entry in entries:
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
        newExtensionCheck(entry)
        for all_extension in all_extensions:
            if (name.endswith(all_extension) or name.endswith(all_extension.upper())) != True :
                move_file(miscellaneousDestination, entry, name)
                logging.info(f"Moved miscellaneious file: {name} to {miscellaneousDestination}")

def newExtensionCheck(extension):
    for extension in all_extensions:
        if all(extension in all_extension for all_extension in [image_extensions, video_extensions, audio_extensions, document_extensions, pdf_extensions, spreadsheet_extensions]):
            break
        else:
            all_extensions.extend(extension)
    

        


        

def main():
    newExtensionCheck()
    cleanerFunction()
    
if __name__ == "__main__":
    main()