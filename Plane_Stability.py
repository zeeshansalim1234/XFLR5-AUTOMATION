import time,pyautogui as pg

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

    elif (countline==253 or countline==256 or countline==259):
        array_inputs.append(line.strip())

    elif (countline>=261 and countline <=265 and countline %2 != 0):
        array_inputs.append(line.strip())

    elif (countline==268 or countline==271):
        array_inputs.append(line.strip())

for i in range(8,16):

    if(i!=11 and i!=12 and i!=13):

        array_inputs[i]=array_inputs[i].split(' ')

"""---------------------------------------------------X--------------------------------------------------------------"""

print("INPUTS:")
print(array_inputs)

def stabilityanalysis():

    time.sleep(5)                   # Analysis menu bar
    pg.click(335,44)

    time.sleep(0.5)                 # Stabilty analysis
    pg.click(464,145)

    fw=pg.getWindowsWithTitle('Stability Polar Definition')
    fw[0].size=(775,540)
    fw[0].topleft=(564,245)

    """-------------------------------------------------ANALYSIS-----------------------------------------------------"""

    time.sleep(0.5)                  # Click left arrow twice
    pg.click(1275,366,clicks=2)

    time.sleep(0.1)                  # Click Analysis menu bar
    pg.click(634,368)

    time.sleep(0.5)
    viscous_analysis_box=pg.locateOnScreen('viscousanalysis_checkbox.PNG')

    if (array_inputs[0] == "y" or array_inputs[0] == "Y"):

        if (viscous_analysis_box is None):                            # Check the box

            time.sleep(0.1)
            pg.click(613, 517)

    elif (array_inputs[0] == "n" or array_inputs[0] == "N"):

        if (viscous_analysis_box is not None):                        # Uncheck the box

            time.sleep(0.1)
            pg.click(613, 517)

    time.sleep(0.1)
    pg.click(748, 615, clicks=3)                                   # Enter Beta
    pg.typewrite(array_inputs[1])
    pg.typewrite(["enter"])

    time.sleep(0.1)
    pg.click(748, 646, clicks=3)                                   # Enter Phi
    pg.typewrite(array_inputs[2])
    pg.typewrite(["enter"])

    """---------------------------------------------------X----------------------------------------------------------"""

    """----------------------------------------------REF. DIMENSIONS-------------------------------------------------"""

    time.sleep(0.1)                             # Ref Dimensions menu
    pg.click(754, 366)

    if (array_inputs[3] == '1'):

        time.sleep(0.1)
        pg.click(635, 451)                      # Wing platform

    elif (array_inputs[3] == '2'):

        time.sleep(0.1)
        pg.click(635, 483)                      # Wing platform projected on XY plane

    elif (array_inputs[3] == '3'):

        time.sleep(0.1)
        pg.click(635, 514)                     # Manual input

        time.sleep(0.1)
        pg.click(1222, 549, clicks=3)          # Enter Ref area
        pg.typewrite(array_inputs[4])

        time.sleep(0.1)
        pg.click(1222, 583, clicks=3)          # Enter Ref span length
        pg.typewrite(array_inputs[5])

        time.sleep(0.1)
        pg.click(1222, 618, clicks=3)          # Enter Ref chord length
        pg.typewrite(array_inputs[6])

    """---------------------------------------------------X----------------------------------------------------------"""

    """---------------------------------------------MASS AND INERTIA-------------------------------------------------"""

    time.sleep(0.1)                         # Mass and Inertia menu
    pg.click(920, 365)

    useplaneinertia_box= pg.locateOnScreen('useplaneinertia_checkbox.PNG')

    if (array_inputs[7] == "y" or array_inputs[7] == "Y"):

        if (useplaneinertia_box is None):                            # Check the box

            time.sleep(0.1)
            pg.click(613, 517)

    elif (array_inputs[7] == "n" or array_inputs[7] == "N"):

        if (useplaneinertia_box is not None):                        # Uncheck the box

            time.sleep(0.1)
            pg.click(613, 517)

    for i in range(0,14):


        if(i<4):

            x = 920
            y = 480

            time.sleep(0.1)
            pg.click(x, y + (45 * (i)), clicks=2)
            pg.typewrite(array_inputs[8][i])
            pg.typewrite(["enter"])

        elif(i<7):

            pg.typewrite(["down"])
            pg.typewrite(array_inputs[i])
            pg.typewrite(["enter"])

        elif(i<14):

            if (i == 7):

                pg.typewrite(["right"])
                pg.typewrite(array_inputs[9][i - 7])
                pg.typewrite(["enter"])

            else:

                pg.typewrite(["up"])
                pg.typewrite(array_inputs[9][i - 7])
                pg.typewrite(["enter"])

    """---------------------------------------------------X----------------------------------------------------------"""

    """--------------------------------------------CONTROL PARAMETERS------------------------------------------------"""

    time.sleep(0.1)
    pg.click(1058,367)                  # Control parameters menu

    time.sleep(0.1)
    pg.click(1267,452, clicks=3)        # Wing tilt
    pg.typewrite(array_inputs[10][0])
    pg.typewrite(["enter"])

    time.sleep(0.1)
    pg.click(1267, 500, clicks=3)       #Elevator tilt
    pg.typewrite(array_inputs[10][1])
    pg.typewrite(["enter"])

    """---------------------------------------------------X----------------------------------------------------------"""

    """-----------------------------------------------AERO DATA------------------------------------------------------"""

    time.sleep(0.1)
    pg.click(1211, 378)                 # Aero data menu

    if(array_inputs[11]=="int"):

        time.sleep(0.1)                 # International radio button
        pg.click(669,439)

    elif(array_inputs[11]=="imp"):

        time.sleep(0.1)                 # Imperial radio button
        pg.click(799, 440)

    time.sleep(0.1)
    pg.click(964, 475, clicks=3)       # Enter Rho
    pg.typewrite(array_inputs[12])

    time.sleep(0.1)
    pg.click(957, 505, clicks=3)       # Enter Mu
    pg.typewrite(array_inputs[13])

    """---------------------------------------------------X----------------------------------------------------------"""

    """-----------------------------------------------EXTRA DRAG-----------------------------------------------------"""

    time.sleep(0.1)                   # Click right arrow
    pg.click(1296,368)

    time.sleep(0.1)                   # Extra drag menu
    pg.click(1211,362)

    for i in range(0,8):

         y=475

         if(i<4):                      # To Fill extra area

             x=1045

             time.sleep(0.1)
             pg.click(x,y+(45*(i)), clicks=3)
             pg.typewrite(array_inputs[14][i])
             pg.typewrite(["enter"])

         else:                          # To Fill extra drag coeff.

             x=1250

             time.sleep(0.1)
             pg.click(x, y+(45*(i-4)), clicks=3)
             pg.typewrite(array_inputs[14][i-4])
             pg.typewrite(["enter"])

    for i in range(0, 2):
        pg.typewrite(["enter"])

    time.sleep(0.5)                         # Save
    pg.click(1137, 742)

    """---------------------------------------------------X----------------------------------------------------------"""

    """-------------------------------------------PlANE ANALYSIS MENU------------------------------------------------"""

    time.sleep(0.5)
    sequence_locator = pg.locateOnScreen('sequence_checkbox.PNG')

    if(sequence_locator is not None):

        time.sleep(0.5)
        pg.click(1661, 217)

    time.sleep(0.5)                  # Analyze
    pg.click(1767, 415)


"""----------------------------------------------END OF FUNCTION-----------------------------------------------------"""

stabilityanalysis()