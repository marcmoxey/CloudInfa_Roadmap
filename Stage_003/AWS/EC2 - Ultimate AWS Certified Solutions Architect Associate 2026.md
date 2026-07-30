

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
- On Demand Instances
	-  short workload,
	- pay by seconds, 
	- predicable pricing 

- Reserved  (1 & 3 years) 
	- Reserved instanced 
	- Long workloads 
	- Convertible Reversed instances for long workloads and flexible pricing

- Saving Plans (1 & 3 years)
	- Commitment to an amount usage
	- Long workloads

- Spot Instance
	- Short workload
	- cheap
	- can lose instance 
	- less reliable

- Dedicated Host
	-  Book a physical server 
	- control instance placement 

- Dedicated Instance
	- No other customer shares your hardware

- Capacity Reservation 
	- reserve capacity in a specific AZ for any duration 

- EC2 On Demand
	- Pay for what you use
	- Linus or windows is billed per second after first minute
	- Other OS is billed per hour 
	- Highest upfront Cost 
	- No long term commitment ]
	- Recommend for sort term  & un-interrupted workload 

- Reserved Instance
	- Up to 72& discount
	- Reserved a specific instance attributes
	- Reservation Period
		- 1 year discount +
		- 3 year discount +++
	- Payment options 
		- Upfront
		- Partial Upfront 
		- All Upfront 

	- Reserved Instance Scope
		- Regional or Zonal

 - Recommend for stead-state usage apps (database)
 - Buy & sell in reserved instance marketplace

	- Convertible Reserved Instance 
		- can change EC2 instance type. instance family & tenancy
		- 60% discount 

- EC2 Savings Plan
	- discount based on long term usage 
	- commit to certain type of usage 
	- usage beyond EC2 savings plan is billed on Demand price 
	- locked to specific instance family & AWS Region 
	- Flexible across
		- instance size
		- OS
		- Tenancy

- EC2 Spot Instance 
	- Discount up to 90%
	- Instance that can be "lose" at any point & time
	- Cost efficient instance
	- Useful for work loads that are resilient to failure 
		- Batch jobs
		- Data analysis 
		- image  processing 
		- Any distribute workloads
		- Workloads with flexible start and end time 
	- Not suitable for critical jobs or database

- EC2 Dedicated Hosts 
	- Physical server with EC2 instance fully dedicate use case
	- Address compliance requirements & use your existing Server bound software licenses
	- Purchasing Options
		- On Demand - pay per seconds for active
		- Reserved - 1 or 3 years 
	- Expensive option
	- useful for software that have complicated licensing  model (BYOL -  Bring your own license)
	- Companies that have strong regulatory or compliance needs

- EC2 Dedicated Instance 
	- Instances that run on hardware dedicated to you 
	- may share hardware with other instance in same account 

- EC2 Capacity Reservation 
	- Reserved On-Demand instanced capacity in a specific AZ for any duration 
	- Have Access to EC2 when needed 
	- No time commitment; no discount 
	- Combined with regional reserved & Savings plan  to benefit from discount
	- Change on-demand rate whether instances are running or not 
	- Suitable for short term uninterrupted workloads that need to be in specific AZ

- Purchasing option right for me ?
	- On-Demand 
		- Pay for Price 
	- Reserved 
		- Planning ahead, may get discount 
	- Savings Plan 
		- pay certain amount per hour for certain period 
	- Spot instance 
		- Highest bidder keeps instance, can get kicked out anytime 
	- Dedicated host 
		- get own hardware
	- Capacity Reservation
		-  Pay full price for a period even if don't stay 

- EC2 Spot instance request
	-  Can get discount 
	- Define max spot price & get instance while current max price less than max
		- Hourly spot instance price varies base on offer & capacity 
		- If current spot price greater than your max price you can choose to stop or terminate instance within 2min grace period 
	-  Used  for 
		- Batch jobs 
		- Data analysis
		- Workloads resilient to failure
	- Not for critical Job or failure 

- How to terminate Spot Instance
	- Can cancel a request that are open, active or disable 
	- Must first cancel a spot request, then terminate the associated spot instances 

- Spot Fleets 
	- Set of Spot instance + (optional) on-demand instances
	- Try to meet target capacity with price constraints 
		- Define possible launch pools 
		- Can have multiple launch pools, so fleet can choose 
		- Spot fleets stop launching instance when reaching capacity or max cost 

- Strategies to allocate Spot Instances  
	- Lowest price; from pool with the lowest price 
	- Diversified; distributed across all workloads
	- Capacity Optimized pool with optimal capacity number of instance
	- Price Capacity optimized (recommend) pool with the highest capacity 
	- Available the select pool with lowest price 
	- Spot fleet allow us to automatically request Spot instance with the lowest price 

- Private Vs Public (IPV4)
	- Networking has two sorts if IPS; IPV4 & IPV6
	- Two different private network can have the same IP
	- Machines connect to the WWW using internet gateway 
	- Only a specified range or IPs can be used as Private IP

- Elastic IP
	- Stop & Start an EC2 instance; Public IP can change 
	- Attach to one instance at a time
	- try to avoid 

- Placement Groups 
	- Control over EC2 instance placement strategy 
	- Defined using placement group[
	- Strategies for the group 
		- Cluster 
			- Cluster instance into low-latency group in single AZ
		- Spread 
			- Spread instance across underlying hardware (max 7 per AZ)
		- Partition
			- Spreads instance across many different partitions within an AZ

- Placement Group Cluster
	- Great network 
	- If Az falls all instances falls at the same time
	- Use case 
		- Big data that needs to be completed fast
		- Apps that need extremely low latency & high network 

- Placement Groups Spread 
	- Can span across 
	- Reduced risk is simultaneous  failure
	- EC2 instance are on different physical hardware 
	- Limited to 7 instance per AZ per placement group 
	- Use case
		- App the need max high availability 
		- Critical app where each instance must be isolated from failure

- Placement Groups Partition 
	- Up to 7 partitions per AZ 
	- Span across multiple AZs in the same region 
	- UP to 100s of EC2
	- Do not share racks with the instance in the other partitions 
	- A failure won't affect other partitions 
	- EC2 instances get access to partitions into OS metadata 
	- Use Case:
		- HDFS
		- HBASE
		- Cassandra
		- Kafka 

- Elastic Network Interface (ENI)
	- Virtual network card 
	- ENI Attributes 
		- Primary private IPV4, one or more secondary IPV4
		- One Elastic IP Per private  IPV4
		- One public IPV4
		- One or more security groups 
		- Mac Address 
- Create ENI independently move them on EC2 instance for  failover 
- Bound to a specific AZ 

- EC2 Hibernate 
	- Stop - data on disk (EBS) is kept intact in the next start 
	- Terminate - any EEBS volumes (root) also set up to be destroyed is lost 
	- On Start 
		- first start; OS Boot & EC2 User Data script runs
		- OS bott up 
		- application starts, cache gets warm
	
	- Intro EC2 Hibernate 
		- in memory state is preserved 
		- Instance boots faster
		- Ram state is written to a file in root EBS volume
		- Use case
			- Long running processing 
			- Saving ram state 
			- Services that take time to initiation

- EBS Instance Storage 
	- What is EBS Volume 
		- Elastic Block Store volume is a network you can attach to your instance while they run
		- Persist data even after termination
		- Bound to specific AZ
		- Network drive
		- Can be detached from EC2 instance & attached to another one
		- Have to provision capacity in advanced 
		- Delete on termination attribute (EBS)
			- Controls EBS behavior when EC2 instance terminated 
			- Other attached EBS volume is not deleted (disable by default)
		- Use case
			- Preserve root volume when instance is terminated 

- EBS Snapshot 
	- Make a backup of EBS volume at any point & time 
	- Not necessary to detached volume to do snapshot (but recommend)
	- Copy snapshots across AZ or Region
	- Snapshot features 
		- EBS Snapshot Archive 
			- Move snapshot to "archive tier" that is 70% cheaper 
			- Takes 24 to 72 hours for restoring snapshot 
		- Recycle bin for EBS Snapshot 
			- retain deleted snapshot
			-  1 day to 1 year 
		- Fast snapshot restore (ESR)
			- force full initialization of snapshot not latency on first use 

- AMI Overview 
	- AMI - Amazon Machine Image
	- Customization of EC2 Instance 
		- Add your own software, config, OS, monitoring 
		- Faster boot/ config; since software is pre-packed 
	- Built for specific region 
	- Launch EC2 instances from
		- A public AMI - AWS provided
		- you own; make and maintain them yourself
		- AWS marketplace AMI; AMI some else made 
	- AMI Process (from EC2 instance)
		- Start EC2 instance& customize it 
		- Stop the instance (Data integrity)
		- Build AMI; also create EBS Snapshot 
		- Launch instance from other AMIs

- EC2 Instance Store
	- Higher performance
	- Better i/o performance
	- Lose their storage if they are stopped (ephemeral)
	- Good for buffer, cache, scratch data, temporary content 
	- Backups & replication are your responsibility

- EBS Volume / Types 
	- gp2/gp3 (SSD) 
		- General purpose that balance price & performance for wide variety of workloads 
	- io1/io2 Block Express (SSD) 
		- highest performance for mission critical or high-throughput workloads 
	- ST1 (HDD) 
		- Low cost designed for frequently access; throughput; intensive workloads 
	- SC1(HDD) 
		- Low cost designed for less frequently access workloads
	- EBS volumes are characterized in size, throughput, IOPS(i/o ops per seconds)
	-  only gp2/gp3 & io1/io2 block expressions can be used as boot volumes 

- General Purpose SSD 
	- Cost effective storage low-latency 
	- System boot vol8ums, VMs, DEV & Test env 
	- 1gb - 16 TB
	- gp3
		- Baseline of 3000 IOPS & Throughput 
		- Can increase IOPs up to 16000 & throughput up to 1000mb/s -*independent* 
	- gp2
		- small gp2 volumes can burst IOPS to 3000
		- Size of the volume & IOPS are limited, max IOPS is 16000
		- 3 IOPS per GFB at 5334 GB are at max IOPS
		- 
- Provisioned IOPS (PIOPS)
	- Critical business applications with sustained IOPS performance
	- Application that need more than 16,000 IOPS
	- Database workloads (sensitive to storage perf & consistency )
		-io1 (4GB - 16TB)
		- Max PIOPs - 64,000 for Nitro EC2 Instance & 22,000 for other 
		- Can increase independently from storage size 
	- io2 Block Express (4GB - 64TB)
		- sub millisecond latency 
		- Max PIOP: 256,000 with IOPS GB ratio of 1,000 : 1
	- Supports EBS Multi-attach
	- 
- Hard Disk Drives
	- Cannot be boot volume 
	- 125GB to 16 TB
	- Throughput Optimized HDD (st1)
		- Big data warehouse, log processing
		- Max throughput 500 MB - Max IOPS 250
	- Cold HHD (st2)
		- Data that is infrequently accessed
		- Where lowest cost is important
		- Max throughput 250mb - Max IOPS 250
	
- EBS Multi-Attach - io1/io2 family 
	- Attach the same EBS volume to multiple EC2 instance in the same AZ
	- Each instance has full read/write permission to performance volume 
	- Use case
		- higher application availability in clustered 
		- Application must manage concurrent write operations
	- Up to 16 EC2 instance at a time
	- Must  use a file system that cluster aware 
	
- EBS Encryption
	- Data at rest is encrypted inside the volume
	- All data moving between the instance is encrypted 
	- All snapshots are encrypted 
	- All volumes create from snapshot is encrypted 
	- Encryption & decryption are handle transparently 
	- Minimal latency 
	- Leverages keys from KMS (AES-256)
	- Copy unencrypted snapshot allows encryption
	- Snapshot of encrypted volumes are encrypted 
- Encrypt an unencrypted EBS Volume
	- Create an EBS snapshot of volume 
	- Encrypted the EBS snaps (using copy)
	- Create new EBS volume from snapshot
	- Attach the encrypted volume to original instance
	
- Amazon EFS - Elastic File System
	- Manage network file system
	- EC2 instances in multi-AZ
	- Highly available, scale, expensive, pay per use 
	
	- Elastic File System
		- uses NFSv4.1 protocol
		- Uses security group to control access to EFS
		- Only compatible with linux base AMI
		- Encryption at rest using KMS
		- Posix file system(Linux)
		- Filesystem scales automatically
		
	- Performance & Storage classes
		- EFS Scale
		- 1000s of concurrent NFS clients, 10GB/s throughput 
		- Grow to petabyte-scale network file system; automatically
	- Performance mode(set at EFS creation time)
		- General purpose (default) - latency-sensitive
		- Max i/o - higher latency, highly parallel
	- Throughput mode 
		- Brusting - 1TB = 50MB + brust up to 100MB
		- Provisioned - set throughput regardless of stage size 
		- Elastic - automatically scales throughput up or down base own your workload 
	- Storage Tiers (Life cycle management feature - move file after N days)
		- Standard: frequently access files 
		- Infrequent access (EFS-IA): cost to retrieve file lower price to store 
		- Archive: rarely accessed data, 50% cheaper 
		- Implement life cycle polices to move files between storage tiers 
	- Availability & durability 
		- Standard: Multi-Az; great for Prod 
		- One Zone: One AZ ; great for DEV
		
	- Elastic Block Store VS Elastic File System
		- EBS Volume 
			- One instance (Except multi attach io1/io2)
			- Locked at AZ level
			- gp2: IO increase if disk size increase 
			- gp3 & io1: can increase IO independently 
		- To migrate an EBS volume across AZ
			- Take snapshot 
			- Restore snapshot to another AZ
			- EBS backups use IO & shouldn't run while application s handling a lot of traffic 
			- Root EBS volume get terminate by default if EC2 instance get terminate
		- EFS 
			- Mounting 100s of instances across AZ
			- EFS shared file system 
			- Only Linux instance 
			- EFS has higher price point 
			- Can leverage storage tiers for cost saving 
		






