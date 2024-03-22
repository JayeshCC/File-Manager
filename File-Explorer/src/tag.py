from tkinter import messagebox
from ttkbootstrap.dialogs.dialogs import Messagebox
import os
import json
import datetime

from main import refresh,selectedItem,file_path

def tag_popup(tag_type):
    global items
    global tag_files
    
    if items.focus() != "":
        try:
            selected = os.getcwd() + "\\" + selectedItem
            found=False
            for file in tag_files:
                if file['file_name'] == selected:
                    found = True
            if not found:
                new_item = {}
                new_item['file_name'] = selected
                new_item['tag_date'] = datetime.datetime.now().strftime(date_format)
                new_item['tag_type'] = tag_type
                tag_files.append(new_item)
                update_tag()
                refresh([])
        except:
            pass
    else:
        messagebox.show_info(
            message="There is no selected file or directory.", title="Info"
        )

def untag_popup():
    global items
    if items.focus() != "":
        try:
            selected = os.getcwd() + "\\" + selectedItem
            found=False
            for file in tag_files:
                if file['file_name'] == selected:
                    found = True
                    founditem = file
            if found:
                tag_files.remove(founditem)
                update_tag()
                refresh([])
        except:
            pass
    else:
        Messagebox.show_info(
            message="There is no selected file or directory.", title="Info"
        )

def update_tag():
    with open(file_path + "../res/tag_files.json", 'w') as outfile:
        # Writing to file
        data={}
        data['items']  = tag_files
        json.dump(data, outfile)
        
def read_tag():
    global tag_files
    if not os.path.isdir(file_path + "../res"):
        os.mkdir(file_path + "../res") 
    if not os.path.isfile(file_path + "../res/tag_files.json"):
        with open(file_path + "../res/tag_files.json", 'w') as outfile:
            # Writing to file
            data={}
            data['items']  = []
            json.dump(data, outfile)
    
    with open(file_path + "../res/tag_files.json", 'r') as open_file:
     # Reading from json file
        data  = json.load(open_file)
        tag_files = data['items']
