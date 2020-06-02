import tkinter as tk

app = tk.Tk()
app.title('App')

lb = tk.Label(app, text='You are so beautiful!', width=20, height=10, fg='red')
lb.pack()


def change_label():
    lb.config(text='Thank you', fg='black')


bt = tk.Button(text='Exit', width=10, bg='pink', command=change_label)
bt.pack()

tk.mainloop()
