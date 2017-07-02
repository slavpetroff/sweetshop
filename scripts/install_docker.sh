sudo apt-get remove -y docker docker-engine
sudo apt-get update

sudo apt-get install -y \
    linux-image-extra-$(uname -r) \
    linux-image-extra-virtual
	
curl -fsSL 'https://sks-keyservers.net/pks/lookup?op=get&search=0xee6d536cf7dc86e2d7d56f59a178ac6c6238f52e' | sudo apt-key add -

sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
	
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
   
sudo add-apt-repository \
   "deb https://packages.docker.com/1.12/apt/repo/ \
   ubuntu-$(lsb_release -cs) \
   main"

sudo apt-get update

sudo apt-get install -y docker-engine

sudo groupadd docker

sudo usermod -aG docker $USER

echo "PLEASE DO REBOOT OR DO LOGOUT ! ! ! ! !"

echo "Rebooting your system! You have 1 minute to CTRL+C to terminate the reboot process. Please reboot the machine, so changes could take effect!"

sleep 1m

sudo reboot now
