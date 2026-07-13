## Date: 07/2026

**Topic:** Packets & Frames (TryHackMe)

**Notes:**

- **Packet**: a piece of data at the Network layer (Layer 3).
- **Frame**: a Data Link layer (Layer 2) container that wraps the packet and adds extra info — like the MAC address.

**TCP/IP model (4 layers — different grouping than the OSI 7-layer model):**

```
Application
Transport
Internet
Network Interface
```

**TCP — the three-way handshake:**

Requires an established connection before any data moves.

|Step|Message|What it does|
|---|---|---|
|1|SYN|Client initiates — sends its Initial Sequence Number (ISN)|
|2|SYN/ACK|Server responds with its own ISN + acknowledges the client's|
|3|ACK|Client acknowledges the server's ISN, connection now open|
|—|DATA|Actual data transmitted|
|—|FIN|Clean, graceful connection close|
|—|RST|Abrupt termination — something went wrong|

Worked example from the room:

```
SYN     — Client:  "My ISN is 0"
SYN/ACK — Server:  "My ISN is 5000, I acknowledge your 0"
ACK     — Client:  "I acknowledge your 5000, here's data at 0+1"
```

**TCP tradeoffs:**

- ✅ Guarantees data integrity (checksum), keeps data in order, prevents flooding
- ❌ Requires a reliable connection — if one chunk is lost, the whole thing has to be resent; slower than UDP because of all the overhead

**Key TCP header fields:** Source/Destination Port, Source/Destination IP, Sequence Number, Acknowledgement Number, Checksum, Data, Flags

**UDP — stateless, no handshake:**

- ✅ Much faster than TCP, no reserved connection, app decides how fast to send
- ❌ Doesn't care if data actually arrives — no delivery guarantee, bad on unstable connections

**Key UDP header fields:** TTL (packet expiry timer), Source/Destination Address, Source/Destination Port, Data

**Common ports:**

|Protocol|Port|Use|
|---|---|---|
|FTP|21|File transfer, client-server|
|SSH|22|Secure remote login, text-based|
|HTTP|80|Web traffic, unencrypted|
|HTTPS|443|Web traffic, encrypted|
|SMB|445|File/device sharing (printers etc.)|
|RDP|3389|Remote desktop, GUI-based login|

**Learned:** This directly explains what my `ufw allow OpenSSH` command in Stage 1 was actually doing — allowing TCP traffic on port 22, specifically. SSH needs TCP (not UDP) because a remote terminal session absolutely cannot tolerate lost or out-of-order data — you need every keystroke and command output to arrive intact and in sequence, which is exactly what TCP's three-way handshake and sequencing guarantee.

This also explains why my `ssh.exec_command()` calls in labcheck work reliably — Paramiko is running over SSH (port 22, TCP), so I don't need to worry about dropped or reordered command output the way I might with a UDP-based protocol.

Security group rules in AWS (coming up in VPC work) will specify a port + protocol combination exactly like this table — e.g. "allow TCP port 22 from my IP" is precisely what I'll configure for SSH access to EC2 instances.