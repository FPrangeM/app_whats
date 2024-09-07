import customtkinter as ctk
import pandas as pd
import os
from tabulate import tabulate
from prettytable import PrettyTable
from driver import rodar_driver





# df = pd.read_excel(r'C:\Users\Prange\Downloads\Ref.xlsx',sheet_name='Consolidado')
# df
# print(tabulate(df[['Aluno', 'Turma']].applymap(lambda x: str(x).strip()),headers='keys', tablefmt='grid',colalign=('left', 'center')))

# Inicializa a aplicação
app = ctk.CTk()
app.geometry('800x500')
# ctk.set_default_font(("Arial", 12))

# Variáveis globais
file_path = ctk.StringVar()
textbox_text = ctk.StringVar()
df = None

textbox_text.set('')

# Funções 
def print_nome():
    global df
    filename = ctk.filedialog.askopenfilename()
    if filename:
        file_path.set(filename)
        name = os.path.basename(filename)  # Utiliza os.path.basename para obter o nome do arquivo
        label.configure(text=f"Arquivo selecionado -> {name}")
        try:
            df = pd.read_excel(filename, sheet_name='Consolidado')
            df = df.reset_index(drop=True)
            df.index += 1
            colunas = ['Aluno','Responsável','Telefone','Status','Turma','Dia']
            df = df[colunas]
            # textbox1.insert("1.0", df[['Aluno', 'Turma']].to_string(index=False, numalign='left', stralign='left'))
            # textbox1.insert("1.0", df[['Aluno', 'Turma']].to_string(index=False))
            textbox1.insert("0.0", tabulate(df,headers='keys', tablefmt='grid',colalign=('left', 'center')))
            textbox1.configure(state='disable')

        except Exception as e:
            print(f"Erro ao ler o arquivo Excel: {e}")
# Elementos da interface principal
label_arquivo = ctk.CTkLabel(app, text="Selecione o arquivo excel com as informações dos contatos:")
label_arquivo.pack(pady=(10,2))

button = ctk.CTkButton(master=app, text="Selecione o arquivo", command=print_nome)
button.pack(pady=(5))

label = ctk.CTkLabel(master=app, text="Nome do arquivo:")
label.pack(pady=0)


textbox1 = ctk.CTkTextbox(master=app, width=700, height=300, corner_radius=2,font=("Courier New", 12))
textbox1.pack(pady=10)

def iniciar_automacao():
    rodar_driver(df)

button = ctk.CTkButton(master=app, text="Iniciar Programa !!!", command=iniciar_automacao)
button.pack(pady=(20))


app.mainloop()






















    
# def find_whats_profile():

#     pasta_raiz = fr'C:/Users/{os.getlogin()}/AppData/Local/Google/Chrome/User Data'
#     profiles = [file for file in os.listdir(pasta_raiz) if 'Profile ' in file]

#     for profile in profiles:
#         folder = os.path.join(pasta_raiz,profile,'IndexedDB')
        
#         if 'https_web.whatsapp.com_0.indexeddb.leveldb' in os.listdir(folder):
#             return profile



# import customtkinter as ctk
# import os
# import threading

# # ... (sua função find_whats_profile)

# ctk.set_appearance_mode("System")
# ctk.set_default_color_theme("blue")

# app = ctk.CTk()
# app.geometry("400x200")
# app.title("Verificador de Perfil WhatsApp")

# frame = ctk.CTkFrame(master=app)
# frame.pack(pady=20, padx=20, fill="both", expand=True)

# label = ctk.CTkLabel(master=frame, text="Verificando perfil...")
# label.pack(pady=10)

# progress_bar = ctk.CTkProgressBar(master=frame)
# progress_bar.pack(pady=10, fill="x", padx=10)

# def verificar_perfil():
#     perfil = find_whats_profile()
#     if perfil:
#         label.configure(text=f"Perfil encontrado: {perfil}")
#         progress_bar.set(100)
#     else:
#         label.configure(text="Perfil não encontrado.")
#         progress_bar.set(0)

# # Iniciar a verificação em uma thread separada
# thread = threading.Thread(target=verificar_perfil)
# thread.start()

# app.mainloop()

