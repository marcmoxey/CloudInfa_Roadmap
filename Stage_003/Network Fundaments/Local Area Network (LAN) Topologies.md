## Date: 07/2026

**Topic:** Local Area Network (LAN) Topologies (TryHackMe)

**Notes:**

**Topologies:**

- **Star**: every device connects individually to a central networking device (switch/router). Scalable and reliable, but more expensive and maintenance grows with scale.
- **Bus**: all devices share a single backbone cable. Slow, bottlenecked (one cable, all traffic), single point of failure.
- **Ring**: devices connected in a loop, data passes device to device until it reaches the target. Each device sends its own data first before passing along others'.

**Core devices:**

- **Router**: connects separate networks and passes data between them.
- **Switch**: aggregates multiple devices within ONE network using ethernet, using packet switching to direct traffic to the right device.

**Subnetting:**

- Splits one network into smaller networks (subnets).
- A subnet mask determines how many hosts can fit in a subnet.
- Three address types within a subnet:
    - **Network Address** — identifies the subnet itself exists
    - **Host Address** — identifies a specific device on the subnet
    - **Default Gateway** — the address that lets a device send traffic OUT to a different network

**ARP (Address Resolution Protocol):**

- Maps a device's MAC address to its IP address.
- **ARP Request**: broadcast to the network — "who owns this IP address?"
- **ARP Reply**: the owning device responds with its MAC address; requester caches this mapping.

**DHCP (Dynamic Host Configuration Protocol):**

- How a device gets an IP address automatically (vs manually/statically assigned).
- 4-step handshake: **Discover** (device asks if any DHCP server exists) → **Offer** (server proposes an IP) → **Request** (device confirms it wants that IP) → **ACK** (server confirms, device can now use it).

**Learned:** This is the missing piece that makes my Stage 1 Netplan config make sense at a deeper level. When I set `dhcp4: no` and manually specified `addresses: - 192.168.0.52/24`, I was explicitly OPTING OUT of the DHCP Discover/Offer/Request/ACK handshake and hardcoding what DHCP would otherwise have assigned automatically. My router's `via: 192.168.0.1` in the routes section is literally the "Default Gateway" concept from this room.

The Star topology description matches my actual home network exactly — Beelink, PC, and (eventually) NAS all connect individually to my router, which is the central networking device.

**Direct connection to upcoming VPC work:** Subnetting here (network address / host address / default gateway) is the exact same three concepts I'll configure explicitly in AWS VPC: a CIDR block for the network, individual EC2 instances as hosts, and a route table pointing to an Internet Gateway as the gateway.