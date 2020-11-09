import time,pyautogui as pg

"""----------------------------------THIS IS THE MODULE FOR ANALYSING AIRFOILS---------------------------------------"""

"""------------------------------------------------INPUTS------------------------------------------------------------"""

countline=0                                 # For counting file lines
array_inputs=[]                             # List of all inputs
ascending_all_foils=[]                      # List of all foil names in ascending order
nacafoils_names=[]                          # List of all NACA foil names
loadedfoils_names=[]                        # List of all Loaded foil names
specificfoils_names=[]                      # List of foils to be analysed
indices=[]                                  # List of indices of all commen elements in specific and ascending arrays
num_nacafoils=[]                            # Number of naca foils to be created
num_loadedfoils=[]                          # Number of loaded foils to be created

"""---------------------------------------------------X--------------------------------------------------------------"""

"""-----------------------------------------------INPUT TEXT FILE----------------------------------------------------"""

file=open("XFLR5inputs.txt","r")
f=file.readlines()


for line in f:
    countline+=1
    if(countline==4):
        num_nacafoils.append(line.strip())
    elif(countline==10):
        num_loadedfoils.append(line.strip())
    elif(countline==6):
        nacafoils_names.append(line.strip())
    elif(countline==14):
        loadedfoils_names.append(line.strip())
    elif(countline>40 and countline<66 and countline%2!=0):
        array_inputs.append(line.strip())

nacafoils_names=nacafoils_names[0].split(' ')
loadedfoils_names=loadedfoils_names[0].split(' ')
specificfoils_names=array_inputs[1].split(' ')

for i in range(0, len(nacafoils_names)):                         # Arranges all NACA foil names in ascending order
    for j in range(i+1, len(nacafoils_names)):
        if(nacafoils_names[i] > nacafoils_names[j]):
            temp = nacafoils_names[i];
            nacafoils_names[i] = nacafoils_names[j];
            nacafoils_names[j] = temp;

for i in range(0, len(loadedfoils_names)):                       # Arranges all loaded foil names in ascending order
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

indices = [i for i, item in enumerate(ascending_all_foils) if item in set(specificfoils_names)]   # To find commen indices of commen elements

"""----------------------------------------------------X-------------------------------------------------------------"""

print("INPUTS:")
print("PARAMETERS:",array_inputs)
print("FOIL LIST:",ascending_all_foils)
print("FOIL TO BE ANALYZED:",specificfoils_names)
print("INDICES:",indices)

time.sleep(0.5)
pg.getWindowsWithTitle("xflr5 v6.47")[0].restore()
time.sleep(1)

def analyzefoil():


    """
    pg.click(241,45)                                              # Analysis menu bar

    time.sleep(0.2)
    pg.click(367,142)                                             # Multi threaded batch analysis """

    time.sleep(0.5)
    pg.hotkey('ctrl','F6');

    time.sleep(0.2)
    fw = pg.getWindowsWithTitle('Multi-threaded batch analysis')  # Finds the window

    fw[0].size = (1294, 708)                                      # To assure window is placed at same spot for everyone
    fw[0].topleft = (20, 20)

    """------------------------------------------FOIL SELECTION------------------------------------------------------"""

    """time.sleep(0.2)
    pg.click(228,131)                                           # Foils list radio button

    time.sleep(0.2)
    pg.click(482,130)                                           # Foils list (rectangle) button"""

    time.sleep(0.2)
    pg.typewrite(['right'])
    pg.typewrite(['tab'])
    pg.typewrite(['space'])
    pg.typewrite(['escape'])
    pg.typewrite(['space'])

    fw1 = pg.getWindowsWithTitle('Foil Selection')

    fw1[0].size = (408, 431)
    fw1[0].topleft = (455, 164)

    """time.sleep(0.2)                                             # Close Analysis
    pg.click(812,185)

    time.sleep(0.2)
    pg.click(482,130)                                           # Doing this to deselect default options"""

    if(array_inputs[0]=="y" or array_inputs[0]=="Y"):           # Analyzing All foils

        """time.sleep(0.2)
        pg.click(778,544)

        time.sleep(0.2)
        pg.click(542,554)"""
        time.sleep(0.2)
        for i in range(0,3):
            pg.typewrite(['tab'])
        pg.typewrite(['space'])
        pg.typewrite(['tab'])

        time.sleep(0.2)
        pg.typewrite(['enter'])



    else:

        for i in range(0,len(indices)):      # Analyzing specific foils

            """y=235

            time.sleep(0.2)
            pg.moveTo(669,235)

            time.sleep(0.2)                 # Selecting the desired number of airfoils from foils list
            pg.click(669,y+(30*indices[i]))"""
            time.sleep(0.2)

            for j in range(0,6):            #Going back to box 1
                pg.typewrite(['up'])

            for i in range(0,int(indices[i])):
                pg.typewrite(['down'])

            pg.typewrite(['space'])


        pg.typewrite(["enter"])

    """--------------------------------------------------X-----------------------------------------------------------"""

    """-----------------------------------------------PARAMETERS-----------------------------------------------------"""

    time.sleep(0.2)
    pg.typewrite(['tab'])              #Range
    pg.typewrite(['space'])

    for k in range(2,9):

        pg.typewrite(['tab'])
        pg.typewrite(array_inputs[k])

    """time.sleep(0.2)
    pg.click(239, 284, clicks=3)  # Reynolds Min
    pg.typewrite(array_inputs[2])

    time.sleep(0.2)
    pg.click(356, 284, clicks=3)  # Reynolds Max
    pg.typewrite(array_inputs[3])

    time.sleep(0.2)
    pg.click(494, 284, clicks=3)  # Reynolds increment
    pg.typewrite(array_inputs[4])

    time.sleep(0.2)
    pg.click(239, 320, clicks=3)  # Mach
    pg.typewrite(array_inputs[5])

    time.sleep(0.2)
    pg.click(239, 355, clicks=3)  # NCrit
    pg.typewrite(array_inputs[6])

    time.sleep(0.2)
    pg.click(505, 437, clicks=3)  # Top Transition
    pg.typewrite(array_inputs[7])

    time.sleep(0.2)
    pg.click(505, 470, clicks=3)  # Bottem Transition
    pg.typewrite(array_inputs[8])"""


    if(array_inputs[9]=='a'):     # Alpha or CL radio button

        time.sleep(0.1)
        pg.press('tab',presses=2)

    else:

        time.sleep(0.1)
        pg.press('tab')
        pg.press('right')


    """
    time.sleep(0.2)
    pg.click(230, 610,clicks=3)         # Alpha Min
    pg.typewrite(array_inputs[10])

    time.sleep(0.2)
    pg.click(359, 609,clicks=3)         # Alpha Max
    pg.typewrite(array_inputs[11])

    time.sleep(0.2)
    pg.click(496,609,clicks=3)          # Alpha increment
    pg.typewrite(array_inputs[12])

    time.sleep(0.2)
    pg.click(316,682)                   # analyze button"""

    for l in range(10,13):

        pg.typewrite(['tab'])
        pg.typewrite(array_inputs[l])

    pg.press('enter',presses=2)


    """-------------------------------------------END OF FUNCTION----------------------------------------------------"""

analyzefoil()

file.close()




