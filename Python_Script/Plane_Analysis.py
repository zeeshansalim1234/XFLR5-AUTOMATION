import time, pyautogui as pg

"""------------------------------------------THIS MODULE IS FOR PLANE ANALYSIS---------------------------------------"""

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

    elif (countline>=212 and countline <=218 and countline %2 == 0):
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
    """
    pg.click(343, 58)  # ANALYSIS MENU BAR

    time.sleep(0.5)
    pg.click(441, 81)  # Define Analysis"""

    pg.hotkey('Fn','F6')

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

        """time.sleep(0.1)
        pg.click(618, 419)  # Type 1

        time.sleep(0.1)
        pg.click(1224, 420, clicks=3)  # Enter Fixed Stream Speed
        pg.typewrite(array_inputs[1])
        pg.typewrite(["enter"])

        time.sleep(0.1)
        pg.click(1224, 487, clicks=3)  # Enter Beta
        pg.typewrite(array_inputs[3])
        pg.typewrite(["enter"])"""



    elif (array_inputs[0] == '2'):

        pg.press('down')
        pg.typewrite(['space'])
        pg.press('tab')
        pg.typewrite(array_inputs[3])

        """time.sleep(0.1)
        pg.click(618, 453)  # Type 2

        time.sleep(0.1)
        pg.click(1224, 487, clicks=3)  # Enter Beta
        pg.typewrite(array_inputs[3])
        pg.typewrite(["enter"])"""

    elif (array_inputs[0] == '4'):

        pg.press('down',presses=2)
        pg.typewrite(['space'])
        pg.press('tab')
        pg.typewrite(array_inputs[2])
        pg.press('tab')
        pg.typewrite(array_inputs[3])

        """time.sleep(0.1)
        pg.click(618, 485)  # Type 4

        time.sleep(0.1)
        pg.click(1224, 454, clicks=3)  # Enter Alpha
        pg.typewrite(array_inputs[2])
        pg.typewrite(["enter"])

        time.sleep(0.1)
        pg.click(1224, 487, clicks=3)  # Enter Beta
        pg.typewrite(array_inputs[3])
        pg.typewrite(["enter"])"""


    elif (array_inputs[0] == '5'):

        pg.press('down', presses=3)
        pg.typewrite(['space'])
        pg.press('tab')
        pg.typewrite(array_inputs[1])
        pg.press('tab')
        pg.typewrite(array_inputs[2])

        """time.sleep(0.1)
        pg.click(618, 517)  # Type 5

        time.sleep(0.1)
        pg.click(1224, 420, clicks=3)  # Enter Fixed Stream Speed
        pg.typewrite(array_inputs[1])
        pg.typewrite(["enter"])

        time.sleep(0.1)
        pg.click(1224, 454, clicks=3)  # Enter Alpha
        pg.typewrite(array_inputs[2])
        pg.typewrite(["enter"])"""

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


    """time.sleep(0.1)
    pg.click(1220, 477, clicks=3)  # Enter Plane Mass
    pg.typewrite(array_inputs[6])

    time.sleep(0.1)
    pg.click(1220, 517, clicks=3)  # Enter X_CoG
    pg.typewrite(array_inputs[7])

    time.sleep(0.1)
    pg.click(1220, 555, clicks=3)  # Enter Z_CoG
    pg.typewrite(array_inputs[8])"""

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

        """
        time.sleep(0.1)
        pg.click(635,514)                  # User defined

        time.sleep(0.1)
        pg.click(1222, 549, clicks=3)      # Enter Ref area
        pg.typewrite(array_inputs[10])

        time.sleep(0.1)
        pg.click(1222, 583, clicks=3)      # Enter Ref span length
        pg.typewrite(array_inputs[11])

        time.sleep(0.1)
        pg.click(1222, 618, clicks=3)      # Enter Ref chord length
        pg.typewrite(array_inputs[12])"""

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


    """time.sleep(0.1)
    pg.click(786, 486, clicks=3)           # Enter rho
    pg.typewrite(array_inputs[14])

    time.sleep(0.1)
    pg.click(778, 519, clicks=3)           # Enter mu
    pg.typewrite(array_inputs[15])"""

    time.sleep(0.5)
    groundeffect_box = pg.locateOnScreen('groundeffect.PNG',region=(500,277,900,700))  # To ON or OFF ground effect checkbox

    pg.press('tab', presses=2)

    if (array_inputs[16] == 'y' or array_inputs[16] == 'Y'):


        if (groundeffect_box is None):      # To ON checkbox

            pg.typewrite(['space'])


        pg.press('tab')
        pg.typewrite(array_inputs[17])
        """time.sleep(0.5)
        pg.click(1153,484,clicks=3)
        pg.typewrite(array_inputs[17])"""

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

    pg.press('enter', presses=3)

    """
    for i in range(0,8):

         y=475

         if(i<4):                           # To Fill extra area

             x=1045

             time.sleep(0.1)
             pg.click(x,y+(45*(i)), clicks=3)
             pg.typewrite(array_inputs[18][i])
             pg.typewrite(["enter"])

         else:                              # To Fill extra drag coeff.

             x=1250

             time.sleep(0.1)
             pg.click(x, y+(45*(i-4)), clicks=3)
             pg.typewrite(array_inputs[19][i-4])
             pg.typewrite(["enter"])

    for i in range(0, 2):
        pg.typewrite(["enter"])"""

    """---------------------------------------------------X----------------------------------------------------------"""

    """-------------------------------------------PLANE ANALYSIS MENU------------------------------------------------"""

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


    """
    fw1 = pg.getWindowsWithTitle("Plane analysis")

    fw1[0].size = (309, 871)  # Assures window is at the same place for all users
    fw1[0].topleft = (1615, 114)

    time.sleep(0.5)
    sequence_box = pg.locateOnScreen('sequence_checkbox.PNG')  # To ON or OFF sequence checkbox

    if (array_inputs[20] == "y" or array_inputs[20] == "Y"):

        if (sequence_box is None):

            time.sleep(0.5)
            pg.click(1661, 217)

            time.sleep(0.5)
            pg.click(1803, 279, clicks=3)
            pg.typewrite(array_inputs[21])
            pg.typewrite(["enter"])

            time.sleep(0.5)
            pg.click(1803, 309, clicks=3)
            pg.typewrite(array_inputs[22])
            pg.typewrite(["enter"])

            time.sleep(0.5)
            pg.click(1803, 349, clicks=3)
            pg.typewrite(array_inputs[23])
            pg.typewrite(["enter"])


    elif (array_inputs[20] == "n" or array_inputs[20] == "N"):

        if (sequence_box is not None):

            time.sleep(0.5)
            pg.click(1661, 217)


    time.sleep(0.5)
    pg.click(1775, 412)"""


"""-----------------------------------------------END OF FUNCTION----------------------------------------------------"""

planeanalysis()

file.close()
