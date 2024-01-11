import pyttsx3
import speech_recognition as sr
#gui import
from tkinter import *
#1
def ipaddress():
    from num2words import num2words
    import socket
    from plyer import notification
    import os
    i= str(os.getcwd()+ '\\callls.ico')
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    speak(f"IP address of Hostname: {hostname} is")
    print(hostname)
    print(ip_address)
    a=str(ip_address).replace(".","")
    notification.notify(title="Your IP Address", message=str(ip_address),app_icon = i,timeout = 5)
    for i in range(0,len(a)):
        c=a[i]
        speak(num2words(c))
#2        
def battery():
    from plyer import notification
    import psutil
    from num2words import num2words
    import os
    i= str(os.getcwd()+ '\\callls.ico')
    try:
        battery=psutil.sensors_battery()
        percent=battery.percent
        notification.notify(title="Battery Percentage", message=str(percent)+ "%Percent Remaining",app_icon = i,timeout = 5)
        a=num2words(percent, to='ordinal')+'percentage sir'
        speak(a)
    except:
        
        notification.notify(title="Battery Percentage", message="No Battery Found",app_icon = i,timeout = 5)
        speak("your device as no battery")
#3
def shutdown(c):
    import os
    try:
        from num2words import num2words
        numbers = [int(word) for word in c.split() if word.isdigit()]
        numbertowords=str(num2words(numbers[0]))
        speak("shutting down the computer in "+numbertowords+" seconds")
        code="shutdown /s /t "+str(numbers[0])
        os.system(code)
        print(code)
    except:
        speak("shutting the computer")
        os.system("shutdown /s /t 1")



#4
def deviceconfig():
    import wmi
    c = wmi.WMI( )
    my_system = c.Win32_ComputerSystem()[0]
    print(f"Manufacturer: {my_system.Manufacturer}")
    print(f"Model: {my_system. Model}")
    print(f"Name: {my_system.Name}")
    print(f"NumberOfProcessors:{my_system.NumberOfProcessors}")
    print(f"SystemType: {my_system. SystemType}")
    print(f"SystemFamily: {my_system. SystemFamily}")
    speak(f"Manufacturer: {my_system.Manufacturer}")
    speak(f"Model: {my_system. Model}")
    speak(f"Name: {my_system.Name}")
    speak(f"NumberOfProcessors:{my_system.NumberOfProcessors}")
    speak(f"SystemType: {my_system. SystemType}")
    speak(f"SystemFamily: {my_system. SystemFamily}")
#5
def opens(c):
    def notepad():
        import os
        speak("opening notepad")
        os.system("Notepad")
    def whatsapp():
        import webbrowser
        webbrowser.open('https://web.whatsapp.com/')
        speak("opening Whatsapp")
    def chrome():
        import webbrowser
        webbrowser.open('chrome')
        speak("opening chrome")
    def facebook():
        import webbrowser
        webbrowser.open('https://www.facebook.com/login/web/')
        speak("opening Facebook")
    def instgram():
        import webbrowser
        webbrowser.open('https://www.instagram.com/')
        speak("opening Instagram")
    def youtube():
        import webbrowser
        webbrowser.open('https://www.youtube.com/')
        speak("opening Youtube")
    def twitter():
        import webbrowser
        webbrowser.open('https://twitter.com/login')
        speak("opening Twitter")
    def controlpanel():
        import os
        os.system("control panel")
        speak("opening control panel")
    def systemsetting():
        import os
        os.system("start ms-settings:")
        speak("opening system settings")
    def cmd():
        import subprocess
        subprocess.call(['cmd.exe'])
        speak("opening command prompt")
    def taskmanger():
        import os
        os.system("taskmgr")
    if "chrome" in c:
        chrome()
    if "whatsapp" in c:
        whatsapp()
    if "controlpanel" in c.replace(" ",""):
        controlpanel()
    if "systemsetting" in c.replace(" ",""):
        systemsetting()
    if "cmd" in c or "command prompt" in c or "terminal" in c:
        cmd()
    if "facebook" in c:
        facebook()
    if "instagram" in c:
        instgram()
    if "youtube" in c:
        youtube()
    if "notepad" in c:
        notepad()
    if "taskmanager" in c.replace(" ",""):
        taskmanger()
    if "twitter" in c:
        twitter()
        
#6
def question(c):
    import information
    a=information.question(c)
    speak(a)
#7
def dateandtime(c):
    from datetime import datetime
    from num2words import num2words 
    from plyer import notification
    import os
    i= str(os.getcwd()+ '\\callls.ico')
    def date():
        now=datetime.now()
        date=now.strftime("%d/%m/%Y")
        a=str(date).replace("/","")
        y=a[4]+a[5]+a[6]+a[7]
        m=a[2]+a[3]
        d=a[0]+a[1]
        notification.notify(title="Date", message=str(date),app_icon = i,timeout = 10)
        speak(num2words(d) + num2words(m) + num2words(y))
        
    def time():
        now = datetime.now()
        time=now.strftime("%H:%M:%S")
        a=str(time).replace(":","")
        h=a[0]+a[1]
        m=a[2]+a[3]
        notification.notify(title="Time", message=str(time),app_icon = i,timeout = 10)
        speak(num2words(h) + num2words(m))

    def day():
        day=datetime.today().strftime('%A')
        notification.notify(title="Day", message=str(day),app_icon = i,timeout = 10)
        speak(day)
        
    if "date" in c:
        date()
    if "time" in c:
        time()
    if "day" in c:
        day()
#8
def wifi(c):
    def passwordchecker():
        import pyperclip
        root = Tk()
        root.geometry("400x400")
        pass_details = StringVar()
        def see_wifi_pass():
            import subprocess
            global myList
            myList=[]
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
            for i in profiles:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    myList.append(i)
                    myList.append("--")
                    myList.append(results[0])
                    myList.append("|")
                except IndexError:
                    myList.append(i)
                    myList.append("--")
                    myList.append("")
        def show_wifi_pass():
            pass_details.set(myList)
        def copytoclipboard():
            password = pass_details.get()
            pyperclip.copy(password)
        if 1==1:
            see_wifi_pass()
        Label(root, text="\nWIFI SCRABER\n", font="calibri 30 bold" ,fg='deeppink').pack()
        Entry(root, textvariable=pass_details, width=50).pack(pady=10)
        speak("sir please click on Show wifi pass details button to show all your saved password")
        Button(root, text="Show wifi pass details", command=show_wifi_pass).pack(pady=10)
        Button(root, text="Copy to clipbord", command=copytoclipboard).pack(pady=10)
        root.mainloop()
    def disconnectwifi():
        import os
        from plyer import notification
        i= str(os.getcwd()+ '\\callls.ico')
        os.system("netsh wlan disconnect")
        notification.notify(title="WI-FI", message="Wi-Fi disconnected",app_icon = i,timeout = 10)
        speak("Wi-Fi is disconnected")

    def wifidetail():
        import subprocess
        devices = subprocess.check_output(['netsh','wlan','show','interface'])
        devices = devices.decode('ascii')
        devices= devices.replace("\r","")
        print(devices)
        speak(devices)

    if "disconnect" in c:
        disconnectwifi()
    if "password" in c:
        passwordchecker()
    if "detail" in c or "signal" in c or "about" in c or "strength" in c:
        wifidetail()
#9
def videodownloader(c):
    def youtube():
        from pytube import YouTube
        root = Tk()
        root.geometry("400x350")
        root.title("Youtube video downloader application")
        def download():
            try:
                myVar.set("Downloading...")
                speak(" your video is downloading please wait") 
                root.update()
                YouTube(link.get()).streams.first().download()
                link.set("Video downloaded successfully")
                speak("your video is downloaded successfully")
            except Exception as e:
                myVar.set("Mistake")
                speak("your are entered the invalid link")
                root.update()
                link.set("Enter correct link")
                speak("Enter correct link")
        Label(root, text="YOUTUBE\n VIDEO DOWNLOADER", font="calibri 20 bold" ,fg='deeppink').pack()
        myVar = StringVar()
        myVar.set("Enter the link below")
        Entry(root, textvariable=myVar, width=50).pack(pady=10)
        link = StringVar()
        Entry(root, textvariable=link, width=50).pack(pady=10)
        Button(root, text="Download video", command=download).pack()
        root.mainloop()
    if "youtube" in c:
        youtube()
#10
def restart(c):
    import os
    try:
        from num2words import num2words
        numbers = [int(word) for word in c.split() if word.isdigit()]
        numbertowords=str(num2words(numbers[0]))
        speak("restarting the computer in "+numbertowords+" seconds")
        os.system("shutdown /r /t "+str(numbers[0]))
    except:
        speak("restarting the computer")
        os.system("-s /r /t 1")
#11
def search(c):
    import webbrowser
    cs=c.split()
    cs.remove("search")
    j=' '.join(cs)
    webbrowser.open('https://www.google.com/search?q='+j)
    speak("searching "+j)
        
#12
def joke():
    import pyjokes
    import os
    from plyer import notification
    i= str(os.getcwd()+ '\\callls.ico')
    My_joke = pyjokes.get_joke(language="en", category="neutral")
    notification.notify(title="JOKE", message=str(My_joke),app_icon = i,timeout = 25)
    speak(My_joke)

#13
def datait():
    if "name" in c:
        speak("i am call")
    if "owner" in c:
        speak("my owner is Aravind Raj")
    if "creator" in c:
        speak("my creator is Aravind Raj")
    if "founder" in c:
        speak("my founder is Aravind Raj")
    if "subscription" in c:
        speak("limit less subscription ")
    if "lifespan" in c:
        speak("my life is limitless")
    if "birthday" in c:
        speak("since 2020, i am corona batch monster baby")
    if "age" in c:
        speak("No age for me i am always young    and   new")
 
#14
def close(c):
    def chrome():
        import os
        try:
            os.system("taskkill /im chrome.exe /f")
        except:
            speak("Chrome is not in use")
    def python():
        import os
        try:
            os.system("taskkill /im pythonw.exe /f")
        except:
            speak("Python is not in use")
    def devc():
        import os
        try:
            os.system("taskkill /im devcpp.exe /f")
        except:
            speak("dev c plus plus is not in use")
    def cmd():
        import os
        try:
            os.system("taskkill /im cmd.exe /f")
        except:
            speak("Command prompt is not in use")
    def notepad():
        import os
        try:
            os.system("taskkill /im notepad.exe /f")
        except:
            speak("Notepad is not in use")
    
    if "all" in c:
        speak("closing aLL the application")
        chrome()
        python()
        devc()
        cmd()
        notepad()
        speak("all the application are closed")
    if "chrome" in c:
        speak("closing chrome")
        chrome()
    if "python" in c:
        speak("closing python")
        python()
    if "notepad" in c:
        speak("closing notepad")
        notepad()
    if "cmd" in c or "command prompt" in c.replace(" ","") or "terminal" in c:
        speak("closing command prompt")
        cmd()
    if "closedevc" in c.replace(" ",""):
        speak("closing c programing")
        devc()
#15
def usage(c):
    def cpu():
        import psutil
        from num2words import num2words
        from plyer import notification
        import os
        i= str(os.getcwd()+ '\\callls.ico')
        try:
            numbers = [int(word) for word in c.split() if word.isdigit()]
            numbertowords=str(num2words(numbers[0]))
            a=psutil.cpu_percent(numbers[0])
            notification.notify(title="Usage CPU", message="The usage CPU in "+str(numbers[0])+" second is "+str(a)+"%",app_icon = i,timeout = 10)
            speak("The usage CPU  in "+numbertowords+" second  is  "+numbertoword+" percentage")
        except:
            a=str(psutil.cpu_percent(1))
            numbertoword=str(num2words(a))
            notification.notify(title="Usage CPU", message="The usage of CPU in 1 second is"+str(a),app_icon = i,timeout = 10)
            speak("The usage of CPU in one second   is  "+numbertoword)
    def ram():
        import psutil
        from plyer import notification
        import os
        i= str(os.getcwd()+ '\\callls.ico')
        print('RAM memory % used:', psutil.virtual_memory()[2])
        notification.notify(title="Usage RAM", message="The usage RAM memory using"+str(psutil.virtual_memory()[2])+"%" ,app_icon = i,timeout = 10)
        speak('RAM memory using'+str(psutil.virtual_memory()[2])+'%')
        

    if "cpu" in c or "computer" in c or "pc" in c:
        cpu()
    if "ram" in c :
        ram()

#16
def boostperformance(c):
    import os
    from plyer import notification
    i= str(os.getcwd()+ '\\callls.ico')
    def tempfiledelete():
        from plyer import notification
        os.system("del /q/f/s %TEMP%\*")
        
        speak("temporary files deleted ")
    def caches():
        from plyer import notification
        os.system("ipconfig/flushDNS")
        speak("caches cleaned")
    if "boost" in c or "increase" in c:
        tempfiledelete()
        caches()
        notification.notify(title="Performance Increased", message="Temporary Files Deleted Successfully \n Cache Cleaned Successfully",app_icon = i,timeout = 0.2)
        speak("your pc performance is increased")
    if "cache" in c:
        caches()
        
    if "temp" in c:
        tempfiledelete()
        notification.notify(title="Temporary Files", message="Deleted Successfully",app_icon = i,timeout = 0.2)
#17
def goto(c):
    import webbrowser
    cs=c
    try:
        a=cs.replace("goto ","")
    except:
        try:
            a=cs.replace("go to ","")
        except:
            a=cs.replace("gotu ","")
    j='https://'+str(a)
    webbrowser.open(j)
#18
def screen(c):
    if "shot" in c:
        import numpy as np
        import cv2
        import pyautogui
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        cv2.imwrite("image1.png", image)
        speak("screen shot taken")
    if "record" in c:
        speak("recording started")
        speak("to stop recording press q")
        import pyautogui
        import cv2
        import numpy as np
        resolution = (1920, 1080)
        codec = cv2.VideoWriter_fourcc(*"XVID")
        # Specify name of Output file
        filename = "Recording.avi"
        # Specify frames rate. We can choose any
        # value and experiment with it
        fps = 60.0
        # Creating a VideoWriter object
        out = cv2.VideoWriter(filename, codec, fps, resolution)
        # Create an Empty window
        # Resize this window
        while True:
        # Take screenshot using PyAutoGUI
            img = pyautogui.screenshot()
  
            # Convert the screenshot to a numpy array
            frame = np.array(img)
  
            # Convert it from BGR(Blue, Green, Red) to
            # RGB(Red, Green, Blue)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  
            # Write it to the output file
            out.write(frame)
            # Stop recording when we press 'q'
            if cv2.waitKey(1) == ord('q'):
                speak("ok sir")
#19                
def brightnesscrt(c):
    import os
    try:
        from num2words import num2words
        numbers = [int(word) for word in c.split() if word.isdigit()]
        numbertowords=str(num2words(numbers[0]))
        speak("Changing brightness to "+numbertowords+" percent")
        os.system("Powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,"+str(numbers[0])+")")
    except:
        speak("Brightness cannot be change because intergrated graphic")
        os.system("Powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,75)")

#20
def switches(c):
    c=c.replace(" ","")
    if "light" in c:
        if "turnon" in c:
            firebasedataupdater("pi message","switch1on")
            speak("light is turned on")
        else:
            firebasedataupdater("pi message","switch1off")
            speak("light is turned off")
    if "fan" in c:
        if "turnon" in c:
            firebasedataupdater("pi message","switch2on")
            speak("fan turned on")
        else:
            firebasedataupdater("pi message","switch2off")
            speak("fan turned off")
#21
def hibernate():
    import os
    os.system("shutdown /h /f")
#22
def sleep():
    import os
    os.system("shutdown /h")
    
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        import firebasesforcontrolpc
        c = firebasesforcontrolpc.getdata()
        c=c.lower()
        print(c)
        if "stop" in c.replace(" ",""):
            speak("ok sir")
            firebasesforcontrolpc.senddata("")
            break
        if "close" in c:
            close(c)
            #firebasesforcontrolpc.senddata("")
        if "who" in c or "what" in c or "where" in c:
            question(c)
            firebasesforcontrolpc.senddata("")
        if "battery" in c.replace(" ",""):
            battery()
            firebasesforcontrolpc.senddata("")
        if "open" in c.replace(" ",""):
            opens(c)
            import os
            os.system("taskkill /im cmd.exe /f")
            firebasesforcontrolpc.senddata("")
        if "shutdown" in c.replace(" ",""):
            #shutdown(c)
            print("shutting the computer")
            #firebasesforcontrolpc.senddata("")
            break
        if "restart" in c.replace(" ",""):
            restart(c)
            firebasesforcontrolpc.senddata("")
            break
        if "sleep" in c.replace(" ",""):
            sleep()
            firebasesforcontrolpc.senddata("")
        if "hibernate" in c.replace(" ",""):
            hibernate()
            firebasesforcontrolpc.senddata("")
        if "search" in c:
            firebasesforcontrolpc.senddata("")
            search(c)
        if "brightness" in c:
            firebasesforcontrolpc.senddata("")
            brightnesscrt(c)
        if "goto" in c or "gotu" in c or "go to" in c:
            goto(c)
            firebasesforcontrolpc.senddata("")
        if "date" or "time " or "day" in c:
            dateandtime(c)
            firebasesforcontrolpc.senddata("")
        if "usage" in c:
            firebasesforcontrolpc.senddata("")
            usage(c)
        if "boost" in c or "performance" in c or "delete" in c:
            boostperformance(c)
            firebasesforcontrolpc.senddata("")
        if "wi-fi" in c:
            wifi(c)
            firebasesforcontrolpc.senddata("")
        if "download" in c:
            videodownloader(c)
            firebasesforcontrolpc.senddata("")
        if "configuration" in c:
            deviceconfig()
            firebasesforcontrolpc.senddata("")
        if "ip" in c:
            ipaddress()
            firebasesforcontrolpc.senddata("")
        if "your" in c or "you" in c:
            datait()
            firebasesforcontrolpc.senddata("")
        if "fan" in c:
            switches(c)
            firebasesforcontrolpc.senddata("")
        if "light" in c:
            switches(c)
            firebasesforcontrolpc.senddata("")
        if "joke" in c:
            joke()
            firebasesforcontrolpc.senddata("")
        if "program" in c and "close" in c:
            speak("ok sir")
            firebasesforcontrolpc.senddata("")
            break
        if "screen" in c:
            firebasesforcontrolpc.senddata("")
            screen(c)
        if "shutup" in c.replace(" ",""):
            firebasesforcontrolpc.senddata("")
            speak("ok")
            break
