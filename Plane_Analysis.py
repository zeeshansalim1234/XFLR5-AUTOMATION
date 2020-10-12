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


def planeanalysis():

    time.sleep(5)
    pg.click(343, 58)  # ANALYSIS MENU BAR

    time.sleep(0.5)
    pg.click(441, 81)  # Define Analysis

    fw = pg.getWindowsWithTitle("Analysis Definition")

    fw[0].size = (767, 517)  # Assures window is placed at same location for all users
    fw[0].topleft = (568, 257)

    """--------------------------------------------------POLAR TYPE--------------------------------------------------"""

    time.sleep(0.1)
    pg.click(648,380)

    if (array_inputs[0] == '1'):

        time.sleep(0.1)
        pg.click(618, 419)  # Type 1

        time.sleep(0.1)
        pg.click(1224, 420, clicks=3)  # Enter Fixed Stream Speed
        pg.typewrite(array_inputs[1])
        pg.typewrite(["enter"])

        time.sleep(0.1)
        pg.click(1224, 487, clicks=3)  # Enter Beta
        pg.typewrite(array_inputs[3])
        pg.typewrite(["enter"])



    elif (array_inputs[0] == '2'):

        time.sleep(0.1)
        pg.click(618, 453)  # Type 2

        time.sleep(0.1)
        pg.click(1224, 487, clicks=3)  # Enter Beta
        pg.typewrite(array_inputs[3])
        pg.typewrite(["enter"])

    elif (array_inputs[0] == '4'):

        time.sleep(0.1)
        pg.click(618, 485)  # Type 4

        time.sleep(0.1)
        pg.click(1224, 454, clicks=3)  # Enter Alpha
        pg.typewrite(array_inputs[2])
        pg.typewrite(["enter"])

        time.sleep(0.1)
        pg.click(1224, 487, clicks=3)  # Enter Beta
        pg.typewrite(array_inputs[3])
        pg.typewrite(["enter"])


    elif (array_inputs[0] == '5'):

        time.sleep(0.1)
        pg.click(618, 517)  # Type 5

        time.sleep(0.1)
        pg.click(1224, 420, clicks=3)  # Enter Fixed Stream Speed
        pg.typewrite(array_inputs[1])
        pg.typewrite(["enter"])

        time.sleep(0.1)
        pg.click(1224, 454, clicks=3)  # Enter Alpha
        pg.typewrite(array_inputs[2])
        pg.typewrite(["enter"])

    """---------------------------------------------------X----------------------------------------------------------"""

    """------------------------------------------------ANALYSIS------------------------------------------------------"""

    time.sleep(0.5)
    pg.click(753, 380)  # analysis menu

    time.sleep(0.5)
    viscous_box = pg.locateOnScreen('viscous_checkbox.PNG')  # To ON or OFF viscous checkbox

    if (array_inputs[4] == "y" or array_inputs[4] == "Y"):

        if (viscous_box is None):                            # Check the box
            time.sleep(0.1)
            pg.click(631, 597)

    elif (array_inputs[4] == "n" or array_inputs[4] == "N"):

        if (viscous_box is not None):                        # Uncheck the box
            time.sleep(0.1)
            pg.click(631, 597)

    time.sleep(0.1)
    pg.click(635, 517)  # Choose Ring vortex(VLM2)

    """---------------------------------------------------X----------------------------------------------------------"""

    """------------------------------------------------INERTIA-------------------------------------------------------"""

    time.sleep(0.1)
    pg.click(843, 380)  # Inertia

    time.sleep(0.5)
    inertia_box = pg.locateOnScreen('inertia_checkbox.PNG')  # To ON or OFF inertia checkbox

    if (array_inputs[5] == 'y' or array_inputs[5] == 'Y'):

        if (inertia_box is None):                            # To ON checkbox

            time.sleep(0.1)
            pg.click(632, 449)

    elif (array_inputs[5] == 'n' or array_inputs[5] == 'N'):

        if (inertia_box is not None):                        # To OFF checkbox

            time.sleep(0.1)
            pg.click(632, 449)

        time.sleep(0.1)
        pg.click(1220, 477, clicks=3)  # Enter Plane Mass
        pg.typewrite(array_inputs[6])

        time.sleep(0.1)
        pg.click(1220, 517, clicks=3)  # Enter X_CoG
        pg.typewrite(array_inputs[7])

        time.sleep(0.1)
        pg.click(1220, 555, clicks=3)  # Enter Z_CoG
        pg.typewrite(array_inputs[8])

    """---------------------------------------------------X----------------------------------------------------------"""

    """---------------------------------------------REF. DIMENSIONS--------------------------------------------------"""

    time.sleep(0.1)                         # Ref Dimensions menu
    pg.click(950, 383)

    if(array_inputs[9] == '1'):

        time.sleep(0.1)
        pg.click(635, 451)                  # Wing platform

    elif(array_inputs[9] == '2'):

        time.sleep(0.1)
        pg.click(635,483)                   # Wing platform projected on XY plane

    elif(array_inputs[9] == '3'):

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
        pg.typewrite(array_inputs[12])

    """---------------------------------------------------X----------------------------------------------------------"""

    """------------------------------------------------AERO DATA-----------------------------------------------------"""

    time.sleep(0.1)                        # Aero data menu
    pg.click(1074,383)

    if(array_inputs[13]=="int"):

        time.sleep(0.1)                    # Choose international
        pg.click(673,452)

    elif(array_inputs[13]=="imp"):

        time.sleep(0.1)                    # Choose imperial
        pg.click(803,452)

    time.sleep(0.1)
    pg.click(786, 486, clicks=3)           # Enter rho
    pg.typewrite(array_inputs[14])

    time.sleep(0.1)
    pg.click(778, 519, clicks=3)           # Enter mu
    pg.typewrite(array_inputs[15])

    time.sleep(0.5)
    groundeffect_box = pg.locateOnScreen('groundeffect.PNG')  # To ON or OFF ground effect checkbox

    if (array_inputs[16] == 'y' or array_inputs[16] == 'Y'):

        if (groundeffect_box is None):      # To ON checkbox

            time.sleep(0.5)
            pg.click(982, 463)

        time.sleep(0.5)
        pg.click(1153,484,clicks=3)
        pg.typewrite(array_inputs[17])

    elif (array_inputs[16] == 'n' or array_inputs[16] == 'N'):

        if (groundeffect_box is not None):  # To OFF checkbox

            time.sleep(0.5)
            pg.click(982, 463)

    """---------------------------------------------------X----------------------------------------------------------"""

    """----------------------------------------------EXTRA DRAG------------------------------------------------------"""

    time.sleep(0.5)                         # Extra drag menu
    pg.click(1185,388)


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
        pg.typewrite(["enter"])

    """---------------------------------------------------X----------------------------------------------------------"""

    """-------------------------------------------PLANE ANALYSIS MENU------------------------------------------------"""

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
    pg.click(1775, 412)


"""-----------------------------------------------END OF FUNCTION----------------------------------------------------"""

planeanalysis()

file.close()
