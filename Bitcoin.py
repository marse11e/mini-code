import tkinter as tk
from tkinter import ttk
import urllib.request
import json
import time

def get_luno():
	req = urllib.request.urlopen("https://api.mybitx.com/api/1/ticker?pair=XBTMYR")
	x = json.loads(req.read().decode("utf-8"))
	req.close()
	return x

def refresh_price():
	aLable.configure(text="Запрашиваемая цена: RM " + get_luno()["ask"])
	bLable.configure(text="Время: " + 
		str(time.strftime("%Y-%m-%d %H:%M:%S", 
		time.gmtime(get_luno()["timestamp"]/1000 + 28800))))

win = tk.Tk()
win.title("Bitcoin цена из MYR")

aLable = ttk.Label(win, text="Запрашиваемая цена: RM " + get_luno()["ask"])
aLable.grid(column=0, row=0, padx=8, pady=4)

bLable = ttk.Label(text="Время: " + 
		str(time.strftime("%Y-%m-%d %H:%M:%S", 
		time.gmtime(get_luno()["timestamp"]/1000 + 28800))))
bLable.grid(column=0, row=1, padx=8, pady=4)

action = ttk.Button(win, text="Обновить", command=refresh_price)
action.grid(column=0, row=2, padx=8, pady=4)

win.mainloop()