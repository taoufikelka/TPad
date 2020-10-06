from Tkinter import *
from tkFileDialog import *

#Crypt text

def popup(event):
    menu4.post(event.x_root, event.y_root)

def clean_all():
 ent.delete('1.0', END)

def select(event):
 print event
 
 ent.tag_add(SEL, "1.0", CURRENT)
 ent.mark_set(INSERT, "1.0")
 ent.see(INSERT)
 print event
 return 'break'

def help():
 helpwin = Tk()
 helpwin.title('A propos')
 l = LabelFrame(helpwin, text="A propos de nous", padx=25, pady=30)
 l.pack(fill="both", expand="yes")
 Label(l, text="T-Pad et un mini block de note, qui \ncrypte les text sauvgarder.").pack()

 helpwin.mainloop()

def save():

 filename = asksaveasfile(parent=fen, mode='a')
 if filename is None :
  return
 # The dic of cars
 dectio={'\'':101,u'\xf9':100,'\r':' 99','\t':' 98','\x08':' 97',u'\xe0':' 96',u'\xe7':' 95',u'\xe8':' 94',u'\xe9':' 93',u'\xb2':' 92','<':' 91','>':' 90',';':' 89','\\':' 88','_':' 87','@':' 86','^':' 85','`':' 84','|':' 83','#':' 82','~':' 81','&':' 80','\n':' 79',':':' 78','+':' 77','-':' 76','*':' 75','/':' 74','{':' 73','[':' 72','(':' 71',')':' 70',']':' 69','}':' 68',',':' 67','?':' 66','!':' 65','%':' 64',' ':' 63','0':' 62','1':' 61','2':' 60','3':' 59','4':' 58','5':' 57','6':' 56','7':' 55','8':' 54','9':' 53','a':' 52','b':' 51','c':' 50','d':' 49','e':' 48','f':' 47','g':' 46','h':' 45','i':' 44','j':' 43','k':' 42','l':' 41','m':' 40','n':' 39','o':' 38','p':' 37','q':' 36','r':' 35','s':' 34','t':' 33','u':' 32','v':' 31','w':' 30','x':' 29','y':' 28','z':' 27','A':' 26','B':' 25','C':' 24','D':' 23','E':' 22','F':' 21','G':' 20','H':' 19','I':' 18','J':' 17','K':' 16','L':' 15','M':' 14','N':' 13','O':' 12','P':' 11','Q':' 10','R':'  9','S':'  8','T':'  7','U':'  6','V':'  5','W':'  4','X':'  3','Y':'  2','Z':'  1'}
 i = 0							     # the start of the loop
 mot = ent.get("1.0",END)	
 c = len(mot)	                	          	     # c = number of caracters
 while i < c :                  	          	     # start the loop
  b=i+1                         	          	     # b refers to the next car addr to select just one car  
  d = mot[i:b]					 	     # d is the car selected
  g = str(dectio[d])					     # g is the code of the car
  filename.write(g)					     # Write the code in the file
  i +=1  						     # for the loop
 clean_all()
 filename.close()					     # Close the file
 

def read():
 # The dic of codes
 decinv={'101':'\'','100':u'\xf9',' 99':'\r',' 98':'\t',' 97':'\x08',' 96':u'\xe0',' 95':u'\xe7',' 94':u'\xe8',' 93':u'\xe9',' 92':u'\xb2',' 91':'<',' 90':'>',' 89':';',' 88':'\\',' 87':'_',' 86':'@',' 85':'^',' 84':'`',' 83':'|',' 82':'#',' 81':'~',' 80':'&',' 79':'\n',' 78':':',' 77':'+',' 76':'-',' 75':'*',' 74':'/',' 73':'{',' 72':'[',' 71':'(',' 70':')',' 69':']',' 68':'}',' 67':',',' 66':'?',' 65':'!',' 64':'%',' 63':' ',' 62':'0',' 61':'1',' 60':'2',' 59':'3',' 58':'4',' 57':'5',' 56':'6',' 55':'7',' 54':'8',' 53':'9',' 52':'a',' 51':'b',' 50':'c',' 49':'d',' 48':'e',' 47':'f',' 46':'g',' 45':'h',' 44':'i',' 43':'j',' 42':'k',' 41':'l',' 40':'m',' 39':'n',' 38':'o',' 37':'p',' 36':'q',' 35':'r',' 34':'s',' 33':'t',' 32':'u',' 31':'v',' 30':'w',' 29':'x',' 28':'y',' 27':'z',' 26':'A',' 25':'B',' 24':'C',' 23':'D',' 22':'E',' 21':'F',' 20':'G',' 19':'H',' 18':'I',' 17':'J',' 16':'K',' 15':'L',' 14':'M',' 13':'N',' 12':'O',' 11':'P',' 10':'Q','  9':'R','  8':'S','  7':'T','  6':'U','  5':'V','  4':'W','  3':'X','  2':'Y','  1':'Z',}
 i=0
 filename = askopenfilename(parent=fen)
 if filename is None :
  return
 fileload = open(filename, 'r')				     # Open the file
 h = fileload.read()					     # Read from the file
 j = len(h)						     # j = number of codes
 while i<j:						     # Start of the loop
  a=i+3							     # a refer to the next code addr
  k = h[i:a]						     # k is the code selected
  l = decinv[k]						     # l is the code car
  ent.insert(INSERT,l)					     # Write the car in the text wid 
  i +=3  						     # for the loop
 fileload.close()					     # close the file

fen = Tk()						     # The window
fen.title('T-pad')

menubar = Menu(fen)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Ouvrir", underline=0, command=read)
menu1.add_command(label="Sauvgarder", underline=0, command=save)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fen.quit, underline=0)
menubar.add_cascade(label="Fichier", menu=menu1, underline=0)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Selectionner tout", underline=0, comman=select)
menu2.add_separator()
menu2.add_command(label="Couper", underline=0)
menu2.add_command(label="Copier", underline=0)
menu2.add_command(label="Coller", underline=0)
menu2.add_separator()
menu2.add_command(label="Effacer tout", underline=0, command=clean_all)
menubar.add_cascade(label="Editer", menu=menu2, underline=0)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", underline=0, command=help)
menubar.add_cascade(label="Aide", menu=menu3, underline=0)

fen.config(menu=menubar)

menu4 = Menu(fen, tearoff=0)
menu4.add_command(label="Selectionner tout", command=select)
menu4.add_command(label="Effacer tout", command=clean_all)


ent = Text(fen)								# The entry 
ent.pack()

ent.bind("<Control-Key-a>", select)					#ctrl+a/A -> select_all
ent.bind("<Control-Key-A>", select)				# just in case caps lock is on
ent.bind("<Button-3>", popup)
ent.bind("<Control-Key-o>", read)					#ctrl+o/O -> read/open a file
ent.bind("<Control-Key-O>", read)				# just in case caps lock is on
ent.bind("<Control-Key-s>", save)					#ctrl+s/S -> save/creat a file
ent.bind("<Control-Key-S>", save)				# just in case caps lock is on


fen.mainloop()
