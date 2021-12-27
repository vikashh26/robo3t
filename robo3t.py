import os
os.system("cd /usr/local/bin && sudo rm -rf robo3t")
if "robo-help" in os.listdir():
    os.system("sudo rm -rf robo-help")
os.system("sudo mkdir robo-help && cd robo-help && sudo wget https://download.studio3t.com/robomongo/linux/robo3t-1.4.4-linux-x86_64-e6ac9ec.tar.gz?submissionGuid=f94aa69b-44e1-49e3-b57a-de75c326fa54 && sudo tar -xvzf robo3t* && sudo mv robo3t-1.4.4-linux-x86_64-e6ac9ec robo3t && sudo mv robo3t /usr/local/bin && cd /usr/local/bin/robo3t/bin && sudo chmod +x robo3t ./robo3t && ./robo3t")
os.system("sudo rm -rf robo-help")
path = os.path.abspath(__file__)
os.system("cd && cd Desktop/ && sudo wget https://github.com/vikashh26/robo3t/raw/main/icon.png && sudo mv icon.png /usr/local/bin/robo3t/bin")

open("robo3t.desktop","w").writelines("""
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Robo3t
Icon=/usr/local/bin/robo3t/bin/icon.png
Exec="/usr/local/bin/robo3t/bin/robo3t"
Comment=Robo3t 
Categories=Development;
Terminal=false
StartupNotify=true
""")
os.system("sudo mv robo3t.desktop /usr/share/applications/")

os.system("sudo rm -rf "+path)
