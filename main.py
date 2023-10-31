import tkinter as tk

def get_chemicalise_translation():

    key = {'a':'h','b':'he','c':'li','d':'be','e':'b','f':'c','g':'n','h':'o',
       'i':'f','j':'ne','k':'na','l':'mg','m':'al','n':'si','o':'p','p':'s',
       'q':'cl','r':'ar','s':'k','t':'ca','u':'ti','v':'v','w':'cr','x':'mn',
       'y':'fe','z':'ni',' ': ' ', '1': 'db', '2': 'sg', '3': 'mt', '4': 'ds',
       '5': 'rg', '6': 'fl', '7': 'mc', '8': 'lv', '9': 'ts', '0': 'og'}
    res = ''

    with open("English.txt","r",encoding='utf-8') as i:
        text = i.read()
    
    for i in range(len(text)):
        char = text[i]

        try:
            if 'A' <= char < 'a' and len(key[char.lower()]) == 2:
                char = char.lower()
                res += key[char][0].upper()+key[char][1]
            elif 'A' <= char < 'a':
                res += key[char][0].upper()

            else:
                res += key[char]
                
        except KeyError:
            res += char
        
    with open("Chemicalise.txt","w",encoding="utf-8") as o:
        o.write(res)
        print("done")

def get_english_translation():
    
    key = {'h': 'a', 'he': 'b', 'li': 'c', 'be': 'd', 'b': 'e', 'c': 'f', 'n': 'g',
     'o': 'h', 'f': 'i', 'ne': 'j', 'na': 'k', 'mg': 'l', 'al': 'm', 'si': 'n',
     'p': 'o', 's': 'p', 'cl': 'q', 'ar': 'r', 'k': 's', 'ca': 't', 'ti': 'u',
     'v': 'v', 'cr': 'w', 'mn': 'x', 'fe': 'y', 'ni': 'z', ' ': ' ', 'db': '1',
     'sg': '2', 'mt': '3', 'ds': '4', 'rg': '5', 'fl': '6', 'mc': '7',
     'lv': '8','ts': '9', 'og': '0'}
    res = ''

    with open("Chemicalise.txt","r",encoding='utf-8') as i:
        text = i.read()

    i = 0
    while i < len(text):
        try:
            char = text[i+1]+text[i+2]
            char = key[char]
            char = text[i]
            
            if 'A' <= char[0] < 'a':
                char = char.lower()
                
                try:
                    res += key[char].upper()
                   
                except KeyError:
                    try:
                        char = text[i]
                        res += key[char]
                    except (KeyError,IndexError):
                        res += char
            else:
                try:
                    res += key[char]
                except KeyError:
                    try:
                        char = text[i]
                        res += key[char]
                    except (KeyError,IndexError):
                        res += char
            
            i += 1
            
        except (KeyError,IndexError):
            try:
                char = text[i]+text[i+1]
            except IndexError:
                char = text[i]
                
            if 'A' <= char[0] < 'a':
                char = char.lower()
                
                try:
                    res += key[char].upper()
                    i += 1
                        
                except KeyError:
                    try:
                        res += key[char[0]].upper()
                    except KeyError:
                        char = text[i]
                        res += key[char]
            else:
                try:
                    res += key[char]
                    i += 1
                        
                except KeyError:
                    try:
                        res += (key[char[0]])
                    except KeyError:
                        try:
                            char = text[i]
                            res += key[char]
                        except (KeyError,IndexError):
                            res += char
            
            i += 1
            
    with open("English.txt","w",encoding="utf-8") as o:
        o.write(res)
        print('done')

def close():
    mainWindow.destroy()
    
def createButtons():
    engButton = tk.Button(mainFrame,text='To English',fg='blue',
                          font='Arial 18',command=get_english_translation)
    engButton.place(x=0,y=0)

    chemButton = tk.Button(mainFrame,text='To Chemicalise',fg='green',
                           font='Arial 18',command=get_chemicalise_translation)
    chemButton.place(x=119,y=0)

    closeButton = tk.Button(mainFrame,text='Quit',fg='red',
                            font='Arial 18 bold',command=close)
    closeButton.place(x=277,y=0)
    
    
##########################################################

mainWindow = tk.Tk()
mainWindow.minsize(348,32)
mainWindow.title("Translator Control Panel")

mainFrame = tk.Frame(mainWindow,height=500,width=500)
mainFrame.place(x=0,y=0)

createButtons()

tk.mainloop()
