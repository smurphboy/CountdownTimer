from playsound import playsound
import tkinter as tk


counter = (15*60)
def counter_label (label):
    counter = 15*60
    def count():
        global counter
        if counter == (15*60):
            playsound("9-5 opener.mp3", block=False)
            print("play")
        if counter == (5*60):
            playsound("9 to 5 sting.mp3", block=False)
        if counter == (0):
            playsound("work alarm.mp3", block=False)
        counter -= 1
        mins,secs = divmod(counter,60)
        if secs < 10:
            seczero = "0"
        else:
            seczero = ""
        label.config(text=str(mins)+":"+ seczero + str(secs), justify="center")
        label.after(1000,count)
    count()

root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("counter")
root.configure(background="deeppink3")
label = tk.Label(root, fg = "white", background="deeppink3", font=("Hammersmith One", 650))
label.pack()
counter_label(label)
button = tk.Button(root, text="stop", width=40, command= root.destroy)
button.pack()
root.mainloop()
