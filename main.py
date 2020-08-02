import tkinter as tk
import pyautogui
import datetime
import numpy as np
import cv2
import os

Width = 600
Height = 500

#texto del label en lower frame
text = '''Da clic en alguno de los botones

SNAPP -> Toma una captura de pantalla
Record a SNAPP -> Graba tu pantalla en tiempo real
EXIT -> Cierra SNAPP
'''
global lf_label

#takes a screenshot of the fullscreen using pyautogui
def takeSnapp():
    screenshot = pyautogui.screenshot()
    #name = 'SNAPP-' + datetime.date.today().strftime("%h-%M-%S") + '.png'
    #genera el tiempo exacto de la captura
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d-%H-%M-%S")
    name = 'SNAP-' + format(now_str) + '.png'
    #saves the SNAPP with the DATE
    screenshot.save(name)

    #global label
    global lf_label
    lf_label.configure(text='Usted tomo una captura!')

    #debug console text
    print("SE TOMO UNA CAPTURA!") #debug purpose line

    path = os.getcwd() #gets the current working directory
    os.system(f"start {os.path.realpath(path)}") #opens the directory allocated in path


#captures the screen
def recordSnapp():
    
    #global label
    global lf_label
    lf_label.configure(text='Recording... \nseleccione la ventana "recordg" y \npresione "q" para detenerse.')

    #gets screen size
    screen_width = snapp.winfo_screenwidth()
    screen_height = snapp.winfo_screenheight()

    #uses screen size to record
    screen = (screen_width, screen_height)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    now = datetime.datetime.now()

    #naming
    now_str = now.strftime("%Y-%m-%d-%H-%M-%S")
    name = 'SNAP-' + format(now_str) + '.avi'

    #output
    vid = cv2.VideoWriter(name, fourcc, 20.0, (screen))


    while True:

        rec = pyautogui.screenshot()
        frame = np.array(rec)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        vid.write(frame)
        
        #resizes recording window
        cv2.resizeWindow('recording', 300, 0)
        cv2.moveWindow("recording", 5, 5)
        cv2.imshow("recording", frame)
        
        

        if cv2.waitKey(1) == ord("q"):
            lf_label.configure(text='''
    Da clic en alguno de los botones

SNAPP -> Toma una captura de pantalla
Record a SNAPP -> Graba tu pantalla en tiempo real
EXIT -> Cierra SNAPP
''')
            break

    vid.release()
    cv2.destroyAllWindows()

    path = os.getcwd() #gets the current working directory
    os.system(f"start {os.path.realpath(path)}") #opens the directory allocated in path



#quit function
def quitSnapp():
    print('Hasta luego') #debug purpose line
    #global label
    global lf_label
    lf_label.configure(text='Hasta luego!')
    snapp.destroy()



#snapp will be the root
snapp = tk.Tk()

#we create the canvas
canvas = tk.Canvas(snapp, height=Height, width=Width)
canvas.pack()


#background
background_image = tk.PhotoImage(file='back.png')
background_label = tk.Label(snapp, image=background_image)
background_label.place(relwidth=1, relheight=1)


#we define the frame area
frame = tk.Frame(snapp, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n") #rel allows to responsive size scaling


#TAKE A SNAPP (FULL SCREEN CAPTURE)
snap = tk.Button(frame, text="SNAPP", font=40, command= takeSnapp)
snap.place(relx=0, relheight=1, relwidth=0.3)

#RECORDS A SNAPP BUTTON
snap = tk.Button(frame, text="RECORD A SNAPP", font=40, command= recordSnapp)
snap.place(relx=0.325, relheight=1, relwidth=0.35)

#EXIT SNAPP BUTTON
snap = tk.Button(frame, text="EXIT", font=40, command= quitSnapp)
snap.place(relx=0.7, relheight=1, relwidth=0.3)


#lower frame
lower_frame = tk.Frame(snapp, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#lower frame label
lf_label = tk.Label(lower_frame, text= text, font=('Courier', 10))
lf_label.place(relwidth=1, relheight=1)



snapp.title('SNAPP by Fernando Alejandro Leon')
snapp.resizable(False, False)
#runs root mainloop
snapp.mainloop()




