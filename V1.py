import tkinter as tk

def menu():
    global image
    Frame1=tk.Frame(r, width=1919, height=5, bg='black', bd=5).place(x=0, y=45)
    frame1=tk.Frame(r, width=1919, height=45, bg='#580070', bd=5).place(x=0, y=0)
    Frame2=tk.Frame(r, width=5, height=1079, bg='black', bd=5).place(x=290, y=50)
    frame2=tk.Frame(r, width=290, height=1039, bg='#580070', bd=5).place(x=0, y=50)
    image=tk.PhotoImage(file="C:\Meghana\SSN\SEM 2\SDP\Pic home.png")
    #resized=image.resize()
    home_button=tk.Button(frame2, text='Home', font= ('Garamond',15,'bold'), image= image, compound=tk.LEFT, 
                        bg='#BCD2EE', bd = 6, command = r.destroy, relief = 'ridge').place(x=20, y=700, width =250, height=70)
    button1 = tk.Button(frame2, text='VIEW SALES',font = ('Garamond',15,'bold'),
                        bg='#BCD2EE', bd = 6, command = r.destroy, relief = 'ridge').place(x=20,y=80, width =250, height=70)
    button2 = tk.Button(frame2, text='TRACK STOCK',font = ('Garamond',15,'bold'),
                        bg='#BCD2EE', bd = 6, relief = 'ridge').place(x=20, y= 170, width =250, height=70)
    button3 = tk.Button(r, text='GENERATE INVOICE',font = ('Garamond',15,'bold'),
                        bg='#BCD2EE', bd = 6, relief = 'ridge').place(x=20, y= 260, width =250, height=70)
    button4 = tk.Button(r, text='LOCATE MEDICINE',font = ('Garamond',15,'bold'),
                        bg='#BCD2EE', bd = 6, relief = 'ridge').place(x=20, y= 350, width =250, height=70)


r = tk.Tk()
r.title('Medi Track')
r.geometry('1920x1080')
r.configure(bg = '#9B7EDE')
menu()
r.mainloop()
