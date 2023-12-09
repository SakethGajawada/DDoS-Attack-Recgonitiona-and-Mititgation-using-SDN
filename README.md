# DDoS-Attack-Recgonitiona-and-Mititgation-using-SDN

# Introduction
Distributed denial of service (DDoS) attacks pose a grave threat to the stability and security of online networks. By hijacking vulnerable devices and forming powerful "botnets", malicious actors can unleash a crippling barrage of traffic to cripple even the most robust of systems. As our digital lives continue their rapid migration online, ensuring uninterrupted access and dependable service has never been more important.

# Motivation 
In today's hyperconnected world, even moments of downtime can have outsized consequences. When bad actors bring servers to their knees with floods of malicious traffic, more is disrupted than just bits and bytes - businesses suffer, communication halts, and vital services risk outage. Traditional defenses have struggled to keep pace with the evolving tactics of sophisticated DDoS attackers. There is an urgent need for innovative solutions capable of detecting and mitigating these advanced threats at the speed and scale demanded in modern networks. By leveraging the programmability of Software Defined Networking, this project aims to develop a proactive, prevention-oriented approach for thwarting DDoS attacks before damage can be done. With SDN's centralized control and real-time traffic analysis, anomalous patterns indicative of an incoming attack can be identified with unprecedented acuity. Countermeasures can then be deployed with lightning speed through dynamic, automated rule adjustments. 

# Tools Used 
The key tools used in this project are:
* Mininet - For emulating a virtual SDN network topology
* sFlow - For collecting flow-level network traffic statistics
* Ryu Controller - For implementing the SDN control logic
* hping3 - For generating attack traffic in the Mininet topology
  
# Installation 
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


# Working
* Ensure the Installation is properly done without any errors.
* Run the following command to start sFlow-RT and run the ryu.js script
    ```
    env "RTPROP=-Dscript.file=$PWD/ryu.js" sflow-rt/start.sh
    ```
* Start the Mininet Topology. Either run the Topology.py or directly make a simple mininet topology using the below command

    ```
    sudo mn --custom sflow-rt/extras/sflow.py --link tc,bw=10 --controller=remote,ip=127.0.0.1 --topo tree,depth=2,fanout=2
    ```

    or 

    ```
    sudo python3 topology.py
    ```

* Run ryu application
    ```
    ryu-manager ryu.app.simple_switch_13 ryu.app.ofctl_rest
    ```

* Enable the Sflow in the switch s1
    ```
    sudo ovs-vsctl -- --id=@sflow create sflow agent=lo target=127.0.0.1 sampling=10 polling=10 -- -- set bridge s1 sflow=@sflow
    ```

* Open the sflow-rt Dashboard
    ```
    http://localhost:8008/html/index.html
    ```
    Open the mininet dashboard from the menu.

# Results

## SFLOW and Mininet Dashboard

<img src="![Alt text](images/sflow.png)" />

## Mininet