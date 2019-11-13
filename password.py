import tkinter as tk
import pyperclip as pyp
master = tk.Tk()


print('please input the password, then close the tk window, the link will automaticly be copied')
def check_pword():
    x = str('%s' % e1.get())
    y = str('KA446mp')
    if x == y:
        pyp.copy('http://www.mediafire.com/folder/fqzhn6o4nsqzz/Maps')
        print('Link Copied!')
    else:
        print('incorrect')


tk.Label(master, text='Password:').grid(row=0)

e1 = tk.Entry(master)
e1.grid(row=0, column=1)

tk.Button(master,
          text='Submit',
          command=check_pword).grid(row=1,
                                    column=0,
                                    stick=tk.W,
                                    pady=4)
tk.mainloop()

