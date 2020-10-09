import pytesseract
import tkinter as tk
import pyperclip
from PIL import ImageGrab
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '.\\Tesseract-OCR\\tesseract.exe'

def processClipboardImage(resultBox):
    resultBox.delete(1.0,tk.END)
    try:
        image = ImageGrab.grabclipboard()
        rgbImage = image.convert('RGB')

        imageString = pytesseract.image_to_string(rgbImage)
        resultBox.insert(1.0,imageString)

    except Exception as e:
        resultBox.insert(1.0,"Your clipboard does not contain a valid form of Image")
        print(e)

def copyText(resultBox):
    pyperclip.copy(resultBox.get(1.0,tk.END))

def main():
    mainWindow = tk.Tk()
    mainWindow.title("CopyTFI")
    mainWindow.geometry("800x600+50+50")

    mainWindow.grid_columnconfigure(0,weight=1)
    mainWindow.grid_columnconfigure(1,weight=1)
    mainWindow.grid_rowconfigure(0,weight=1)
    mainWindow.grid_rowconfigure(1,weight=1)

    resultBox = tk.Text(mainWindow,font=("Consolas",18),height=17)
    resultBox.grid(row=0,column=0,columnspan=2,padx=8,pady=5,sticky="nwes")

    PasteButton = tk.Button(text="Paste",command = lambda : processClipboardImage(resultBox))
    PasteButton.grid(row=1,column=0,padx=5,pady=2,sticky="nwes")

    CopyTextButton = tk.Button(text="Copy Text",command = lambda : copyText(resultBox))
    CopyTextButton.grid(row=1,column=1,padx=5,pady=2,sticky="nwes")

    mainWindow.mainloop()

if __name__ == "__main__":
    main()