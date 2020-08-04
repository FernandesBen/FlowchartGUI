from tkinter import *
from tkinter import filedialog


class topBar():
    fileName=""
    def __init__(self, frameBar, windowMaster, frameWindow, canvasFrame):  # toolbar,master,window,canvasFrame
        self.frameBar = frameBar
        self.windowMaster = windowMaster
        self.frameWindow = frameWindow
        self.canvasFrame = canvasFrame

        self.windowSize()
        self.openButon()
        self.saveasButon()
        #self.saveButon()

    def windowSize(self):
        # Print window size
        self.windowMaster.update()
        tbx = self.frameWindow.winfo_width()
        winhSize = Label(self.frameBar, width=10, text="Height: " + str(self.windowMaster.winfo_height()))
        winhSize.place(x=tbx, y=150, anchor=NE)
        winwSize = Label(self.frameBar, width=10, text="Width: " + str(self.windowMaster.winfo_width()))
        winwSize.place(x=tbx, y=175, anchor=NE)

        def windowSize(event):
            winhSize.configure(text="Height: " + str(event.height))
            winhSize.place(x=event.width, y=150, anchor=NE)
            winwSize.configure(text="Width: " + str(event.width))
            winwSize.place(x=event.width, y=175, anchor=NE)

        self.frameWindow.bind("<Configure>", windowSize)

    def openButon(self):
        def openFile(DrawCanvasFrame):
            fileName = filedialog.askopenfile()

            nameofFile=str(fileName.name)
            splitNameoffile=nameofFile.split("/")
            topBar.fileName=splitNameoffile[-1]

            if fileName is not None:
                dataFile = fileName.read()
            dataFile = eval(dataFile)
            drawData(dataFile, DrawCanvasFrame)

            myApp.rootdict = dataFile
            myApp.numCircles = len(dataFile)

        def drawData(openData, drawcanvasFrame):
            for value in openData:
                print(openData[value])
                canvasBub(openData[value], drawcanvasFrame)

        openButton = Button(self.frameBar, text="Open", command=lambda: openFile(self.canvasFrame))
        openButton.pack(anchor=NW)

    def saveasButon(self):
        def saveasFile():
            fileName = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
            if fileName is None:
                return
            fileName.write(str(myApp.rootdict))
            fileName.close()

        saveas = Button(self.frameBar, text="Save As", command=saveasFile)
        saveas.pack(anchor=NW)

'''
    def saveButon(self):
        def saveFile():
            if topBar.fileName is not None:
                open(topBar.fileName)
                #filedialog.asksaveasfile(topBar.fileName)
            #fileName.filedialog.asksaveasfile(str(myApp.rootdict))

        save = Button(self.frameBar,text="Save",command=saveFile)
        save.pack(anchor=NW)
'''

class myApp():
    numCircles = 0
    rootdict = {}

    def __init__(self):
        # main window
        master = Tk()
        master.geometry("800x500")

        # frame everything goes into
        window = Frame(master)
        window.pack(fill=BOTH, expand=1)

        # frame that makes up top bar of program
        toolBar = Frame(window, bg="blue", height=200)
        toolBar.pack(fill=BOTH)
        toolBar.pack_propagate(0)

        # Canvas
        whiteBoard = Frame(window)
        whiteBoard.pack(fill=BOTH, expand=1)

        hbar = Scrollbar(whiteBoard, orient=HORIZONTAL)
        vbar = Scrollbar(whiteBoard, orient=VERTICAL)

        canHeight = 1080
        canWidth = 1920

        board = Canvas(whiteBoard, height=canHeight, width=canWidth, bg="white",
                       xscrollcommand=hbar.set, yscrollcommand=vbar.set,
                       scrollregion=(0, 0, canWidth, canHeight))

        canvasFrame = Frame(board, background="black", width=canWidth, height=canHeight)

        hbar.config(command=board.xview)
        hbar.pack(side=BOTTOM, fill=BOTH)
        vbar.config(command=board.yview)
        vbar.pack(side=RIGHT, fill=Y)
        board.pack(fill=BOTH, expand=1)

        board.create_window((0, 0), anchor=NW, window=canvasFrame)

        topBar(toolBar, master, window, canvasFrame)
        canvasFrame.bind("<Button-1>", lambda event: self.createBubbles(event, canvasFrame))

        master.mainloop()

    def createBubbles(self, coords, bubFrame):
        myApp.rootdict[myApp.numCircles] = {"x": coords.x, "y": coords.y, "text": ""}
        canvasBub(myApp.rootdict[myApp.numCircles], bubFrame)
        myApp.numCircles = myApp.numCircles + 1


class canvasBub():
    def __init__(self, bubbleData, bubbleFrame):  # bubbleData=rootdict #bubbleFrame=canvasFrame
        self.bubbleData = bubbleData
        self.xCoord = bubbleData["x"]
        self.yCoord = bubbleData["y"]
        self.text = bubbleData["text"]
        self.frameBub(bubbleFrame)
        self.entryBub()
        self.textBub()
        print(self.text)

        def retrieve_input(self):
            inputty = self.wan.get()  # "1.0",END)
            inputty = str(inputty)
            self.bubbleData["text"] = inputty
            print(myApp.rootdict)

        self.wan.bind("<FocusOut>", lambda event: retrieve_input(self))

    def frameBub(self, bubFrame):
        self.frame = Frame(bubFrame, height=100, width=200, bg="blue")
        self.frame.place(x=self.xCoord - 100, y=self.yCoord - 50)
        self.frame.propagate(0)

    def entryBub(self):
        self.wan = Entry(self.frame, width=200)
        self.wan.insert(0, self.text)
        self.wan.pack()

    def textBub(self):
        self.toxt = Text(self.frame)
        self.toxt.pack()


if __name__ == "__main__":
    myApp()


'''
class StartApp:
    def __init__(self,master):
        self.master=master
        self.master.geometry("800x600") #w,h
        self.startScreen()

    def startScreen(self):
        self.startFrame=Frame(self.master, bg="green")
        self.startFrame.pack(fill=BOTH,expand=1)

        #self.buttonFrame=Frame(self.startFrame,)
        self.newButton=Button(self.startFrame,text="New Project",height=10,width=20,command=self.newProject)
        self.newButton.pack(side=LEFT,fill=X,expand=1)
        self.oldButton=Button(self.startFrame,text="Old Project",height=10,width=20,command=self.oldProject)
        self.oldButton.pack(side=RIGHT,fill=X,expand=1)

    def newProject(self):
        nmCircs=0
        newString={}
        self.startFrame.destroy()
        RunApp(newString,nmCircs,self.master)
    def oldProject(self):
        oldString="blah blah blah"
        self.startFrame.destroy()
        RunApp(oldString,self.master)
'''
