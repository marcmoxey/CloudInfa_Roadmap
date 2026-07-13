## Date: 07/2026

**Topic:** What is Networking? (TryHackMe)

**Notes:**

- Networking = how devices communicate with each other; the internet is just many small private and public networks joined together.
- **IP Address**: identifies a device. 4 octets (e.g. `192.168.1.1`). Public IP identifies a device on the internet; private IP identifies a device among other devices on a local network. Can be reassigned to a different device, but not two devices at once.
- **MAC Address**: hardware address, globally unique (though can be spoofed/faked).
- **Ping (ICMP)**: sends packets to test connectivity/performance between devices.

**Learned:** Public vs private IP is the same distinction I already implemented hands-on in Stage 1 — `192.168.0.52` (private, Netplan) vs my EC2's public IP `3.146.255.160` (reachable from the internet) and its private IP `172.31.2.166` (only reachable inside AWS's network). The theory confirms what I already built.
