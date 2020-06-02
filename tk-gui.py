import tkinter as tk

app = tk.Tk()
app.title('App')

lb = tk.Label(app, text='You are so beautiful!', width=20, height=10, fg='red')
lb.pack(side = tk.LEFT, padx = 5)


def change_label():
    lb.config(text='Thank you', fg='black')


text = tk.Entry(app, width=10)
text.pack()

txt = tk.Text()
txt.pack()

bt = tk.Button(text='Exit', width=10, bg='pink', command=change_label)
bt.pack()

tk.mainloop()
