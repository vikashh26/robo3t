sudo apt-get update
cd && cd Desktop/
sudo wget https://download.studio3t.com/robomongo/linux/robo3t-1.4.4-linux-x86_64-e6ac9ec.tar.gz?submissionGuid=f94aa69b-44e1-49e3-b57a-de75c326fa54 && sudo tar -xvzf robo3t*
sudo mv robo3t-1.4.4-linux-x86_64-e6ac9ec robo3t
sudo mv robo3t /usr/local/bin/
cd /usr/local/bin/robo3t/bin
sudo chmod +x robo3t ./robo3t
./robo3t
