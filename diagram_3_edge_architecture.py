import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 10))

# Define colors
colors = {
    'iot': '#4CAF50',
    'edge': '#FF9800', 
    'gateway': '#2196F3',
    'processing': '#9C27B0',
    'local': '#607D8B'
}

# IoT Devices Layer
iot_y = 8.5
iot_devices = [
    {'name': 'Sensors', 'icon': 'S', 'x': 1},
    {'name': 'Cameras', 'icon': 'C', 'x': 3},
    {'name': 'Mobile\nDevices', 'icon': 'M', 'x': 5},
    {'name': 'Vehicles', 'icon': 'V', 'x': 7},
    {'name': 'Wearables', 'icon': 'W', 'x': 9}
]

# Draw IoT devices
for device in iot_devices:
    # Device circle
    device_circle = Circle((device['x'], iot_y), 0.4, facecolor=colors['iot'], 
                          edgecolor='black', linewidth=2)
    ax.add_patch(device_circle)
    ax.text(device['x'], iot_y, device['icon'], ha='center', va='center', 
            fontsize=14, fontweight='bold', color='white')
    ax.text(device['x'], iot_y-0.8, device['name'], ha='center', va='center', 
            fontsize=9, fontweight='bold')

# Edge Gateways Layer
gateway_y = 6.5
gateways = [
    {'name': 'Gateway 1', 'x': 2},
    {'name': 'Gateway 2', 'x': 5},
    {'name': 'Gateway 3', 'x': 8}
]

# Draw gateways
for gateway in gateways:
    gateway_box = FancyBboxPatch((gateway['x']-0.8, gateway_y-0.4), 1.6, 0.8,
                                boxstyle="round,pad=0.1", facecolor=colors['gateway'],
                                edgecolor='black', linewidth=2)
    ax.add_patch(gateway_box)
    ax.text(gateway['x'], gateway_y, 'GW', ha='center', va='center', 
            fontsize=12, fontweight='bold', color='white')
    ax.text(gateway['x'], gateway_y-0.8, gateway['name'], ha='center', va='center', 
            fontsize=9, fontweight='bold')

# Draw connections from IoT to Gateways
connections = [
    (1, 2), (3, 2),  # Sensors and Cameras to Gateway 1
    (5, 5),          # Mobile to Gateway 2
    (7, 8), (9, 8)   # Vehicles and Wearables to Gateway 3
]

for iot_x, gw_x in connections:
    ax.plot([iot_x, gw_x], [iot_y-0.4, gateway_y+0.4], 'g--', linewidth=2, alpha=0.7)

# Edge Servers Layer
server_y = 4.5
servers = [
    {'name': 'Edge Server A', 'x': 2.5, 'type': 'AI Processing'},
    {'name': 'Edge Server B', 'x': 5, 'type': 'Real-time Analytics'},
    {'name': 'Edge Server C', 'x': 7.5, 'type': 'Local Storage'}
]

# Draw edge servers
for server in servers:
    server_box = Rectangle((server['x']-1, server_y-0.6), 2, 1.2, 
                          facecolor=colors['edge'], edgecolor='black', linewidth=2)
    ax.add_patch(server_box)
    
    # Server rack representation
    for i in range(3):
        rack = Rectangle((server['x']-0.8, server_y-0.4+i*0.25), 1.6, 0.2, 
                        facecolor='white', edgecolor='black', linewidth=1)
        ax.add_patch(rack)
    
    ax.text(server['x'], server_y-1, server['name'], ha='center', va='center', 
            fontsize=10, fontweight='bold')
    ax.text(server['x'], server_y-1.3, server['type'], ha='center', va='center', 
            fontsize=8, style='italic')

# Draw connections from Gateways to Servers
for i, gateway in enumerate(gateways):
    server = servers[i]
    ax.plot([gateway['x'], server['x']], [gateway_y-0.4, server_y+0.6], 
            'b-', linewidth=3, alpha=0.8)

# Local Processing Capabilities
processing_y = 2.5
processing_boxes = [
    {'name': 'Computer\nVision', 'x': 1.5, 'color': '#E91E63'},
    {'name': 'Machine\nLearning', 'x': 3.5, 'color': '#673AB7'},
    {'name': 'Real-time\nControl', 'x': 5.5, 'color': '#3F51B5'},
    {'name': 'Data\nFiltering', 'x': 7.5, 'color': '#009688'},
    {'name': 'Local\nStorage', 'x': 9.5, 'color': '#795548'}
]

for proc in processing_boxes:
    proc_box = FancyBboxPatch((proc['x']-0.6, processing_y-0.4), 1.2, 0.8,
                             boxstyle="round,pad=0.1", facecolor=proc['color'],
                             edgecolor='black', linewidth=1)
    ax.add_patch(proc_box)
    ax.text(proc['x'], processing_y, proc['name'], ha='center', va='center', 
            fontsize=9, fontweight='bold', color='white')

# Data Flow Arrows
ax.text(5.5, 7.5, 'Data Collection', ha='center', va='center', 
        fontsize=12, fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.8))

ax.text(5.5, 5.5, 'Local Processing', ha='center', va='center', 
        fontsize=12, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.8))

ax.text(5.5, 3.5, 'Edge Analytics', ha='center', va='center', 
        fontsize=12, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8))

# Benefits Panel
benefits_box = Rectangle((11, 1), 3, 7.5, facecolor='lightgray', 
                        edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(benefits_box)

benefits_text = """EDGE COMPUTING
BENEFITS

⚡ Ultra-Low Latency
📍 Data Locality
🔒 Enhanced Privacy
💾 Reduced Bandwidth
🔄 Real-time Processing
🛡️ Improved Security

APPLICATIONS:
• Autonomous Vehicles
• Industrial IoT
• Smart Cities
• AR/VR Systems
• Healthcare Monitoring

CHALLENGES:
• Limited Resources
• Device Management
• Heterogeneity
• Security at Scale"""

ax.text(12.5, 4.75, benefits_text, ha='center', va='center', 
        fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

# Local Decision Making
decision_y = 1
decision_box = FancyBboxPatch((1, decision_y-0.3), 9, 0.6,
                             boxstyle="round,pad=0.1", facecolor=colors['processing'],
                             edgecolor='black', linewidth=2, alpha=0.8)
ax.add_patch(decision_box)
ax.text(5.5, decision_y, 'LOCAL DECISION MAKING & IMMEDIATE RESPONSE', 
        ha='center', va='center', fontsize=12, fontweight='bold', color='white')

# Add latency indicators
latency_indicators = [
    {'x': 2, 'y': 7.8, 'text': '<1ms'},
    {'x': 5, 'y': 5.8, 'text': '<5ms'},
    {'x': 8, 'y': 3.8, 'text': '<10ms'}
]

for indicator in latency_indicators:
    latency_circle = Circle((indicator['x'], indicator['y']), 0.3, 
                           facecolor='red', edgecolor='white', linewidth=2)
    ax.add_patch(latency_circle)
    ax.text(indicator['x'], indicator['y'], indicator['text'], 
            ha='center', va='center', fontsize=8, fontweight='bold', color='white')

# Set title
ax.set_title('Edge-Only Architecture: Decentralized Computing at Network Edge', 
             fontsize=18, fontweight='bold', pad=20)

# Configure axes
ax.set_xlim(0, 14.5)
ax.set_ylim(0.5, 9.5)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('/workspace/diagram_3_edge_architecture.png', dpi=300, bbox_inches='tight')
plt.savefig('/workspace/diagram_3_edge_architecture.pdf', bbox_inches='tight')
plt.show()