# ===================== IMPORTS =====================
import matplotlib.pyplot as plt
from analyzer import analysis_data

# ===================== EXTRACT DATA =====================
df = analysis_data["df"]

protocol_labels = analysis_data["protocol_labels"]
protocol_values = analysis_data["protocol_values"]

top_src = analysis_data["top_src"]
top_dst = analysis_data["top_dst"]
top_ports = analysis_data["top_ports"]


# ===================== SAVE FUNCTION =====================
def save_fig(name):
    plt.savefig(name, dpi=300, bbox_inches="tight")


# ===================== 1. PIE CHART =====================
plt.figure(figsize=(6, 6))

plt.pie(
    protocol_values,
    labels=protocol_labels,
    autopct="%1.1f%%",
    colors=["#4DA3FF", "#2EE59D", "#FF4D6D", "#FFB020"]
)

plt.title("Protocol Distribution")
save_fig("01_protocol_pie.png")
plt.show()


# ===================== 2. BAR CHART =====================
plt.figure(figsize=(6, 5))

plt.bar(protocol_labels, protocol_values, color="#8A5CFF")

plt.title("Protocol Count")
save_fig("02_protocol_bar.png")
plt.show()


# ===================== 3. TOP SOURCE IP =====================
plt.figure(figsize=(8, 5))

plt.bar([i[0] for i in top_src], [i[1] for i in top_src], color="#4DA3FF")

plt.title("Top Source IPs")
plt.xticks(rotation=45)
save_fig("03_source_ips.png")
plt.show()


# ===================== 4. TOP DESTINATION IP =====================
plt.figure(figsize=(8, 5))

plt.bar([i[0] for i in top_dst], [i[1] for i in top_dst], color="#2EE59D")

plt.title("Top Destination IPs")
plt.xticks(rotation=45)
save_fig("04_destination_ips.png")
plt.show()


# ===================== 5. TOP PORTS =====================
plt.figure(figsize=(8, 5))

plt.bar([str(i[0]) for i in top_ports], [i[1] for i in top_ports], color="#FFB020")

plt.title("Top Destination Ports")
save_fig("05_ports.png")
plt.show()


# ===================== 6. DASHBOARD =====================
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

fig.suptitle("NETWORK DASHBOARD SUMMARY", fontsize=14)

top_ports_text = "\n".join([f"• Port {p}: {c}" for p, c in top_ports])

fig.text(
    0.02, 0.95,
    "TOP DESTINATION PORTS:\n" + top_ports_text,
    fontsize=10,
    va="top",
    ha="left",
    bbox=dict(facecolor="white", alpha=0.7, edgecolor="gray")
)

axs[0, 0].pie(
    protocol_values,
    labels=protocol_labels,
    autopct="%1.1f%%",
    colors=["#4DA3FF", "#2EE59D", "#FF4D6D", "#FFB020"]
)
axs[0, 0].set_title("Protocol distribution")

axs[0, 1].bar(protocol_labels, protocol_values, color="#8A5CFF")
axs[0, 1].set_title("Protocol Count")

axs[1, 0].bar([i[0] for i in top_src], [i[1] for i in top_src], color="#4DA3FF")
axs[1, 0].set_title("Source IPs")

axs[1, 1].bar([i[0] for i in top_dst], [i[1] for i in top_dst], color="#2EE59D")
axs[1, 1].set_title("Destination IPs")

plt.tight_layout(rect=[0, 0, 1, 0.88])
save_fig("06_dashboard_summary.png")
plt.show()