import tkinter as tk

app = tk.Tk()
app.title('App')

lb = tk.Label(app, text='You are so beautiful!', width = 20, height = 10, fg = 'red')
lb.pack()

bt = tk.Button(text = 'Exit', width = 10, bg = 'pink')
bt.pack()

tk.mainloop()


