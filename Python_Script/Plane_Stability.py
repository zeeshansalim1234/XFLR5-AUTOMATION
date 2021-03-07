import time, pyautogui as pg
from tkinter import *
from PIL import ImageTk,Image

"""---------------------------------------THIS MODULE IS FOR STABILITY ANALYSIS--------------------------------------"""

"""----------------------------------------------------GUI-----------------------------------------------------------"""

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
    arr_gui.append(fourteenthentry.get())
    arr_gui.append(fifteenthentry.get())
    arr_gui.append(sixteenthentry.get())
    arr_gui.append(seventeenthentry.get())
    arr_gui.append(eighteenthentry.get())
    arr_gui.append(nineteenthentry.get())
    arr_gui.append(twenteethentry.get())
    arr_gui.append(twentyonethentry.get())
    arr_gui.append(twentysecondentry.get())




    print(arr_gui)

    f = open("XFLR5inputs.txt", "r")
    lines = f.readlines()

    x=0

    for k in range(235,250,2):

        if (arr_gui[x] != ''):
            lines[k] =str(arr_gui[x])+'\n'

        x+=1

    for k in range(252,259,3):

        if (arr_gui[x] != ''):
            lines[k] =str(arr_gui[x])+'\n'

        x+=1

    for k in range(260,265,2):

        if (arr_gui[x] != ''):
            lines[k] =str(arr_gui[x])+'\n'

        x+=1

    for k in range(267,271,3):

        if (arr_gui[x] != ''):
            lines[k] =str(arr_gui[x])+'\n'

        x+=1

    for k in range(272,283,2):

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

heading = Label(text="STABILITY ANALYSIS",fg="white",bg="black",font="Helvetica 13 bold italic",width="500",height="3")

heading.pack()


img1 = ImageTk.PhotoImage(Image.open('university_logo.png'))
label=Label(image=img1,bg="#F7F7F7")
label.pack()
label.place(x=1700,y=820)

img2 = ImageTk.PhotoImage(Image.open('SAED_logo.jpg'))
label=Label(image=img2,bg="#F7F7F7")
label.pack()
label.place(x=1350,y=870)

img3 = ImageTk.PhotoImage(Image.open('stability_menu1.PNG'))
label=Label(image=img3,bg="#F7F7F7")
label.pack()
label.place(x=1005,y=110)

img4 = ImageTk.PhotoImage(Image.open('stability_menu2.PNG'))
label=Label(image=img4,bg="#F7F7F7")
label.pack()
label.place(x=1375,y=110)

img5 = ImageTk.PhotoImage(Image.open('stability_menu3.PNG'))
label=Label(image=img5,bg="#F7F7F7")
label.pack()
label.place(x=1005,y=370)

img6 = ImageTk.PhotoImage(Image.open('stability_menu4.PNG'))
label=Label(image=img6,bg="#F7F7F7")
label.pack()
label.place(x=1375,y=370)

img7 = ImageTk.PhotoImage(Image.open('stability_menu5.PNG'))
label=Label(image=img7,bg="#F7F7F7")
label.pack()
label.place(x=1005,y=630)

img8 = ImageTk.PhotoImage(Image.open('stability_menu6.PNG'))
label=Label(image=img8,bg="#F7F7F7")
label.pack()
label.place(x=1375,y=630)


firstentry_text = Label(text="Viscous Anlaysis check box ON in analysis menu(y/n)?")
secondentry_text = Label(text="Enter Beta value for flight altitude:")
thirdentry_text = Label(text="Enter Phi value for flight altitude:")
fourthentry_text =Label(text="Select Wing Platform (1)/Wing Platform projected on xy plane/Manual input")
fifthentry_text =Label(text="Enter Ref. area (Only if you chose Manual input):")
sixthentry_text = Label(text="Enter Ref. span length (Only if you chose Manual input):")
seventhentry_text = Label(text="Enter Ref. cord length (Only if you chose Manual input):")
eighthentry_text = Label(text="Use plane inertia check box ON in Mass and inertia menu(y/n)?")
ninthentry_text = Label(text="Enter mean value of inertia parameters CoG_x CoG_y Ixx Iyy Izz Ixz")
tenthentry_text = Label(text="Enter Gain(unit/ctrl)of parameters Mass CoG_x CoG_y Ixx Iyy Izz Ixz")
eleventhentry_text = Label(text="Enter Gain(Â°/ctrl) for control parameters Wing_Tilt Elevator_Tilt")
twelvethentry_text = Label(text="Choose international or imperial for Air Data menu (enter int or imp):")
thirteenthentry_text = Label(text="Enter the value of Rho:")
fourteenthentry_text = Label(text="Enter the value of Mu:")
fifteenthentry_text= Label(text="Enter Extra Area(m^2) for Extra drag table")
sixteenthentry_text= Label(text="Enter Extra drag coeff. for EXtra drag table")
seventeenthentry_text= Label(text="Sequence ON or OFF(y/n)?")
eighteenthentry_text= Label(text="Enter Start value:")
nineteenthentry_text= Label(text="Enter End value:")
twenteethentry_text= Label(text="Enter increment value:")
twentyonethentry_text= Label(text="Run analysis on ALL planes?(y/n)",fg="red")
twentysecondentry_text= Label(text="Enter number of planes currently loaded on XFLR5:",fg="red")


firstentry_text.place(x=15,y=110)
secondentry_text.place(x=15,y=160)
thirdentry_text.place(x=15,y=210)
fourthentry_text.place(x=15,y=260)
fifthentry_text.place(x=15,y=310)
sixthentry_text.place(x=15,y=360)
seventhentry_text.place(x=15,y=410)
eighthentry_text.place(x=15,y=460)
ninthentry_text.place(x=15,y=510)
tenthentry_text.place(x=15,y=560)
eleventhentry_text.place(x=15,y=610)
twelvethentry_text.place(x=15,y=660)
thirteenthentry_text.place(x=15,y=710)
fourteenthentry_text.place(x=15,y=760)
fifteenthentry_text.place(x=560,y=110)
sixteenthentry_text.place(x=560,y=160)
seventeenthentry_text.place(x=560,y=310)
eighteenthentry_text.place(x=560,y=360)
nineteenthentry_text.place(x=560,y=410)
twenteethentry_text.place(x=560,y=460)
twentyonethentry_text.place(x=560,y=560)
twentysecondentry_text.place(x=560,y=610)



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
fourteenthentry=StringVar()
fifteenthentry=StringVar()
sixteenthentry=StringVar()
seventeenthentry=StringVar()
eighteenthentry=StringVar()
nineteenthentry=StringVar()
twenteethentry=StringVar()
twentyonethentry=StringVar()
twentysecondentry=StringVar()




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
fourteenthentry_enter= Entry(textvariable=fourteenthentry,width="30")
fifteenthentry_enter=Entry(textvariable=fifteenthentry,width="30")
sixteenthentry_enter= Entry(textvariable=sixteenthentry,width="30")
seventeenthentry_enter= Entry(textvariable=seventeenthentry,width="30")
eighteenthentry_enter= Entry(textvariable=eighteenthentry,width="30")
nineteenthentry_enter= Entry(textvariable=nineteenthentry,width="30")
twenteethentry_enter= Entry(textvariable=twenteethentry,width="30")
twentyonethentry_enter= Entry(textvariable=twentyonethentry,width="30")
twentysecondentry_enter= Entry(textvariable=twentysecondentry,width="30")



firstentry_enter.place(x=15,y=140)
secondentry_enter.place(x=15,y=190)
thirdentry_enter.place(x=15,y=240)
fourthentry_enter.place(x=15,y=290)
fifthentry_enter.place(x=15,y=340)
sixthentry_enter.place(x=15,y=390)
seventhentry_enter.place(x=15,y=440)
eighthentry_enter.place(x=15,y=490)
ninthentry_enter.place(x=15,y=540)
tenthentry_enter.place(x=15,y=590)
eleventhentry_enter.place(x=15,y=640)
twelvethentry_enter.place(x=15,y=690)
thirteenthentry_enter.place(x=15,y=740)
fourteenthentry_enter.place(x=15,y=790)
fifteenthentry_enter.place(x=560,y=140)
sixteenthentry_enter.place(x=560,y=190)
seventeenthentry_enter.place(x=560,y=340)
eighteenthentry_enter.place(x=560,y=390)
nineteenthentry_enter.place(x=560,y=440)
twenteethentry_enter.place(x=560,y=490)
twentyonethentry_enter.place(x=560,y=590)
twentysecondentry_enter.place(x=560,y=640)



button1 = Button(app,text="Save",command=save_info,width="30",height="2",bg="orange")
button1.place(x=15,y=900)





mainloop()




"""------------------------------------------------------X-----------------------------------------------------------"""


"""--------------------------------------------READING FROM TEXT FILE------------------------------------------------"""

countline = 0
array_inputs = []

file = open("XFLR5inputs.txt", "r")
f = file.readlines()

for line in f:

    countline += 1
    if (countline >= 236 and countline <= 250 and countline % 2 == 0):
        array_inputs.append(line.strip())

    elif (countline == 253 or countline == 256 or countline == 259):
        array_inputs.append(line.strip())

    elif (countline >= 261 and countline <= 265 and countline % 2 != 0):
        array_inputs.append(line.strip())

    elif (countline == 268 or countline == 271):
        array_inputs.append(line.strip())

    elif (countline >= 273 and countline <= 283 and countline % 2 != 0):
        array_inputs.append(line.strip())

for i in range(8, 16):

    if (i != 11 and i != 12 and i != 13):
        array_inputs[i] = array_inputs[i].split(' ')

"""---------------------------------------------------X--------------------------------------------------------------"""

print("INPUTS:")
print(array_inputs)
time.sleep(0.5)
pg.getWindowsWithTitle("xflr5 v6.47")[0].restore()


def stabilityanalysis():
    time.sleep(1)  # Analysis menu bar
    pg.hotkey('Shift', 'F6')

    time.sleep(1)
    fw = pg.getWindowsWithTitle('Stability Polar Definition')
    fw[0].size = (775, 540)
    fw[0].topleft = (564, 245)

    """-------------------------------------------------ANALYSIS-----------------------------------------------------"""

    time.sleep(0.5)
    viscous_analysis_box = pg.locateOnScreen('viscousanalysis_checkbox.PNG', region=(500, 240, 790, 550))

    for i in range(0, 3):
        pg.hotkey('shift', 'tab')

    if (array_inputs[0] == "y" or array_inputs[0] == "Y"):

        if (viscous_analysis_box is None):  # Check the box

            time.sleep(0.1)
            pg.typewrite(['space'])

    elif (array_inputs[0] == "n" or array_inputs[0] == "N"):

        if (viscous_analysis_box is not None):  # Uncheck the box

            time.sleep(0.1)
            pg.typewrite(['space'])

    for j in range(1, 3):
        time.sleep(0.1)
        pg.press('tab')
        pg.typewrite(array_inputs[j])

    pg.press('tab', presses=4)

    """---------------------------------------------------X----------------------------------------------------------"""

    """----------------------------------------------REF. DIMENSIONS-------------------------------------------------"""

    time.sleep(0.1)  # Ref Dimensions menu
    pg.press('right')
    pg.press('tab', presses=2)

    if (array_inputs[3] == '1'):

        time.sleep(0.1)
        pg.press('space')

    elif (array_inputs[3] == '2'):

        time.sleep(0.1)
        pg.press('down')
        pg.press('space')

    elif (array_inputs[3] == '3'):

        time.sleep(0.1)
        pg.press('down', presses=2)
        pg.press('space')

        for j in range(4, 7):

            pg.press('tab')
            pg.typewrite(array_inputs[j])

    pg.press('tab', presses=4)

    """---------------------------------------------------X----------------------------------------------------------"""

    """---------------------------------------------MASS AND INERTIA-------------------------------------------------"""

    time.sleep(0.1)  # Mass and Inertia menu
    pg.press('right')

    time.sleep(0.5)
    useplaneinertia_box = pg.locateOnScreen('useplaneinertia_checkbox.PNG', region=(500, 240, 790, 550))

    if (array_inputs[7] == "y" or array_inputs[7] == "Y"):

        if (useplaneinertia_box is None):  # Check the box

            time.sleep(0.1)
            pg.press('tab', presses=3)
            pg.typewrite(['enter'])

            for j in range(0, 2):
                pg.hotkey('shift', 'tab')

            pg.press('space')
            pg.press('tab', presses=4)


    elif (array_inputs[7] == "n" or array_inputs[7] == "N"):

        if (useplaneinertia_box is not None):  # Uncheck the box

            time.sleep(0.1)
            pg.press('tab', presses=2)
            pg.press('space')
            pg.press('tab', presses=7)

        else:

            time.sleep(0.1)
            pg.press('tab', presses=3)

        for j in range(0, 7):

            if (j == 0):
                pg.typewrite(array_inputs[8][0])

            else:

                pg.press('down')
                pg.typewrite(array_inputs[8][j])

        pg.press('tab')
        pg.press('up', presses=6)

        for j in range(0, 7):

            if (j == 0):
                pg.typewrite(array_inputs[9][0])

            else:

                pg.press('down')
                pg.typewrite(array_inputs[9][j])

        pg.press('enter',presses=2)
        pg.press('tab',presses=2)


    """---------------------------------------------------X----------------------------------------------------------"""

    """--------------------------------------------CONTROL PARAMETERS------------------------------------------------"""

    time.sleep(0.1)
    pg.press('right')

    pg.press('tab', presses=3)
    pg.typewrite(array_inputs[10][0])

    time.sleep(0.2)
    pg.press('down')
    pg.typewrite(array_inputs[10][1])

    time.sleep(0.2)
    pg.typewrite(['enter'])
    pg.typewrite(['enter'])
    pg.press('tab', presses=2)

    """---------------------------------------------------X----------------------------------------------------------"""

    """-----------------------------------------------AERO DATA------------------------------------------------------"""

    time.sleep(0.1)
    pg.press('right')
    pg.press('tab', presses=2)

    if (array_inputs[11] == "int"):

        time.sleep(0.1)  # International radio button
        pg.press('left')

    elif (array_inputs[11] == "imp"):

        time.sleep(0.1)  # Imperial radio button
        pg.press('right')

    for j in range(12, 14):
        pg.press('tab')
        pg.typewrite(array_inputs[j])

    pg.press('tab', presses=5)

    """---------------------------------------------------X----------------------------------------------------------"""

    """-----------------------------------------------EXTRA DRAG-----------------------------------------------------"""

    time.sleep(0.1)  # Click right arrow
    pg.press('right')

    pg.press('tab', presses=3)

    for k in range(14, 16):

        for j in range(0, 4):

            if (j == 0):

                pg.typewrite(array_inputs[k][j])

            else:

                pg.press('down')
                pg.typewrite(array_inputs[k][j])

        pg.press('tab')
        pg.press('up', presses=3)

    pg.press('enter', presses=3)



    """---------------------------------------------------X----------------------------------------------------------"""

    """-------------------------------------------PlANE ANALYSIS MENU------------------------------------------------"""

    time.sleep(0.5)
    pg.typewrite(['esc'])   #in-case overwrite pops up

    time.sleep(1)
    fw1 = pg.getWindowsWithTitle("Plane analysis")

    fw1[0].size = (309, 871)  # Assures window is at the same place for all users
    fw1[0].topleft = (1615, 114)

    time.sleep(0.5)
    sequence_on = pg.locateOnScreen('sequence_on.PNG', region=(1400, 0, 400, 400))
    sequence_off = pg.locateOnScreen('sequence_off.PNG', region=(1400, 0, 400, 400))
    pg.press('enter')

    if (sequence_on is not None):

        for j in range(0,5):

            pg.hotkey('shift','tab')

        if (array_inputs[16] == 'y' or array_inputs[16] == 'Y'):

            for j in range(17,20):

                pg.press('tab')
                pg.typewrite(array_inputs[j])

            pg.press('tab',presses=2)
            pg.typewrite(['space'])

        if (array_inputs[16] == 'n' or array_inputs[16] == 'N'):

            pg.typewrite(['space'])
            pg.press('tab',presses=3)
            pg.typewrite(['space'])


    elif (sequence_off is not None):

        for j in range(0,3):

            pg.hotkey('shift','tab')

        if (array_inputs[16] == 'y' or array_inputs[16] == 'Y'):

            pg.typewrite(['space'])

            for j in range(17,20):

                pg.press('tab')
                pg.typewrite(array_inputs[j])

            pg.press('tab',presses=2)
            pg.typewrite(['space'])


        if (array_inputs[16] == 'n' or array_inputs[16] == 'N'):

            pg.press('tab',presses=3)
            pg.typewrite(['space'])


    time.sleep(5)


"""----------------------------------------------END OF FUNCTION-----------------------------------------------------"""

if(array_inputs[20]=='n'):

    stabilityanalysis()

elif(array_inputs[20]=='y'):

    for i in range(0, int(array_inputs[21])):

        time.sleep(1)
        pg.typewrite(['F7'])
        time.sleep(1)
        pg.press('up',presses=(int(array_inputs[21])+1))
        pg.press('down',presses=i)
        pg.typewrite(['enter'])
        pg.typewrite(['enter'])
        print("bye")
        stabilityanalysis()

