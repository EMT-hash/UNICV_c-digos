import customtkinter as ctk
janela = ctk.CTk()
janela.geometry('450x500')
janela.minsize(450,500)
janela.maxsize(450,500)
janela.title('Calculadora')







fim = False


num = ctk.CTkTextbox(janela,font=('arial',50),border_color='#4C2B6E',border_width=5,height=100,width=390,)
num.place(x=25,y=50)
num.configure(state='disable')

row = 1
column = 1
janela.grid_rowconfigure(0, minsize=220)

    


for i in range(1, 10):
    def numero(b = i):
        global fim        
        num.configure(state='normal')
        num.insert(ctk.END,b)
        num.configure(state='disabled')

        if fim == True:
            num.configure(state='normal')
            num.delete('1.0',ctk.END)
            num.insert(ctk.END,b)
            fim = False
            num.configure(state='disabled') 

    botao = ctk.CTkButton(janela,text=i,
font=('arial',25),
fg_color='#4C2B6E',
border_color="#121114",
border_width=2,
corner_radius=15,
command=numero,
hover_color="#2A913B",
height=50,width=90).grid(row=row, column=column,pady=5,padx=5)     

               
    column += 1
    if column > 3:
        column = 1
        row += 1

zero = ctk.CTkButton(janela,text=0,
font=('arial',25),
fg_color='#4C2B6E',
border_color="#121114",
border_width=2,
corner_radius=15,
command= lambda i=0:(num.configure(state='normal'),num.insert(ctk.END,i),num.configure(state='normal')),
hover_color="#2A913B",
height=50,width=90).grid(row=4, column=2,pady=10,padx=10)


adicao = ctk.CTkButton(janela,text='+',
font=('arial',25),
fg_color="#1C0963",
border_color="#121114",
border_width=2,
corner_radius=15,
command=lambda i='+': (num.configure(state='normal'), num.insert(ctk.END,i), num.configure(state='disabled')),
hover_color="#2A913B",
height=50,width=90).grid(row=1, column=4,pady=10,padx=10)

subt = ctk.CTkButton(janela,text='-',
font=('arial',25),
fg_color="#1C0963",
border_color="#121114",
border_width=2,
corner_radius=15,
command=lambda i='-':(num.configure(state='normal'), num.insert(ctk.END,i),num.configure(state='disabled')),
hover_color="#2A913B",
height=50,width=90).grid(row=2, column=4,pady=10,padx=10) 

mult = ctk.CTkButton(janela,text='x',
font=('arial',25),
fg_color="#1C0963",
border_color="#121114",
border_width=2,
corner_radius=15,
command=lambda i='*': (num.configure(state='normal'), num.insert(ctk.END,i),num.configure(state='disabled')),
hover_color="#2A913B",
height=50,width=90).grid(row=3, column=4,pady=10,padx=10) 

div = ctk.CTkButton(janela,text='÷',
font=('arial',25),
fg_color="#1C0963",
border_color="#121114",
border_width=2,
corner_radius=15,
command=lambda i='/': (num.configure(state='normal'), num.insert(ctk.END,i),num.configure(state='disabled')),
hover_color="#2A913B",
height=50,width=90).grid(row=4, column=4,pady=10,padx=10)

virg = ctk.CTkButton(janela,text=',',
font=('arial',30),
fg_color="#1C0963",
border_color="#121114",
border_width=2,
corner_radius=15,
command=lambda i='.': (num.configure(state='normal'), num.insert(ctk.END,i),num.configure(state='disabled')),
hover_color="#2A913B",
height=50,width=90).grid(row=4, column=1,pady=10,padx=10) 

apagar = ctk.CTkButton(janela,text='←',
font=('arial',25),
fg_color="#A63624",
border_color="#121114",
border_width=2,
corner_radius=15,
command=lambda: (num.configure(state='normal'), num.delete("end-2c", "end-1c"),num.configure(state='disabled')),
hover_color="#2A913B",
height=40,width=90).place(x=10,y=170)


def calcular():
    global fim
    try:
        num.configure(state='normal')
        conta = num.get('1.0',ctk.END)
        resultado = eval(conta)
        num.delete('1.0',ctk.END)
        num.insert('1.0',resultado)
        fim = True
        num.configure(state='disabled')        



    except:
        num.configure(state='normal')
        num.delete('1.0',ctk.END)  
        num.configure(state='disabled')
  

igual = ctk.CTkButton(janela,text='=',
font=('arial',25),
fg_color="#1C0963",
border_color="#121114",
border_width=2,
corner_radius=15,
command=calcular,
hover_color="#2A913B",
height=50,width=90).grid(row=4, column=3,pady=10,padx=10)  







janela.mainloop()