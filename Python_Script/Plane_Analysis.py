import time,pyautogui as pg
from tkinter import *
from PIL import ImageTk,Image


"""------------------------------------------THIS MODULE IS FOR PLANE ANALYSIS---------------------------------------"""


"""-------------------------------------------------------GUI--------------------------------------------------------"""

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
    arr_gui.append(twentythirdentry.get())
    arr_gui.append(twentyfourthentry.get())
    arr_gui.append(twentyfifthentry.get())
    arr_gui.append(twentysixthentry.get())



    print(arr_gui)

    f = open("XFLR5inputs.txt", "r")
    lines = f.readlines()

    x=0

    for k in range(169,204,2):

        if (arr_gui[x] != ''):
            lines[k] =str(arr_gui[x])+'\n'

        x+=1

    for k in range(206,210,3):

        if (arr_gui[x] != ''):
            lines[k] =str(arr_gui[x])+'\n'

        x+=1

    for k in range(211, 222, 2):

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

heading = Label(text="FLIGHT ANALYSIS",fg="white",bg="black",font="Helvetica 13 bold italic",width="500",height="3")

heading.pack()


img1 = ImageTk.PhotoImage(Image.open('university_logo.png'))
label=Label(image=img1,bg="#F7F7F7")
label.pack()
label.place(x=1700,y=820)

img2 = ImageTk.PhotoImage(Image.open('SAED_logo.jpg'))
label=Label(image=img2,bg="#F7F7F7")
label.pack()
label.place(x=1350,y=870)

img3 = ImageTk.PhotoImage(Image.open('plane_analysis_menu1.PNG'))
label=Label(image=img3,bg="#F7F7F7")
label.pack()
label.place(x=1005,y=110)

img4 = ImageTk.PhotoImage(Image.open('plane_analysis_menu2.PNG'))
label=Label(image=img4,bg="#F7F7F7")
label.pack()
label.place(x=1375,y=110)

img5 = ImageTk.PhotoImage(Image.open('plane_analysis_menu3.PNG'))
label=Label(image=img5,bg="#F7F7F7")
label.pack()
label.place(x=1005,y=370)

img6 = ImageTk.PhotoImage(Image.open('plane_analysis_menu4.PNG'))
label=Label(image=img6,bg="#F7F7F7")
label.pack()
label.place(x=1375,y=370)

img7 = ImageTk.PhotoImage(Image.open('plane_analysis_menu5.PNG'))
label=Label(image=img7,bg="#F7F7F7")
label.pack()
label.place(x=1005,y=630)

img8 = ImageTk.PhotoImage(Image.open('plane_analysis_menu6.PNG'))
label=Label(image=img8,bg="#F7F7F7")
label.pack()
label.place(x=1375,y=630)

firstentry_text = Label(text="Choose Type of analysis?")
secondentry_text = Label(text="Enter Free Stream Speed:(Option depends on your choosen Type)")
thirdentry_text = Label(text="Enter alpha:(Option depends on your choosen Type)")
fourthentry_text =Label(text="Enter beta:(Option depends on your choosen Type)")
fifthentry_text =Label(text="Viscous Check box ON in analysis menu (y or n)?")
sixthentry_text = Label(text="Plane Inertia checkbox ON in inerta menu (y or n)?")
seventhentry_text = Label(text="Enter Plane mass(kg):")
eighthentry_text = Label(text="Enter X_CoG(m):")
ninthentry_text = Label(text="Enter Z_CoG(m):")
tenthentry_text = Label(text="Select Wing Platform projected on xy plane ")
eleventhentry_text = Label(text="Enter Ref. area (Only if you chose User defined):")
twelvethentry_text = Label(text="Enter Ref. span length (Only if you chose User defined):")
thirteenthentry_text = Label(text="Enter Ref. cord length (Only if you chose User defined)")
fourteenthentry_text = Label(text="Choose international or imperial for Air Data menu(enter int or imp):")
fifteenthentry_text= Label(text="Enter value of Rho (kg/m^3):")
sixteenthentry_text= Label(text="Enter value of Mu in scientific notation (ex: 1.5e-5):")
seventeenthentry_text= Label(text="Ground effect checkbox ON in aero data menu (y or n)?")
eighteenthentry_text= Label(text="Enter height (if chose ON):")
nineteenthentry_text= Label(text="Enter Extra Area(m^2) for Extra drag table")
twenteethentry_text= Label(text="Enter Extra drag coeff. for EXtra drag table")
twentyonethentry_text= Label(text="Sequence ON or OFF(y/n)?")
twentysecondentry_text= Label(text="Enter Start value:")
twentythirdentry_text= Label(text="Enter End value:")
twentyfourthentry_text= Label(text="Enter increment value:")
twentyfifthentry_text= Label(text="Run analysis on ALL planes?(y/n)",fg="red")
twentysixthentry_text= Label(text="Enter number of planes currently loaded on XFLR5:",fg="red")

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
seventeenthentry_text.place(x=560,y=210)
eighteenthentry_text.place(x=560,y=260)
nineteenthentry_text.place(x=560,y=310)
twenteethentry_text.place(x=560,y=360)
twentyonethentry_text.place(x=560,y=460)
twentysecondentry_text.place(x=560,y=510)
twentythirdentry_text.place(x=560,y=560)
twentyfourthentry_text.place(x=560,y=610)
twentyfifthentry_text.place(x=560,y=710)
twentysixthentry_text.place(x=560,y=760)



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
twentythirdentry=StringVar()
twentyfourthentry=StringVar()
twentyfifthentry=StringVar()
twentysixthentry=StringVar()



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
twentythirdentry_enter= Entry(textvariable=twentythirdentry,width="30")
twentyfourthentry_enter= Entry(textvariable=twentyfourthentry,width="30")
twentyfifthentry_enter= Entry(textvariable=twentyfifthentry,width="30")
twentysixthentry_enter= Entry(textvariable=twentysixthentry,width="30")


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
seventeenthentry_enter.place(x=560,y=240)
eighteenthentry_enter.place(x=560,y=290)
nineteenthentry_enter.place(x=560,y=340)
twenteethentry_enter.place(x=560,y=390)
twentyonethentry_enter.place(x=560,y=490)
twentysecondentry_enter.place(x=560,y=540)
twentythirdentry_enter.place(x=560,y=590)
twentyfourthentry_enter.place(x=560,y=640)
twentyfifthentry_enter.place(x=560,y=740)
twentysixthentry_enter.place(x=560,y=790)


button1 = Button(app,text="Save",command=save_info,width="30",height="2",bg="orange")
button1.place(x=15,y=900)


mainloop()



"""----------------------------------------------------------X-------------------------------------------------------"""



"""-----------------------------------------------READING FROM TEXT FILE---------------------------------------------"""

countline = 0
array_inputs = []

file = open("XFLR5inputs.txt", "r")
f = file.readlines()

for line in f:

    countline += 1
    if (countline >= 170 and countline <= 204 and countline % 2 == 0):
        array_inputs.append(line.strip())

    elif (countline==207 or countline==210):
        array_inputs.append(line.strip())

    elif (countline>=212 and countline <=222 and countline %2 == 0):
        array_inputs.append(line.strip())

for i in range(18,20):
    array_inputs[i]=array_inputs[i].split(' ')

"""------------------------------------------------------X-----------------------------------------------------------"""

print("INPUTS:")
print(array_inputs)
time.sleep(0.5)
pg.getWindowsWithTitle("xflr5 v6.47")[0].restore()


def planeanalysis():


    time.sleep(1)


    pg.press('F6')

    time.sleep(0.2)
    fw = pg.getWindowsWithTitle("Analysis Definition")

    fw[0].size = (767, 517)  # Assures window is placed at same location for all users
    fw[0].topleft = (568, 257)

    """--------------------------------------------------POLAR TYPE--------------------------------------------------"""

    pg.press('enter')
    pg.press('tab',presses=3)

    if (array_inputs[0] == '1'):

        pg.typewrite(['space'])
        pg.press('tab')
        pg.typewrite(array_inputs[1])
        pg.press('tab')
        pg.typewrite(array_inputs[3])



    elif (array_inputs[0] == '2'):

        pg.press('down')
        pg.typewrite(['space'])
        pg.press('tab')
        pg.typewrite(array_inputs[3])


    elif (array_inputs[0] == '4'):

        pg.press('down',presses=2)
        pg.typewrite(['space'])
        pg.press('tab')
        pg.typewrite(array_inputs[2])
        pg.press('tab')
        pg.typewrite(array_inputs[3])



    elif (array_inputs[0] == '5'):

        pg.press('down', presses=3)
        pg.typewrite(['space'])
        pg.press('tab')
        pg.typewrite(array_inputs[1])
        pg.press('tab')
        pg.typewrite(array_inputs[2])


    pg.press('tab',presses=4)


    """---------------------------------------------------X----------------------------------------------------------"""

    """------------------------------------------------ANALYSIS------------------------------------------------------"""

    time.sleep(0.5)
    pg.press('right')

    time.sleep(0.5)
    viscous_box = pg.locateOnScreen('viscous_checkbox.PNG',region=(500,257,700,500))  # To ON or OFF viscous checkbox

    pg.press('tab')
    pg.press('down')
    pg.press('tab')

    if (array_inputs[4] == "y" or array_inputs[4] == "Y"):

        if (viscous_box is None):                            # Check the box

            pg.press('space')

    elif (array_inputs[4] == "n" or array_inputs[4] == "N"):

        if (viscous_box is not None):                        # Uncheck the box

            pg.press('space')

    pg.press('tab',presses=5)


    """---------------------------------------------------X----------------------------------------------------------"""

    """------------------------------------------------INERTIA-------------------------------------------------------"""

    time.sleep(0.1)
    pg.press('right')

    time.sleep(0.5)
    inertia_box = pg.locateOnScreen('inertia_checkbox.PNG' ,region=(500,257,700,500))  # To ON or OFF inertia checkbox

    pg.press('tab')

    if (array_inputs[5] == 'y' or array_inputs[5] == 'Y'):

        if (inertia_box is None):                            # To ON checkbox

            pg.typewrite(['space'])

    elif (array_inputs[5] == 'n' or array_inputs[5] == 'N'):

        if (inertia_box is not None):                        # To OFF checkbox

            pg.typewrite(['space'])

        for j in range(6,9):

            pg.press('tab')
            pg.typewrite(array_inputs[j])

    pg.press('tab',presses=4)


    """---------------------------------------------------X----------------------------------------------------------"""

    """---------------------------------------------REF. DIMENSIONS--------------------------------------------------"""

    time.sleep(0.1)                         # Ref Dimensions menu
    pg.press('right')
    pg.press('tab')

    if(array_inputs[9] == '1'):

        pg.typewrite(['space'])             # Wing platform

    elif(array_inputs[9] == '2'):

        pg.press('down')                    # Wing platform projected on XY plane
        pg.typewrite(['space'])

    elif(array_inputs[9] == '3'):

        pg.press('down',presses=2)  # Wing platform projected on XY plane
        pg.typewrite(['space'])

        for j in range(10,13):

            pg.press('tab')
            pg.typewrite(array_inputs[j])


    pg.press('tab',presses=4)


    """---------------------------------------------------X----------------------------------------------------------"""

    """------------------------------------------------AERO DATA-----------------------------------------------------"""

    time.sleep(0.1)                        # Aero data menu
    pg.press('right')
    pg.press('tab')

    if(array_inputs[13]=="int"):

        pg.press('left')                   # Choose international

    elif(array_inputs[13]=="imp"):

        pg.press('right')                  # Choose imperial

    for j in range(14,16):

        pg.press('tab')
        pg.typewrite(array_inputs[j])


    time.sleep(0.5)
    groundeffect_box = pg.locateOnScreen('groundeffect.PNG',region=(500,277,900,700))  # To ON or OFF ground effect checkbox

    pg.press('tab', presses=2)

    if (array_inputs[16] == 'y' or array_inputs[16] == 'Y'):


        if (groundeffect_box is None):      # To ON checkbox

            pg.typewrite(['space'])


        pg.press('tab')
        pg.typewrite(array_inputs[17])


    elif (array_inputs[16] == 'n' or array_inputs[16] == 'N'):


        if (groundeffect_box is not None):  # To OFF checkbox


            pg.typewrite(['space'])

    pg.press('tab',presses=4)


    """---------------------------------------------------X----------------------------------------------------------"""

    """----------------------------------------------EXTRA DRAG------------------------------------------------------"""

    time.sleep(0.5)                         # Extra drag menu
    pg.press('right')

    pg.press('tab', presses=2)

    for k in range(18, 20):

        for j in range(0, 4):

            if (j == 0):

                pg.typewrite(array_inputs[k][j])

            else:

                pg.press('down')
                pg.typewrite(array_inputs[k][j])

        pg.press('tab')
        pg.press('up', presses=3)

    pg.typewrite(['enter'])
    pg.typewrite(['enter'])
    pg.typewrite(['enter'])


    """---------------------------------------------------X----------------------------------------------------------"""

    """-------------------------------------------PLANE ANALYSIS MENU------------------------------------------------"""

    time.sleep(0.5)
    pg.typewrite(['esc'])  # in-case overwrite pops up

    time.sleep(1)
    fw1 = pg.getWindowsWithTitle("Plane analysis")

    fw1[0].size = (309, 871)  # Assures window is at the same place for all users
    fw1[0].topleft = (1615, 114)

    time.sleep(0.5)
    sequence_on = pg.locateOnScreen('sequence_on.PNG', region=(1400, 0, 400, 400))
    sequence_off = pg.locateOnScreen('sequence_off.PNG', region=(1400, 0, 400, 400))
    pg.press('enter')

    if (sequence_on is not None):

        for j in range(0, 5):
            pg.hotkey('shift', 'tab')

        if (array_inputs[20] == 'y' or array_inputs[20] == 'Y'):

            for j in range(21, 24):
                pg.press('tab')
                pg.typewrite(array_inputs[j])

            pg.press('tab', presses=2)
            pg.typewrite(['space'])

        if (array_inputs[20] == 'n' or array_inputs[20] == 'N'):
            pg.typewrite(['space'])
            pg.press('tab', presses=3)
            pg.typewrite(['space'])


    elif (sequence_off is not None):

        for j in range(0, 3):
            pg.hotkey('shift', 'tab')

        if (array_inputs[20] == 'y' or array_inputs[20] == 'Y'):

            pg.typewrite(['space'])

            for j in range(21, 24):
                pg.press('tab')
                pg.typewrite(array_inputs[j])

            pg.press('tab', presses=2)
            pg.typewrite(['space'])

        if (array_inputs[20] == 'n' or array_inputs[20] == 'N'):
            pg.press('tab', presses=3)
            pg.typewrite(['space'])

    time.sleep(5)

"""-----------------------------------------------END OF FUNCTION----------------------------------------------------"""


if(array_inputs[24]=='n'):

    planeanalysis()

elif(array_inputs[24]=='y'):

    for i in range(0, int(array_inputs[25])):

        time.sleep(1)
        pg.press('F7')
        time.sleep(1)
        pg.press('up',presses=(int(array_inputs[25])+1))
        pg.press('down',presses=i)
        pg.typewrite(['enter'])
        pg.typewrite(['enter'])
        planeanalysis()


file.close()
