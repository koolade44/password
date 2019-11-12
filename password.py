import tkinter as tk
master = tk.Tk()


def check_pword():
    x = str('%s' % e1.get())
    y = str('hello')
    if x == y:
        print('correct')
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
