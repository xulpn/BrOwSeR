from tkinter import filedialog as fd
def fexplore():
    return fd.askopenfilename(
        title='Open a file',
        initialdir='./config/',
        filetypes=(('text files', '*.txt'),)
        )




#  LAST
# import tkinter
# from tkinter import filedialog
#
# def fexplore():
#     file = None
#     try:
#         file = filedialog.Tk().withdraw()
#         return filedialog.askopenfile(mode='r').name
#     except:
#         print(f"Cannot find file '{file}'")
#         exit()
