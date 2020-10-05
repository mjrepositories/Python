#we are opening the file here
from tkinter import Tk
from tkinter.filedialog import askopenfilename

root = Tk()
ftypes = [('All files','*.*')]
ttl  = "Select the file"
dir1 = r'C:\Users\310295192\Desktop\Work\Optilo\Transfer errors report\IDOCS'
root.fileName = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
naming = str(root.fileName).split(".")


with open(root.fileName,'r') as k, open(naming[0]+'-corrected.xml','w+') as corrected:
#then i read content so that we have it as ordered list
    content=k.read().splitlines()
    previous_line=''
#checking the file for AIR, SEA, LND or UKN indicator
    for x in content:
        #if it finds AIR - mode is AIR
        if 'AIR' in x:
            mode = 'AIR'
            break
            # if it finds SEA - mode is SEA
        elif "SEA" in x:
            mode = "SEA"
            break
            # if it finds LND - mode is LND
        elif "LND" in x:
            mode = "LND"
            break
            # if it finds nothing - it is UKN
        else:
            mode = "UKN"


    i =0
    #loop through each line
    while i<len(content):
    #  if line had <IncoTerms> phrase -it assigns what is in previous line
        if content[i][:11] =="<IncoTerms>":
            previous_line=content[i-1]
            #if in previous line we do not have delivery type -> it adds it
            if previous_line !="<DeliveryType>D2D</DeliveryType>":
                corrected.write("<DeliveryType>D2D</DeliveryType>\n"+content[i]+"\n")
                i+=1
                pass
            #if delivery type is present it assigns current lane
            else:
                corrected.write(content[i]+'\n')
                i+=1
                pass
        #if lane had <TransportationMode/> phrase-> it addes UKN line
        elif content[i][:21]=="<TransportationMode/>":
            corrected.write("<TransportationMode>"+mode+"</TransportationMode>\n")
            i+=1
            pass
    # just goes and assigns new lane (not considering incoterms
        corrected.write(content[i] + '\n')
        i+=1

