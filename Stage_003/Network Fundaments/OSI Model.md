## Date: 07/2026

**Topic:** OSI Model (TryHackMe)

**Notes:** 7 layers, top to bottom:

|Layer|Name|Responsibility|
|---|---|---|
|7|Application|How the user interacts with data (GUI)|
|6|Presentation|Translates data format between application and network|
|5|Session|Creates, maintains, and closes a connection between two computers|
|4|Transport|Transmits data across the network — **TCP** (reliable, reserves a constant connection) vs **UDP** (fast, no delivery guarantee)|
|3|Network|Determines the most optimal path; handles IP addressing; protocols like OSPF and RIP|
|2|Data Link|Physical addressing via NIC + MAC address|
|1|Physical|Raw electrical signals (0s and 1s) over the physical medium (ethernet cables)|

**Learned:** Layer 3 (Network) and Layer 4 (Transport) are the two layers that matter most for AWS/VPC work:

- **Layer 3** = what VPC, subnets, CIDR blocks, and route tables are all about — determining how traffic gets from one network to another.
- **Layer 4** = what security groups filter on — allowing "SSH from My IP" is a Layer 4 rule (TCP, port 22).

TCP vs UDP maps directly to real decisions: SSH uses TCP (needs a reliable connection), while something like a game server voice channel might use UDP (speed over guaranteed delivery).