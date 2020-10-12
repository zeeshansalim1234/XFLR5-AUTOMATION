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

for line in f:

    countline1+=1

    if (countline1 == 6):
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

ascending_all_foils=loadedfoils_names+nacafoils_names

"""----------------------------------------------------X-------------------------------------------------------------"""

print(array_inputs)
print(ascending_all_foils)

def planedesign():


    time.sleep(5)                    #Timer to switch to XFLR5 window
    pg.click(14, 51)                 #Files

    time.sleep(0.5)
    pg.click(249,409)                #Plane and Wing Design

    time.sleep(0.5)
    pg.click(125,43)                 #Plane menu bar

    time.sleep(0.5)
    pg.click(220,82)                 #Define a new plane

    fw.size = (867, 928)             #To assure window is placed at same spot for everyone
    fw.topleft = (518, 51)

    time.sleep(0.5)
    pg.click(621,160,clicks=3)       #Naming Plane
    pg.typewrite(array_inputs[3])

    """--------------------------------------CODE TO FILL MAIN WINGS DETAILS IN TABLE--------------------------------"""

    time.sleep(0.5)
    pg.click(616,463)                #Main wing : Define

    time.sleep(1)
    pg.keyDown('alt')  # for full screen
    pg.press(' ')
    pg.press('x')
    pg.keyUp('alt')

    outercounter=1
    y=230

    numsection_wing=int(array_inputs[0])

    for i in range(0,numsection_wing):

        x=115                               #x-coordinate of main wing 1st table box
        innercounter=1

        if(outercounter==1):

            for j in range(0,10):             #Loop for filling Main wing details

                if(innercounter!=6 or innercounter!=8 or innercounter!=10):
                    if(innercounter==7):
                        x+=115
                    time.sleep(0.05)
                    pg.click(x,y)

                if (innercounter== 1):                     #To enter y_mainwing
                    pg.typewrite(array_inputs[11][0])
                    pg.typewrite(["enter"])

                elif(innercounter==2):                      #To enter Chord_mainwing
                    pg.typewrite(array_inputs[11][1])
                    pg.typewrite(["enter"])

                elif(innercounter==3):                      #To enter offset
                    pg.typewrite(array_inputs[11][2])
                    pg.typewrite(["enter"])

                elif(innercounter==4):                       #To enter  dihedral
                    pg.typewrite(array_inputs[11][3])
                    pg.typewrite(["enter"])

                elif(innercounter==5):                        #To enter twist
                    pg.typewrite(array_inputs[11][4])
                    pg.typewrite(["enter"])

                elif (innercounter == 6):                     #To choose the foil from drop box
                    time.sleep(0.1)
                    pg.click(x,y,clicks=2)
                    for i in range(0,4):
                        pg.typewrite(['up'])

                    b = [array_inputs[11][5]]
                    index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]

                    for i in range(0, index[0]):
                        pg.typewrite(["down"])

                    pg.typewrite(["enter"])

                    pg.typewrite(["enter"])

                elif (innercounter == 7):                     #Enter X-panel
                    pg.typewrite(array_inputs[11][6])
                    pg.typewrite(["enter"])

                elif (innercounter == 8):                     #To choose X-dist from drop box
                    time.sleep(0.1)
                    pg.click(x,y,clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if(array_inputs[11][7]=='1'):
                        pg.typewrite(["enter"])
                    elif(array_inputs[11][7]=='2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])

                elif (innercounter == 9):                     #To enter Y-panel
                    pg.typewrite(array_inputs[11][8])
                    pg.typewrite(["enter"])

                elif (innercounter == 10):                     #To choose Y-dist from drop box
                    time.sleep(0.1)
                    pg.click(x,y,clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if(array_inputs[11][9]=='1'):
                        pg.typewrite(["enter"])
                    elif(array_inputs[11][9]=='2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])
                    elif(array_inputs[11][9]=='3'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])
                    elif(array_inputs[11][9]=='4'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])

                x += 115
                innercounter += 1



        elif(outercounter==2):

            for j in range(0, 10):  # Loop for filling Main wing details

                if (innercounter != 6 or innercounter != 8 or innercounter != 10):
                    if (innercounter == 7):
                        x += 115
                    time.sleep(0.05)
                    pg.click(x, y)

                if (innercounter== 1):  # To enter y_mainwing
                    pg.typewrite(array_inputs[12][0])
                    pg.typewrite(["enter"])

                elif (innercounter== 2):  # To enter Chord_mainwing
                    pg.typewrite(array_inputs[12][1])
                    pg.typewrite(["enter"])

                elif (innercounter== 3):  # To enter offset
                    pg.typewrite(array_inputs[12][2])
                    pg.typewrite(["enter"])

                elif (innercounter== 4):  # To enter  dihedral
                    pg.typewrite(array_inputs[12][3])
                    pg.typewrite(["enter"])

                elif (innercounter== 5):  # To enter twist
                    pg.typewrite(array_inputs[12][4])
                    pg.typewrite(["enter"])

                elif (innercounter == 6):                     #To choose the foil from drop box

                    time.sleep(0.1)
                    pg.click(x,y,clicks=2)
                    for i in range(0, 5):
                        pg.typewrite(['up'])

                    b=[array_inputs[12][5]]
                    index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]

                    for i in range(0,index[0]):

                        pg.typewrite(["down"])

                    pg.typewrite(["enter"])
                    pg.typewrite(["enter"])

                elif (innercounter == 7):  # Enter X-panel
                    pg.typewrite(array_inputs[12][6])
                    pg.typewrite(["enter"])

                elif (innercounter == 8):  # To choose X-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[12][7] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[12][7] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])

                elif (innercounter == 9):  # To enter Y-panel
                    pg.typewrite(array_inputs[12][8])
                    pg.typewrite(["enter"])

                elif (innercounter == 10):  # To choose Y-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[12][9] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[12][9] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])
                    elif (array_inputs[12][9] == '3'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])
                    elif (array_inputs[12][9] == '4'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])

                x += 115
                innercounter += 1


        elif (outercounter == 3):

            time.sleep(0.1)
            pg.click(1137,139)     #To add another column

            for j in range(0, 10):  # Loop for filling Main wing details

                if (innercounter != 6 or innercounter != 8 or innercounter != 10):
                    if (innercounter == 7):
                        x += 115
                    time.sleep(0.05)
                    pg.click(x, y)

                if (innercounter== 1):  # To enter y_mainwing
                    pg.typewrite(array_inputs[13][0])
                    pg.typewrite(["enter"])

                elif (innercounter== 2):  # To enter Chord_mainwing
                    pg.typewrite(array_inputs[13][1])
                    pg.typewrite(["enter"])

                elif (innercounter== 3):  # To enter offset
                    pg.typewrite(array_inputs[13][2])
                    pg.typewrite(["enter"])

                elif (innercounter== 4):  # To enter  dihedral
                    pg.typewrite(array_inputs[13][3])
                    pg.typewrite(["enter"])

                elif (innercounter== 5):  # To enter twist
                    pg.typewrite(array_inputs[13][4])
                    pg.typewrite(["enter"])

                elif (innercounter == 6):  # To choose the foil from drop box

                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 5):
                        pg.typewrite(['up'])

                    b=[array_inputs[13][5]]
                    index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]

                    for i in range(0,index[0]):

                        pg.typewrite(["down"])

                    pg.typewrite(["enter"])
                    pg.typewrite(["enter"])


                elif (innercounter == 7):  # Enter X-panel
                    pg.typewrite(array_inputs[13][6])
                    pg.typewrite(["enter"])

                elif (innercounter == 8):  # To choose X-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[13][7] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[13][7] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])

                elif (innercounter == 9):  # To enter Y-panel
                    pg.typewrite(array_inputs[13][8])
                    pg.typewrite(["enter"])

                elif (innercounter == 10):  # To choose Y-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[13][9] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[13][9] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])
                    elif (array_inputs[13][9] == '3'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])
                    elif (array_inputs[13][9] == '4'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])

                x += 115
                innercounter+=1

        elif (outercounter == 4):

            time.sleep(0.1)
            pg.click(1137, 139)  # To add another column

            for j in range(0, 10):  # Loop for filling Main wing details

                if (innercounter != 6 or innercounter != 8 or innercounter != 10):
                    if (innercounter == 7):
                        x += 115
                    time.sleep(0.05)
                    pg.click(x, y)

                if (innercounter== 1):  # To enter y_mainwing
                    pg.typewrite(array_inputs[14][0])
                    pg.typewrite(["enter"])

                elif (innercounter== 2):  # To enter Chord_mainwing
                    pg.typewrite(array_inputs[14][1])
                    pg.typewrite(["enter"])

                elif (innercounter== 3):  # To enter offset
                    pg.typewrite(array_inputs[14][2])
                    pg.typewrite(["enter"])

                elif (innercounter== 4):  # To enter  dihedral
                    pg.typewrite(array_inputs[14][3])
                    pg.typewrite(["enter"])

                elif (innercounter== 5):  # To enter twist
                    pg.typewrite(array_inputs[14][4])
                    pg.typewrite(["enter"])

                elif (innercounter == 6):  # To choose the foil from drop box

                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    b = [array_inputs[14][5]]
                    index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]

                    for i in range(0, index[0]):
                        pg.typewrite(["down"])

                    pg.typewrite(["enter"])

                    pg.typewrite(["enter"])

                elif (innercounter == 7):  # Enter X-panel
                    pg.typewrite(array_inputs[14][6])
                    pg.typewrite(["enter"])

                elif (innercounter == 8):  # To choose X-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[14][7] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[14][7] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])

                elif (innercounter == 9):  # To enter Y-panel
                    pg.typewrite(array_inputs[14][8])
                    pg.typewrite(["enter"])

                elif (innercounter == 10):  # To choose Y-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[14][9] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[14][9] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])
                    elif (array_inputs[14][9] == '3'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])
                    elif (array_inputs[14][9] == '4'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])

                x += 115
                innercounter+= 1

        outercounter+=1
        y+=50

    time.sleep(0.5)
    pg.typewrite(["enter"])
    pg.click(1701, 962)

    """-------------------------------------------------X------------------------------------------------------------"""

    """----------------------------------CODE TO FILL ELEVATOR DEATILS TABLE-----------------------------------------"""

    time.sleep(0.5)
    pg.click(616,664)                #Elevator : Define

    pg.keyDown('alt')  # for full screen
    pg.press(' ')
    pg.press('x')
    pg.keyUp('alt')

    outercounter=1
    y=230

    numsection_elevator=int(array_inputs[1])

    for i in range(0,numsection_elevator):

        x=115                               #x-coordinate of main wing 1st table box
        innercounter=1

        if(outercounter==1):

            for j in range(0,10):             #Loop for filling Main wing details

                if(innercounter!=6 or innercounter!=8 or innercounter!=10):
                    if(innercounter==7):
                        x+=115
                    time.sleep(0.05)
                    pg.click(x,y)

                if (innercounter== 1):                     #To enter y_mainwing
                    pg.typewrite(array_inputs[15][0])
                    pg.typewrite(["enter"])

                elif(innercounter==2):                      #To enter Chord_mainwing
                    pg.typewrite(array_inputs[15][1])
                    pg.typewrite(["enter"])

                elif(innercounter==3):                      #To enter offset
                    pg.typewrite(array_inputs[15][2])
                    pg.typewrite(["enter"])

                elif(innercounter==4):                       #To enter  dihedral
                    pg.typewrite(array_inputs[15][3])
                    pg.typewrite(["enter"])

                elif(innercounter==5):                        #To enter twist
                    pg.typewrite(array_inputs[15][4])
                    pg.typewrite(["enter"])

                elif (innercounter == 6):                     #To choose the foil from drop box
                    time.sleep(0.1)
                    pg.click(x,y,clicks=2)
                    for i in range(0,4):
                        pg.typewrite(['up'])

                    b = [array_inputs[15][5]]
                    index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]

                    for i in range(0, index[0]):
                        pg.typewrite(["down"])

                    pg.typewrite(["enter"])

                    pg.typewrite(["enter"])

                elif (innercounter == 7):                     #Enter X-panel
                    pg.typewrite(array_inputs[15][6])
                    pg.typewrite(["enter"])

                elif (innercounter == 8):                     #To choose X-dist from drop box
                    time.sleep(0.1)
                    pg.click(x,y,clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if(array_inputs[15][7]=='1'):
                        pg.typewrite(["enter"])
                    elif(array_inputs[15][7]=='2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])

                elif (innercounter == 9):                     #To enter Y-panel
                    pg.typewrite(array_inputs[15][8])
                    pg.typewrite(["enter"])

                elif (innercounter == 10):                     #To choose Y-dist from drop box
                    time.sleep(0.1)
                    pg.click(x,y,clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if(array_inputs[15][9]=='1'):
                        pg.typewrite(["enter"])
                    elif(array_inputs[15][9]=='2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])
                    elif(array_inputs[15][9]=='3'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])
                    elif(array_inputs[15][9]=='4'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])

                x += 115
                innercounter += 1



        elif(outercounter==2):

            for j in range(0, 10):  # Loop for filling Main wing details

                if (innercounter != 6 or innercounter != 8 or innercounter != 10):
                    if (innercounter == 7):
                        x += 115
                    time.sleep(0.05)
                    pg.click(x, y)

                if (innercounter== 1):  # To enter y_mainwing
                    pg.typewrite(array_inputs[16][0])
                    pg.typewrite(["enter"])

                elif (innercounter== 2):  # To enter Chord_mainwing
                    pg.typewrite(array_inputs[16][1])
                    pg.typewrite(["enter"])

                elif (innercounter== 3):  # To enter offset
                    pg.typewrite(array_inputs[16][2])
                    pg.typewrite(["enter"])

                elif (innercounter== 4):  # To enter  dihedral
                    pg.typewrite(array_inputs[16][3])
                    pg.typewrite(["enter"])

                elif (innercounter== 5):  # To enter twist
                    pg.typewrite(array_inputs[16][4])
                    pg.typewrite(["enter"])

                elif (innercounter == 6):                     #To choose the foil from drop box

                    time.sleep(0.1)
                    pg.click(x,y,clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    b = [array_inputs[16][5]]
                    index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]

                    for i in range(0, index[0]):
                        pg.typewrite(["down"])

                    pg.typewrite(["enter"])

                    pg.typewrite(["enter"])

                elif (innercounter == 7):  # Enter X-panel
                    pg.typewrite(array_inputs[16][6])
                    pg.typewrite(["enter"])

                elif (innercounter == 8):  # To choose X-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[16][7] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[16][7] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])

                elif (innercounter == 9):  # To enter Y-panel
                    pg.typewrite(array_inputs[16][8])
                    pg.typewrite(["enter"])

                elif (innercounter == 10):  # To choose Y-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[16][9] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[16][9] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])
                    elif (array_inputs[16][9] == '3'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])
                    elif (array_inputs[16][9] == '4'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])

                x += 115
                innercounter += 1


        elif (outercounter == 3):

            time.sleep(0.1)
            pg.click(1137,139)     #To add another column

            for j in range(0, 10):  # Loop for filling Main wing details

                if (innercounter != 6 or innercounter != 8 or innercounter != 10):
                    if (innercounter == 7):
                        x += 115
                    time.sleep(0.05)
                    pg.click(x, y)

                if (innercounter== 1):  # To enter y_mainwing
                    pg.typewrite(array_inputs[17][0])
                    pg.typewrite(["enter"])

                elif (innercounter== 2):  # To enter Chord_mainwing
                    pg.typewrite(array_inputs[17][1])
                    pg.typewrite(["enter"])

                elif (innercounter== 3):  # To enter offset
                    pg.typewrite(array_inputs[17][2])
                    pg.typewrite(["enter"])

                elif (innercounter== 4):  # To enter  dihedral
                    pg.typewrite(array_inputs[17][3])
                    pg.typewrite(["enter"])

                elif (innercounter== 5):  # To enter twist
                    pg.typewrite(array_inputs[17][4])
                    pg.typewrite(["enter"])

                elif (innercounter == 6):  # To choose the foil from drop box

                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    b = [array_inputs[17][5]]
                    index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]

                    for i in range(0, index[0]):
                        pg.typewrite(["down"])

                    pg.typewrite(["enter"])

                    pg.typewrite(["enter"])

                elif (innercounter == 7):  # Enter X-panel
                    pg.typewrite(array_inputs[17][6])
                    pg.typewrite(["enter"])

                elif (innercounter == 8):  # To choose X-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[17][7] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[17][7] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])

                elif (innercounter == 9):  # To enter Y-panel
                    pg.typewrite(array_inputs[17][8])
                    pg.typewrite(["enter"])

                elif (innercounter == 10):  # To choose Y-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[17][9] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[17][9] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])
                    elif (array_inputs[17][9] == '3'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])
                    elif (array_inputs[17][9] == '4'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])

                x += 115
                innercounter+=1

        elif (outercounter == 4):

            time.sleep(0.1)
            pg.click(1137, 139)  # To add another column

            for j in range(0, 10):  # Loop for filling Main wing details

                if (innercounter != 6 or innercounter != 8 or innercounter != 10):
                    if (innercounter == 7):
                        x += 115
                    time.sleep(0.05)
                    pg.click(x, y)

                if (innercounter== 1):  # To enter y_mainwing
                    pg.typewrite(array_inputs[18][0])
                    pg.typewrite(["enter"])

                elif (innercounter== 2):  # To enter Chord_mainwing
                    pg.typewrite(array_inputs[18][1])
                    pg.typewrite(["enter"])

                elif (innercounter== 3):  # To enter offset
                    pg.typewrite(array_inputs[18][2])
                    pg.typewrite(["enter"])

                elif (innercounter== 4):  # To enter  dihedral
                    pg.typewrite(array_inputs[18][3])
                    pg.typewrite(["enter"])

                elif (innercounter== 5):  # To enter twist
                    pg.typewrite(array_inputs[18][4])
                    pg.typewrite(["enter"])

                elif (innercounter == 6):  # To choose the foil from drop box

                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    b = [array_inputs[18][5]]
                    index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]

                    for i in range(0, index[0]):
                        pg.typewrite(["down"])

                    pg.typewrite(["enter"])

                    pg.typewrite(["enter"])

                elif (innercounter == 7):  # Enter X-panel
                    pg.typewrite(array_inputs[18][6])
                    pg.typewrite(["enter"])

                elif (innercounter == 8):  # To choose X-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[18][7] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[18][7] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])

                elif (innercounter == 9):  # To enter Y-panel
                    pg.typewrite(array_inputs[18][8])
                    pg.typewrite(["enter"])

                elif (innercounter == 10):  # To choose Y-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[18][9] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[18][9] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])
                    elif (array_inputs[18][9] == '3'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])
                    elif (array_inputs[18][9] == '4'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])

                x += 115
                innercounter+= 1

        outercounter+=1
        y+=50
    time.sleep(0.5)
    pg.click(1701,962)

    """------------------------------------------------X-------------------------------------------------------------"""

    """------------------------------------CODE TO FILL FIN DETAILS TABLE--------------------------------------------"""



    time.sleep(0.5)
    pg.click(1014,664)                #Elevator : Define

    time.sleep(1)
    pg.keyDown('alt')  # for full screen
    pg.press(' ')
    pg.press('x')
    pg.keyUp('alt')

    outercounter=1
    y=230

    numsection_fin=int(array_inputs[2])

    for i in range(0,numsection_fin):

        x=115                               #x-coordinate of main wing 1st table box
        innercounter=1

        if(outercounter==1):

            for j in range(0,10):             #Loop for filling Main wing details

                if(innercounter!=6 or innercounter!=8 or innercounter!=10):
                    if(innercounter==7):
                        x+=115
                    time.sleep(0.05)
                    pg.click(x,y)

                if (innercounter== 1):                     #To enter y_mainwing
                    pg.typewrite(array_inputs[19][0])
                    pg.typewrite(["enter"])

                elif(innercounter==2):                      #To enter Chord_mainwing
                    pg.typewrite(array_inputs[19][1])
                    pg.typewrite(["enter"])

                elif(innercounter==3):                      #To enter offset
                    pg.typewrite(array_inputs[19][2])
                    pg.typewrite(["enter"])

                elif(innercounter==4):                       #To enter  dihedral
                    pg.typewrite(array_inputs[19][3])
                    pg.typewrite(["enter"])

                elif(innercounter==5):                        #To enter twist
                    pg.typewrite(array_inputs[19][4])
                    pg.typewrite(["enter"])

                elif (innercounter == 6):                     #To choose the foil from drop box
                    time.sleep(0.1)
                    pg.click(x,y,clicks=2)
                    for i in range(0,4):
                        pg.typewrite(['up'])

                    b = [array_inputs[19][5]]
                    index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]

                    for i in range(0, index[0]):
                        pg.typewrite(["down"])

                    pg.typewrite(["enter"])

                    pg.typewrite(["enter"])

                elif (innercounter == 7):                     #Enter X-panel
                    pg.typewrite(array_inputs[19][6])
                    pg.typewrite(["enter"])

                elif (innercounter == 8):                     #To choose X-dist from drop box
                    time.sleep(0.1)
                    pg.click(x,y,clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if(array_inputs[19][7]=='1'):
                        pg.typewrite(["enter"])
                    elif(array_inputs[19][7]=='2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])

                elif (innercounter == 9):                     #To enter Y-panel
                    pg.typewrite(array_inputs[19][8])
                    pg.typewrite(["enter"])

                elif (innercounter == 10):                     #To choose Y-dist from drop box
                    time.sleep(0.1)
                    pg.click(x,y,clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if(array_inputs[19][9]=='1'):
                        pg.typewrite(["enter"])
                    elif(array_inputs[19][9]=='2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])
                    elif(array_inputs[19][9]=='3'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])
                    elif(array_inputs[19][9]=='4'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])

                x += 115
                innercounter += 1



        elif(outercounter==2):

            for j in range(0, 10):  # Loop for filling Main wing details

                if (innercounter != 6 or innercounter != 8 or innercounter != 10):
                    if (innercounter == 7):
                        x += 115
                    time.sleep(0.05)
                    pg.click(x, y)

                if (innercounter== 1):  # To enter y_mainwing
                    pg.typewrite(array_inputs[20][0])
                    pg.typewrite(["enter"])

                elif (innercounter== 2):  # To enter Chord_mainwing
                    pg.typewrite(array_inputs[20][1])
                    pg.typewrite(["enter"])

                elif (innercounter== 3):  # To enter offset
                    pg.typewrite(array_inputs[20][2])
                    pg.typewrite(["enter"])

                elif (innercounter== 4):  # To enter  dihedral
                    pg.typewrite(array_inputs[20][3])
                    pg.typewrite(["enter"])

                elif (innercounter== 5):  # To enter twist
                    pg.typewrite(array_inputs[20][4])
                    pg.typewrite(["enter"])

                elif (innercounter == 6):                     #To choose the foil from drop box

                    time.sleep(0.1)
                    pg.click(x,y,clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    b = [array_inputs[20][5]]
                    index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]

                    for i in range(0, index[0]):
                        pg.typewrite(["down"])

                    pg.typewrite(["enter"])

                    pg.typewrite(["enter"])

                elif (innercounter == 7):  # Enter X-panel
                    pg.typewrite(array_inputs[20][6])
                    pg.typewrite(["enter"])

                elif (innercounter == 8):  # To choose X-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[20][7] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[20][7] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])

                elif (innercounter == 9):  # To enter Y-panel
                    pg.typewrite(array_inputs[20][8])
                    pg.typewrite(["enter"])

                elif (innercounter == 10):  # To choose Y-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[20][9] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[20][9] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])
                    elif (array_inputs[20][9] == '3'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])
                    elif (array_inputs[20][9] == '4'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])

                x += 115
                innercounter += 1


        elif (outercounter == 3):

            time.sleep(0.1)
            pg.click(1137,139)     #To add another column

            for j in range(0, 10):  # Loop for filling Main wing details

                if (innercounter != 6 or innercounter != 8 or innercounter != 10):
                    if (innercounter == 7):
                        x += 115
                    time.sleep(0.05)
                    pg.click(x, y)

                if (innercounter== 1):  # To enter y_mainwing
                    pg.typewrite(array_inputs[21][0])
                    pg.typewrite(["enter"])

                elif (innercounter== 2):  # To enter Chord_mainwing
                    pg.typewrite(array_inputs[21][1])
                    pg.typewrite(["enter"])

                elif (innercounter== 3):  # To enter offset
                    pg.typewrite(array_inputs[21][2])
                    pg.typewrite(["enter"])

                elif (innercounter== 4):  # To enter  dihedral
                    pg.typewrite(array_inputs[21][3])
                    pg.typewrite(["enter"])

                elif (innercounter== 5):  # To enter twist
                    pg.typewrite(array_inputs[21][4])
                    pg.typewrite(["enter"])

                elif (innercounter == 6):  # To choose the foil from drop box

                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    b = [array_inputs[21][5]]
                    index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]

                    for i in range(0, index[0]):
                        pg.typewrite(["down"])

                    pg.typewrite(["enter"])

                    pg.typewrite(["enter"])

                elif (innercounter == 7):  # Enter X-panel
                    pg.typewrite(array_inputs[21][6])
                    pg.typewrite(["enter"])

                elif (innercounter == 8):  # To choose X-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[21][7] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[21][7] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])

                elif (innercounter == 9):  # To enter Y-panel
                    pg.typewrite(array_inputs[21][8])
                    pg.typewrite(["enter"])

                elif (innercounter == 10):  # To choose Y-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[21][9] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[21][9] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])
                    elif (array_inputs[21][9] == '3'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])
                    elif (array_inputs[21][9] == '4'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])

                x += 115
                innercounter+=1

        elif (outercounter == 4):

            time.sleep(0.1)
            pg.click(1137, 139)  # To add another column

            for j in range(0, 10):  # Loop for filling Main wing details

                if (innercounter != 6 or innercounter != 8 or innercounter != 10):
                    if (innercounter == 7):
                        x += 115
                    time.sleep(0.05)
                    pg.click(x, y)

                if (innercounter== 1):  # To enter y_mainwing
                    pg.typewrite(array_inputs[22][0])
                    pg.typewrite(["enter"])

                elif (innercounter== 2):  # To enter Chord_mainwing
                    pg.typewrite(array_inputs[22][1])
                    pg.typewrite(["enter"])

                elif (innercounter== 3):  # To enter offset
                    pg.typewrite(array_inputs[22][2])
                    pg.typewrite(["enter"])

                elif (innercounter== 4):  # To enter  dihedral
                    pg.typewrite(array_inputs[22][3])
                    pg.typewrite(["enter"])

                elif (innercounter== 5):  # To enter twist
                    pg.typewrite(array_inputs[22][4])
                    pg.typewrite(["enter"])

                elif (innercounter == 6):  # To choose the foil from drop box

                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    b = [array_inputs[22][5]]
                    index = [i for i, item in enumerate(ascending_all_foils) if item in set(b)]

                    for i in range(0, index[0]):
                        pg.typewrite(["down"])

                    pg.typewrite(["enter"])

                    pg.typewrite(["enter"])

                elif (innercounter == 7):  # Enter X-panel
                    pg.typewrite(array_inputs[18][6])
                    pg.typewrite(["enter"])

                elif (innercounter == 8):  # To choose X-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[22][7] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[22][7] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])

                elif (innercounter == 9):  # To enter Y-panel
                    pg.typewrite(array_inputs[18][8])
                    pg.typewrite(["enter"])

                elif (innercounter == 10):  # To choose Y-dist from drop box
                    time.sleep(0.1)
                    pg.click(x, y, clicks=2)
                    for i in range(0, 4):
                        pg.typewrite(['up'])

                    if (array_inputs[22][9] == '1'):
                        pg.typewrite(["enter"])
                    elif (array_inputs[22][9] == '2'):
                        pg.typewrite(['down'])
                        pg.typewrite(['enter'])
                    elif (array_inputs[22][9] == '3'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])
                    elif (array_inputs[22][9] == '4'):
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(['down'])
                        pg.typewrite(["enter"])

                x += 115
                innercounter+= 1

        outercounter+=1
        y+=50
    time.sleep(0.5)
    pg.click(1701,962)

    """-------------------------------------END OF FILLING THE TABLE DETAILS-----------------------------------------"""

    """--------------------------------------------Plane inertia---------------------------------------------------- """

    time.sleep(0.5)

    time.sleep(0.5)
    pg.click(737, 338)  # Plane Inertia

    iw = pg.getWindowsWithTitle('inertia properties')

    time.sleep(1)
    iw[0].size = (613, 825)  # makes sure window is on same position for all users
    iw[0].topleft = (658, 96)

    """-------------------------------------------------X------------------------------------------------------------"""

    """---------------------------------------------Main Wing--------------------------------------------------------"""

    time.sleep(0.5)
    pg.click(850, 260)  # Main Wing

    iw1 = pg.getWindowsWithTitle('inertia properties for Main Wing')

    iw1[0].size = (613, 825)  # makes sure window is on same position for all users
    iw1[0].topleft = (658, 96)

    time.sleep(0.5)
    pg.click(894, 291, clicks=3)  # Mass Main wing
    pg.typewrite(array_inputs[4])

    for i in range(0, 2):
        pg.typewrite(["enter"])

    """-------------------------------------------------X------------------------------------------------------------"""

    """----------------------------------------------Elevator--------------------------------------------------------"""

    time.sleep(0.5)
    pg.click(959, 307)  # Elevator

    iw2 = pg.getWindowsWithTitle('inertia properties for Elevator')

    iw2[0].size = (613, 825)  # makes sure window is on same position for all users
    iw2[0].topleft = (658, 96)

    time.sleep(0.5)
    pg.click(894, 291, clicks=3)  # Mass Elevator
    pg.typewrite(array_inputs[5])

    for i in range(0, 2):
        pg.typewrite(["enter"])

    """-------------------------------------------------X------------------------------------------------------------"""

    """------------------------------------------------FIN-----------------------------------------------------------"""

    time.sleep(0.5)
    pg.click(965, 357)  # Fin

    iw3 = pg.getWindowsWithTitle('inertia properties for Fin')

    iw3[0].size = (613, 825)  # makes sure window is on same position for all users
    iw3[0].topleft = (658, 96)

    time.sleep(0.5)
    pg.click(894, 291, clicks=3)  # Mass Fin
    pg.typewrite(array_inputs[6])

    for i in range(0, 2):
        pg.typewrite(["enter"])

    pg.click(949, 872)  # save

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
    pg.typewrite(["enter"])

    time.sleep(0.1)
    pg.click(1278, 665, clicks=3)  # Fin X
    pg.typewrite(array_inputs[10])
    pg.typewrite(["enter"])

    time.sleep(0.1)
    pg.click(1278, 769, clicks=3)  # Fin Tilt angle
    pg.typewrite(array_inputs[9])
    pg.typewrite(["enter"])

    time.sleep(0.5)
    pg.click(1174,930)

    """---------------------------------------------END OF FUNCTION--------------------------------------------------"""

planedesign()

file.close()
