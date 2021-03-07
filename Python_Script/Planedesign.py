import time, pyautogui as pg
from tkinter import *
from PIL import ImageTk, Image

fw = pg.getActiveWindow()  # object for accessing active windows

"""------------------------------------THIS IS THE MODULE FOR PLANE AND WING DESIGN----------------------------------"""

"""---------------------------------------------------GUI-----------------------------------------------------------"""

arr_gui = []


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
    arr_gui.append(twentythirdentry.get())

    print(arr_gui)

    f = open("XFLR5inputs.txt", "r")
    lines = f.readlines()

    x = 0

    for k in range(80, 101, 2):

        if (arr_gui[x] != ''):
            lines[k] = str(arr_gui[x]) + '\n'

        x += 1

    for k in range(103, 137, 3):

        if (arr_gui[x] != ''):
            lines[k] = str(arr_gui[x]) + '\n'

        x += 1

    f.close()

    lines = ''.join([str(elem) for elem in lines])

    f = open("XFLR5inputs.txt", "w")

    f.writelines(lines)
    f.close()


app = Tk()

app.geometry("1900x1500")

app.title("XFLR5 AUTOMATION")

app.configure(background="#F7F7F7")

heading = Label(text="CREATING PLANE", fg="white", bg="black", font="Helvetica 13 bold italic", width="500", height="3")

heading.pack()

img1 = ImageTk.PhotoImage(Image.open('university_logo.png'))
label = Label(image=img1, bg="#F7F7F7")
label.pack()
label.place(x=1700, y=820)

img2 = ImageTk.PhotoImage(Image.open('SAED_logo.jpg'))
label = Label(image=img2, bg="#F7F7F7")
label.pack()
label.place(x=1350, y=870)

img3 = ImageTk.PhotoImage(Image.open('create_plane_menu.PNG'))
label = Label(image=img3, bg="#F7F7F7")
label.pack()
label.place(x=1220, y=350)

img4 = ImageTk.PhotoImage(Image.open('mainwing_table.PNG'))
label = Label(image=img4, bg="#F7F7F7")
label.pack()
label.place(x=620, y=600)

firstentry_text = Label(text="Enter the number of columns required to fill Main Wing Details(2/3/4)")
secondentry_text = Label(text="Enter the number of columns required to fill Elevator Details(2/3/4):")
thirdentry_text = Label(text="Enter the number of columns required to fill Fin Details(2/3/4):")
fourthentry_text = Label(text="Enter a name for the Plane:")
fifthentry_text = Label(text="Enter Mass for Main Wing (Plane inertia menu):")
sixthentry_text = Label(text="Enter Mass for Elevator (Plane inertia menu):")
seventhentry_text = Label(text="Enter Mass for Fin  (Plane inertia menu):")
eighthentry_text = Label(text="Enter x for Elevator:")
ninthentry_text = Label(text="Enter z for Elevator:")
tenthentry_text = Label(text="Enter Tilt angle for Elevator:")
eleventhentry_text = Label(text="Enter x for Fin:")
twelvethentry_text = Label(text="Enter 10 parameters to fill Main Wing table column 1(keep spaces)")
thirteenthentry_text = Label(text="Enter 10 parameters to fill Main Wing table column 2(keep spaces)")
fourteenthentry_text = Label(text="Enter 10 parameters to fill Main Wing table column 3(keepspaces)")
fifteenthentry_text = Label(text="Enter 10 parameters to fill Main Wing table column 4(keepspaces)")
sixteenthentry_text = Label(text="Enter 10 parameters to fill Elevator table column 1(keepspaces)")
seventeenthentry_text = Label(text="Enter 10 parameters to fill Elevator table column 2(keepspaces)")
eighteenthentry_text = Label(text="Enter 10 parameters to fill Elevator table column 3(keepspaces)")
nineteenthentry_text = Label(text="Enter 10 parameters to fill Elevator table column 4(keepspaces)")
twenteethentry_text = Label(text="Enter 10 parameters to fill Fin table column 1(keepspaces)")
twentyonethentry_text = Label(text="Enter 10 parameters to fill Fin table column 2(keepspaces)")
twentysecondentry_text = Label(text="Enter 10 parameters to fill Fin table column 3(keepspaces)")
twentythirdentry_text = Label(text="Enter 10 parameters to fill Fin table column 4(keepspaces)")

firstentry_text.place(x=15, y=110)
secondentry_text.place(x=15, y=160)
thirdentry_text.place(x=15, y=210)
fourthentry_text.place(x=15, y=260)
fifthentry_text.place(x=15, y=310)
sixthentry_text.place(x=15, y=360)
seventhentry_text.place(x=15, y=410)
eighthentry_text.place(x=15, y=460)
ninthentry_text.place(x=15, y=510)
tenthentry_text.place(x=15, y=560)
eleventhentry_text.place(x=15, y=610)
twelvethentry_text.place(x=620, y=110)
thirteenthentry_text.place(x=620, y=160)
fourteenthentry_text.place(x=620, y=210)
fifteenthentry_text.place(x=620, y=260)
sixteenthentry_text.place(x=620, y=360)
seventeenthentry_text.place(x=620, y=410)
eighteenthentry_text.place(x=620, y=460)
nineteenthentry_text.place(x=620, y=510)
twenteethentry_text.place(x=1225, y=110)
twentyonethentry_text.place(x=1225, y=160)
twentysecondentry_text.place(x=1225, y=210)
twentythirdentry_text.place(x=1225, y=260)

firstentry = StringVar()
secondentry = StringVar()
thirdentry = StringVar()
fourthentry = StringVar()
fifthentry = StringVar()
sixthentry = StringVar()
seventhentry = StringVar()
eighthentry = StringVar()
ninthentry = StringVar()
tenthentry = StringVar()
eleventhentry = StringVar()
twelvethentry = StringVar()
thirteenthentry = StringVar()
fourteenthentry = StringVar()
fifteenthentry = StringVar()
sixteenthentry = StringVar()
seventeenthentry = StringVar()
eighteenthentry = StringVar()
nineteenthentry = StringVar()
twenteethentry = StringVar()
twentyonethentry = StringVar()
twentysecondentry = StringVar()
twentythirdentry = StringVar()

firstentry_enter = Entry(textvariable=firstentry, width="30")
secondentry_enter = Entry(textvariable=secondentry, width="30")
thirdentry_enter = Entry(textvariable=thirdentry, width="30")
fourthentry_enter = Entry(textvariable=fourthentry, width="30")
fifthentry_enter = Entry(textvariable=fifthentry, width="30")
sixthentry_enter = Entry(textvariable=sixthentry, width="30")
seventhentry_enter = Entry(textvariable=seventhentry, width="30")
eighthentry_enter = Entry(textvariable=eighthentry, width="30")
ninthentry_enter = Entry(textvariable=ninthentry, width="30")
tenthentry_enter = Entry(textvariable=tenthentry, width="30")
eleventhentry_enter = Entry(textvariable=eleventhentry, width="30")
twelvethentry_enter = Entry(textvariable=twelvethentry, width="30")
thirteenthentry_enter = Entry(textvariable=thirteenthentry, width="30")
fourteenthentry_enter = Entry(textvariable=fourteenthentry, width="30")
fifteenthentry_enter = Entry(textvariable=fifteenthentry, width="30")
sixteenthentry_enter = Entry(textvariable=sixteenthentry, width="30")
seventeenthentry_enter = Entry(textvariable=seventeenthentry, width="30")
eighteenthentry_enter = Entry(textvariable=eighteenthentry, width="30")
nineteenthentry_enter = Entry(textvariable=nineteenthentry, width="30")
twenteethentry_enter = Entry(textvariable=twenteethentry, width="30")
twentyonethentry_enter = Entry(textvariable=twentyonethentry, width="30")
twentysecondentry_enter = Entry(textvariable=twentysecondentry, width="30")
twentythirdentry_enter = Entry(textvariable=twentythirdentry, width="30")

firstentry_enter.place(x=15, y=140)
secondentry_enter.place(x=15, y=190)
thirdentry_enter.place(x=15, y=240)
fourthentry_enter.place(x=15, y=290)
fifthentry_enter.place(x=15, y=340)
sixthentry_enter.place(x=15, y=390)
seventhentry_enter.place(x=15, y=440)
eighthentry_enter.place(x=15, y=490)
ninthentry_enter.place(x=15, y=540)
tenthentry_enter.place(x=15, y=590)
eleventhentry_enter.place(x=15, y=640)
twelvethentry_enter.place(x=620, y=140)
thirteenthentry_enter.place(x=620, y=190)
fourteenthentry_enter.place(x=620, y=240)
fifteenthentry_enter.place(x=620, y=290)
sixteenthentry_enter.place(x=620, y=390)
seventeenthentry_enter.place(x=620, y=440)
eighteenthentry_enter.place(x=620, y=490)
nineteenthentry_enter.place(x=620, y=540)
twenteethentry_enter.place(x=1225, y=140)
twentyonethentry_enter.place(x=1225, y=190)
twentysecondentry_enter.place(x=1225, y=240)
twentythirdentry_enter.place(x=1225, y=290)

button1 = Button(app, text="Save", command=save_info, width="30", height="2", bg="orange")
button1.place(x=15, y=900)

mainloop()

"""-----------------------------------------------------X------------------------------------------------------------"""

"""-----------------------------------------------READING TEXT FILE--------------------------------------------------"""

file = open("XFLR5inputs.txt", "r")
f = file.readlines()

countline1 = 0
countline2 = -1

array_inputs = []
nacafoils_names = []  # import
loadedfoils_names = []
num_nacafoils = []
num_loadedfoils = []

for line in f:

    countline1 += 1

    if (countline1 == 4):
        num_nacafoils.append(line.strip())

    elif (countline1 == 10):
        num_loadedfoils.append(line.strip())

    elif (countline1 == 6):
        nacafoils_names.append(line.strip())  # Change when import starts working

    elif (countline1 == 14):
        loadedfoils_names.append(line.strip())

    elif (countline1 >= 81 and countline1 <= 101 and countline1 % 2 != 0):
        array_inputs.append(line.strip())

    elif (countline1 >= 104 and countline1 <= 137):
        countline2 += 1

        if (countline2 % 3 == 0):
            array_inputs.append(line.strip())

for i in range(11, 22):
    array_inputs[i] = array_inputs[i].split(' ')  # For 2D array

"""-------------------------------------------------X----------------------------------------------------------------"""

""""----------------------------------------------IMPORT-------------------------------------------------------------"""

nacafoils_names = nacafoils_names[0].split(' ')
loadedfoils_names = loadedfoils_names[0].split(' ')

for i in range(0, len(nacafoils_names)):  # Arranges all NACA foil names in ascending order
    for j in range(i + 1, len(nacafoils_names)):
        if (nacafoils_names[i] > nacafoils_names[j]):
            temp = nacafoils_names[i];
            nacafoils_names[i] = nacafoils_names[j];
            nacafoils_names[j] = temp;

for i in range(0, len(loadedfoils_names)):  # Arranges all loaded foil names in ascending order
    for j in range(i + 1, len(loadedfoils_names)):
        if (loadedfoils_names[i] > loadedfoils_names[j]):
            temp = loadedfoils_names[i];
            loadedfoils_names[i] = loadedfoils_names[j];
            loadedfoils_names[j] = temp;

if (num_nacafoils[0] == '0'):
    ascending_all_foils = loadedfoils_names  # List that contains all foil names in Ascending order
elif (num_loadedfoils[0] == '0'):
    ascending_all_foils = nacafoils_names
else:
    ascending_all_foils = loadedfoils_names + nacafoils_names

"""----------------------------------------------------X-------------------------------------------------------------"""

print(array_inputs)
print(ascending_all_foils)

time.sleep(0.5)
pg.getWindowsWithTitle("xflr5 v6.47")[0].restore()


def planedesign():
    time.sleep(1)  # Timer to switch to XFLR5 window
    pg.hotkey('ctrl', '6')

    time.sleep(0.2)
    pg.hotkey('fn', 'F3')

    time.sleep(1)
    fw.size = (867, 928)  # To assure window is placed at same spot for everyone
    fw.topleft = (518, 51)

    time.sleep(0.5)
    pg.hotkey('ctrl', 'a')
    pg.typewrite(array_inputs[3])

    for l in range(0, 20):
        pg.hotkey('shift', 'tab')

    pg.typewrite(['space'])

    """--------------------------------------CODE TO FILL MAIN WINGS DETAILS IN TABLE--------------------------------"""

    time.sleep(1)
    pg.keyDown('alt')  # for full screen
    pg.press(' ')
    pg.press('x')
    pg.keyUp('alt')

    pg.press('tab', presses=6)

    for i in range(0, int(array_inputs[0]) - 2):
        pg.press('space')

    pg.press('tab', presses=3)
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')

    for m in range(11, 11 + int(array_inputs[0])):

        for n in range(0, 10):

            pg.press('tab')
            pg.typewrite(array_inputs[m][n])

            if (n == 5):

                b = [array_inputs[m][n]]
                index = [i for i, item in enumerate(ascending_all_foils) if
                         item in set(b)]  # for selecting the desired foil

                pg.press('space')
                for p in range(0, index[0] + 1):
                    pg.press('down')

                pg.press('enter')

            elif (n == 7 or n == 9):

                pg.press('space')

                for p in range(0, 4):
                    pg.press('up')

                for p in range(0, int(array_inputs[m][n])):
                    pg.press('down')

                pg.press('enter')

    for k in range(0, 3):  # save main wing table

        time.sleep(0.1)
        pg.press('enter')

    """-------------------------------------------------X------------------------------------------------------------"""

    """----------------------------------CODE TO FILL ELEVATOR DEATILS TABLE-----------------------------------------"""

    time.sleep(0.5)
    pg.press('tab', presses=7)
    pg.press('space')

    pg.keyDown('alt')  # for full screen
    pg.press(' ')
    pg.press('x')
    pg.keyUp('alt')

    pg.press('tab', presses=6)

    for i in range(0, int(array_inputs[1]) - 2):
        pg.press('space')

    pg.press('tab', presses=3)
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')

    for m in range(15, 15 + int(array_inputs[1])):

        for n in range(0, 10):

            pg.press('tab')
            pg.typewrite(array_inputs[m][n])

            if (n == 5):

                b = [array_inputs[m][n]]
                index = [i for i, item in enumerate(ascending_all_foils) if
                         item in set(b)]  # for selecting the desired foil

                pg.press('space')
                for p in range(0, index[0] + 1):
                    pg.press('down')

                pg.press('enter')

            elif (n == 7 or n == 9):

                pg.press('space')

                for p in range(0, 4):
                    pg.press('up')

                for p in range(0, int(array_inputs[m][n])):
                    pg.press('down')

                pg.press('enter')

    for k in range(0, 3):
        time.sleep(0.1)
        pg.press('enter')  # save elevator table

    """------------------------------------------------X-------------------------------------------------------------"""

    """------------------------------------CODE TO FILL FIN DETAILS TABLE--------------------------------------------"""

    time.sleep(0.5)
    pg.press('tab', presses=5)
    pg.press('space')

    time.sleep(1)
    pg.keyDown('alt')  # for full screen
    pg.press(' ')
    pg.press('x')
    pg.keyUp('alt')

    pg.press('tab', presses=6)

    for i in range(0, int(array_inputs[2]) - 2):
        pg.press('space')

    pg.press('tab', presses=3)
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')

    for m in range(19, 19 + int(array_inputs[2])):

        for n in range(0, 10):

            pg.press('tab')
            pg.typewrite(array_inputs[m][n])

            if (n == 5):

                b = [array_inputs[m][n]]
                index = [i for i, item in enumerate(ascending_all_foils) if
                         item in set(b)]  # for selecting the desired foil

                pg.press('space')
                for p in range(0, index[0] + 1):
                    pg.press('down')

                pg.press('enter')

            elif (n == 7 or n == 9):

                pg.press('space')

                for p in range(0, 4):
                    pg.press('up')

                for p in range(0, int(array_inputs[m][n])):
                    pg.press('down')

                pg.press('enter')

    for j in range(0, 3):  # save Fin table

        time.sleep(0.1)
        pg.press('enter')

    """-------------------------------------END OF FILLING THE TABLE DETAILS-----------------------------------------"""

    """--------------------------------------------Plane inertia---------------------------------------------------- """

    time.sleep(0.2)
    for i in range(0, 14):
        pg.hotkey('shift', 'tab')

    pg.press('space')

    time.sleep(0.5)
    iw = pg.getWindowsWithTitle('inertia properties')

    iw[0].size = (613, 825)  # makes sure window is on same position for all users
    iw[0].topleft = (658, 96)

    """-------------------------------------------------X------------------------------------------------------------"""

    """---------------------------------------------Main Wing--------------------------------------------------------"""

    time.sleep(0.2)
    for i in range(0, 6):
        pg.hotkey('shift', 'tab')

    pg.press('space')

    time.sleep(0.5)
    iw1 = pg.getWindowsWithTitle('inertia properties for Main Wing')

    iw1[0].size = (613, 825)  # makes sure window is on same position for all users
    iw1[0].topleft = (658, 96)

    for i in range(0, 4):
        pg.hotkey('shift', 'tab')

    pg.typewrite(array_inputs[4])
    pg.press('enter', presses=2)

    """-------------------------------------------------X------------------------------------------------------------"""

    """----------------------------------------------Elevator--------------------------------------------------------"""

    time.sleep(0.2)
    pg.press('tab')
    pg.press('space')

    time.sleep(0.5)
    iw2 = pg.getWindowsWithTitle('inertia properties for Elevator')

    iw2[0].size = (613, 825)  # makes sure window is on same position for all users
    iw2[0].topleft = (658, 96)

    for i in range(0, 4):
        pg.hotkey('shift', 'tab')

    pg.typewrite(array_inputs[5])
    pg.press('enter', presses=2)

    """-------------------------------------------------X------------------------------------------------------------"""

    """------------------------------------------------FIN-----------------------------------------------------------"""

    time.sleep(0.2)
    pg.press('tab')
    pg.press('space')

    time.sleep(0.5)
    iw3 = pg.getWindowsWithTitle('inertia properties for Fin')

    iw3[0].size = (613, 825)  # makes sure window is on same position for all users
    iw3[0].topleft = (658, 96)

    for i in range(0, 4):
        pg.hotkey('shift', 'tab')

    pg.typewrite(array_inputs[6])
    pg.press('enter', presses=2)

    for j in range(0, 3):
        pg.hotkey('shift', 'tab')

    for i in range(0, 3):
        pg.typewrite(['enter'])

    pg.press('tab', presses=9)

    for j in range(7, 10):
        pg.press('tab')
        pg.typewrite(array_inputs[j])

    pg.press('tab', presses=5)
    pg.typewrite(array_inputs[10])

    pg.press('tab', presses=2)
    pg.typewrite(array_inputs[9])

    pg.press('enter', presses=3)

    for i in range(0, 3):
        time.sleep(0.2)
        pg.press('enter')

    """---------------------------------------------END OF FUNCTION--------------------------------------------------"""


planedesign()

file.close()
