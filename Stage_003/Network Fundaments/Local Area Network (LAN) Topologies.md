
**Star Topology** 
- Device are connected individually via c central networking device
	- Scalability and reliability , more expensive
	- More  maintenance the more they scale

**Bus Topology** 
- Relies on a single connection (backbone)
-  Data slow and bottlenecked because each device on the same cable 
-  Single point of failure 

**Ring Topology**
- Device are connected to each other in loops 
- Send data across the loops till it reach the dedicated device 
- if has data to send it will send it own data first before send the other device data 

**What is a Router?** 
-  Connect networks and pass data between them

**What is a Switch?**
- dedicated devices within a network that are designed to aggregate multiple other devices using ethernet 
-  uses packet switch to break down data 

**A Primer on Subnetting**
- Subnetting is split a network into to smaller, miniature networks within itself 
-  Splitting up the number of hosts that can fit within a network, called a subnet mask
	-  Subnets use IP address to  Identify network, host address and default gateway
		-  Network Address - identify network existence 
		- Host Address - identify a device on the subnet 
		- Default Gateway - special address assigned to a device on the network that can send information to another network

**Address Resolution Protocol (ARP)**
- allows a device to associate its MAC address with an IP address on the network

**How does ARP Work?**
- Within a network has a ledger to store information, (cache) 
-  Cache store identifiers of other devices on the network
- ARP Request - message broadcast on the network to other devices asking "What is the mac address that owns the IP address" 
-  ARP Reply - with its MAC address; the requesting device remember this mapping stores it in ARP cache

**Dynamic Host Configuration Protocol (DHCP)**
- device connects to a network, if it has not already been manually assigned an IP address, it sends out a request (DHCP Discover) to see if any DHCP servers are on the network. The DHCP server then replies back with an IP address the device could use (DHCP Offer). The device then sends a reply confirming it wants the offered IP Address (DHCP Request), and then lastly, the DHCP server sends a reply acknowledging this has been completed, and the device can start using the IP Address (DHCP ACK).