# Packet Sniffer and Network Analyzer

## Group Members

- Farhaan Sher
- Manahil Nousherwani

---

## Project Description

This project is a simple Packet Sniffer and Network Analyzer developed using Python. It captures live network packets, analyzes different network protocols, stores packet information in a CSV file, and visualizes the collected data using graphs.

The main objective of this project is to understand basic network traffic analysis and packet capturing techniques.

---

## Features

- Capture live network packets
- Analyze TCP, UDP, and ICMP protocols
- Save packet details in a CSV file
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

The program will:

- Capture network packets
- Save packet information into a CSV file
- Generate protocol distribution graph
- Display top active IP addresses

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

### Protocol Distribution

![Protocol Distribution](figures/protocol_distribution.png)

### Top Active IP Addresses

![Top Active IPs](figures/top_ips.png)

---

## Conclusion

This project demonstrates the basic concepts of packet capturing and network traffic analysis using Python. It helps users understand how packets travel through a network, identify commonly used protocols, and visualize network activity through graphs.

---

## Thank You
