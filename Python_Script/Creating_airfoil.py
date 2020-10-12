import time,pyautogui as pg

"""------------------------------------THIS IS THE MODULE FOR CREATING AIRFOILS--------------------------------------"""

"""---------------------------------------------READING TEXT FILE----------------------------------------------------"""

file=open("XFLR5inputs.txt","r")
f=file.readlines()

countline=0
array_inputs=[]
loadingfoil=[]

for line in f:
    countline+=1
    if(countline>3 and countline<9 and countline%2==0):
        array_inputs.append(line.strip())
    if(countline==10 or countline==12):
        loadingfoil.append(line.strip())

for i in range(1,3):

    array_inputs[i] = array_inputs[i].split(' ')  # For 2D array

loadingfoil[1]=loadingfoil[1].split(' ')           # For 2D array

"""---------------------------------------------------------X--------------------------------------------------------"""

"""------------------------------------------------------VARIABLES---------------------------------------------------"""

x_color = 875                           # x coordinate of the light green color
counter = 1                             # Keep a track of iterations
stopper = 0                             # For stopping loading foil loop iteration

"""-----------------------------------------------------------X------------------------------------------------------"""

print("INPUTS:")
print(array_inputs)
print(loadingfoil)

time.sleep(5)

def createfoil(i,stopper):


    """--------------------------------------------LOADING FOIL------------------------------------------------------"""

    if(int(loadingfoil[0])!=0 and stopper!=1):            # For loading foil

        for j in range(0,int(loadingfoil[0])):

            time.sleep(0.5)
            pg.click(14, 51)            # files

            time.sleep(0.2)
            pg.click(172,119)           # Open

            time.sleep(1)
            iw0 = pg.getWindowsWithTitle('Open File')     # To assure window is at same location for all users
            iw0[0].size=(960,720)
            iw0[0].topleft=(0,35)

            time.sleep(1)
            pg.click(765, 108)          # Searchbar
            time.sleep(0.5)
            pg.typewrite(loadingfoil[1][j])

            time.sleep(1)
            pg.typewrite(["down"])
            pg.typewrite(["enter"])

            time.sleep(1)
            pg.click(360, 287)

            time.sleep(1)
            pg.typewrite(["enter"])

    """---------------------------------------------------X----------------------------------------------------------"""

    """-----------------------------------------------CREATING AIRFOIL-----------------------------------------------"""

    if(numfoils>0):                  #For creating new foils

        time.sleep(0.2)
        pg.click(14,51)               #files

        time.sleep(0.2)
        pg.click(115,377)             #Xfoil direct analysis

        time.sleep(0.2)
        pg.click(176,47)              #Design foil

        time.sleep(0.2)
        pg.click(220,412)             #Naca foils

        fw = pg.getWindowsWithTitle('NACA Foils')       #To Find the window

        fw[0].size=(371,251)             #To assure window is placed at same spot for everyone
        fw[0].topleft=(766,390)

        time.sleep(0.2)
        pg.click(1086,465,clicks=2)   #Naca foil no(4 or 5 digits)
        pg.typewrite(array_inputs[1][i])

        for i in range(0,3):
            pg.typewrite(["enter"])

        time.sleep(0.2)
        pg.click(115,49)              #Foil menu bar

        time.sleep(0.2)
        pg.click(185,86)              #Foil management

        iw = pg.getWindowsWithTitle('Foil Management')

        iw[0].size=(975,280)
        iw[0].topleft=(464,375)

        time.sleep(0.2)
        pg.click(1391,400)            #Close foil management

        time.sleep(0.2)
        pg.click(115,49)              #Foil menu bar

        time.sleep(0.2)
        pg.click(173,121)             #Current foil->

        time.sleep(0.2)
        pg.click(478,129)             #Set style

        fw1 = pg.getWindowsWithTitle('Line Picker')  # To Find the window

        fw1[0].width = 310                #Places the window at same location for all users
        fw1[0].height = 258
        fw1[0].topleft = (796, 386)

        time.sleep(0.2)
        pg.click(984,459)             #Points

        time.sleep(0.2)
        pg.click(985,508)             #Choosing desired point style

        time.sleep(0.2)
        pg.click(983,559)             #Color

        time.sleep(0.2)
        pg.click(x_color,407)         #Choosing a different color for every foil

        for i in range(0,2):
            pg.typewrite(["enter"])

        time.sleep(0.2)
        pg.click(169,44)              #Design menu

        time.sleep(0.2)
        pg.click(244,144)             #refine globally

        fw2 = pg.getWindowsWithTitle('Global Panel Refinement')

        fw2[0].width = 566                #Places the window at same location for all users
        fw2[0].height = 326
        fw2[0].topleft = (668, 352)

        pg.typewrite(array_inputs[2][i])       #entering number of panels

        for i in range(0,5):
            pg.typewrite(["enter"])

    """------------------------------------------END OF FUNCTION-----------------------------------------------------"""

"""------------------------------------------FUNCTION CALL-----------------------------------------------------------"""

numfoils=int(array_inputs[0])

for i in range(0,numfoils):

    createfoil(i,stopper)
    x_color-=25
    stopper=1

if(numfoils==0):

    createfoil(0,stopper)

file.close()

"""-----------------------------------------------------X-----------------------------------------------------=------"""
