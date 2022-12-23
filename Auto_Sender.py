import pyautogui as auto
import tkinter as tk
import time 


def Start():
	time.sleep(5)
	for x in range(int(e2.get())):
		time.sleep(int(e3.get()))
		auto.write(e.get())
		auto.press("enter")

root = tk.Tk()
root.config(background="#07273d")
root.geometry("570x350")

title = tk.Label(foreground="white",text="Auto Sender", font = ("Roboto", 35), background="#07273d")
blank = tk.Label(foreground="white",text="", background="#07273d")
blank2 = tk.Label(foreground="white",text="", background="#07273d")
message = tk.Label(foreground="white",text="Write The Message Below", font = ("Roboto", 20), background="#07273d")
message2 = tk.Label(foreground="white",text="How many times would you like to repeat", font = ("Roboto", 20), background="#07273d")
message3 = tk.Label(foreground="white",text="Time between messages", font = ("Roboto", 20), background="#07273d")
e = tk.Entry()
e2 = tk.Entry()
e3 = tk.Entry()
b = tk.Button(text="Start", command=Start)


title.pack()
blank.pack()
blank2.pack()
message.pack()
e.pack()
message2.pack()
e2.pack()
message3.pack()
e3.pack()
b.pack()

root.mainloop()
