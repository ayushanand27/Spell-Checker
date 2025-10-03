import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(16, 12))

# Define colors
colors = {
    'device': '#4CAF50',
    'edge': '#FF9800', 
    'fog': '#2196F3',
    'cloud': '#9C27B0',
    'data_flow': '#F44336'
}

# Device Layer (Bottom)
device_y = 1.5
devices = [
    {'name': 'IoT Sensors', 'x': 2, 'icon': 'S'},
    {'name': 'Mobile Devices', 'x': 4, 'icon': 'M'},
    {'name': 'Smart Cameras', 'x': 6, 'icon': 'C'},
    {'name': 'Vehicles', 'x': 8, 'icon': 'V'},
    {'name': 'Wearables', 'x': 10, 'icon': 'W'},
    {'name': 'Industrial IoT', 'x': 12, 'icon': 'I'}
]

# Draw Device Layer
device_layer_box = FancyBboxPatch((1, device_y-0.8), 12, 1.6,
                                 boxstyle="round,pad=0.1", facecolor=colors['device'],
                                 edgecolor='black', linewidth=2, alpha=0.3)
ax.add_patch(device_layer_box)

ax.text(0.5, device_y, 'DEVICE\nLAYER', ha='center', va='center', 
        fontsize=12, fontweight='bold', rotation=90)

for device in devices:
    device_circle = Circle((device['x'], device_y), 0.3, facecolor=colors['device'], 
                          edgecolor='black', linewidth=2)
    ax.add_patch(device_circle)
    ax.text(device['x'], device_y, device['icon'], ha='center', va='center', 
            fontsize=12, fontweight='bold', color='white')
    ax.text(device['x'], device_y-0.6, device['name'], ha='center', va='center', 
            fontsize=8, fontweight='bold')

# Edge Layer
edge_y = 4
edge_nodes = [
    {'name': 'Edge Node A', 'x': 3, 'capability': 'Real-time\nProcessing'},
    {'name': 'Edge Node B', 'x': 7, 'capability': 'Local\nAnalytics'},
    {'name': 'Edge Node C', 'x': 11, 'capability': 'Data\nAggregation'}
]

# Draw Edge Layer
edge_layer_box = FancyBboxPatch((1, edge_y-0.8), 12, 1.6,
                               boxstyle="round,pad=0.1", facecolor=colors['edge'],
                               edgecolor='black', linewidth=2, alpha=0.3)
ax.add_patch(edge_layer_box)

ax.text(0.5, edge_y, 'EDGE\nLAYER', ha='center', va='center', 
        fontsize=12, fontweight='bold', rotation=90)

for edge in edge_nodes:
    edge_box = Rectangle((edge['x']-0.8, edge_y-0.5), 1.6, 1, 
                        facecolor=colors['edge'], edgecolor='black', linewidth=2)
    ax.add_patch(edge_box)
    
    # Add server representation
    for i in range(2):
        server_rect = Rectangle((edge['x']-0.6, edge_y-0.3+i*0.3), 1.2, 0.2, 
                               facecolor='white', edgecolor='black', linewidth=1)
        ax.add_patch(server_rect)
    
    ax.text(edge['x'], edge_y-0.7, edge['name'], ha='center', va='center', 
            fontsize=9, fontweight='bold')
    ax.text(edge['x'], edge_y+0.7, edge['capability'], ha='center', va='center', 
            fontsize=8, style='italic')

# Fog Layer
fog_y = 6.5
fog_nodes = [
    {'name': 'Fog Node 1', 'x': 4.5, 'capability': 'Intermediate\nProcessing'},
    {'name': 'Fog Node 2', 'x': 9.5, 'capability': 'Data\nOrchestration'}
]

# Draw Fog Layer
fog_layer_box = FancyBboxPatch((1, fog_y-0.8), 12, 1.6,
                              boxstyle="round,pad=0.1", facecolor=colors['fog'],
                              edgecolor='black', linewidth=2, alpha=0.3)
ax.add_patch(fog_layer_box)

ax.text(0.5, fog_y, 'FOG\nLAYER', ha='center', va='center', 
        fontsize=12, fontweight='bold', rotation=90)

for fog in fog_nodes:
    fog_box = Rectangle((fog['x']-1, fog_y-0.6), 2, 1.2, 
                       facecolor=colors['fog'], edgecolor='black', linewidth=2)
    ax.add_patch(fog_box)
    
    # Add multiple server representation
    for i in range(3):
        server_rect = Rectangle((fog['x']-0.8, fog_y-0.4+i*0.25), 1.6, 0.2, 
                               facecolor='white', edgecolor='black', linewidth=1)
        ax.add_patch(server_rect)
    
    ax.text(fog['x'], fog_y-0.8, fog['name'], ha='center', va='center', 
            fontsize=9, fontweight='bold')
    ax.text(fog['x'], fog_y+0.8, fog['capability'], ha='center', va='center', 
            fontsize=8, style='italic')

# Cloud Layer
cloud_y = 9
cloud_box = FancyBboxPatch((1, cloud_y-0.8), 12, 1.6,
                          boxstyle="round,pad=0.1", facecolor=colors['cloud'],
                          edgecolor='black', linewidth=3, alpha=0.8)
ax.add_patch(cloud_box)

ax.text(0.5, cloud_y, 'CLOUD\nLAYER', ha='center', va='center', 
        fontsize=12, fontweight='bold', rotation=90)

# Cloud services
cloud_services = [
    {'name': 'Big Data\nAnalytics', 'x': 3},
    {'name': 'Machine Learning\nTraining', 'x': 7},
    {'name': 'Global\nOrchestration', 'x': 11}
]

for service in cloud_services:
    service_box = Rectangle((service['x']-1, cloud_y-0.5), 2, 1, 
                           facecolor=colors['cloud'], edgecolor='black', linewidth=2)
    ax.add_patch(service_box)
    ax.text(service['x'], cloud_y, service['name'], ha='center', va='center', 
            fontsize=10, fontweight='bold', color='white')

# Data Flow Arrows
# Device to Edge connections
device_edge_connections = [(2, 3), (4, 3), (6, 7), (8, 7), (10, 11), (12, 11)]
for dev_x, edge_x in device_edge_connections:
    ax.annotate('', xy=(edge_x, edge_y-0.8), xytext=(dev_x, device_y+0.3),
                arrowprops=dict(arrowstyle='->', lw=2, color=colors['data_flow']))

# Edge to Fog connections
ax.annotate('', xy=(4.5, fog_y-0.8), xytext=(3, edge_y+0.8),
            arrowprops=dict(arrowstyle='->', lw=3, color=colors['data_flow']))
ax.annotate('', xy=(4.5, fog_y-0.8), xytext=(7, edge_y+0.8),
            arrowprops=dict(arrowstyle='->', lw=3, color=colors['data_flow']))
ax.annotate('', xy=(9.5, fog_y-0.8), xytext=(11, edge_y+0.8),
            arrowprops=dict(arrowstyle='->', lw=3, color=colors['data_flow']))

# Fog to Cloud connections
ax.annotate('', xy=(7, cloud_y-0.8), xytext=(4.5, fog_y+0.8),
            arrowprops=dict(arrowstyle='->', lw=4, color=colors['data_flow']))
ax.annotate('', xy=(7, cloud_y-0.8), xytext=(9.5, fog_y+0.8),
            arrowprops=dict(arrowstyle='->', lw=4, color=colors['data_flow']))

# Workload Distribution Panel
workload_box = Rectangle((14.5, 2), 4, 7, facecolor='lightgray', 
                        edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(workload_box)

workload_text = """WORKLOAD
DISTRIBUTION

DEVICE LAYER:
• Data Collection
• Basic Filtering
• Immediate Response

EDGE LAYER:
• Real-time Processing
• Local Decision Making
• Sensor Fusion

FOG LAYER:
• Intermediate Analytics
• Data Aggregation
• Regional Coordination

CLOUD LAYER:
• Complex Analytics
• ML Model Training
• Global Optimization
• Long-term Storage"""

ax.text(16.5, 5.5, workload_text, ha='center', va='center', 
        fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

# Latency and Processing Power Indicators
latency_box = Rectangle((14.5, 0.5), 4, 1.2, facecolor='lightyellow', 
                       edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(latency_box)

latency_text = """LATENCY & PROCESSING
Device: <1ms, Low Power
Edge: 1-10ms, Moderate
Fog: 10-100ms, High
Cloud: 100ms+, Unlimited"""

ax.text(16.5, 1.1, latency_text, ha='center', va='center', 
        fontsize=8, fontweight='bold')

# Dynamic Orchestration
orchestration_y = 10.5
orchestration_box = FancyBboxPatch((3, orchestration_y-0.3), 8, 0.6,
                                  boxstyle="round,pad=0.1", facecolor='red',
                                  edgecolor='black', linewidth=2, alpha=0.8)
ax.add_patch(orchestration_box)
ax.text(7, orchestration_y, 'DYNAMIC WORKLOAD ORCHESTRATION', 
        ha='center', va='center', fontsize=12, fontweight='bold', color='white')

# Bidirectional arrows for orchestration
for x in [3, 7, 11]:
    ax.annotate('', xy=(x, cloud_y+0.8), xytext=(x, orchestration_y-0.3),
                arrowprops=dict(arrowstyle='<->', lw=2, color='red'))

# Set title
ax.set_title('Hybrid Cloud-Edge Architecture: Multi-Tier Distributed Computing', 
             fontsize=18, fontweight='bold', pad=20)

# Configure axes
ax.set_xlim(0, 19)
ax.set_ylim(0.5, 11.5)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('/workspace/diagram_4_hybrid_architecture.png', dpi=300, bbox_inches='tight')
plt.savefig('/workspace/diagram_4_hybrid_architecture.pdf', bbox_inches='tight')
plt.show()