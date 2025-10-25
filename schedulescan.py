import os
import sys
try:
    import easyocr
    from tkinter import filedialog as fd
    from PIL import Image
except Exception as e:
    libr = str(e).split("'")[-2]
    os.system("pip install "+libr)
    python = sys.executable
    os.execv(python, [python] + sys.argv)

filename = fd.askopenfilename(initialdir="/", title="Select a File")
#filename = "C:/Users/gohal/Downloads/E-SPLOST_homeslider_girl-laptop.png"
print(filename)
reader = easyocr.Reader(['en']) # 'en' for English, add other languages as needed
results = reader.readtext(filename)
