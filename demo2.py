import requests
import json
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import musicplayer_support

#mykeys = ['active','confirmed','recovered']
#mydict= {}
#data = requests.get('https://api.covid19india.org/state_district_wise.json')
#text_data = data.text
#parse_data = json.loads(text_data)
# print(parse_data)

# for getting all states name.
# print(parse_data.keys())

# print(parse_data['Andaman and Nicobar Islands'])

# print(len(parse_data.keys()))

# for printing the states names.
# for i in parse_data.keys():
#         print(i)

# for getting district data.
#obj = parse_data['Andaman and Nicobar Islands']['districtData'].keys()
#print(obj)


# for getting district data details.
#obj = parse_data['Andaman and Nicobar Islands']['districtData']
#my_list = []
#for i,j in obj.items():
#    my_list.append(i)
#    for k in mykeys:
#            my_list.append({k:j[k]})
#    print()

#print(my_list)


#obj = parse_data['Andaman and Nicobar Islands']['districtData']
#my_list = []
#for i,j in obj.items():
#    my_list.append(i)

#print(my_list)
root = tk.Tk()
top = View(root)
playList = ScrolledListBox(top)
playList.place(relx=0.0, rely=0.38, relheight=0.532, relwidth=0.999)
playList.configure(background="white")
playList.configure(disabledforeground="#a3a3a3")
playList.configure(font="TkFixedFont")
playList.configure(foreground="black")
playList.configure(highlightbackground="#d9d9d9")
playList.configure(highlightcolor="#d9d9d9")
playList.configure(selectbackground="#c4c4c4")
playList.configure(selectforeground="black")
playList.configure(width=10)
for song_name in range(10):
            self.playList.insert(tk.END, song_name)
