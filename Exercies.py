import tkinter as tk

def show_output():
    number= int(number_input.get())

    if number == 0:
        output_label.configure(text="ใส่มาหาพ่อมึงอ่ะ")
        return
    

    output = " "
    for i in range(1,13):
        output += str(number) + "  x  "  + str(i)
        output += "  =  "  +  str(number * i) + "\n"

    output_label.configure(text=output)


 


window = tk.Tk()
window.title("Hee bo")
window.minsize(width=400, height = 400)


title_label = tk.Label(master = window, text= "สูตรคูณแม่มึงอ่ะ")
title_label.pack(pady =20)

number_input = tk.Entry(master= window, width=15)
number_input.pack()

hee_button = tk.Button(
    master= window,text="กดหาแม่มึงอ่ะ",
    command=show_output, width=10 , height=5
    )
hee_button.pack()

output_label = tk.Label(master=window)
output_label.pack(pady = 30)


window.mainloop()