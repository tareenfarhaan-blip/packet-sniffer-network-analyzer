import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP, ICMP

# ===================== PACKET STORAGE =====================
packet_data = []

# ===================== PACKET PROCESSING =====================
def process_packet(packet):
    if IP in packet:
        protocol = "OTHER"
        dst_port = 0

        if TCP in packet:
            protocol = "TCP"
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            dst_port = packet[UDP].dport
        elif ICMP in packet:
            protocol = "ICMP"

        packet_data.append({
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Source IP": packet[IP].src,
            "Destination IP": packet[IP].dst,
            "Destination Port": dst_port,
            "Protocol": protocol,
            "Size": len(packet)
        })

# ===================== CAPTURE PACKETS =====================
print("Capturing 100 packets...")

sniff(prn=process_packet, count=100, store=False)

print("Capture completed.")

# ===================== CREATE DATAFRAME =====================
df = pd.DataFrame(packet_data)

# ===================== SAVE CSV =====================
df.to_csv("captured_packets.csv", index=False)
print("CSV saved: captured_packets.csv")

# ===================== TERMINAL LOG =====================
print("\n================ FIRST 20 PACKETS ================\n")

for _, row in df.head(20).iterrows():
    print(
        f"{row['Time']} | "
        f"{row['Source IP']} -> {row['Destination IP']} | "
        f"{row['Protocol']} | "
        f"PORT {row['Destination Port']} | "
        f"SIZE {row['Size']}"
    )

print("\nTOTAL PACKETS:", len(df))

# ===================== ANALYSIS =====================
protocol_counts = df["Protocol"].value_counts()

tcp = protocol_counts.get("TCP", 0)
udp = protocol_counts.get("UDP", 0)
icmp = protocol_counts.get("ICMP", 0)
other = protocol_counts.get("OTHER", 0)

labels = ["TCP", "UDP", "ICMP", "OTHER"]
values = [tcp, udp, icmp, other]

top_src = Counter(df["Source IP"]).most_common(5)
top_dst = Counter(df["Destination IP"]).most_common(5)
top_ports = Counter(df["Destination Port"]).most_common(5)

# ===================== SAVE FUNCTION =====================
def save(name):
    plt.savefig(name, dpi=300, bbox_inches="tight")

# ===================== PIE =====================
plt.figure(figsize=(6,6))
plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%",
    colors=["skyblue","lightgreen","salmon","orange"]
)
plt.title("Protocol Distribution")
save("01_protocol_pie.png")
plt.show()

# ===================== BAR =====================
plt.figure(figsize=(6,5))
plt.bar(labels, values, color="purple")
plt.title("Protocol Count")
save("02_protocol_bar.png")
plt.show()

# ===================== SOURCE IP =====================
plt.figure(figsize=(8,5))
plt.bar(
    [x[0] for x in top_src],
    [x[1] for x in top_src],
    color="dodgerblue"
)
plt.xticks(rotation=45)
plt.title("Top Source IPs")
save("03_source_ips.png")
plt.show()

# ===================== DESTINATION IP =====================
plt.figure(figsize=(8,5))
plt.bar(
    [x[0] for x in top_dst],
    [x[1] for x in top_dst],
    color="green"
)
plt.xticks(rotation=45)
plt.title("Top Destination IPs")
save("04_destination_ips.png")
plt.show()

# ===================== PORTS =====================
plt.figure(figsize=(7,5))
plt.bar(
    [str(x[0]) for x in top_ports],
    [x[1] for x in top_ports],
    color="orange"
)
plt.title("Top Destination Ports")
save("05_ports.png")
plt.show()

# ===================== DASHBOARD =====================
fig, axs = plt.subplots(2,2,figsize=(14,9))

fig.suptitle(
    "NETWORK TRAFFIC ANALYTICS DASHBOARD",
    fontsize=18,
    fontweight="bold"
)

fig.text(
    0.5,
    0.93,
    f"TOTAL PACKETS: {len(df)} | TCP:{tcp} UDP:{udp} ICMP:{icmp} OTHER:{other}",
    ha="center",
    fontsize=11,
    bbox=dict(facecolor="lightgray")
)

axs[0,0].pie(
    values,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)
axs[0,0].set_title("Protocol Distribution")

axs[0,1].bar(labels, values, color="purple")
axs[0,1].set_title("Protocol Count")

axs[1,0].bar(
    [x[0] for x in top_src],
    [x[1] for x in top_src],
    color="dodgerblue"
)
axs[1,0].tick_params(axis="x", rotation=45)
axs[1,0].set_title("Top Source IPs")

axs[1,1].bar(
    [x[0] for x in top_dst],
    [x[1] for x in top_dst],
    color="green"
)
axs[1,1].tick_params(axis="x", rotation=45)
axs[1,1].set_title("Top Destination IPs")

plt.tight_layout(rect=[0,0,1,0.90])
save("06_dashboard_summary.png")
plt.show()
