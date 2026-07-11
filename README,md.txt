# Packet Sniffer and Network Analyzer

## Group Members

- Farhaan Sher
- Manahil Nousherwani

---

## Project Description

This project is a simple Packet Sniffer and Network Analyzer developed using Python. It captures network packets from the network interface, analyzes different protocols, stores packet information in a CSV file, and presents the collected data using graphs.

The main objective of this project is to understand network traffic analysis and basic packet capturing techniques using Python.

---

## Features

- Capture live network packets
- Analyze network traffic
- Detect different protocols (TCP, UDP, ICMP)
- Save captured packets into a CSV file
- Generate protocol distribution graph
- Display top active IP addresses
- Easy to understand and user-friendly

---

## Tools and Libraries Used

- Python 3
- Scapy
- Pandas
- Matplotlib
- CSV Module

---

## Installation Instructions

### Step 1

Clone the repository.

```bash
git clone https://github.com/yourusername/packet-sniffer-network-analyzer.git
```

### Step 2

Open the project folder.

```bash
cd packet-sniffer-network-analyzer
```

### Step 3

Install the required libraries.

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

Run the following command:

```bash
python src/packet_sniffer.py
```

After running the program:

- Network packets will be captured.
- Packet information will be saved in a CSV file.
- Protocol distribution graph will be generated.
- Top active IP addresses graph will be displayed.

---

## Sample Output

```text
Packet Sniffer Started...

Packet 1
Source IP: 192.168.1.10
Destination IP: 8.8.8.8
Protocol: TCP

Packet 2
Source IP: 192.168.1.15
Destination IP: 142.250.183.78
Protocol: UDP

Packet Capture Completed Successfully.
```

---

## Project Folder Structure

```text
packet-sniffer-network-analyzer/
│
├── README.md
├── requirements.txt
│
├── src/
│   └── packet_sniffer.py
│
├── data/
│   └── captured_packets.csv
│
├── figures/
│   ├── protocol_distribution.png
│   └── top_ips.png
│
├── report/
│   └── final_report.pdf
│
└── screenshots/
    └── output_screenshot.png
```

---

## Screenshots

### Program Output

![Program Output](screenshots/output_screenshot.png)

---

### Protocol Distribution

![Protocol Distribution](figures/protocol_distribution.png)

---

### Top Active IP Addresses

![Top Active IPs](figures/top_ips.png)

---

## Conclusion

The Packet Sniffer and Network Analyzer project demonstrates how Python can be used to capture and analyze network traffic efficiently. It helps users understand packet transmission, identify commonly used protocols, and visualize network activity through graphs. This project provides a practical introduction to network monitoring and packet analysis concepts.

---

## Thank You