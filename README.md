from tkinter import *
from tkinter import ttk
from rec1 import *


def find_bin(event=None):
    global dict1, top_level, medname_entry
    medname = medname_entry.get().title()


    for i in range(1,21):
        for j in root.children[3].children[0].data[i]:
            if j==medname:
                   disp = Label(top_level, text="It is located in bin num {}".format(i), bg='#BCD2EE',
                      font=('Garamond', 25, 'bold'))
                   disp.place(relx=0.5,rely=0.65,anchor='center')


def locate():
    global medname_entry,top_level
    global image_loc
    big_image_loc = PhotoImage(file="C:\Meghana\SSN\SEM 2\SDP\Pic home.png")
    image_loc = big_image_loc.subsample(20, 20)

    top_level=Toplevel(r)
    top_level.title('Locate Medicine')
    top_level.geometry("1000x600+200+100")
    top_level.configure(bg='#BCD2EE')

    home_button = Button(top_level, text='Home', font=('Garamond', 13, 'bold'),
                         image=image_loc, compound=LEFT, bd=6, command=top_level.destroy,
                         relief='ridge').place(relx=1, x=-120, y=20,width=100, height=50)

    Heading = Label(top_level, text='Locate Medicine', bg='#BCD2EE',
                          font=('Garamond', 50, 'bold', 'underline')).place(relx=0.5,
                                                               y=100,
                                                               anchor='center')


    name =Label(top_level, text='Name: ', bg='#BCD2EE',
                     font=('Garamond', 30,'bold')).place(relx=0.5, x=-120,
                                                        rely= 0.4,
                                                        anchor='center')

    medname_entry = Entry(top_level, font=('Garamond', 20))
    medname_entry.place(relx=0.5,x=120, rely=0.4 ,anchor='center')
    medname_entry.bind('<Return>', find_bin)
    submit_button = Button(top_level, font=('Garamond', 18, 'bold'), text="Submit",
                           relief='ridge', bd=4, command=find_bin)
    submit_button.place(relx=0.5, rely=0.8,anchor='center')



def menu():
  global image
  big_image = PhotoImage(file="C:\Meghana\SSN\SEM 2\SDP\exit pic.png")
  image = big_image.subsample(15, 15)
  Heading = ttk.Label(r, text='MediTrack',
                      font=('Garamond', 60, 'bold')).place(relx=0.5,
                                                           y=70,
                                                           anchor='center')
  SHeading = ttk.Label(r, text='Pharmacy Inventory and Sales Management System',
                       font=('Garamond', 25, 'bold')).place(relx=0.5,
                                                            y=130,
                                                            anchor='center')

  home_button = Button(r, text='  EXIT',
                       font=('Garamond', 15, 'bold'),
                       image=image, compound=LEFT,
                       bd=6, command=r.destroy, bg='white',
                       relief='ridge').place(relx=1,
                                             x=-250,
                                             y=50,
                                             width=200,
                                             height=70)

  button1 = Button(r, text='VIEW SALES',
                   font=('Garamond', 20, 'bold'),
                   bg='#BCD2EE', bd=6,
                   command=r.destroy,
                   relief='ridge').place(relx=0.25,
                                         rely=0.25,
                                         y=130,
                                         width=300,
                                         height=125,
                                         anchor='center')

  button2 = Button(r, text='MANAGE STOCK',
                   font=('Garamond', 20, 'bold'),
                   bg='#BCD2EE', bd=6,
                   command=r.destroy,
                   relief='ridge').place(relx=0.75,
                                         rely=0.25,
                                         y=130,
                                         width=300,
                                         height=125,
                                         anchor='center')

  button3 = Button(r, text='GENERATE INVOICE',
                   font=('Garamond', 20, 'bold'),
                   bg='#BCD2EE', bd=6,
                   command=r.destroy,
                   relief='ridge').place(relx=0.25,
                                         rely=0.75,
                                         width=300,
                                         height=125,
                                         anchor='center')

  button4 = Button(r,
                   text='LOCATE MEDICINE',
                   font=('Garamond', 20, 'bold'),
                   bg='#BCD2EE', bd=6,
                   command=locate,
                   relief='ridge').place(relx=0.75, rely=0.75, width=300,
                                         height=125, anchor='center')

r = Tk()
r.title('Medi Track')
r.geometry('1500x800+0+0')
menu()
r.mainloop()
