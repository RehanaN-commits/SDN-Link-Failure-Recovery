# SDN Link Failure Detection and Recovery

##  Project Description
This project demonstrates link failure detection and recovery in a Software Defined Network (SDN) using Mininet and the POX controller.

The controller dynamically installs flow rules using the OpenFlow protocol. When a link failure occurs, connectivity is disrupted, and upon restoration, normal communication resumes.

---

##  Objectives
- Monitor network topology using SDN
- Detect link failures in the network
- Demonstrate dynamic flow rule behavior
- Restore connectivity after failure

---

##  Tools & Technologies
- Mininet (Network Emulator)
- POX Controller
- OpenFlow Protocol
- Ubuntu (WSL)

---

##  Network Topology
- 1 Switch (s1)
- 3 Hosts (h1, h2, h3)
- All hosts connected to a single switch

---

##  Execution Steps

### Step 1: Start POX Controller
```bash
cd ~/pox
./pox.py log.level --DEBUG forwarding.l2_learning
```

### Step 2: Start Mininet
```bash
sudo mn --controller=remote,ip=127.0.0.1,port=6633 --topo=single,3
```

### Step 3: Test Connectivity
```bash
pingall
```

Expected Output:
```
0% dropped
```

### Step 4: Simulate Link Failure
```bash
h2 ifconfig h2-eth0 down
pingall
```

Expected Output:
- Packet loss observed

### Step 5: Recover the Network
```bash
h2 ifconfig h2-eth0 up
pingall
```

Expected Output:
```
0% dropped
```

---

##  Results

###  Normal Operation
- All hosts communicate successfully
- No packet loss

###  Link Failure
- Communication disrupted
- Packet loss observed

###  Recovery
- Connectivity restored
- Normal communication resumes

---

##  Working Principle
- The switch sends packet_in messages to the controller
- The controller installs flow rules (match + action)
- Traffic is forwarded based on learned MAC addresses
- When a link fails, communication breaks
- When restored, new flow rules re-enable communication

---

##  Conclusion
This project demonstrates how SDN enables centralized control and dynamic network behavior. It highlights how link failures affect communication and how recovery restores connectivity.

---

## Future Enhancements
- Automatic link failure detection
- Dynamic rerouting using multiple paths
- Load balancing using SDN controller logic


---

##  Project Structure
```
SDN-Link-Failure-Recovery/
│
├── README.md
├── link_failure_recovery.py
├── commands.txt
└── screenshots/
    ├── 1_normal.png
    ├── 2_failure.png
    └── 3_recovery.png
    └── 4_flows.png
    └── 5_iperf.png


##  Author
- Name: Rehana N
- Course: Computer Networks 

--- 