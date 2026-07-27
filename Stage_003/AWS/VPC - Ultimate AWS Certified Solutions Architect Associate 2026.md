 
- VPC
	- Understanding CIDR - IPV4
		- Classless Inter-Domain Routing; method for allocating IP Address
		- Used in security groups and AWS networking in general 
		- They help define an IP address range
			- EX: 
				- WW.XX.YY.ZZ/32 - one IP
				- 0.0.0.0/0 - All Ips
				- 192.168.0.0/26: 192.168.0.0 - 192.168.0.0 - 192.168.0.53 (64 IP address)
					- /24 → 32-24 = 8 bits remaining → 2^8 = 256 addresses
					- /25 → 32-25 = 7 bits remaining → 2^7 = 128 addresses
		- CIDR has two components 
		- Base IP
			- Represents IP contained in the range (XX.XX.XX.XX)
				- EX: 10.0.0.0, 192.168.0.0
		- Subnet mask
			- Defines how many bits change in the IP
				- EX: /10, /24, /32
			- Takes two forms
				- /8 or 255.0.0.0
		- Allows part of the underlying IP to get additional next values from the base IP

	- Public Vs Private (IPV4)
		-  The internet Assigned Number Authority (IANA) established certain blocks of IPV4 address for the use of private (LAN) & public (internet) address  
			- 10.0.0.0 - 10.255.255.255 (10.0.0.0/8) -> Big network
			- 172.16.0.0 - 172.31.255.255 (172.16.0.0/16) -> AWS default VPC in that range
			- 192.168.0.0 - 192.168.255.255/16 -> Home network
		- All the rest of the IP address on the internet are public 
	
	- Default VPC
		- Allow new AWS account have default VPC
		- New EC2 instance are launched into the default VPC if no subject is specified
		- Default VPC has internet connectivity and all EC2 instance inside it have public IPV4 addresses 
		- We also get a public and a private IPV4 DNS name
	- VPC in AWS
		- VPC = Virtual Private Cloud
		- Can have multiple VPCs in AWS Region (Max 5 per region - soft limit)
		- Max CIDR per VPC is 5 for each CIDR
			- Min size is /28
			- Max size /16
		- Only Private IPV4 ranges are allowed 
		- VPC CIDR should NOY overlap with other networks 
	- Subnet 
		- AWS reserves 5 IP addresses (first 4 & last 1) in each  subnet
		- These 5 IP address are not available for use and can't be assigned to EC2 instance 
	- Internet Gateway (IGW)
		- Allow resources in a VPC to connect to the internet
		- Scales horizontally and is highly available & redundant
		- Must be created separately from a VPC
		- Internet gateway on their own do not allows internet access vice versa
		- Route tables must also be edit 
	- Bastion Hosts
		- Use SSH into our private EC2 instance
		- Bastion in public subnet which is then connect to all other private subnet
		- Bastion Host Security group must inbound from internet on port 22 from restricted CIDR
		- Security Group of EC2 instance must allow security group of Bastion host, or private IP of the Bastion host 
	- NAT Instance (outdated on exam)
		- NAT = Network Address Translation
		- Allows EC2 instance in private subnet to connect to internet 
		- Must be launch in public subnet 
		- Must disable EC2 setting Source / destination check
		- Route table must be config to route traffic from private subnets to NAT instance 



	