import time, pyautogui as pg

"""---------------------------------------THIS MODULE IS FOR STABILITY ANALYSIS--------------------------------------"""

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

    elif (countline >= 273 and countline <= 279 and countline % 2 != 0):
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
    pg.press('enter', presses=2)
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


"""----------------------------------------------END OF FUNCTION-----------------------------------------------------"""

stabilityanalysis()
