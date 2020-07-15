from tkinter import*
import os
from tkinter import ttk,StringVar,Tk,messagebox
import cv2
import numpy as np
import pickle
from tkinter import messagebox


#import tkMessageBox
#import tkFont
from PIL import ImageTk,Image
top=Tk()
top.geometry('1400x1200+0+0')
top.title("FACE RECOGNITION")
label1=Label(top,text='FACE RECOGNITION SYSTEM',font=('arial',40,'bold'),bg='blue',fg='red',width=41)
label1.place_configure(relx=0.01,rely=0)



def file_path():
    print(var6.get())
   
    final_path=os.path.join(var4.get(),var5.get())
    
    final_path1=os.path.join(final_path,var6.get())
    print(final_path1)
    
    
    dir_list3=os.listdir(final_path1)
    print(dir_list3)
    #print(dir_list2[0])
    files=(tuple(dir_list3))
    cbodestination1=ttk.Combobox(top,textvariable=var7,font=('arial',20,'bold'),width=8,)
    cbodestination1["values"]=files
    cbodestination1.current(0)
    cbodestination1.place_configure(relx=0.4,rely=0.6)
    


def folder_list():
    print(var5.get())
    
    hi=os.path.join(var4.get(),var5.get())
    
    print(hi)
    dir_list2=os.listdir(hi)
    print(dir_list2)
    #print(dir_list2[0])
    folder=(tuple(dir_list2))
    cbodestination1=ttk.Combobox(top,textvariable=var6,font=('arial',20,'bold'),width=8,)
    cbodestination1["values"]=folder
    cbodestination1.current(0)
    cbodestination1.place_configure(relx=0.4,rely=0.5)
    combobtn3=Button(top,width=4,bd=2,text='ok',font=('arial',13,'bold'),command=file_path)
             
    combobtn3.place_configure(relx=0.52,rely=0.5)
    


def dir_list():
    print(var4.get())
    dir_list1=os.listdir((var4.get()))
    print(dir_list1)
    #print(dir_list1[0])
    folders=(tuple(dir_list1))
    cbodestination1=ttk.Combobox(top,textvariable=var5,font=('arial',20,'bold'),width=8,)
    cbodestination1["values"]=folders
    cbodestination1.current(0)
    cbodestination1.place_configure(relx=0.4,rely=0.4)
    combobtn2=Button(top,width=4,bd=2,text='ok',font=('arial',13,'bold'),command=folder_list)
             
    combobtn2.place_configure(relx=0.52,rely=0.4)
def submit1():
    global fd

    final_dir1=os.path.join(var4.get(),var5.get())
    
    final_dir2=os.path.join(final_dir1,var6.get())
    final_dir3=os.path.join(final_dir2,var7.get())
    
    opencv(final_dir3)





def cam():
    opencv(0)
def uploadvideo():
    
    #file_name1=Entry(top,textvariable=var1,width=10,font=('arial',25,'bold'))
    #file_name1.place_configure(relx=0.4,rely=0.3)
    cbodestination=ttk.Combobox(top,textvariable=var4,font=('arial',20,'bold'),width=4,)
    cbodestination["values"]=('','G:','E:','F:')
    cbodestination.current(0)
    cbodestination.place_configure(relx=0.4,rely=0.3)
    combobtn1=Button(top,width=4,bd=2,text='ok',font=('arial',15,'bold'),command=dir_list)
             
    combobtn1.place_configure(relx=0.5,rely=0.3)

sumbtn=Button(top,width=10,bd=2,text='submit',font=('arial',20,'bold'),command=submit1)
             
sumbtn.place_configure(relx=0.3,rely=0.8)
sumbtn=Button(top,width=10,bd=2,text='CAM',font=('arial',20,'bold'),command=cam)
             
sumbtn.place_configure(relx=0.5,rely=0.8)



    
    
#======================================================================================
    

def file_path1():
    print(var10.get())
   
    final_path11=os.path.join(var8.get(),var9.get())
    
    final_path111=os.path.join(final_path11,var10.get())
    print(final_path111)
    
    
    dir_list33=os.listdir(final_path111)
    print(dir_list33)
    #print(dir_list2[0])
    files=(tuple(dir_list33))
    cbodestination1=ttk.Combobox(top,textvariable=var11,font=('arial',20,'bold'),width=8,)
    cbodestination1["values"]=files
    cbodestination1.current(0)
    cbodestination1.place_configure(relx=0.1,rely=0.6)
    


def folder_list1():
    print(var9.get())
    
    hi1=os.path.join(var8.get(),var9.get())
    
    print(hi1)
    dir_list22=os.listdir(hi1)
    print(dir_list22)
    #print(dir_list2[0])
    folder1=(tuple(dir_list22))
    cbodestination1=ttk.Combobox(top,textvariable=var10,font=('arial',20,'bold'),width=8,)
    cbodestination1["values"]=folder1
    cbodestination1.current(0)
    cbodestination1.place_configure(relx=0.1,rely=0.5)
    combobtn3=Button(top,width=4,bd=2,text='ok',font=('arial',13,'bold'),command=file_path1)
             
    combobtn3.place_configure(relx=0.2,rely=0.5)
    


def dir_list1():
    print(var8.get())
    dir_list11=os.listdir((var8.get()))
    print(dir_list11)
    #print(dir_list1[0])
    folders1=(tuple(dir_list11))
    cbodestination1=ttk.Combobox(top,textvariable=var9,font=('arial',20,'bold'),width=8,)
    cbodestination1["values"]=folders1
    cbodestination1.current(0)
    cbodestination1.place_configure(relx=0.1,rely=0.4)
    combobtn2=Button(top,width=4,bd=2,text='ok',font=('arial',13,'bold'),command=folder_list1)
             
    combobtn2.place_configure(relx=0.2,rely=0.4)



def submit2():
    final_dir11=os.path.join(var8.get(),var9.get())
    
    final_dir111=os.path.join(final_dir11,var10.get())
    final_dir1111=os.path.join(final_dir111,var11.get())
    print(final_dir1111)
        
        
def uploadimage():
    #file_name2=Entry(top,textvariable=var2,width=10,font=('arial',25,'bold'))
    #file_name2.place_configure(relx=0.1,rely=0.3)
    image=ttk.Combobox(top,textvariable=var8,font=('arial',20,'bold'),width=4,)
    image["values"]=('','G:','E:','F:')
    image.current(0)
    image.place_configure(relx=0.1,rely=0.3)
    combobtn11=Button(top,width=4,bd=2,text='ok',font=('arial',15,'bold'),command=dir_list1)
             
    combobtn11.place_configure(relx=0.2,rely=0.3)

sumbtn1=Button(top,width=10,bd=2,text='submit',font=('arial',20,'bold'),command=submit2)
             
sumbtn1.place_configure(relx=0.1,rely=0.8)    




var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
var10=StringVar()
var11=StringVar()
hi=StringVar()
#===================================== function for image_train================================================



def image_train():
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    print(BASE_DIR)
    IMG_DIR=os.path.join(BASE_DIR,'images')
    print(IMG_DIR)

    face_cascade=cv2.CascadeClassifier('C:\project opencv\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
    #eye_cascade=cv2.CascadeClassifier('C:\project opencv\Lib\site-packages\cv2\data\haarcascade_eye.xml')
    recognizer=cv2.face.LBPHFaceRecognizer_create()




    current_id=0
    label_ids={}
    y_labels=[]
    x_train=[]
    #ex_train=[]
    #ey_labels=[]


    for root,dirs,files in os.walk(IMG_DIR):
        for file in files:
            if file.endswith('png') or file.endswith('jpg'):
                path=os.path.join(root,file)

                label=os.path.basename(os.path.dirname(path)).replace(' ','-').lower()
                
                print(path)
                if not label in label_ids:
                    label_ids[label]=current_id
                    current_id+=1
                id_=label_ids[label]
                #print(label_ids )

                pil_image=Image.open(path).convert('L')
                size=(550,550)
                final_image=pil_image.resize(size,Image.ANTIALIAS)
         
                
                image_array=np.array(final_image,'uint8')
                #print(image_array)
                faces=face_cascade.detectMultiScale(image_array,scaleFactor=1.5,minNeighbors=5)
                #eyes=eye_cascade.detectMultiScale(image_array,scaleFactor=1.5,minNeighbors=5)
                for (x,y,w,h) in faces:
                    roi=image_array[y:y+h,x:x+w]
                    x_train.append(roi)
                    y_labels.append(id_)

                    #for (ex,ey,ew,eh) in faces:
                        #rei=image_array[ey:ey+eh,ex:ex+ew]
                        #ex_train.append(rei)
                        #ey_labels.append(id_)
                    
                 

                
    with open('labels.pickle','wb') as f:
        pickle.dump(label_ids,f)
        
    recognizer.train(x_train,np.array(y_labels))
    #recognizer.train(ex_train,np.array(ey_labels))
    recognizer.save('./recognizer/trainner.yml')



    

train=Button(top,width=10,bd=2,text='upload image',font=('arial',20,'bold'),command=uploadimage)
             
train.place_configure(relx=0.1,rely=0.2)
train=Button(top,width=10,bd=2,text='upload video',font=('arial',20,'bold'),command=uploadvideo)
             
train.place_configure(relx=0.4,rely=0.2)
train=Button(top,width=10,bd=2,text='train image',font=('arial',20,'bold'),command=image_train)
             
train.place_configure(relx=0.7,rely=0.2)

#w=image1.width()
#h=image1.height()
#top.configure(ImageTk.PhotoImage='C:/Users/Chellakkutty/Desktop/img1.jpg')




    
#===========================================================================





def opencv(video_dir):

    face_cascade=cv2.CascadeClassifier('C:\project opencv\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
    eye_cascade=cv2.CascadeClassifier('C:\project opencv\Lib\site-packages\cv2\data\haarcascade_eye.xml')

    #smile_cascade=cv2.CascadeClassifier('C:\project opencv\Lib\site-packages\cv2\data\haarcascade_smile.xml')


    recognizer=cv2.face.LBPHFaceRecognizer_create()



    recognizer.read('./recognizer/trainner.yml')
      


    def rename(fold_path):
        count=0
        for root,dirs,files in os.walk(fold_path):
            for files in files:
                count+=1
        return (count+1)
    def unknown ():
        img_item='my-image.png'
        cv2.imwrite(img_item,roi_color)
        #print("img written")
        
        top=Tk()
        top.geometry('700x400+200+150')
        top.title("NEW FACE DETECTED")
        top.configure(background='white')
        n1=StringVar()  

        def load():
        #inputvalue=textBox.get("1.0","end-1c")
            messagebox.showinfo("Information",n1.get()+' '+'is stored for training,run the trainer to recognize this face')
            top.destroy()
            
       
       
        canvas1=Canvas(top,width=300,height=200)
        canvas2=Canvas(top,width=300,height=200)
        canvas3=Canvas(top,width=300,height=200)
        canvas4=Canvas(top,width=300,height=200)
        canvas1.pack()
        canvas2.pack()
        canvas3.pack()
        canvas4.pack()
        
        
        img=PhotoImage(file='C:\project opencv\my-image.png')
        canvas1.create_image(100,50,anchor=NW,image=img)
        #frame=Frame(top,width=300,height=320,bd=8,relief='raise')
        #frame.create_image(275,100,anchor=NW,image=img)

        label=Label(canvas2,text='Enter NAME OF THIS PERSION',font=('arial',20,'bold'),width=50,justify='center')
        label.pack()
        

        e1=Entry(canvas3,width=15,bd=2,textvariable=n1,font=('arial',20,'bold'))
        e1.pack()
        
        b1=Button(canvas4,text='LOAD',font=('arial',12,'bold'),width=8,justify='center',command=load)
        b1.pack()
        top.mainloop()
        return n1.get()
        
        
        
    def new_train(newname):
        print(len(labels))
        img_path='C:\project opencv\images'
        va=os.path.join(img_path,newname)
        for i in range(0,len(labels)):
           while (newname==labels[i]):
               
           
               
               
                
               #flag=1
               #if flag==1:
               imgname=rename(va)
               img_item=os.path.join(va,(str(imgname)+'.jpg'))
               cv2.imwrite(img_item,roi_color)
               print('yes')
               break
               

           else:
           #while (newname!=labels[i]):
               

               os.mkdir(va)
               img_item=os.path.join(va,'1.jpg')
               cv2.imwrite(img_item,roi_color)
               print('else is excuted')
               break
    
    cap=cv2.VideoCapture(video_dir)
    font=cv2.FONT_HERSHEY_SIMPLEX
    stroke=2
    color=(255,0,230)
    
    
    while(True):
        ret, frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
        labels={'person':0}
        with open('labels.pickle','rb') as f:
           og_labels= pickle.load(f)
           labels={v:k for k,v in og_labels.items()}
        for (x,y,w,h) in faces:
            #print(x,y,w,h)
            cv2.equalizeHist(gray)
            roi_gray=gray[y:y+h,x:x+w]
            roi_color=frame[y:y+h,x:x+w]

            
            id_,conf=recognizer.predict(roi_gray)
            if conf >=60 and conf <=100:
                
                name=labels[id_]
                
               
                #if id_>=0 and id_ <= dic_size:
                print(id_,'-',labels[id_])
                cv2.putText(frame,name,(x,y),font,1,(0,0,250),stroke,cv2.LINE_AA)
                    
            else:     
                cv2.putText(frame,'unknown',(x,y),font,1,(0,150,240),stroke,cv2.LINE_AA)
                print("unknown")
                #new_p=unknown()
                #new_train(new_p)

                                    
            img_item='my-image.png'
            cv2.imwrite(img_item,roi_color)

            color=(250,0,0) #BGR
            stroke=5
            cv2.rectangle(frame,(x,y),(x+w,y+h),color,stroke)
            #eyes=eye_cascade.detectMultiScale(roi_gray)
            #for (ex,ey,ew,eh) in eyes:
                #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,250,0),2)
                
            #smile=smile_cascade.detectMultiScale(roi_gray)
            
            #for(sx,sy,sw,sh) in smile:
                #cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,250,0),1)
                
            
        cv2.imshow('frame',frame)
        k=cv2.waitKey(50)& 0xFF == ord('q')
    
        if k==10:
            break


    cap.release()
    cv2.destroyAllWindows()
        

        
    




  

    
def exitbtn():
    
    qExit=messagebox.askyesno("Quite System","Do you want to quit?")
    if qExit> 0:
        
        #cap.release()
        cv2.destroyAllWindows()
        top.destroy()
        
        return

ebtn=Button(top,width=10,bd=2,text='EXIT',font=('arial',20,'bold'),command=exitbtn)
             
ebtn.place_configure(relx=0.7,rely=0.8)





        

top.mainloop()
