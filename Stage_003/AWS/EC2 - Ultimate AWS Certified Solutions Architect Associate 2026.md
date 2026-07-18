

EC2 Fundaments 
- EC2 - Elastic Compute Cloud  = Infrastructure as a service 
- Consist of 
	- Renting virtual machine (EC2)
	- Storing data on virtual Driver (EBS)
	- Distributing load machines (ELB)
	- Scaling the service using auto-scaling groups (ASG)

EC2 Sizing & Configuration options 
- OS: Linux, MAC OS, Windows 
- How much CPU
- How much storage space 
	- Network - attached (EBS & EFS)
	- Hardware (EC2 instance store)
- Network card: speed of card, public IP address
- Firewall rules: Security group
- Bootstrap script (config first launch): EC2 User Data 

EC2 User Data
- bootstrap instance using EC2 User Data script
- launching commands when machine starts 
- Automate boot task
	- installing update
	- installing software
	- downloading common files from the web
	- anything
	- runs with root user

EC2 Instance Types
- AWS naming conventions 
	- m5.2xLarge
		- m - instance class
		- 5 - generation
		- 2xLarge - size within instance class 
- General Purpose 
	- great for diversity of workloads 
		- web servers or code repo
	- Balance between
		- compute, memory & network 
- Compute Optimized
	- Great for compute intensive task
		- Ex: Batch processing workloads, media transcoding, high performance web server, scientific modeling & machine learning, high performance computing, dedicated game servers 
- Memory Optimized
	- Fast performance workload that process large data set in memory 
		- Ex: Distributed web scale cache stores, in-memory data optimized for business intelligence, Apps performing real-time processing of big unstructured data 
- Store Optimized
	- Great for storage-intensive task that require, sequential read/write access to large data sets on local storage 
		- EX: high frequency online transaction processing system, Relational & NoSQL databases, cache for in-memory database (Redis), Data warehouse applications, distributed file system

Security Groups 
- Control how traffic is allowed in or out EC2 Instance 
- only contain allow rules 
- Reference by IP or by Security Group 
- Firewall on EC2 instance
- Regulate 
	- Access to ports
	- Authorized IP ranges (IPV4 & IPV6)
- Can be attached to multiply instances
- Locked down to a region/ VPC Combination 
- Live outside EC2
- Good to main one security group for SSH Access 
- All inbound traffic is blocked 
- All outbound traffic is authorized by default 

Classic Ports to know 
- 22 = SSH (Secure Shell)
- 21 = FTP (File Transfer Protocol) - upload into file share 
- 22 = SFTP (Secure File Transfer Protocol) - upload file using SSH
- 80 = HTTP - access unsecured website 
- 443 HTTS - access to secured website 
- 3389 = RDP (Remote Desktop Protocol)

EC2 Instance Purchasing Options 
	