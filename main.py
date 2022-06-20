from tkinter.ttk import Combobox
from tkinter import filedialog as fd
from tkinter import *
import os
import vlc

# ==================================================================RootWindow


root = Toplevel()
root.title('H-MusicPlayer')
root.geometry('400x250')
root.resizable(width=False, height=False)


# ==================================================================Variabels


global song_dict, media_list, Player
play_list= []
song_dict = {}
Player = vlc.MediaListPlayer()
media_list = vlc.Instance().media_list_new()


# ==================================================================Frame


btn_frame = LabelFrame(root, width=100, bg='#173f5f')
btn_frame.pack(side=LEFT, fill=Y)

Speed_JumpStep_labelframe = LabelFrame(btn_frame, width=100, bg='#808080', borderwidth=0 )
Speed_JumpStep_labelframe.grid(row=4, column=0, rowspan=2, columnspan=2, ipady=5 , pady= 5)

Listbox_frame = LabelFrame(root, bg='#404040')
Listbox_frame.pack(fill=BOTH)

Information_labelframe = LabelFrame(root, text='A Message From Creator',fg='White', bg='#333333', height=100, borderwidth=10 )
Information_labelframe.pack(side=BOTTOM, fill= BOTH)


# ===================================================================Function


def AddSong():
    songs_path = fd.askopenfilenames(title="Choose your song")
    for i in songs_path:
        media_list.add_media(i)
        play_list.append(i)
    for count,song in enumerate(songs_path):
        song_name = os.path.basename(song)
        song_dict[count] = [song_name,song] 
        song_listbox.insert(END, song_name) 
    Player.set_media_list(media_list)



def RemoveSong():
    global play_list
    idx = song_listbox.curselection()[0]
    song_dict.pop(idx)
    song_listbox.delete(0, END)
    for i in song_dict:
        song_listbox.insert(END, (song_dict[i][0]))
    dict_pathValues = list(song_dict.values())
    play_list = []
    for i in dict_pathValues:
        play_list.append(i[1])    
   


def PlaySelected_f(s):
    if s.widget.curselection():
        Player.play_item_at_index(
           play_list.index(play_list[s.widget.curselection()[0]]))
        
        

def Play_f():
    if Player.is_playing() == 0:
        Player.play()
    else:
        pass    
    


def Pause_f():
    if Player.is_playing() == 1:
        Player.pause()
    else:
        pass    


def FastForward_f():
    if Player.is_playing() == 1:
        Songcurrenttime = Player.get_media_player().get_position()
        Song_length = Player.get_media_player().get_length()//1000
        Frwdingtime = int(JumpStep_combobox.get())  / Song_length
        New_time = Songcurrenttime + Frwdingtime
        Player.get_media_player().set_position(New_time)
    else:
        pass


def FastBackward_f():
    if Player.is_playing() == 1:
        Songcurrenttime = Player.get_media_player().get_position()
        Song_length = Player.get_media_player().get_length()//1000
        Frwdingtime = int(JumpStep_combobox.get())  / Song_length
        New_time = Songcurrenttime - Frwdingtime
        Player.get_media_player().set_position(New_time)
    else:
        pass


def Next_f():
    if Player.is_playing() == 1:
        Player.next()
    else:
        pass


def Previous_f():
    if Player.is_playing() == 1:
        Player.previous()
    else:
        pass

def Repeat_f():
    #double click on white part of listbox does same thing
    Player.get_media_player().set_position(0)
    if Player.is_playing() == 0:
        Player.get_media_player().set_position(0)
        Player.play()
 


def PlaySpeed_f(Spd):
    Player.get_media_player().set_rate(float(Spd.widget.get()))


# ==================================================================Widgets


play_image = PhotoImage(file=os.path.join('Image', 'play.png'))
play_image = play_image.subsample(2,2)
play_btn = Button(btn_frame,image=play_image, width=40 , height= 25, borderwidth=0, command=Play_f)
play_btn.grid(row=1, column=0, padx=10, pady=8)


pause_image = PhotoImage(file=os.path.join('Image', 'pause.png'))
pause_image = pause_image.subsample(3,3)
Pause_btn = Button(btn_frame, image=pause_image, width=40, height=25, borderwidth=0, command=Pause_f)
Pause_btn.grid(row=1, column=1, padx=10, pady=8)


forward_image = PhotoImage(file=os.path.join('Image', 'forward.png'))
forward_image = forward_image.subsample(2,2)
Forward_btn = Button(btn_frame, image=forward_image, width=40, height=25, borderwidth=0, command=FastForward_f)
Forward_btn.grid(row=0, column=1, padx=10 )


backward_image = PhotoImage(file=os.path.join('Image', 'backward.png'))
backward_image = backward_image.subsample(2,2)
Backward_btn = Button(btn_frame, image=backward_image, width=40, height=25, borderwidth=0, command=FastBackward_f)
Backward_btn.grid(row=0, column=0, padx=10, pady=8)


next_image = PhotoImage(file=os.path.join('Image', 'next.png'))
next_image = next_image.subsample(2,2)
Next_btn = Button(btn_frame, image=next_image, width=40, height=25, borderwidth=0, command=Next_f)
Next_btn.grid(row=2, column=1, padx=2, pady=8)


pervious_image = PhotoImage(file=os.path.join('Image', 'previous.png'))
previous_image = pervious_image.subsample(2,2)
Previous_btn = Button(btn_frame, image=previous_image, width=40, height=25, borderwidth=0, command=Previous_f)
Previous_btn.grid(row=2, column=0, padx=2, pady=8)


repeat_image = PhotoImage(file=os.path.join('Image', 'rep.png'))
repeat_image = repeat_image.subsample(2,2)
Repeat_btn = Button(btn_frame, text='Repeat   ', image=repeat_image, compound=RIGHT, width=120 , height=20, borderwidth=0, command=Repeat_f)
Repeat_btn.grid(row=3, column=0, columnspan=2, padx=20, pady=8)


speed_label = Label(Speed_JumpStep_labelframe, text='Speed', bg='#808080')
speed_label.grid(row=0, column=0, sticky=W)


JumpStep_label = Label(Speed_JumpStep_labelframe, text='JumpStep', bg='#808080')
JumpStep_label.grid(row=1, column=0, sticky=W)


Speed_combobox = Combobox(Speed_JumpStep_labelframe, state='readonly', width=6, values=['0.5', '0.75', '1.0', '1.25', '1.5','1.75', '2.0'])
Speed_combobox.bind("<<ComboboxSelected>>", PlaySpeed_f)
Speed_combobox.current(2)
Speed_combobox.grid(row=0, column=1, padx=5, pady=5, ipady=2)


JumpStep_combobox = Combobox(Speed_JumpStep_labelframe, state='readonly', width=6, values=['5', '10', '15', '20', '30'])
JumpStep_combobox.current(1)
JumpStep_combobox.grid(row=1, column=1, padx=0, pady=5, ipady=2)


song_listbox = Listbox(Listbox_frame, width=35, bg='#ffffff', border=0, selectbackground='#8c8c8c',selectforeground='Black')
song_listbox.bind("<<ListboxSelect>>", PlaySelected_f)
song_listbox.pack(side=TOP, fill=Y)


Message_label = Label(Information_labelframe, text='Close your eyes & Enjoy your lovely Songs\n\n Created By Hamed With <3',bg='#333333',
 fg='#ff751a', height=100, font=('',8 ))
Message_label.pack(fill=BOTH)


# ==================================================================Menu


menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label='Add Song', command=AddSong)
file_menu.add_command(label='Remove Song', command=RemoveSong)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)


root.mainloop()
