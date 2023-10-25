import os
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("FO")
root.minsize(200, 180)  # width, height
root.maxsize(200, 180)  # width, height
root.geometry("200x180")

execute_code = True
path = None


def browse():
    global path
    file = filedialog.askdirectory()
    if file:
        path = os.path.abspath(file)
        Label(root, text=str(path), font=('Aerial 8')).pack()
        organizebutton.config(state='normal')


def organize():
    root.destroy()


def xpressed():
    global execute_code
    execute_code = False
    root.destroy()


root.protocol("WM_DELETE_WINDOW", xpressed)

Label(root, text='File Organizer',
      font=('Verdana', 15)).pack(side=TOP, pady=10)

Label(root, text='Choose what folder to organize',
      font=('Verdana', 8)).pack()

Button(root, text='Browse', command=browse).pack(side=TOP, pady=10)
organizebutton = Button(root, text='Organize', command=organize, state='disabled')
organizebutton.pack()

root.mainloop()

folder = {
    "txt": "Text Files",
    "exe": "Executable Files",
    "docx": "Word and PDF",
    "pdf": "Word and PDF",
    "jpg": "Images",
    "png": "Images",
    "gif": "Images",
    "xlsx": "Excel",
    "pptx": "PowerPoints",
    "mp3": "Audios",
    "wav": "Audios",
    "mp4": "Videos",
    "zip": "Compressed Files",
    "rar": "Compressed Files",
    "jar": "Java Files",
    "msi": "Installers",
    "ini": "Shortcuts"
}


def getFiles():
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield path + f'\{file}'


def getExtensions():
    all_extensions = []
    for file in getFiles():
        filename = os.path.basename(file)
        all_extensions.append(os.path.splitext(filename)[1][1:])
    extensions = list(set(all_extensions))
    return extensions


def initFolders():
    extensions = getExtensions()

    for i in range(len(extensions)):
        if not extensions[i] in folder:
            folder[extensions[i]] = extensions[i]

        if not os.path.isdir(os.path.join(path, folder[extensions[i]])):
            os.mkdir(path + f'\{folder[extensions[i]]}')


def main():
    initFolders()
    for file in getFiles():
        moveto = os.path.join(path, folder[os.path.splitext(file)[1][1:]], os.path.basename(file), )
        os.rename(file, moveto)


if __name__ == "__main__" and execute_code:
    main()
