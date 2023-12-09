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

[Installation Setup](Installation_Setup)

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
    Open the mininet dashboard from apps in the menu.
* Run hping3 to attack the network
  ```
  h1 hping3 --flood --udp -k -s 53 h3
  ```
# Results
### The below image shows the initialization of sflow-rt.
<div align="center">
  <img src="https://github.com/SakethGajawada/DDoS-Attack-Recgonitiona-and-Mititgation-using-SDN/blob/main/images/sflow.png" />
</div>

### Construct the topology using mininet either using direct command or using the topology.py. The below diagram is an example of a simple topology with 4 hosts and 3 switches.
  <div align="center">
  <img src="https://github.com/SakethGajawada/DDoS-Attack-Recgonitiona-and-Mititgation-using-SDN/blob/main/images/topo.png"  width="400"/>
  <img src="https://github.com/SakethGajawada/DDoS-Attack-Recgonitiona-and-Mititgation-using-SDN/blob/main/images/mininet.png" />
</div>

### Start Ryu application simple switch and ofctl rest, Simple switch is for switching and ofctl rest to communicate to ryu application for adding the blockage of flow when an attack is detected/recognized. 
  <div align="center">
  <img src="https://github.com/SakethGajawada/DDoS-Attack-Recgonitiona-and-Mititgation-using-SDN/blob/main/images/ryu_manager.png" />
  </div>
  
### Configure s1 flow (include SFlow)
<div align="center">
  <img src="https://github.com/SakethGajawada/DDoS-Attack-Recgonitiona-and-Mititgation-using-SDN/blob/main/images/flow-rule.png" />
</div>

### Pingall to ensure our topology is connected to ryu controller and working.
### Open localhost:8008 and view mininet dashborad.
### Start attacking/flooding the network. Either run the the hping3 command mentioned earlier or any one of the generate_ddos_traffic.py/generate_ddos_traffic_1.py.
### Below Digaram of mininet dasbhboard shows the sudden spike in the transfer rate of incoming packets.
<div align ="center">
<img src="https://github.com/SakethGajawada/DDoS-Attack-Recgonitiona-and-Mititgation-using-SDN/blob/main/images/ddos_attack.png" />
</div>

### The below diagram shows that whenever there is flooding happening at a node(host), It is blocked with the help of sflow.  
<div align ="center">
<img src="https://github.com/SakethGajawada/DDoS-Attack-Recgonitiona-and-Mititgation-using-SDN/blob/main/images/blocking.png" />\
</div>

### We can also see the POST command from RYU controller terminal given below communicating with SFlow
<div align ="center">
<img src="https://github.com/SakethGajawada/DDoS-Attack-Recgonitiona-and-Mititgation-using-SDN/blob/main/images/flowentry%20for%20blocking.png" />
</div>
