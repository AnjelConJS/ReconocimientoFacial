import pickle
from tkinter import *
import tkinter as tk
import cv2
import numpy as np
import os
from PIL import ImageTk, Image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
raiz= Tk()

key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)
cont: int=1
cont2: int=1
cont3: int=1
cont4: int=1
cont6: int=1
cont7: int=1

FileFoto=''
raiz.title("camara")
mycolorGris='#%02x%02x%02x' %(35,43,50)
mycolorBlue='#%02x%02x%02x' %(60,141,168)
mycolorGrisB='#%02x%02x%02x' %(54,73,80)
mycolorBlueB='#%02x%02x%02x' %(0,176,243)
mycolorGreen='#%02x%02x%02x' %(105,231,129)
RutaV="C:/Users/arman/PycharmProjects/Interfaz/saved_img-final.png"
RutaO="C:/Users/arman/PycharmProjects/Interfaz/saved_img-final.png"
RutaD="C:/Users/arman/PycharmProjects/Interfaz/saved_img-final.png"
RutaE="C:/Users/arman/PycharmProjects/Interfaz/saved_img-final.png"
ICamara= PhotoImage(file="C:/Users/arman/Desktop/Universidad 5to/Sistemas digitales/bonito/camaraa.png")
IBuscar= PhotoImage(file="C:/Users/arman/Desktop/Universidad 5to/Sistemas digitales/bonito/lupita.png")
IEGrises= PhotoImage(file="C:/Users/arman/Desktop/Universidad 5to/Sistemas digitales/bonito/escaladegrises.png")
IEErosion= PhotoImage(file="C:/Users/arman/Desktop/Universidad 5to/Sistemas digitales/bonito/anadir.png")
IDDilatacion= PhotoImage(file="C:/Users/arman/Desktop/Universidad 5to/Sistemas digitales/bonito/menos (1).png")
ILimpiar= PhotoImage(file="C:/Users/arman/Desktop/Universidad 5to/Sistemas digitales/bonito/limpiar.png")
IAcamara= PhotoImage(file="C:/Users/arman/Desktop/Universidad 5to/Sistemas digitales/bonito/abrircamara.png")
ICcamara= PhotoImage(file="C:/Users/arman/Desktop/Universidad 5to/Sistemas digitales/bonito/cerrarcamara.png")
IPuntos= PhotoImage(file="C:/Users/arman/Desktop/Universidad 5to/Sistemas digitales/bonito/editar (4).png")
IGuardar= PhotoImage(file="C:/Users/arman/Desktop/Universidad 5to/Sistemas digitales/bonito/guardar.png")
IComparar= PhotoImage(file="C:/Users/arman/Desktop/Universidad 5to/Sistemas digitales/bonito/lista.png")
ICerrar= PhotoImage(file="C:/Users/arman/Desktop/Universidad 5to/Sistemas digitales/bonito/salir.png")
IFOTO= PhotoImage(file=RutaO)
IErosion= PhotoImage(file=RutaE)
IPrueba= PhotoImage(file=RutaV)
IDilatacion= PhotoImage(file=RutaD)
miFrame= Frame(raiz,width='1360',height='760')
miFrame.pack()
miFrameM= Frame(miFrame,width='210',height='720',bg=mycolorGris)
miFrameM.place(x=0, y=40)
miFramebar= Frame(miFrame,width='1360',height='40',bg=mycolorBlue)
miFramebar.place(x=0, y=0)
miFrameThings= Frame(miFrame,width='1250',height='720',bg='white')
miFrameThings.place(x=210, y=40)
MiFrameEfectos=Frame(miFrame, width='625',height='720', bg='white')
MiFrameEfectos.place(x=210,y=40)
MiFrameTrabajar=Frame(miFrame, width='625',height='300', bg='green')
MiFrameTrabajar.place(x=835,y=40)
MiFramePuntos=Frame(miFrame, width='625',height='420', bg='orange')
MiFramePuntos.place(x=835,y=340)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 150)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 130)
lmain = tk.Label(MiFrameTrabajar)
lmain.pack()
def show_frame():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
    frame = cv2.flip(frame, 1)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
show_frame()
MBlabel= Label(miFramebar,text='camara',font=('Century Gothic',20), fg='white', bg=mycolorBlue)
MBlabel.place(x=10,y=0)



#Los buscar
TFBuscar= Entry(miFrameM,font=('Century Gothic',20), fg='white', bg= mycolorGrisB,borderwidth=0)
TFBuscar.grid(row=0, column=1,ipady=0)
BTBuscar= Button(miFrameM,image=IBuscar, bg= mycolorGrisB,borderwidth=0)
BTBuscar.grid(row=0, column=0, ipadx=7, ipady=6.5)
print(TFBuscar.get())


#BotonTomarFoto
def TOMARFOTO():
    global cont2
    global RutaO
    global IFOTO
    global cont6
    global cont7
    cont2 += 1
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

    cv2.imwrite(filename='saved_img.jpg', img=frame)
    webcam.release()
    img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
    img_new = cv2.imshow("Captured Image", img_new)
    cv2.waitKey(1650)
    cv2.destroyAllWindows()
    color = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    img_ = cv2.resize(color, (300, 300))
    img_resized = cv2.imwrite(filename=str(cont2) + 'color.png', img=frame[y:y + h, x:x + w])
    RutaO = "C:/Users/arman/PycharmProjects/Interfaz/"+str(cont2)+"color.png"
    IFOTO = PhotoImage(file=RutaO)
    cont6=1
    cont7=1


BTFoto= Button(miFrameM,text='Tomar Foto',font=('Century Gothic',18), fg='white', bg= mycolorGris,borderwidth=0, command=TOMARFOTO)
BTFoto.grid(row=1, column=1,sticky='w', padx=5, pady=3)
IconFoto= Label(miFrameM,image=ICamara, bg= mycolorGris)
IconFoto.grid(row=1, column=0, padx=5, pady=3)
#BotonEscalaDeGrises
lEscala = tk.Label(MiFrameTrabajar)
lEscala.pack()

def EscalaGrises():
    global cont
    global RutaV
    global IPrueba
    global RutaO
    cont += 1
    _, frame = cap.read()
    img_ = cv2.imread(RutaO, cv2.IMREAD_ANYCOLOR)
    gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
    img_ = cv2.resize(gray, (300, 300))
    img_resized = cv2.imwrite(filename=str(cont) + 'saved_img-final.png', img=img_)
    print("Image saved!")
    RutaV = "C:/Users/arman/PycharmProjects/Interfaz/" + str(cont) + "saved_img-final.png"
    IPrueba = PhotoImage(file=RutaV)

BTEGrises= Button(miFrameM,text='Escala Grises',font=('Century Gothic',18), fg='white', bg= mycolorGris,borderwidth=0, command=EscalaGrises)
BTEGrises.grid(row=2, column=1,sticky='w', padx=5, pady=3)
IconEgrises= Label(miFrameM,image=IEGrises, bg= mycolorGris)
IconEgrises.grid(row=2, column=0, padx=5, pady=3)
#BotonErosionado
def Erosion():
    global cont3
    global RutaE
    global IErosion
    global RutaV
    global cont6
    cont3 += 1
    cont6 += 1
    _, frame = cap.read()
    if cont6<3:
        RepErosion(RutaV)
    elif cont6>4:
        RepErosion(RutaE)

def RepErosion(ruta):
    global cont3
    global RutaE
    global IErosion
    img_ = cv2.imread(ruta, cv2.IMREAD_ANYCOLOR)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(img_, kernel)
    print("Converted RGB image to grayscale...")
    print("Resizing image to 28x28 scale...")
    img_ = cv2.resize(erosion, (300, 300))
    print("Resized...")
    img_resized = cv2.imwrite(filename=str(cont3) + 'Erosion.png', img=img_)
    print("Image saved!")
    RutaE = "C:/Users/arman/PycharmProjects/Interfaz/" + str(cont3) + "Erosion.png"
    IErosion = PhotoImage(file=RutaE)

BTErosionado= Button(miFrameM,text='Erosionado',font=('Century Gothic',18), fg='white', bg= mycolorGris,borderwidth=0, command=Erosion)
BTErosionado.grid(row=3, column=1,sticky='w', padx=5, pady=3)
IconErosionado= Label(miFrameM,image=IEErosion, bg= mycolorGris)
IconErosionado.grid(row=3, column=0, padx=5, pady=3)
#BotonDilatado

def dilatacion():
    global cont4
    global cont7
    global RutaD
    global IErosion
    global RutaV
    cont4 += 1
    cont7 += 1
    _, frame = cap.read()
    if cont7<3:
        Repdilatacion(RutaV)
    elif cont7>4:
        Repdilatacion(RutaD)

def Repdilatacion(ruta2):
    global cont4
    global RutaD
    global IDilatacion
    img_ = cv2.imread(ruta2, cv2.IMREAD_ANYCOLOR)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.dilate(img_, kernel)
    img_ = cv2.resize(erosion, (300, 300))
    img_resized = cv2.imwrite(filename=str(cont4) + 'dilatacion.png', img=img_)
    RutaD = "C:/Users/arman/PycharmProjects/Interfaz/" + str(cont4) + "dilatacion.png"
    IDilatacion = PhotoImage(file=RutaD)

BTDilatado= Button(miFrameM,text='Dilatado',font=('Century Gothic',18), fg='white', bg= mycolorGris,borderwidth=0, command=dilatacion)
BTDilatado.grid(row=4, column=1,sticky='w', padx=5, pady=3)
IconDilatado= Label(miFrameM,image=IDDilatacion, bg= mycolorGris)
IconDilatado.grid(row=4, column=0, padx=5, pady=3)
#BotonLimpieza
BTLimpiar= Button(miFrameM,text='Limpiar',font=('Century Gothic',18), fg='white', bg= mycolorGris,borderwidth=0)
BTLimpiar.grid(row=5, column=1,sticky='w', padx=5, pady=3)
IconLimpiar= Label(miFrameM,image=ILimpiar, bg= mycolorGris)
IconLimpiar.grid(row=5, column=0, padx=5, pady=3)
#BotonCrear carpeta
def CrearCarpeta():
    ruta= 'C:/Users/arman/PycharmProjects/Interfaz/Images/'
    global TFBuscar
    carpeta= TFBuscar.get()
    os.makedirs(ruta+carpeta)
BTAcam= Button(miFrameM,text='N. Carpeta',font=('Century Gothic',18), fg='white', bg= mycolorGris,borderwidth=0, command=CrearCarpeta)
BTAcam.grid(row=6, column=1,sticky='w', padx=5, pady=3)
IconAcam= Label(miFrameM,image=IAcamara, bg= mycolorGris)
IconAcam.grid(row=6, column=0, padx=5, pady=3)
#BotonCerrarCam
BTCcam= Button(miFrameM,text='Cerrar Cam.',font=('Century Gothic',18), fg='white', bg= mycolorGris,borderwidth=0)
BTCcam.grid(row=7, column=1,sticky='w', padx=5, pady=3)
IconCcam= Label(miFrameM,image=ICcamara, bg= mycolorGris)
IconCcam.grid(row=7, column=0, padx=5, pady=3)
#BotonEntrenar
def NuevoPerfil ():
    cont8 = 0
    global TFBuscar
    Wey= TFBuscar.get()
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cont8 += 1
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            cv2.imwrite('C:/Users/arman/PycharmProjects/Interfaz/Images/'+str(Wey)+'/'+str(cont8) +str(Wey)+'.png',gray[y:y + h, x:x + w])
            print(cont8)
        if cont8 == 100:
            cv2.destroyAllWindows()
            break
        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
BTPuntos= Button(miFrameM,text='Nuevo Perfil',font=('Century Gothic',18), fg='white', bg= mycolorGris,borderwidth=0, command=NuevoPerfil)
BTPuntos.grid(row=8, column=1,sticky='w', padx=5, pady=3)
IconPuntos= Label(miFrameM,image=IPuntos, bg= mycolorGris)
IconPuntos.grid(row=8, column=0, padx=5, pady=3)
#Entrenar
def Entrenar():
    cascPath = "Cascades/haarcascade_frontalface_alt2.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    reconocimiento = cv2.face.LBPHFaceRecognizer_create()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR, "Images")
    current_id = 0
    etiquetas_id = {}
    y_etiquetas = []
    x_entrenamiento = []
    for root, dirs, archivos in os.walk(image_dir):
        for archivo in archivos:
            if archivo.endswith("png") or archivo.endswith("jpg"):
                pathImagen = os.path.join(root, archivo)
                etiqueta = os.path.basename(root).replace(" ", "-")
                if not etiqueta in etiquetas_id:
                    etiquetas_id[etiqueta] = current_id
                    current_id += 1
                id_ = etiquetas_id[etiqueta]
                pil_image = Image.open(pathImagen).convert("L")
                tamanio = (300, 300)
                imagenFinal = pil_image.resize(tamanio, Image.ANTIALIAS)
                image_array = np.array(pil_image, "uint8")
                rostros = faceCascade.detectMultiScale(image_array, 1.5, 5)
                for (x, y, w, h) in rostros:
                    roi = image_array[y:y + h, x:x + w]
                    x_entrenamiento.append(roi)
                    y_etiquetas.append(id_)
    with open("labels.pickle", 'wb') as f:
        pickle.dump(etiquetas_id, f)

    reconocimiento.train(x_entrenamiento, np.array(y_etiquetas))
    reconocimiento.save("entrenamiento.yml")
BTPuntos= Button(miFrameM,text='Entrenar',font=('Century Gothic',18), fg='white', bg= mycolorGris,borderwidth=0, command=Entrenar)
BTPuntos.grid(row=9, column=1,sticky='w', padx=5, pady=3)
IconPuntos= Label(miFrameM,image=IGuardar, bg= mycolorGris)
IconPuntos.grid(row=9, column=0, padx=5, pady=3)
#GuardarComparar
def comparar():
    cascPath = "Cascades/haarcascade_frontalface_alt2.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    eyeCascade = cv2.CascadeClassifier("Cascades/haarcascade_eye.xml")
    smileCascade = cv2.CascadeClassifier("Cascades/haarcascade_smile.xml")
    reconocimiento = cv2.face.LBPHFaceRecognizer_create()
    reconocimiento.read("entrenamiento.yml")
    etiquetas = {"nombre_persona": 1}
    with open("labels.pickle", 'rb') as f:
        pre_etiquetas = pickle.load(f)
        etiquetas = {v: k for k, v in pre_etiquetas.items()}
    web_cam = cv2.VideoCapture(0)
    while True:
        ret, marco = web_cam.read()
        grises = cv2.cvtColor(marco, cv2.COLOR_BGR2GRAY)
        rostros = faceCascade.detectMultiScale(grises, 1.5, 5)
        for (x, y, w, h) in rostros:
            roi_gray = grises[y:y + h, x:x + w]
            roi_color = marco[y:y + h, x:x + w]
            id_, conf = reconocimiento.predict(roi_gray)
            if conf >= 4 and conf < 85:
                font = cv2.FONT_HERSHEY_SIMPLEX
                nombre = etiquetas[id_]
                if conf > 50:
                    nombre = "Desconocido"
                color = (255, 255, 255)
                grosor = 2
                cv2.putText(marco, nombre, (x, y), font, 1, color, grosor, cv2.LINE_AA)
            img_item = "my-image.png"
            cv2.imwrite(img_item, roi_gray)
            cv2.rectangle(marco, (x, y), (x + w, y + h), (0, 255, 0), 2)
            rasgos = smileCascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in rasgos:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        marco_display = cv2.resize(marco, (1200, 650), interpolation=cv2.INTER_CUBIC)
        cv2.imshow('Reconocimiento', marco_display)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
BTPuntos= Button(miFrameM,text='Comparar',font=('Century Gothic',18), fg='white', bg= mycolorGris,borderwidth=0,command=comparar)
BTPuntos.grid(row=10, column=1,sticky='w', padx=5, pady=3)
IconPuntos= Label(miFrameM,image=IComparar, bg= mycolorGris)
IconPuntos.grid(row=10, column=0, padx=5, pady=3)
#CerrarComparar
BTCerrar= Button(miFrameM,text='Cerrar App',font=('Century Gothic',18), fg='white', bg= mycolorGris,borderwidth=0)
BTCerrar.grid(row=11, column=1,sticky='w', padx=5, pady=3)
IconCerrar= Label(miFrameM,image=ICerrar, bg= mycolorGris)
IconCerrar.grid(row=11, column=0, padx=5, pady=3)
#EspacioVacio
BTPVacio= Label(miFrameM,text='',font=('Century Gothic',18), fg='white', bg= mycolorGris,borderwidth=0)
BTPVacio.grid(row=12, column=1,sticky='w', padx=5, pady=3)
IconVacio= Label(miFrameM,text="", bg= mycolorGris)
IconVacio.grid(row=12, column=0, padx=5, pady=3)
#EspacioFoto

def FotoOriginal():
    LFoto = Label(MiFrameEfectos, text='Imagen Original', font=('Century Gothic', 18), fg='black', bg='white',
                  borderwidth=0)
    LFoto.grid(row=1, column=0, sticky='w', padx=5, pady=3)
    IOriginal = Label(MiFrameEfectos, image=IFOTO, bg=mycolorBlueB)
    IOriginal.grid(row=0, column=0, ipadx=0, ipady=0)
    IOriginal.after(10, FotoOriginal)
FotoOriginal()

#EspacioEscalaG

def EscalaIteracion():
    LFoto2 = Label(MiFrameEfectos, text='Imagen Escala', font=('Century Gothic', 18), fg='black', bg='white',
                   borderwidth=0)
    LFoto2.grid(row=1, column=1, sticky='w', padx=5, pady=3)
    IEscala = Label(MiFrameEfectos, image=IPrueba, bg=mycolorGreen)
    IEscala.grid(row=0, column=1, ipadx=0, ipady=0)
    IEscala.after(10, EscalaIteracion)
EscalaIteracion()

#EspacioErosion

def ErosionIteracion():
    LFoto3 = Label(MiFrameEfectos, text='Imagen Erosion', font=('Century Gothic', 18), fg='black', bg='white',
                   borderwidth=0)
    LFoto3.grid(row=3, column=0, sticky='w', padx=5, pady=3)
    LErosion = Label(MiFrameEfectos, image=IErosion, bg=mycolorGreen)
    LErosion.grid(row=2, column=0, ipadx=0, ipady=0)
    LErosion.after(10, ErosionIteracion)
ErosionIteracion()

#EspacioDilatacion

def DilatacionItereacion():
    LFoto4= Label(MiFrameEfectos,text='Imagen Dilatacion',font=('Century Gothic',18), fg='black', bg= 'white',borderwidth=0)
    LFoto4.grid(row=3, column=1,sticky='w', padx=5, pady=3)
    LEDilatacion= Label(MiFrameEfectos,image=IDilatacion, bg= mycolorBlueB)
    LEDilatacion.grid(row=2, column=1, ipadx=0, ipady=0)
    LEDilatacion.after(10, DilatacionItereacion)
DilatacionItereacion()

raiz.mainloop()

