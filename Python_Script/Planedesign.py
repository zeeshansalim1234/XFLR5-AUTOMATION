import time,pyautogui as pg

fw = pg.getActiveWindow()      # object for accessing active windows

"""------------------------------------THIS IS THE MODULE FOR PLANE AND WING DESIGN----------------------------------"""

"""-----------------------------------------------READING TEXT FILE--------------------------------------------------"""

file=open("XFLR5inputs.txt","r")
f=file.readlines()

countline1=0
countline2=-1

array_inputs=[]
nacafoils_names=[]                              #import
loadedfoils_names=[]
num_nacafoils=[]
num_loadedfoils=[]


for line in f:

    countline1+=1

    if (countline1 == 4):
        num_nacafoils.append(line.strip())

    elif (countline1 == 10):
        num_loadedfoils.append(line.strip())

    elif (countline1 == 6):
        nacafoils_names.append(line.strip())     #Change when import starts working

    elif (countline1 == 14):
        loadedfoils_names.append(line.strip())

    elif(countline1>=81 and countline1<=101 and countline1%2!=0):
        array_inputs.append(line.strip())

    elif(countline1>=104 and countline1<=137):
        countline2+=1

        if(countline2%3==0):
            array_inputs.append(line.strip())

for i in range(11,22):

    array_inputs[i]= array_inputs[i].split(' ')         #For 2D array

"""-------------------------------------------------X----------------------------------------------------------------"""

""""----------------------------------------------IMPORT-------------------------------------------------------------"""

nacafoils_names=nacafoils_names[0].split(' ')
loadedfoils_names=loadedfoils_names[0].split(' ')

for i in range(0, len(nacafoils_names)):                         #Arranges all NACA foil names in ascending order
    for j in range(i+1, len(nacafoils_names)):
        if(nacafoils_names[i] > nacafoils_names[j]):
            temp = nacafoils_names[i];
            nacafoils_names[i] = nacafoils_names[j];
            nacafoils_names[j] = temp;

for i in range(0, len(loadedfoils_names)):                       #Arranges all loaded foil names in ascending order
    for j in range(i+1, len(loadedfoils_names)):
        if(loadedfoils_names[i] > loadedfoils_names[j]):
            temp = loadedfoils_names[i];
            loadedfoils_names[i] = loadedfoils_names[j];
            loadedfoils_names[j] = temp;

if(num_nacafoils[0]=='0'):
    ascending_all_foils=loadedfoils_names            # List that contains all foil names in Ascending order
elif(num_loadedfoils[0]=='0'):
    ascending_all_foils=nacafoils_names
else:
    ascending_all_foils=loadedfoils_names+nacafoils_names

"""----------------------------------------------------X-------------------------------------------------------------"""

print(array_inputs)
print(ascending_all_foils)

time.sleep(0.5)
pg.getWindowsWithTitle("xflr5 v6.47")[0].restore()


def planedesign():


    time.sleep(1)                    #Timer to switch to XFLR5 window
    pg.hotkey('ctrl','6')
    """
    pg.click(14, 51)                 #Files

    time.sleep(0.5)
    pg.click(249,409)                #Plane and Wing Design 

    time.sleep(0.5)
    pg.click(125,43)                 #Plane menu bar

    time.sleep(0.5)
    pg.click(220,82)                 #Define a new plane"""

    time.sleep(0.2)
    pg.hotkey('fn','F3')

    time.sleep(1)
    fw.size = (867, 928)             #To assure window is placed at same spot for everyone
    fw.topleft = (518, 51)

    time.sleep(0.5)
    pg.hotkey('ctrl','a')
    pg.typewrite(array_inputs[3])

    """pg.click(621,160,clicks=3)       #Naming Plane
    pg.typewrite(array_inputs[3])"""

    for l in range(0,20):

        pg.hotkey('shift','tab')

    pg.typewrite(['space'])

    """--------------------------------------CODE TO FILL MAIN WINGS DETAILS IN TABLE--------------------------------"""

    """time.sleep(0.5)
    pg.click(616,463)                #Main wing : Define"""

    time.sleep(1)
    pg.keyDown('alt')  # for full screen
    pg.press(' ')
    pg.press('x')
    pg.keyUp('alt')

    pg.press('tab',presses=6)

    for i in range(0,int(array_inputs[0])-2):
        pg.press('space')

    pg.press('tab',presses=3)
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')


    for m in range(11,11+int(array_inputs[0])):

        for n in range(0,10):

            pg.press('tab')
            pg.typewrite(array_inputs[m][n])

            if(n==5):

                b = [array_inputs[m][n]]
                index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]  # for selecting the desired foil

                pg.press('space')
                for p in range(0,index[0]+1):
                    pg.press('down')

                pg.press('enter')

            elif(n==7 or n==9):

                pg.press('space')

                for p in range(0,4):

                    pg.press('up')

                for p in range(0,int(array_inputs[m][n])):

                    pg.press('down')

                pg.press('enter')


    pg.press('enter',presses=3)             #save main wing table


    """-------------------------------------------------X------------------------------------------------------------"""

    """----------------------------------CODE TO FILL ELEVATOR DEATILS TABLE-----------------------------------------"""

    """time.sleep(0.5)
    pg.click(616,664)                #Elevator : Define"""

    time.sleep(0.5)
    pg.press('tab',presses=7)
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

    for m in range(15,15+int(array_inputs[1])):

        for n in range(0,10):

            pg.press('tab')
            pg.typewrite(array_inputs[m][n])

            if(n==5):

                b = [array_inputs[m][n]]
                index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]  # for selecting the desired foil
                print(index)

                pg.press('space')
                for p in range(0,index[0]+1):
                    pg.press('down')

                pg.press('enter')

            elif(n==7 or n==9):

                pg.press('space')

                for p in range(0,4):

                    pg.press('up')

                for p in range(0,int(array_inputs[m][n])):

                    pg.press('down')

                pg.press('enter')


    pg.press('enter',presses=3)             #save elevator table


    """------------------------------------------------X-------------------------------------------------------------"""

    """------------------------------------CODE TO FILL FIN DETAILS TABLE--------------------------------------------"""



    time.sleep(0.5)
    pg.press('tab',presses=5)
    pg.press('space')
    """pg.click(1014,664)                #Elevator : Define"""

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
                index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]  # for selecting the desired foil
                print(index)

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

    pg.press('enter', presses=3)  # save fin table


    """-------------------------------------END OF FILLING THE TABLE DETAILS-----------------------------------------"""

    """--------------------------------------------Plane inertia---------------------------------------------------- """

    time.sleep(0.5)
    for i in range(0,14):
        pg.hotkey('shift','tab')

    pg.press('space')

    """pg.click(737, 338)  # Plane Inertia"""

    iw = pg.getWindowsWithTitle('inertia properties')

    time.sleep(1)
    iw[0].size = (613, 825)  # makes sure window is on same position for all users
    iw[0].topleft = (658, 96)

    """-------------------------------------------------X------------------------------------------------------------"""

    """---------------------------------------------Main Wing--------------------------------------------------------"""

    time.sleep(0.5)
    for i in range(0,6):
        pg.hotkey('shift','tab')

    pg.press('space')

    iw1 = pg.getWindowsWithTitle('inertia properties for Main Wing')

    iw1[0].size = (613, 825)  # makes sure window is on same position for all users
    iw1[0].topleft = (658, 96)

    for i in range(0,4):
        pg.hotkey('shift','tab')

    time.sleep(0.5)
    pg.typewrite(array_inputs[4])
    pg.press('enter',presses=2)

    """pg.click(850, 260)  # Main Wing"""

    """time.sleep(0.5)
    pg.click(894, 291, clicks=3)  # Mass Main wing
    pg.typewrite(array_inputs[4])

    for i in range(0, 2):
        pg.typewrite(["enter"])"""

    """-------------------------------------------------X------------------------------------------------------------"""

    """----------------------------------------------Elevator--------------------------------------------------------"""

    time.sleep(0.5)
    pg.press('tab')
    pg.press('space')

    iw2 = pg.getWindowsWithTitle('inertia properties for Elevator')

    iw2[0].size = (613, 825)  # makes sure window is on same position for all users
    iw2[0].topleft = (658, 96)

    for i in range(0,4):
        pg.hotkey('shift','tab')

    time.sleep(0.5)
    pg.typewrite(array_inputs[5])
    pg.press('enter',presses=2)

    """pg.click(959, 307)  # Elevator


    time.sleep(0.5)
    pg.click(894, 291, clicks=3)  # Mass Elevator
    pg.typewrite(array_inputs[5])

    for i in range(0, 2):
        pg.typewrite(["enter"])"""

    """-------------------------------------------------X------------------------------------------------------------"""

    """------------------------------------------------FIN-----------------------------------------------------------"""

    time.sleep(0.5)
    pg.press('tab')
    pg.press('space')

    iw3 = pg.getWindowsWithTitle('inertia properties for Fin')

    iw3[0].size = (613, 825)  # makes sure window is on same position for all users
    iw3[0].topleft = (658, 96)

    for i in range(0,4):
        pg.hotkey('shift','tab')

    time.sleep(0.5)
    pg.typewrite(array_inputs[6])
    pg.press('enter',presses=2)

    for j in range(0,3):
        pg.hotkey('shift', 'tab')

    for i in range(0,3):
        pg.typewrite(['enter'])

    """
    pg.click(965, 357)  # Fin

    time.sleep(0.5)
    pg.click(894, 291, clicks=3)  # Mass Fin
    pg.typewrite(array_inputs[6])

    for i in range(0, 2):
        pg.typewrite(["enter"])

    pg.click(949, 872)  # save"""

    pg.press('tab',presses=9)

    for j in range(7,10):

        pg.press('tab')
        pg.typewrite(array_inputs[j])

    pg.press('tab',presses=5)
    pg.typewrite(array_inputs[10])

    pg.press('tab',presses=2)
    pg.typewrite(array_inputs[9])

    time.sleep(0.5)
    pg.press('enter',presses=2)

    """time.sleep(0.1)
    pg.click(1278, 665, clicks=3)  # Fin X
    pg.typewrite(array_inputs[10])
    pg.typewrite(["enter"])

    time.sleep(0.1)
    pg.click(1278, 769, clicks=3)  # Fin Tilt angle
    pg.typewrite(array_inputs[9])
    pg.typewrite(["enter"])

    time.sleep(0.5)
    pg.click(1174, 930)"""

    """
    time.sleep(0.1)
    pg.click(863, 663, clicks=3)  # elevator X
    pg.typewrite(array_inputs[7])
    pg.typewrite(["enter"])

    time.sleep(0.1)
    pg.click(864, 702, clicks=3)  # elevator Z
    pg.typewrite(array_inputs[8])
    pg.typewrite(["enter"])

    time.sleep(0.1)
    pg.click(864, 737, clicks=3)  # elevator tilt angle
    pg.typewrite(array_inputs[9])
    pg.typewrite(["enter"])"""

    """---------------------------------------------END OF FUNCTION--------------------------------------------------"""

planedesign()

file.close()

