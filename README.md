<div align="center">

# 🌐 Computer Networks Lab

### Course Code: CSBB 301

*Lab manual and experiment record · Department of Computer Science and Engineering*

</div>

---

## 👤 Student Information

| Field | Details |
|:------|:--------|
| **Name** | CHUNDURI VIKRANTH |
| **Roll No.** | 241210032 |
| **Course** | Computer Networks (CSBB 301) |
| **Department** | Computer Science and Engineering |

---

## 📑 Table of Contents

1. [Experiment Index](#1-experiment-index)
2. [Experiments in Detail](#2-experiments-in-detail)
3. [Requirements](#3-requirements)
4. [Running the Programs](#4-running-the-programs)

---

## 1. Experiment Index

| # | Experiment | Platform / Tool |
|:-:|:-----------|:----------------|
| 01 | Network cables | Hardware |
| 02 | Basic network commands | Command line |
| 03 | Network devices | Hardware |
| 04 | IP addressing | Packet Tracer |
| 05 | LAN connection | Packet Tracer |
| 06 | Router configuration | Packet Tracer |
| 07 | Peer-to-peer network | Packet Tracer |
| 08 | Network Address Translation | Packet Tracer |
| 09 | Routing protocols | Python |
| 10 | TCP and UDP client-server | Packet Tracer, Python |
| 11 | Socket programming | Python |
| 12 | Network tools | NS-3, OMNeT++, GNS3, pfSense, Wireshark, SDN |
| 13 | DHCP server implementation | Packet Tracer |

---

## 2. Experiments in Detail

### 🔌 Part A: Hardware and Basic Commands

#### Experiment 01: Network Cables

> **Tool:** Hardware

- Study the types of network cable: **twisted pair**, **coaxial** and **fibre**.
- Make a **straight-through cable** and a **cross-wired cable** using a crimping tool.

| Cable Type | Connects | Example |
|:-----------|:---------|:--------|
| Straight-through | Unlike devices | PC to switch |
| Cross-wired | Like devices | PC to PC |

#### Experiment 02: Basic Network Commands

> **Tool:** Command line

Use the common commands to check and troubleshoot a network:

```text
ping    ipconfig    tracert    nslookup    netstat    arp    hostname
```

#### Experiment 03: Network Devices

> **Tool:** Hardware

- Study the **hub, switch, bridge, router, repeater** and **access point**.
- Note the layer of operation of each device.
- Learn how each device is installed and connected.

---

### 🖧 Part B: Addressing, LAN and Router Setup

#### Experiment 04: IP Addressing

> **Tool:** Packet Tracer

- Configure **IPv4 addresses**, **subnet masks** and **default gateways** on devices.
- Study address **classes A to E** and the **private address ranges**.

#### Experiment 05: LAN Connection

> **Tool:** Packet Tracer

1. Connect several computers through a switch to form a Local Area Network.
2. Assign addresses in one subnet.
3. Check connectivity with `ping`.

#### Experiment 06: Router Configuration

> **Tool:** Packet Tracer

Configure router interfaces, passwords and routes using the Cisco Packet Tracer CLI.

```text
enable
configure terminal
interface
ip address
no shutdown
```

#### Experiment 07: Peer-to-Peer Network

> **Tool:** Packet Tracer

- Connect two systems through a switch and a router in a LAN.
- Test communication between them.

#### Experiment 08: Network Address Translation

> **Tool:** Packet Tracer

- Examine **NAT**.
- Configure **PAT (NAT overload)** so that private addresses share one public address.
- Check the translations with:

```text
show ip nat translations
```

---

### 🧭 Part C: Routing and Transport Protocols

#### Experiment 09: Routing Protocols

> **Tool:** Python

A Python simulation of two routing protocols on a **five-router topology**.

| Protocol | Type | Metric / Algorithm | Behaviour |
|:---------|:-----|:-------------------|:----------|
| **RIP** | Distance vector | Hop count | Tables converge in 3 rounds |
| **OSPF** | Link state | Dijkstra's algorithm on link cost | Computes the shortest path by cost |

**Link failure:** OSPF finds a new path after a link is removed.

#### Experiment 10: TCP and UDP Client-Server

> **Tool:** Packet Tracer, Python

**Setup:** The Packet Tracer project `expt10.pkt` has one server, one switch and three PCs in the network `192.168.1.0/24`.

| Device | IP Address |
|:-------|:-----------|
| Server0 | `192.168.1.1` |
| PC1 to PC3 | `192.168.1.2` to `192.168.1.4` |

**Services tested:**

| Service | Protocol | Port | Test |
|:--------|:--------:|:----:|:-----|
| HTTP | TCP | 80 | Web Browser to `http://192.168.1.1` |
| FTP | TCP | 21 | `ftp 192.168.1.1` (user `cisco`) |
| DNS | UDP | 53 | `nslookup www.test.com` |

**Procedure:**

1. Switch to **Simulation mode** and apply the filters TCP, UDP, HTTP, DNS and FTP.
2. Open **Inbound PDU Details** of a packet.
3. Compare the results:
   - **TCP** shows the SYN, SYN-ACK and ACK handshake.
   - **UDP** shows only the ports.

The script `tcp_udp_demo.py` repeats the same comparison in Python.

#### Experiment 11: Socket Programming

> **Tool:** Python

TCP and UDP client-server programs using the Python `socket` module.

| Program | Protocol | Port | Description |
|:--------|:--------:|:----:|:------------|
| TCP echo server | TCP | 7070 | One thread per client, so several clients work at once |
| UDP echo server | UDP | 8080 | Reads each datagram and replies to the sender |

**TCP call sequence:**

```text
socket → bind → listen → accept → recv/send → close
```

---

### 🛠️ Part D: Tools and Services

#### Experiment 12: Network Tools

> **Tool:** NS-3, OMNeT++, GNS3, pfSense, Wireshark, SDN

| Category | Tool |
|:---------|:-----|
| Simulators | NS-3, OMNeT++ |
| Emulators | GNS3, Mininet |
| Firewall | pfSense |
| Packet analyser | Wireshark |
| Software-defined networking | OpenFlow-based SDN |

#### Experiment 13: DHCP Server Implementation

> **Tool:** Packet Tracer

A DHCP server implementation means setting up a server that automatically hands out IP configuration to the computers on a network, so nobody has to type it in on each machine.

The configuration provided to each client:

- IP address
- Subnet mask
- Default gateway
- DNS server

---

## 3. Requirements

| Requirement | Used For |
|:------------|:---------|
| **Python 3.8 or newer** (standard library only) | Python programs |
| **Cisco Packet Tracer** | `expt10.pkt` and Experiments 4 to 8 |
| **Wireshark, NS-3, OMNeT++, GNS3, pfSense and Mininet** | Experiment 12 |

---

## 4. Running the Programs

Run each program from inside its own experiment folder. On Windows, use `python` instead of `python3`.

**Experiment 10: TCP/UDP comparison**

```bash
python3 tcp_udp_demo.py
```

**Experiment 11: TCP client-server**

```bash
# Terminal 1
python3 tcp_server.py

# Terminal 2 (new terminal)
python3 tcp_client.py
```

**Experiment 11: UDP client-server**

```bash
# Terminal 1
python3 udp_server.py

# Terminal 2 (new terminal)
python3 udp_client.py
```

---

<div align="center">

</div>
