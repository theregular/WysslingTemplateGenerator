import tkinter as tk
import docedit

#TODO: Handle blank inputs
#TODO: change simpler ones to radio choices
#TODO: correct input?
#TODO: save directory?
#TODO: user inputs template? preferably not

categories = ["Customer Name:",
              "Customer Address:",
              "State:",
              "System Size:",
              "Framing:",
              "Roof Material",
              "Slope:",
              "Attic Access:",
              "Existing Dead Load:",
              "New Dead Load:",
              "Total Dead Load:",
              "Snow Load:",
              "ASCE:",
              "Wind Speed:",
              "Exposure Category",
              "Code Year:",
              "Mount Type:",
              #"Mount Info:", TODO: implement
              "Spacing:"
              ]

#possible to use this?
def generateWindow(inWindow):
    rowNum = 0
    #colNum = 0
    for string in categories:
        label = tk.Label(inWindow, text=string)
        label.grid(row=rowNum, column=0)
        entry = tk.Entry(inWindow)
        entry.grid(row=rowNum, column = 1)
        rowNum+=1


entries = []
#userInput = []
rowNum = 0
#colNum = 0
def generateRow(inWindow, autofill=""):
    label = tk.Label(inWindow, text=categories[rowNum])
    label.grid(row=rowNum, column=0)
    entry = tk.Entry(inWindow, width=50)
    entry.grid(row=rowNum, column = 1)
    if autofill != None:
        entry.insert(0, autofill)
    entries.append(entry)
    
def get_input():
    userInput = []
    for entry in entries:
        input = entry.get()
        userInput.append(input)
    print(userInput)
    docedit.setUserInput(userInput)
    docedit.run()

window = tk.Tk()
window.title("Wyssling Template Generator")
window.minsize(500,400)
window.resizable(False,False)

#generateWindow(window)

#name
generateRow(window)
rowNum+=1

#address
generateRow(window)
rowNum+=1

#state
generateRow(window, docedit.state_fill)
rowNum+=1

#systemSize
generateRow(window, docedit.systemSize_fill)
rowNum+=1

#framing
generateRow(window, docedit.framing_fill)
rowNum+=1

#roofMaterial
generateRow(window, docedit.roofMaterial_fill)
rowNum+=1

#slope
generateRow(window, docedit.slope_fill)
rowNum+=1

#atticAccess
generateRow(window, docedit.atticAccess_fill)
rowNum+=1

#existingDead
generateRow(window, docedit.existingDead_fill)
rowNum+=1

#newDead
generateRow(window, docedit.newDead_fill)
rowNum+=1

#totalDead
generateRow(window, docedit.totalDead_fill)
rowNum+=1

#snow
generateRow(window, docedit.snow_fill)
rowNum+=1

#asce
generateRow(window, docedit.asce_fill)
rowNum+=1

#wind
generateRow(window, docedit.wind_fill)
rowNum+=1


#code year
generateRow(window, docedit.exposureCat_fill)
rowNum+=1

#exposure category
generateRow(window, docedit.codeYear_fill)
rowNum+=1

#mount type
generateRow(window, docedit.mountingType_fill)
rowNum+=1

#mount info
    #TODO: implement

#spacing
generateRow(window, docedit.spacing_fill)
#rowNum+=1

#print(rowNum)
button = tk.Button(window, text="Generate", command=get_input)
button.grid()

window.mainloop()