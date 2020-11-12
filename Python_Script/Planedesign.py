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

    time.sleep(0.2)
    pg.hotkey('fn','F3')

    time.sleep(1)
    fw.size = (867, 928)             #To assure window is placed at same spot for everyone
    fw.topleft = (518, 51)

    time.sleep(0.5)
    pg.hotkey('ctrl','a')
    pg.typewrite(array_inputs[3])


    for l in range(0,20):

        pg.hotkey('shift','tab')

    pg.typewrite(['space'])

    """--------------------------------------CODE TO FILL MAIN WINGS DETAILS IN TABLE--------------------------------"""


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



    for k in range(0,3):            #save main wing table

        time.sleep(0.1)
        pg.press('enter')


    """-------------------------------------------------X------------------------------------------------------------"""

    """----------------------------------CODE TO FILL ELEVATOR DEATILS TABLE-----------------------------------------"""


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

    for k in range(0, 3):

        time.sleep(0.1)
        pg.press('enter')             #save elevator table


    """------------------------------------------------X-------------------------------------------------------------"""

    """------------------------------------CODE TO FILL FIN DETAILS TABLE--------------------------------------------"""



    time.sleep(0.5)
    pg.press('tab',presses=5)
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
                index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]  # for selecting the desired foil

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

    time.sleep(0.5)
    for i in range(0,14):
        pg.hotkey('shift','tab')

    pg.press('space')


    time.sleep(1)
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

    time.sleep(1)
    iw1 = pg.getWindowsWithTitle('inertia properties for Main Wing')

    iw1[0].size = (613, 825)  # makes sure window is on same position for all users
    iw1[0].topleft = (658, 96)

    for i in range(0,4):
        pg.hotkey('shift','tab')

    time.sleep(0.5)
    pg.typewrite(array_inputs[4])
    pg.press('enter',presses=2)


    """-------------------------------------------------X------------------------------------------------------------"""

    """----------------------------------------------Elevator--------------------------------------------------------"""

    time.sleep(0.5)
    pg.press('tab')
    pg.press('space')

    time.sleep(1)
    iw2 = pg.getWindowsWithTitle('inertia properties for Elevator')

    iw2[0].size = (613, 825)  # makes sure window is on same position for all users
    iw2[0].topleft = (658, 96)

    for i in range(0,4):
        pg.hotkey('shift','tab')

    time.sleep(0.5)
    pg.typewrite(array_inputs[5])
    pg.press('enter',presses=2)


    """-------------------------------------------------X------------------------------------------------------------"""

    """------------------------------------------------FIN-----------------------------------------------------------"""

    time.sleep(0.5)
    pg.press('tab')
    pg.press('space')

    time.sleep(1)
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


    pg.press('tab',presses=9)

    for j in range(7,10):

        pg.press('tab')
        pg.typewrite(array_inputs[j])

    pg.press('tab',presses=5)
    pg.typewrite(array_inputs[10])

    pg.press('tab',presses=2)
    pg.typewrite(array_inputs[9])

    pg.press('enter', presses=3)

    for i in range(0, 3):

        time.sleep(0.2)
        pg.press('enter')


    """---------------------------------------------END OF FUNCTION--------------------------------------------------"""

planedesign()

file.close()
