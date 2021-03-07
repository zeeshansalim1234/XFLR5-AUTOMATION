import time,pyautogui as pg
from tkinter import *
from PIL import ImageTk,Image


"""----------------------------------THIS IS THE MODULE FOR ANALYSING AIRFOILS---------------------------------------"""

"""------------------------------------------------INPUTS------------------------------------------------------------"""

countline=0                                 # For counting file lines
array_inputs=[]                             # List of all inputs
ascending_all_foils=[]                      # List of all foil names in ascending order
nacafoils_names=[]                          # List of all NACA foil names
loadedfoils_names=[]                        # List of all Loaded foil names
specificfoils_names=[]                      # List of foils to be analysed
indices=[]                                  # List of indices of all commen elements in specific and ascending arrays
num_nacafoils=[]                            # Number of naca foils to be created
num_loadedfoils=[]                          # Number of loaded foils to be created

"""---------------------------------------------------X--------------------------------------------------------------"""

"""----------------------------------------------------GUI-----------------------------------------------------------"""


from tkinter import *
from PIL import ImageTk,Image

arr_gui=[]

def save_info():

    arr_gui.append(firstentry.get())
    arr_gui.append(secondentry.get())
    arr_gui.append(thirdentry.get())
    arr_gui.append(fourthentry.get())
    arr_gui.append(fifthentry.get())
    arr_gui.append(sixthentry.get())
    arr_gui.append(seventhentry.get())
    arr_gui.append(eighthentry.get())
    arr_gui.append(ninthentry.get())
    arr_gui.append(tenthentry.get())
    arr_gui.append(eleventhentry.get())
    arr_gui.append(twelvethentry.get())
    arr_gui.append(thirteenthentry.get())


    print(arr_gui)

    f = open("XFLR5inputs.txt", "r")
    lines = f.readlines()

    x=0

    for k in range(40,65,2):

        if (arr_gui[x] != ''):
            lines[k] =str(arr_gui[x])+'\n'

        x+=1

    f.close()

    lines = ''.join([str(elem) for elem in lines])


    f = open("XFLR5inputs.txt", "w")

    f.writelines(lines)
    f.close()



app = Tk()

app.geometry("1900x1500")

app.title("XFLR5 AUTOMATION")

app.configure(background="#F7F7F7")

heading = Label(text="AIRFOIL ANALYSIS",fg="white",bg="black",font="Helvetica 13 bold italic",width="500",height="3")

heading.pack()


img1 = ImageTk.PhotoImage(Image.open('university_logo.png'))
label=Label(image=img1,bg="#F7F7F7")
label.pack()
label.place(x=1700,y=820)

img2 = ImageTk.PhotoImage(Image.open('SAED_logo.jpg'))
label=Label(image=img2,bg="#F7F7F7")
label.pack()
label.place(x=1350,y=870)

img3 = ImageTk.PhotoImage(Image.open('multi_analysis_menu.png'))
label=Label(image=img3,bg="#F7F7F7")
label.pack()
label.place(x=900,y=200)


firstentry_text = Label(text="Do you wish to analyze All Foils(y/n)?")
secondentry_text = Label(text="Enter the Specific foil name(s) (seperate by space)")
thirdentry_text = Label(text="Enter Reynolds Min value:")
fourthentry_text =Label(text="Enter Reynolds Max value")
fifthentry_text =Label(text="Enter Reynolds Increment value")
sixthentry_text = Label(text="Enter Mach value")
seventhentry_text = Label(text="Enter NCrit value")
eighthentry_text = Label(text="Enter Top Transition location(x/c)")
ninthentry_text = Label(text="Enter Bottem Transition location(x/c)")
tenthentry_text = Label(text="Specify Alpha or CL (Enter a or c)")
eleventhentry_text = Label(text="Enter Alpha/CL Min value")
twelvethentry_text = Label(text="Enter Alpha/CL Max value")
thirteenthentry_text = Label(text="Enter Alpha/CL increment value")


firstentry_text.place(x=15,y=110)
secondentry_text.place(x=15,y=200)
thirdentry_text.place(x=15,y=290)
fourthentry_text.place(x=15,y=380)
fifthentry_text.place(x=15,y=470)
sixthentry_text.place(x=15,y=560)
seventhentry_text.place(x=400,y=110)
eighthentry_text.place(x=400,y=200)
ninthentry_text.place(x=400,y=290)
tenthentry_text.place(x=400,y=380)
eleventhentry_text.place(x=400,y=470)
twelvethentry_text.place(x=400,y=560)
thirteenthentry_text.place(x=400,y=650)


firstentry = StringVar()
secondentry = StringVar()
thirdentry = StringVar()
fourthentry= StringVar()
fifthentry= StringVar()
sixthentry= StringVar()
seventhentry=StringVar()
eighthentry=StringVar()
ninthentry=StringVar()
tenthentry=StringVar()
eleventhentry=StringVar()
twelvethentry=StringVar()
thirteenthentry=StringVar()



firstentry_enter = Entry(textvariable=firstentry,width="30")
secondentry_enter = Entry(textvariable=secondentry,width="30")
thirdentry_enter = Entry(textvariable=thirdentry,width="30")
fourthentry_enter = Entry(textvariable=fourthentry,width="30")
fifthentry_enter = Entry(textvariable=fifthentry,width="30")
sixthentry_enter = Entry(textvariable=sixthentry,width="30")
seventhentry_enter= Entry(textvariable=seventhentry,width="30")
eighthentry_enter= Entry(textvariable=eighthentry,width="30")
ninthentry_enter= Entry(textvariable=ninthentry,width="30")
tenthentry_enter= Entry(textvariable=tenthentry,width="30")
eleventhentry_enter= Entry(textvariable=eleventhentry,width="30")
twelvethentry_enter= Entry(textvariable=twelvethentry,width="30")
thirteenthentry_enter= Entry(textvariable=thirteenthentry,width="30")


firstentry_enter.place(x=15,y=140)
secondentry_enter.place(x=15,y=230)
thirdentry_enter.place(x=15,y=320)
fourthentry_enter.place(x=15,y=410)
fifthentry_enter.place(x=15,y=500)
sixthentry_enter.place(x=15,y=590)
seventhentry_enter.place(x=400,y=140)
eighthentry_enter.place(x=400,y=230)
ninthentry_enter.place(x=400,y=320)
tenthentry_enter.place(x=400,y=410)
eleventhentry_enter.place(x=400,y=500)
twelvethentry_enter.place(x=400,y=590)
thirteenthentry_enter.place(x=400,y=680)


button1 = Button(app,text="Save",command=save_info,width="30",height="2",bg="orange")
button1.place(x=15,y=900)





mainloop()

"""------------------------------------------------------X-----------------------------------------------------------"""


"""-----------------------------------------------INPUT TEXT FILE----------------------------------------------------"""

file=open("XFLR5inputs.txt","r")             # Open Text File in read mode
f=file.readlines()


for line in f:                               # Reading required input line by line
    countline+=1
    if(countline==4):
        num_nacafoils.append(line.strip())
    elif(countline==10):
        num_loadedfoils.append(line.strip())
    elif(countline==6):
        nacafoils_names.append(line.strip())
    elif(countline==14):
        loadedfoils_names.append(line.strip())
    elif(countline>40 and countline<66 and countline%2!=0):
        array_inputs.append(line.strip())

nacafoils_names=nacafoils_names[0].split(' ')                   # For converting to 2D array
loadedfoils_names=loadedfoils_names[0].split(' ')               # For converting to 2D array
specificfoils_names=array_inputs[1].split(' ')                  # For converting to 2D array

for i in range(0, len(nacafoils_names)):                        # Arranges all NACA foil names in ascending order
    for j in range(i+1, len(nacafoils_names)):
        if(nacafoils_names[i] > nacafoils_names[j]):
            temp = nacafoils_names[i];
            nacafoils_names[i] = nacafoils_names[j];
            nacafoils_names[j] = temp;

for i in range(0, len(loadedfoils_names)):                       # Arranges all loaded foil names in ascending order
    for j in range(i+1, len(loadedfoils_names)):
        if(loadedfoils_names[i] > loadedfoils_names[j]):
            temp = loadedfoils_names[i];
            loadedfoils_names[i] = loadedfoils_names[j];
            loadedfoils_names[j] = temp;

if(num_nacafoils[0]=='0'):                      #if only loaded foils (will arrange those in ascending order)
    ascending_all_foils=loadedfoils_names
elif(num_loadedfoils[0]=='0'):                  #if only created Naca foils (will arrange those in ascending order)
    ascending_all_foils=nacafoils_names
else:
    ascending_all_foils=loadedfoils_names+nacafoils_names     #if user loaded and created foils (ascending order)

indices = [i for i, item in enumerate(ascending_all_foils) if item in set(specificfoils_names)]   # To find indices of commen elements

"""----------------------------------------------------X-------------------------------------------------------------"""

print("INPUTS:")
print("PARAMETERS:",array_inputs)
print("FOIL LIST:",ascending_all_foils)
print("FOIL TO BE ANALYZED:",specificfoils_names)
print("INDICES:",indices)

time.sleep(0.5)
pg.getWindowsWithTitle("xflr5 v6.47")[0].restore()         #To open XFLR5 window
time.sleep(1)

def analyzefoil():


    time.sleep(0.5)
    pg.hotkey('ctrl','F6')            # Open Multi-threaded batch analysis menu

    time.sleep(0.2)
    fw = pg.getWindowsWithTitle('Multi-threaded batch analysis')  # Finds the window

    fw[0].size = (1294, 708)                                      # To assure window is placed at same spot for everyone
    fw[0].topleft = (20, 20)

    """------------------------------------------FOIL SELECTION------------------------------------------------------"""


    time.sleep(0.2)
    pg.typewrite(['right'])
    pg.typewrite(['tab'])
    pg.typewrite(['space'])
    pg.typewrite(['escape'])
    pg.typewrite(['space'])

    time.sleep(1)
    fw1 = pg.getWindowsWithTitle('Foil Selection')

    fw1[0].size = (408, 431)
    fw1[0].topleft = (455, 164)


    if(array_inputs[0]=="y" or array_inputs[0]=="Y"):           # Analyzing All foils

        time.sleep(0.2)

        for i in range(0,3):
            pg.typewrite(['tab'])

        pg.typewrite(['space'])
        pg.typewrite(['tab'])

        time.sleep(0.2)
        pg.typewrite(['enter'])



    else:

        for i in range(0,len(indices)):     # Analyzing specific foils provided by user

            time.sleep(0.2)

            for j in range(0,6):            # Going back to box 1
                pg.typewrite(['up'])

            for i in range(0,int(indices[i])):
                pg.typewrite(['down'])

            pg.typewrite(['space'])


        pg.typewrite(["enter"])

    """--------------------------------------------------X-----------------------------------------------------------"""

    """-----------------------------------------------PARAMETERS-----------------------------------------------------"""

    time.sleep(0.2)
    pg.typewrite(['tab'])               # Choosing range
    pg.typewrite(['space'])

    for k in range(2,9):

        pg.typewrite(['tab'])           # Entering parameters
        pg.typewrite(array_inputs[k])


    if(array_inputs[9]=='a'):           # Chooses Alpha

        time.sleep(0.1)
        pg.press('tab',presses=2)

    else:                               # Chooses Cl

        time.sleep(0.1)
        pg.press('tab')
        pg.press('right')


    for l in range(10,13):

        pg.typewrite(['tab'])           # Entering parameters
        pg.typewrite(array_inputs[l])

    pg.press('enter',presses=2)         # Start analysis


    """-------------------------------------------END OF FUNCTION----------------------------------------------------"""

analyzefoil()          # Function call

file.close()           # Closing text file


