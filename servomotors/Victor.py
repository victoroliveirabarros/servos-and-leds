import Tkinter as tk
import serial
class App:

    #construct
    def __init__(self, root, ser):

        self.root = root
        self.ser = ser
        self.root.title("Automacao Cesupa")
        self.servo1 = 5
        self.servo2 = 5
        self.lampada1 = 0
        self.lampada2 = 0
        self.iniciar_interface()

    def iniciar_interface(self):

        self.btLigar1 = tk.Button(self.root , text = "Ligar", command = self.btLigado1)
        self.lbl1 = tk.Label(self.root, text = "Servo1")
        
        self.btLigar2 = tk.Button(self.root, text = "Ligar", command = self.btLigado2)
        self.lbl2 = tk.Label(self.root, text = "Servo2")
        
        self.lbl3 = tk.Label(self.root, text = "Lampada1")
        self.btLampada1 = tk.Button(self.root, text = "Ligar", command = self.Lampada1)

        self.lbl4 = tk.Label(self.root, text = "Lampada2")
        self.btLampada2 = tk.Button(self.root, text = "Ligar", command = self.Lampada2)
        
        self.lbl1.pack()
        self.btLigar1.pack()
        self.lbl2.pack()
        self.btLigar2.pack()
        self.lbl3.pack()
        self.btLampada1.pack()
        self.lbl4.pack()
        self.btLampada2.pack()
        

    def btLigado1(self):
        if self.servo1 == 0:
            self.servo1 = 1
            self.btLigar1["text"] = "Ligar"
            self.ser.write("servo1_desligar")
            print self.servo1
        else:
            self.servo1 = 0
            self.btLigar1["text"] = "Desligar"
            self.ser.write("servo1_ligar")
            print self.servo1
        
    def btLigado2(self):
        if self.servo2 == 0:
            self.servo2 = 1
            self.btLigar2["text"] = "Ligar"
            self.ser.write("servo2_desligar")
            print self.servo2
        else:
            self.servo2 = 0
            self.btLigar2["text"] = "Desligar"
            self.ser.write("servo2_ligar")
            print self.servo2
            

    def Lampada1(self):
        if self.lampada1 == 0:
            self.lampada1 = 1;
            self.btLampada1["text"] = "Desligar"
            self.ser.write("lampada1_ligar")
            print self.lampada1

        else:
            self.lampada1 = 0;
            self.btLampada1["text"] = "Ligar"
            self.ser.write("lampada1_desligar")
            print self.lampada1

    def Lampada2(self):
        if self.lampada2 == 0:
            self.lampada2 = 1;
            self.btLampada2["text"] = "Desligar"
            self.ser.write("lampada2_ligar")
            print self.lampada2
        else:
            self.lampada2 = 0
            self.btLampada2["text"] = "Ligar"
            self.ser.write("lampada2_desligar")
            print self.lampada2
        
        
        
ser = serial.Serial(
    port='/COM3',
    baudrate=9600,
    )
root = tk.Tk()
app = App(root, ser)
root.mainloop()
        

