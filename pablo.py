import tkinter as tk

def repeat_text(text, label):

    text = text.get("1.0", tk.END)
    label.config(text=text)


main = tk.Tk()
main.geometry('400x500')
main.title('')
main.config(bg='grey')

tk.Label(main, text='аываывавы', bg='grey', font=('Roboto', 25,'bold', 'italic'), pady=30).pack()
tk.Label(main, text='бубубубубу', bg='grey', font=('Roboto', 25,'bold')).pack()

text = tk.Text(main, width=40, height=2)
text.pack()

frame = tk.Frame(main, bg='grey', pady=10).pack()

label = tk.Label(main, bg='grey')
label.pack()

btn = tk.Button(main, text='нажми',
                command=lambda: repeat_text(text, label))
btn.pack()



main.mainloop()