"""             elif 'alarm' in query:
                speak("Enter the time !")
                time = input(": Enter the time :")

                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")

                    if now == time:
                        speak("time to wake up sir!")
                        playsound('hp.mp3')
                        speak("alaram Closed!")

                    elif now>time:
                        break
             """



""" 
                             CrossIT= "E:\\python\\Games\\CrossIT.py"
                jumping_jack= "E:\\python\\Games\\Jumping_Jack.py"
                pacman= "E:\\python\\Games\\pacman.py"
                paint= "E:\\python\\Games\\paint.py"
                ping_pong= "E:\\python\\Games\\Ping_Pong.py"
                Simon_says= "E:\\python\\Games\\Simon_says.py"
                snakegame= "E:\\python\\Games\\snakegame.py"
                x_and_0= "E:\\python\\Games\\XandO.py"
                os.startfile(games)  
                os.startfile(CrossIT)
                
                os.startfile(jumping_jack)
                os.startfile(pacman)
                os.startfile(paint)
                os.startfile(ping_pong)
                os.startfile(Simon_says)
                os.startfile(snakegame)
                os.startfile(x_and_0)   """


             #------------   ui----------------#
"""              from JarvisUi import Ui_MainWindow
from ools.PyQt5.QtCore import QThread, QTimer
from ools.PyQt5.QtWidgets import QMainWindow """


##########################################################
""" class MainThread(QThread):
    def __init__(self):

        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        main.TakeExe()

startFunctions = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_MainWindow()
        self.jarvis_ui.setupUi(self)
        self.jarvis_ui.pushButton.clickrd.connect(self.startFunc)
        self.jarvis_ui.pushButton_2.clickrd.connect(self.close)

    def startFunc(self):
        self.jarvis_ui.moves = QtGui.QMovie("../../../../2 -python/3 - Materials/G.U.I Material/B.G/1.gif")
        self.jarvis_ui.Gif.setMovie(self.jarvis_ui.movies)
        self.jarvis_ui.movies.start()


    def startFunc(self):
        self.jarvis_ui.moves_2 = QtGui.QMovie("../../../../2 -python/3 - Materials/G.U.I Material/B.G/1.gif")
        self.jarvis_ui.Gif.setMovie(self.jarvis_ui.movies)
        self.jarvis_ui.movies_2.start()


        timer = QTimer(self)
        time.timeout.connect(self.showtime)
        timer.start(1000)
        startFunctions.start()

    def showtime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString("hh:mm:ss")
        labbel = "Time Is Now : "+ label_time
        self.jarvis_ui.textBrowser.SetText(labbel)
 """

#########################################################