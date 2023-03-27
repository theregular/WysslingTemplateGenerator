import tkinter as tk
import docedit

#TODO: Handle blank inputs
#TODO: correct input?
#TODO: choose save directory?
#TODO: implement mounting info with built in selection?
#TODO: change template based on state input
#TODO: handle florida code/other weird codes

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
              "Snow Load:",
              "ASCE:",
              "Wind Speed:",
              "Exposure Category:",
              "Code Year:",
              "Mount Type:",
              "Mount Info:",
              "Spacing:"
              ]

states = [
      'AK',
      'AL',
      'AR',
      'AZ',
      'CA',
      'CO',
      'CT',
      'DE',
      'FL',
      'GA',
      'HI',
      'IA',
      'ID',
      'IL',
      'IN',
      'KS',
      'KY',
      'LA',
      'MA',
      'MD',
      'ME',
      'MI',
      'MN',
      'MO',
      'MS',
      'MT',
      'NC',
      'ND',
      'NE',
      'NH',
      'NJ',
      'NM',
      'NV',
      'NY',
      'OH',
      'OK',
      'OR',
      'PA',
      'RI',
      'SC',
      'SD',
      'TN',
      'TX',
      'UT',
      'VA',
      'VT',
      'WA',
      'WI',
      'WV',
      'WY',
        ]

asces = ["98","05","10","16"]

#exposures = ["B","C"]

#possible to use this? NOT BEING USED RIGHT NOW
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
#global rowNum
#rowNum = 0
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
    for currEntry in entries:
        input = currEntry.get()
        userInput.append(input)
    #print(accessChoice.get())
    #print(stateChoice.get()) #TODO: change template based on state input
    #print(asceChoice.get())
    #print(exposChoice.get())

    userInput.append(accessChoice.get())
    userInput.append(stateChoice.get())
    userInput.append(asceChoice.get())
    userInput.append(exposChoice.get())

    print(userInput)
    #print("INPUT LENGTH: " + str(len(userInput)))
    docedit.setUserInput(userInput)
    docedit.run()

def reset():
    #print("RESET CALLED")
    for widget in window.winfo_children():
        widget.destroy()
    generateWidgets()

#window = tk.Tk()
#window.title("Wyssling Template Generator")
#window.minsize(500,400)
#window.resizable(False,False)

#generateWindow(window)

def generateWidgets():
    global rowNum
    rowNum = 0
    #name
    #generateRow(window)
    generateRow(window, docedit.name_fill)
    rowNum+=1

    #address
    #generateRow(window)
    generateRow(window, docedit.address_fill)
    rowNum+=1

    #state
    #generateRow(window, docedit.state_fill)
    label = tk.Label(window, text=categories[rowNum])
    label.grid(row=rowNum, column=0)
 
    global stateChoice #TODO: change from global variable
    stateChoice = tk.StringVar(window)
    stateChoice.set(states[30]) #sets NJ as default
    stateList = tk.OptionMenu(window, stateChoice, *states)
    stateList.grid(row=rowNum, column = 1)

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
    #generateRow(window, docedit.atticAccess_fill)
    label = tk.Label(window, text=categories[rowNum])
    label.grid(row=rowNum, column=0)

    global accessChoice
    accessChoice = tk.StringVar(value="Accessible")
    radio1 = tk.Radiobutton(window, text="Accessible", value="Accessible", variable=accessChoice)
    radio2 = tk.Radiobutton(window, text="Inaccessible", value="Inaccessible", variable=accessChoice)
    radio1.grid(row=rowNum, column=1)
    radio2.grid(row=rowNum, column=2)

    rowNum+=1

    #existingDead
    generateRow(window, docedit.existingDead_fill)
    rowNum+=1

    #newDead
    generateRow(window, docedit.newDead_fill)
    rowNum+=1

    #totalDead #doesn't need to be generated
    #generateRow(window, docedit.totalDead_fill)
    #rowNum+=1

    #snow
    generateRow(window, docedit.snow_fill)
    rowNum+=1

    #asce
    #generateRow(window, docedit.asce_fill)
    label = tk.Label(window, text=categories[rowNum])
    label.grid(row=rowNum, column=0)

    global asceChoice
    asceChoice = tk.StringVar(window)
    asceChoice.set(asces[3]) #sets 16 as default
    asceList = tk.OptionMenu(window, asceChoice, *asces)
    asceList.grid(row=rowNum, column = 1)

    rowNum+=1

    #wind
    generateRow(window, docedit.wind_fill)
    rowNum+=1

    #exposure category
    #generateRow(window, docedit.codeYear_fill)
    label = tk.Label(window, text=categories[rowNum])
    label.grid(row=rowNum, column=0)

    global exposChoice
    exposChoice = tk.StringVar(value="B")
    radio1 = tk.Radiobutton(window, text="B", value="B", variable=exposChoice)
    radio2 = tk.Radiobutton(window, text="C", value="C", variable=exposChoice)
    radio1.grid(row=rowNum, column=1)
    radio2.grid(row=rowNum, column=2)

    rowNum+=1

    #code year #TODO: handle florida code/other weird codes
    generateRow(window, docedit.codeYear_fill)
    rowNum+=1

    #mount type
    generateRow(window, docedit.mountingType_fill)
    rowNum+=1

    #mount info
    generateRow(window, docedit.mountingInfo_fill)
    rowNum+=1

    #spacing
    generateRow(window, docedit.spacing_fill)
    rowNum+=1

    #generate button
    genButton = tk.Button(window, text="Generate", command=get_input)
    genButton.grid(row=rowNum, column=0)

    #reset button #TODO:implement
    resetButton = tk.Button(window, text="Reset", command=reset)
    resetButton.grid(row=rowNum, column=1)

window = tk.Tk()
window.title("Wyssling Template Generator")
window.minsize(500,400)
window.resizable(False,False)

generateWidgets()

window.mainloop()