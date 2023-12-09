from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.node import OVSKernelSwitch, RemoteController
from time import sleep
from datetime import datetime
from random import randrange, choice

class CustomTopology(Topo):
    def build(self):
        switches = []
        hosts = []

        for i in range(1, 7):
            switch = self.addSwitch(f's{i}', cls=OVSKernelSwitch, protocols='OpenFlow13')
            switches.append(switch)

            for j in range(1, 4):
                host = self.addHost(f'h{i * 3 + j}', cpu=1.0/20, mac=f"00:00:00:00:00:{i * 3 + j}",
                                     ip=f"10.0.0.{i * 3 + j}/24")
                hosts.append(host)
                self.addLink(host, switch)

        for i in range(5):
            self.addLink(switches[i], switches[i + 1])

def generate_ip():
    return ".".join(["10", "0", "0", str(randrange(1, 19))])

def perform_icmp_flood(source_host, destination_ip):
    print("Performing ICMP (Ping) Flood")
    source_host.cmd(f"timeout 20s hping3 -1 -V -d 120 -w 64 -p 80 --flood {destination_ip}")
    sleep(100)

def perform_udp_flood(source_host, destination_ip):
    print("Performing UDP Flood")
    source_host.cmd(f"timeout 20s hping3 -2 -V -d 120 -w 64 --flood {destination_ip}")
    sleep(100)

def perform_tcp_syn_flood(source_host, destination_ip):
    print("Performing TCP-SYN Flood")
    source_host.cmd(f"timeout 20s hping3 -S -V -d 120 -w 64 -p 80 --flood {destination_ip}")
    sleep(100)

def perform_land_attack(source_host, destination_ip):
    print("Performing LAND Attack")
    source_host.cmd(f"timeout 20s hping3 -1 -V -d 120 -w 64 --flood -a {destination_ip} {destination_ip}")
    sleep(100)

def start_network():
    topo = CustomTopology()
    controller = RemoteController('c0', ip='192.168.0.101', port=6653)
    net = Mininet(topo=topo, link=TCLink, controller=controller)
    net.start()

    # Configure and start web server on h1
    h1 = net.get('h1')
    h1.cmd('cd /home/mininet/webserver')
    h1.cmd('python -m SimpleHTTPServer 80 &')

    hosts = net.hosts

    for _ in range(3):
        src_host = choice(hosts)
        dest_ip = generate_ip()

        perform_icmp_flood(src_host, dest_ip)
        perform_udp_flood(src_host, dest_ip)
        perform_tcp_syn_flood(src_host, dest_ip)
        perform_land_attack(src_host, dest_ip)

        sleep(100)

    net.stop()

if __name__ == '__main__':
    start_time = datetime.now()

    setLogLevel('info')
    start_network()

    end_time = datetime.now()
    print(end_time - start_time)
