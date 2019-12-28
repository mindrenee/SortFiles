#!/usr/bin/python

import os
import shutil
import time
import re
from pathlib import Path

audio_regex_list = [".mp3", ".wav", ".m3u"]
text_regex_list = [".txt", ".doc", ".docx", ".odt", ".pdf", ".tex", ".epub", ".PDF"]
image_regex_list = [".gif", ".ico", ".jpg", ".jpeg", ".png", ".svg", ".drawio"]
video_regex_list = [".flv", ".m4v", ".mkv", ".mov", ".mp4"]
internet_regex_list = [".html", ".css"]
compressed_regex_list = [".zip", ".rar", ".tar.gz"]
disc_regex_list = [".iso", ".dmg"]
data_regex_list = [".csv", ".sql", ".json"]
executables_regex_list = [".exe", ".apk", ".jar"]
programming_regex_list = [".sh", ".c", ".java", ".py"]

def main():
    print("Welcome by the folder organizer")
    folder_path = input("What is the folder you want to organize? Enter the path: ")
    response = input("Is " + folder_path + " correct path? ")
    if response == "y" or response == "yes":
        sort_files(folder_path)

def sort_files(folder_path):
    for file in os.listdir(folder_path):
        path = folder_path + "/" + file
        if Path(path).is_file():
            move_file(folder_path, path)
        elif Path(path).is_dir():
            print("Dir: " + file)

def move_file(folder_path, file):
    basefile = os.path.basename(file)
    folder_path = folder_path + "/"
    rename_file = basefile.replace(" ", "_")
    rename_file2 = rename_file.replace("'","")
    if rename_file2 != basefile:
        os.rename(folder_path + basefile, folder_path + rename_file2)
    filename, file_extension = os.path.splitext(file)
    if re.match('(?:% s)' % '|'.join(audio_regex_list), file_extension):
        new_folder = Path(folder_path + "Music/" + rename_file2)
        if not os.path.exists(folder_path + "Music"):
            os.makedirs(folder_path + "Music")
        shutil.move(folder_path + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(text_regex_list), file_extension):
        new_folder = Path(folder_path + "Text/" + rename_file2)
        if not os.path.exists(folder_path + "Text"):
            os.makedirs(folder_path + "Text")
        shutil.move(folder_path + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(image_regex_list), file_extension):
        new_folder = Path(folder_path + "Images/" + rename_file2)
        if not os.path.exists(folder_path + "Images"):
            os.makedirs(folder_path + "Images")
        shutil.move(folder_path + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(video_regex_list), file_extension):
        new_folder = Path(folder_path + "Video/" + rename_file2)
        if not os.path.exists(folder_path + "Video"):
            os.makedirs(folder_path + "Video")
        shutil.move(folder_path + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(internet_regex_list), file_extension):
        new_folder = Path(folder_path + "Other/Internet/" + rename_file2)
        if not os.path.exists(folder_path + "Other/Internet/"):
            os.makedirs(folder_path + "Other/Internet")
        shutil.move(folder_path + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(compressed_regex_list), file_extension):
        new_folder = Path(folder_path + "Other/Compressed/" + rename_file2)
        if not os.path.exists(folder_path + "Other/Compressed/"):
            os.makedirs(folder_path + "Other/Compressed")
        shutil.move(folder_path + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(disc_regex_list), file_extension):
        new_folder = Path(folder_path + "Other/Disc/" + rename_file2)
        if not os.path.exists(folder_path + "Other/Disc/"):
            os.makedirs(folder_path + "Other/Disc")
        shutil.move(folder_path + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(data_regex_list), file_extension):
        new_folder = Path(folder_path + "Other/Data/" + rename_file2)
        if not os.path.exists(folder_path + "Other/Data/"):
            os.makedirs(folder_path + "Other/Data")
        shutil.move(folder_path + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(executables_regex_list), file_extension):
        new_folder = Path(folder_path + "Other/Executables/" + rename_file2)
        if not os.path.exists(folder_path + "Other/Executables/"):
            os.makedirs(folder_path + "Other/Executables")
        shutil.move(folder_path + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(programming_regex_list), file_extension):
        new_folder = Path(folder_path + "Other/Programming/" + rename_file2)
        if not os.path.exists(folder_path + "Other/Programming/"):
            os.makedirs(folder_path + "Other/Programming")
        shutil.move(folder_path + rename_file2, new_folder)
    else:
        print("File: " + file)
        print("File not regonized")

main()
