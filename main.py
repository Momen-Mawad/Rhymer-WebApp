import tkinter as tk
from tkinter.filedialog import askopenfilename
import pronouncing

def open_file(fileLabel):
    """Open a file for editing."""
    global filepath
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    fileName = filepath.split('/')[-1][:-4]
    fileLabel.config(text=fileName + ' loaded')

def findRhyme(x):
    file = open(x, "r", encoding='UTF-8')
    word = wordEnrty.get()
    txt_edit.delete('1.0', tk.END)
    text = file.read().splitlines()
    text = [i for i in text if not i == '']
    text = [i for i in text if not i[0] == 'P' and not i[-1] == '"']
    Rhyme = [i for i in text if i.split()[-1] in pronouncing.rhymes(word)]
    Rhyme ='\n'.join(Rhyme)
    txt_edit.insert(tk.END, Rhyme)

window = tk.Tk()
window.title("Rhymer")
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
fileLabel = tk.Label(fr_buttons, text="No file loaded")
wordEnrty = tk.Entry(fr_buttons)
btn_open = tk.Button(fr_buttons, text="Load Master File", command=lambda:open_file(fileLabel))
btn_rhyme = tk.Button(fr_buttons, text="Find Rhyme", command=lambda:findRhyme(filepath))

btn_open.grid(row=0, column=0, padx=5, pady=5)
wordEnrty.grid(row=0, column=1, padx=5)
btn_rhyme.grid(row=0, column=2, padx=5)
fileLabel.grid(row=0, column=3, sticky='e')
fr_buttons.grid(row=2, column=0, sticky='e'+'w')
txt_edit.grid(row=1, column=0)

window.mainloop()

#pyinstaller --onefile main.py
#pyinstaller -w -F main.py
#PyInstaller --add-data=C:/Users/User/Documents/Python/Rhymer:cmudict/ main.spec
#PyInstaller --hidden-import pronouncing --noconsole --hidden-import pkg_resources.py2_warn --add-data C:/Users/User/Documents/Python/Rhymer/venv/lib/site-packages/cmudict/;cmudict/ --onefile --paths=C:/Users/User/Documents/Python/Rhymer/venv/lib/site-packages/ --paths=C:/Users/User/AppData/Local/Programs/Python/Python38-32/Lib/site-packages main.py
#PyInstaller --hidden-import pronouncing --noconsole --add-data C:/Users/User/Documents/Python/Rhymer/venv/lib/site-packages/cmudict/;cmudict/ --onefile --paths=C:/Users/User/Documents/Python/Rhymer/venv/lib/site-packages/ --paths=C:/Users/User/AppData/Local/Programs/Python/Python38-32/Lib/site-packages -i icon.ico main.py



