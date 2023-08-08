#!/usr/bin/python3
import customtkinter as ctk
import tkinter as tk
import os
from PIL import Image
import sys




class Left:
        def get_repertory(self):
            self.k=os.listdir(f"{dir}")
            for i in self.k:
                if os.listdir(f"{dir}\{i}")==[]:
                    os.system(f"rmdir {dir}\{i}")
            self.k=os.listdir(f"{dir}")
            return self.k
        def get_chap_inorder(self, liste):
            self._liste=[]
            for k in liste:
                self._liste.append(int(k.replace("chapitre", '')))
            self._liste.sort()
            for m in range(len(self._liste)):
                self._liste[m]='chapitre'+str(self._liste[m])
            return self._liste
        def __init__(self):
            global all_chap_buttons
            global frame
            frame=ctk.CTkFrame(root1, width=200, height=800)
            frame.pack(side='left', anchor='nw', fill=tk.Y, pady=40, padx=40)
            self.tabview = ctk.CTkTabview(master=frame, command=lambda:mangavar.set(self.tabview.get()))
            self.tabview.pack(padx=20, pady=20, expand=tk.YES, fill=tk.Y, side=tk.BOTTOM)
            all_chap_buttons=[]
            self.repertory=self.get_repertory()
            if self.repertory==[]:
                self.norepositorylabel=ctk.CTkLabel(frame, text='no chapter installed', font=('', 30))
                self.norepositorylabel.pack(side=tk.TOP, pady=10)
            else:
                self.liblabel=ctk.CTkLabel(frame, text='Directory', font=('', 30))
                self.liblabel.pack(side=tk.TOP, pady=10)
                mangavar.set(self.repertory[0])
                for i in self.repertory:
                    _tab=self.tabview.add(f"{i}")
                    self.tab=ctk.CTkScrollableFrame(_tab, fg_color='transparent')#, fg_color='transparent')
                    self.tab.pack(expand=tk.YES, fill=tk.BOTH)
                    for i2 in self.get_chap_inorder(os.listdir(f"{dir}\{i}")):
                        self.button=ctk.CTkButton(self.tab, text=i2, command=lambda j=i2:Rdw.addnew(j))
                        self.button.pack(fill=tk.X)
                        all_chap_buttons.append([i2, self.button, 'normal'])
        def get_all_chap_buttons():
            return all_chap_buttons
        def get_frame():
            return frame
        


class Rdw:
    def __init__(self):
        global frame2
        global label
        frame2=ctk.CTkFrame(root1, height=800)
        frame2.pack(anchor='ne', fill=tk.BOTH, pady=40, padx=40, expand=tk.YES)
        label=ctk.CTkLabel(frame2 ,textvariable=chapvar, font=('', 30))
        label.pack(expand=1)
    def get_frame():
        return frame2
    def get_label():
        return label
    class addnew:
        def __init__(self, name):
            name=name
            rdwindow=Rdw.get_frame()
            for e in rdwindow.winfo_children():
                if ".!ctkbutton" in str(e):
                    e.destroy()
            #but.pack_forget()
            for i in Left.get_all_chap_buttons():
                if i[2]=='disabled':
                    if i[0]!=name:
                        i[1].configure(state=tk.NORMAL)
                        i[2]='normal'
                elif i[0]==name:
                    i[1].configure(state=tk.DISABLED)
                    i[2]='disabled'
            but=ctk.CTkButton(rdwindow, text="READ", command=Rd)#, command=Reader.createrdingwindow)
            but.pack(expand=tk.YES)
            chapvar.set(name)
            Rdw.get_label().configure(textvariable=chapvar)



"""class Reader:
    def createrdingwindow():
        global rdingwindow
        global chapframe
        global next
        global precedent
        pagevar.set(1)
        maxpagevar.set(len(os.listdir(f"{dir}\{mangavar.get()}\{chapvar.get()}")))
        chapvar.set("")
        label.configure(textvariable=chapvar)
        Rdw.get_frame().destroy()
        Left.get_frame().destroy()
        rdingwindow = ctk.CTkFrame(root1)
        rdingwindow.pack(fill=tk.BOTH, expand=1)
        home=ctk.CTkButton(rdingwindow, text='⮌', width=10, command=Reader.Back)
        home.pack(anchor="nw")
        precedent=ctk.CTkButton(rdingwindow, text='<<', width=30, height=60, command=Reader.Read_back)
        precedent.pack(side=tk.LEFT)
        precedent.configure(state=tk.DISABLED)
        next=ctk.CTkButton(rdingwindow, text='>>', width=30, height=60, command=Reader.Read_next)
        next.pack(side=tk.RIGHT)
        chapframe=ctk.CTkFrame(rdingwindow)
        chapframe.pack()
        Reader.Read(f"{dir}\{mangavar.get()}\{chapvar.get()}\page{pagevar.get()}.jpg", chapframe)
        root1.attributes("-fullscreen", "True")
        
    def Read(path_to_img, surface):
        path=path_to_img
        my_image = ctk.CTkImage(light_image=Image.open(path),
                                  dark_image=Image.open(path), 
                                  size=Reader.resize(path, 1100, 1000))
        image_label=ctk.CTkLabel(surface, image=my_image)
        image_label.pack()
    def Read_next():
        pagevar.set(pagevar.get()+1)
        for e in chapframe.winfo_children():
            e.destroy()
        Reader.Read(f"{dir}\{mangavar.get()}\{chapvar.get()}\page{pagevar.get()}.jpg", chapframe)
        if pagevar.get()==maxpagevar.get():
            next.configure(state=tk.DISABLED)
        if precedent.cget('state')=='disabled':
            precedent.configure(state=tk.NORMAL)
    def Read_back():
        pagevar.set(pagevar.get()-1)
        for e in chapframe.winfo_children():
            e.destroy()
        Reader.Read(f"{dir}\{mangavar.get()}\{chapvar.get()}\page{pagevar.get()}.jpg", chapframe)
        if pagevar.get()==1:
            precedent.configure(state=tk.DISABLED)
        if next.cget('state')=='disabled':
            next.configure(state=tk.NORMAL)
    def resize(image_from_local_disk, maxx, maxy):
        im=Image.open(image_from_local_disk)
        x, y=im.size
        if x>y:
            if x> maxx:
                kx=x-(x-maxx)
                factorx=kx/x
                x_resize=int(x*factorx)
                y_resize=int(y*factorx)
            else:
                x_resize=x
                y_resize=y
        elif y>=x:
            if y>maxy:
                ky=y-(y-maxy)
                factory=ky/y
                y_resize=int(y*factory)
                x_resize=int(x*factory)
            else:
                y_resize=y
                x_resize=x
        return (x_resize, y_resize)

    def Back():
        chapvar.set('')
        rdingwindow.destroy()
        Left()
        Rdw()
        root1.attributes("-fullscreen", "False")"""

class Rd:
    def __init__(self):
        global rdingwindow
        global next
        global precedent
        pagevar.set(1)
        maxpagevar.set(len(os.listdir(f"{dir}\{mangavar.get()}\{chapvar.get()}")))
        tk.Grid.rowconfigure(root1, (0,1), weight=1)
        tk.Grid.columnconfigure(root1,(0, 1, 2), weight=1)
        #======CLEANING WINDOW======
        Rdw.get_frame().destroy()
        Left.get_frame().destroy()
        #======DISPLAYING======
        precedent=ctk.CTkButton(root1, text='<<', width=30, height=60, command=Rd.Read_back)
        precedent.grid(row=1, column=0, sticky="w")
        precedent.configure(state=tk.DISABLED)
        next=ctk.CTkButton(root1, text='>>', width=30, height=60, command=Rd.Read_next)
        next.grid(row=1, column=2, sticky="e")
        rdingwindow=ctk.CTkFrame(root1)
        rdingwindow.grid(row=1, column=1)
        self.home=ctk.CTkButton(rdingwindow, text='×', width=10, command=Rd.Back)
        self.home.grid(row=0, column=0, sticky="nw")
        Rd.Read(f"{dir}\{mangavar.get()}\{chapvar.get()}\page{pagevar.get()}.jpg", rdingwindow)
    def get_rdingwindow():
        return rdingwindow
    def get_back_button():
        return precedent
    def get_next_button():
        return next

    def Read(path_to_img, surface):
        path=path_to_img
        my_image = ctk.CTkImage(light_image=Image.open(path),
                                  dark_image=Image.open(path), 
                                  size=Rd.resize(path, 1100, 1000))
        image_label=ctk.CTkLabel(surface, image=my_image)
        image_label.grid(row=0, column=1, sticky='nesw')

    def Read_back():
        pagevar.set(pagevar.get()-1)
        for e in Rd.get_rdingwindow().winfo_children():
            if str(e) == ".!ctkframe3.!ctkbutton":
                pass
            else:
                e.destroy()
        Rd.Read(f"{dir}\{mangavar.get()}\{chapvar.get()}\page{pagevar.get()}.jpg", Rd.get_rdingwindow())
        if pagevar.get()==1:
            Rd.get_back_button().configure(state=tk.DISABLED)
        if Rd.get_next_button().cget('state')=='disabled':
            Rd.get_next_button().configure(state=tk.NORMAL)

    def Read_next():
        pagevar.set(pagevar.get()+1)
        for e in Rd.get_rdingwindow().winfo_children():
            if str(e) == ".!ctkframe3.!ctkbutton":
                pass
            else:
                e.destroy()
        Rd.Read(f"{dir}\{mangavar.get()}\{chapvar.get()}\page{pagevar.get()}.jpg", Rd.get_rdingwindow())
        if pagevar.get()==maxpagevar.get():
            Rd.get_next_button().configure(state=tk.DISABLED)
        if Rd.get_back_button().cget('state')=='disabled':
            Rd.get_back_button().configure(state=tk.NORMAL)

    def Back():
        chapvar.set('')
        for e in root1.winfo_children():
            e.destroy()
        Left()
        Rdw()
        root1.attributes("-fullscreen", "False")



    def resize(image_from_local_disk, maxx, maxy):
        im=Image.open(image_from_local_disk)
        x, y=im.size
        if x>y:
            if x> maxx:
                kx=x-(x-maxx)
                factorx=kx/x
                x_resize=int(x*factorx)
                y_resize=int(y*factorx)
            else:
                x_resize=x
                y_resize=y
        elif y>=x:
            if y>maxy:
                ky=y-(y-maxy)
                factory=ky/y
                y_resize=int(y*factory)
                x_resize=int(x*factory)
            else:
                y_resize=y
                x_resize=x
        return (x_resize, y_resize)








class main:
    def __init__(self):
        global root1
        global mangavar
        global chapvar
        global pagevar
        global maxpagevar
        global dir
        root1=ctk.CTk()
        root1.geometry('1400x800')
        mangavar=tk.StringVar()
        chapvar=tk.StringVar()
        pagevar=tk.IntVar()
        maxpagevar=tk.IntVar()
        dir='C:\ScansManga'
        ctk.set_appearance_mode("light")
        root1.title('GUI')
        Left()
        Rdw()
        root1.mainloop()


if __name__=='__main__':
    main()
