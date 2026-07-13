# ===================== IMPORTS =====================
import pandas as pd
import random
from collections import Counter
from datetime import datetime


# ===================== PACKET GENERATION =====================
def generate_packets(n=120):
    ips = [
        "192.168.1.1", "192.168.1.2", "10.0.0.5",
        "10.0.0.6", "8.8.8.8", "1.1.1.1"
    ]

    protocols = ["TCP", "UDP", "ICMP", "OTHER"]
    ports = [80, 443, 22, 21, 53, 8080]

    data = []

    for _ in range(n):
        proto = random.choice(protocols)

        data.append({
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Source IP": random.choice(ips),
            "Destination IP": random.choice(ips),
            "Destination Port": random.choice(ports),
            "Protocol": proto,
            "Size": random.randint(60, 1500)
        })

    return pd.DataFrame(data)


# ===================== MAIN DATA CREATION =====================
df = generate_packets(120)

# ===================== SAVE CSV =====================
df.to_csv("packets.csv", index=False)
print("✅ packets.csv saved successfully")


# ===================== PROTOCOL ANALYSIS =====================
protocol_counts = df["Protocol"].value_counts().to_dict()

tcp_count = protocol_counts.get("TCP", 0)
udp_count = protocol_counts.get("UDP", 0)
icmp_count = protocol_counts.get("ICMP", 0)
other_count = protocol_counts.get("OTHER", 0)

protocol_labels = ["TCP", "UDP", "ICMP", "OTHER"]
protocol_values = [tcp_count, udp_count, icmp_count, other_count]


# ===================== TOP VALUES =====================
top_src = Counter(df["Source IP"]).most_common(5)
top_dst = Counter(df["Destination IP"]).most_common(5)
top_ports = Counter(df["Destination Port"]).most_common(5)


# ===================== EXPORT DATA =====================
analysis_data = {
    "df": df,
    "protocol_labels": protocol_labels,
    "protocol_values": protocol_values,
    "top_src": top_src,
    "top_dst": top_dst,
    "top_ports": top_ports
}