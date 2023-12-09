# Installation Setup
## Mininet
Update package indexes from repositories
```
sudo apt update
```
Upgrade any existing packages
```
sudo apt upgrade
```
Install Mininet
```
sudo apt-get install mininet
```
Check Mininet version to verify installation
```
mn --version
```
## sFLow-RT
Download sFlow-RT tarball
```
wget https://inmon.com/products/sFlow-RT/sflow-rt.tar.gz
```
Extract tarball
```
tar -xvzf sflow-rt.tar.gz
```
Install Mininet dashboard plugin
```
sflow-rt/get-app.sh sflow-rt mininet-dashboard
```
Check sFlow-RT version to verify installation
```
sflow-rt/bin/sflow-rt --version
```
## Ryu Controller
Install Ryu SDN controller
```
sudo pip3 install ryu
```
Check Ryu version to verify installation
```
ryu-manager --version
```
## hping3
```
sudo apt-get install hping3
```



