import tkinter as tk
from tkinter import ttk,messagebox
import json

with open('data.json','r', encoding='utf-8') as file:
    dictionar = json.load(file)

carte_aleasa,optiune_aleasa,carte_introdusa,stoc_introdus = 0,0,0,0
def get_values():
    global carte_aleasa,optiune_aleasa,carte_introdusa,stoc_introdus
    carte_aleasa = carti_list.get()
    optiune_aleasa = optiuni_button.get()
    carte_introdusa = carte_input.get()
    stoc_introdus = stoc_input.get()
    evaluare_alegere()
    update_combobox()

def update_combobox():
    carti_list['values'] = dictionar['carti']
    carti_list.set("Carti")

def evaluare_alegere():
    global carte_aleasa, optiune_aleasa,carte_introdusa,stoc_introdus
    ok = 1
    while ok:
        if optiune_aleasa == "Adaugare":
            if carte_introdusa == '':
                messagebox.showwarning("Boule", "Evident ca nu sti nici macar un titlu de carte...")
                ok = 0
            elif stoc_introdus == '':
                messagebox.showwarning("Boule", "Nu pot sa adaug numarul de carti citite de tine pana acum.")
                ok = 0
            else:
                dictionar['carti'].append(carte_introdusa)
                dictionar['stoc'].append(int(stoc_introdus))
                with open('data.json', 'w', encoding='utf-8') as file:
                    json.dump(dictionar,file,indent=4)
                messagebox.showinfo("Bravo boss!","Carte adaugate cu succes.")
                ok = 0

        elif optiune_aleasa == "Stergere":
            for i in range(len(dictionar['carti'])):
                if dictionar['carti'][i] == carte_aleasa:
                    dictionar['carti'].pop(i)
                    dictionar['stoc'].pop(i)
                    with open('data.json', 'w', encoding='utf-8') as file:
                        json.dump(dictionar, file,indent=4)
                    messagebox.showinfo("Bravo boss!", "Carte stearsa cu succes.")
                    ok = 0
                    break
            if ok!=0:
                messagebox.showwarning("Boule", "Ce vrei sa-ti sterg? Mucii la nas?!\nAlege o carte pe care vrei sa o elimini in loc sa te tot joci cu butoanele.")
                ok = 0
        elif optiune_aleasa == "Modificare":
            for i in range(len(dictionar['carti'])):
                if dictionar['carti'][i] == carte_aleasa and stoc_introdus!='':
                    dictionar['stoc'][i] = int(stoc_introdus)
                    with open('data.json', 'w', encoding='utf-8') as file:
                        json.dump(dictionar, file,indent=4)
                    messagebox.showinfo("Bravo boss!", "Stoc modificat cu succes.")
                    ok = 0
                    break
                elif stoc_introdus == '':
                    messagebox.showwarning("Boule","Nu te mai tot juca cu butoanele si introdu noul stoc!")
                    ok = 0
                    break
            if ok!=0:
                messagebox.showwarning("Boule", "Nu te mai tot juca cu butoanele si alege o carte si introdu-i noul stoc!")
                ok = 0
        elif optiune_aleasa == "Informatii":
            for i in range(len(dictionar['carti'])):
                if dictionar['carti'][i] == carte_aleasa:
                    messagebox.showinfo("Nerd-ule", f"Exista {dictionar['stoc'][i]} de carti cu titlul: {carte_aleasa}.")
                    ok = 0
                    break
            if ok!=0:
                messagebox.showwarning("Boule", "Nu te mai tot juca cu butoanele si alege o carte!")
                ok = 0
        else:
            messagebox.showwarning("Prostea","Nu sti introduce date bune? HĂ?!")
            ok = 0


root = tk.Tk()
root.title("Libraria lui 乒乓叮咚")
root.geometry("600x140")

root.createcommand("Get", get_values)

main_frame = tk.Frame(root,bg='black')
main_frame.pack_propagate(False)
main_frame.pack(fill = 'both', expand=True)

secondary_frame = tk.Frame(main_frame, width = 200, height = 120, bg = 'gray')
secondary_frame.pack_propagate(False)
secondary_frame.pack(side = 'left',anchor='n', padx = 10, pady = 10)

data_frame = tk.Frame(main_frame,width= 300,height=120,bg='gray')
data_frame.pack_propagate(False)
data_frame.pack(side='left',anchor='n',pady=10)

carte_input = tk.Entry(data_frame,width=50)
carte_input.pack(anchor='w',side='top',padx=10,pady=10)

stoc_input = tk.Entry(data_frame,width=10)
stoc_input.pack(anchor='w',side='top',padx=10)

values_button = tk.Button(data_frame, width=12,height=1,text="Lock in", command="Get")
values_button.pack(anchor='e',side='bottom', padx=10,pady=10)

quit_button = tk.Button(main_frame, width = 12, height = 1, text = "Quit", command = root.destroy)
quit_button.pack(side = 'right',anchor='n',padx=10,pady=10)

carti_list = ttk.Combobox(secondary_frame,width = 10, height= 5,state='readonly',values=dictionar['carti'])
carti_list.pack(side='left',anchor='n',padx=10,pady=10)
carti_list.set("Carti")

optiuni_button = ttk.Combobox(secondary_frame,width = 10, height= 5,state='readonly',values=["Adaugare","Stergere","Modificare","Informatii"])
optiuni_button.pack(side='left',anchor='n', padx=10,pady=10)
optiuni_button.set("Optiuni")

root.mainloop()