import time,pyautogui as pg

"""------------------------------------THIS IS THE MODULE FOR CREATING AIRFOILS--------------------------------------"""

"""---------------------------------------------READING TEXT FILE----------------------------------------------------"""

file=open("XFLR5inputs.txt","r")                    # Opening Text File
f=file.readlines()

countline=0
array_inputs=[]
loadingfoil=[]

for line in f:                                      # Reading the required input line by line
    countline+=1
    if(countline>3 and countline<9 and countline%2==0):
        array_inputs.append(line.strip())
    if(countline>=10 and countline<=12 and countline%2==0):
        loadingfoil.append(line.strip())

for i in range(1,3):

    array_inputs[i] = array_inputs[i].split(' ')    # For creating a 2D array


"""---------------------------------------------------------X--------------------------------------------------------"""

"""------------------------------------------------------VARIABLES---------------------------------------------------"""

x_color = 875                           # x coordinate of the light green color
counter = 1                             # Keep a track of iterations
stopper = 0                             # For stopping loading foil loop iteration

"""-----------------------------------------------------------X------------------------------------------------------"""

print("INPUTS:")
print(array_inputs)
print(loadingfoil)

time.sleep(0.5)
pg.getWindowsWithTitle("xflr5 v6.47")[0].restore()  # start XFLR5

pg.keyDown('alt')                                   # for full screen
pg.press(' ')
pg.press('x')
pg.keyUp('alt')

time.sleep(1)

def createfoil(i,stopper):


    """--------------------------------------------LOADING FOIL------------------------------------------------------"""


    if(int(loadingfoil[0])!=0 and stopper!=1):         # For loading foil

        time.sleep(0.5)
        pg.hotkey('ctrl','o')                          # To open File explorer

        time.sleep(2)
        iw0 = pg.getWindowsWithTitle('Open File')      # To assure window is at same location for all users
        iw0[0].size=(960,720)
        iw0[0].topleft=(0,35)

        time.sleep(2)
        pg.hotkey('alt','d')                           # To enter file address
        pg.typewrite(loadingfoil[1])

        time.sleep(1)
        pg.typewrite(["enter"])

        for k in range(0,2):

            time.sleep(0.2)
            pg.hotkey('shift','tab')

        pg.hotkey('ctrl','a')                          # To select all files in the directory


        time.sleep(1)
        pg.typewrite(["enter"])


    """---------------------------------------------------X----------------------------------------------------------"""

    """-----------------------------------------------CREATING AIRFOIL-----------------------------------------------"""

    pg.moveTo(1050,550)              # To make sure the cursor is on the XFLR5 window

    if(numfoils>0):                  # For creating new foils

        time.sleep(0.2)
        pg.hotkey('Ctrl','5')        # Open XFoil Direct Analysis
        pg.hotkey('Fn', 'F5')        # Op point view


        """-------------------------------------NACA FOIL MENU--------------------------------------------------"""

        time.sleep(0.5)
        pg.click(button='right')                   # accessing the Naca Foils menu

        for k in range(0,3):

            pg.typewrite(["down"])

        pg.typewrite(["right"])

        for j in range(0,10):

            pg.typewrite(["down"])

        pg.typewrite(["enter"])

        time.sleep(1)
        fw = pg.getWindowsWithTitle('NACA Foils')  # To Find the window

        fw[0].size = (371, 251)                    # To assure window is placed at same spot for everyone
        fw[0].topleft = (766, 390)

        time.sleep(0.2)
        pg.hotkey('ctrl', 'a')                     # To Highlight the text

        pg.typewrite(array_inputs[1][i])

        for i in range(0,3):
            pg.typewrite(["enter"])

        """------------------------------------------------X-----------------------------------------------------"""


        time.sleep(0.2)
        pg.hotkey('fn','F7')                               # Open Foil Management

        time.sleep(0.2)
        iw = pg.getWindowsWithTitle('Foil Management')     # To Find the window

        iw[0].size=(975,280)                               # To assure window is placed at same spot for everyone
        iw[0].topleft=(464,375)

        time.sleep(0.2)
        pg.press('escape')

        time.sleep(0.2)
        pg.click(button='right')

        pg.typewrite(["down"])
        pg.typewrite(["right"])
        pg.typewrite(["enter"])

        fw1 = pg.getWindowsWithTitle('Line Picker')  # To Find the window

        fw1[0].width = 310            # Places the window at same location for all users
        fw1[0].height = 258
        fw1[0].topleft = (796, 386)

        time.sleep(0.1)
        pg.click(984,459)             # Points

        time.sleep(0.1)
        pg.click(985,508)             # Choosing desired point style

        time.sleep(0.1)
        pg.click(983,559)             # Color

        time.sleep(0.1)
        pg.click(x_color,407)         # Choosing a different color for every foil

        for i in range(0,2):
            pg.typewrite(["enter"])

        time.sleep(0.1)
        pg.hotkey('fn','F3')          # Open global refinement Panel

        time.sleep(0.2)
        fw2 = pg.getWindowsWithTitle('Global Panel Refinement')

        fw2[0].width = 566                     # Places the window at same location for all users
        fw2[0].height = 326
        fw2[0].topleft = (668, 352)

        pg.typewrite(array_inputs[2][i])       # entering number of panels

        for i in range(0,5):
            pg.typewrite(["enter"])

    """------------------------------------------END OF FUNCTION-----------------------------------------------------"""

"""------------------------------------------FUNCTION CALL-----------------------------------------------------------"""

numfoils=int(array_inputs[0])

for i in range(0,numfoils):    # Function call if user wants to create and load airfoils

    createfoil(i,stopper)
    x_color-=25
    stopper=1

if(numfoils==0):                # Function call if user only wants to load airfoils

    createfoil(0,stopper)

file.close()

"""-----------------------------------------------------X-----------------------------------------------------=------"""
