import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(16, 10))

# Define colors for different performance levels
colors = {
    'excellent': '#4CAF50',
    'good': '#8BC34A',
    'moderate': '#FFC107',
    'poor': '#FF9800',
    'very_poor': '#F44336'
}

# Define the comparison data
models = ['Cloud Computing', 'Fog Computing', 'Edge Computing']
parameters = [
    'Latency',
    'Processing Power', 
    'Storage Capacity',
    'Scalability',
    'Bandwidth Usage',
    'Energy Efficiency',
    'Security & Privacy',
    'Cost Efficiency',
    'Reliability',
    'Real-time Capability'
]

# Performance matrix (0=Very Poor, 1=Poor, 2=Moderate, 3=Good, 4=Excellent)
performance_matrix = {
    'Cloud Computing': [1, 4, 4, 4, 1, 2, 2, 3, 3, 1],
    'Fog Computing': [2, 3, 3, 3, 2, 3, 3, 2, 3, 2], 
    'Edge Computing': [4, 2, 1, 2, 4, 4, 4, 2, 2, 4]
}

# Color mapping for performance levels
color_map = [colors['very_poor'], colors['poor'], colors['moderate'], 
             colors['good'], colors['excellent']]

# Create the comparison table
table_x = 2
table_y = 8
cell_width = 3
cell_height = 0.6

# Draw headers
header_box = Rectangle((table_x-1, table_y), cell_width*4, cell_height,
                      facecolor='navy', edgecolor='black', linewidth=2)
ax.add_patch(header_box)
ax.text(table_x + cell_width*1.5, table_y + cell_height/2, 'COMPARATIVE ANALYSIS OF COMPUTING MODELS',
        ha='center', va='center', fontsize=14, fontweight='bold', color='white')

# Column headers
col_headers = ['Parameters'] + models
for i, header in enumerate(col_headers):
    header_box = Rectangle((table_x + i*cell_width, table_y-cell_height), cell_width, cell_height,
                          facecolor='darkblue', edgecolor='black', linewidth=1)
    ax.add_patch(header_box)
    ax.text(table_x + i*cell_width + cell_width/2, table_y - cell_height/2, header,
            ha='center', va='center', fontsize=11, fontweight='bold', color='white')

# Draw parameter rows and performance cells
for row, param in enumerate(parameters):
    y_pos = table_y - (row + 2) * cell_height
    
    # Parameter name cell
    param_box = Rectangle((table_x, y_pos), cell_width, cell_height,
                         facecolor='lightblue', edgecolor='black', linewidth=1)
    ax.add_patch(param_box)
    ax.text(table_x + cell_width/2, y_pos + cell_height/2, param,
            ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Performance cells for each model
    for col, model in enumerate(models):
        x_pos = table_x + (col + 1) * cell_width
        performance = performance_matrix[model][row]
        
        perf_box = Rectangle((x_pos, y_pos), cell_width, cell_height,
                            facecolor=color_map[performance], edgecolor='black', linewidth=1)
        ax.add_patch(perf_box)
        
        # Add performance indicators
        indicators = ['★☆☆☆☆', '★★☆☆☆', '★★★☆☆', '★★★★☆', '★★★★★']
        ax.text(x_pos + cell_width/2, y_pos + cell_height/2, indicators[performance],
                ha='center', va='center', fontsize=10, fontweight='bold')

# Legend
legend_x = 2
legend_y = 1.5
legend_box = Rectangle((legend_x, legend_y-0.5), 12, 1.5,
                      facecolor='lightgray', edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(legend_box)

ax.text(legend_x + 6, legend_y + 0.7, 'PERFORMANCE LEGEND', 
        ha='center', va='center', fontsize=12, fontweight='bold')

legend_items = [
    ('★☆☆☆☆ Very Poor', colors['very_poor']),
    ('★★☆☆☆ Poor', colors['poor']),
    ('★★★☆☆ Moderate', colors['moderate']),
    ('★★★★☆ Good', colors['good']),
    ('★★★★★ Excellent', colors['excellent'])
]

for i, (text, color) in enumerate(legend_items):
    legend_item_box = Rectangle((legend_x + 0.5 + i*2.3, legend_y), 2.2, 0.4,
                               facecolor=color, edgecolor='black', linewidth=1)
    ax.add_patch(legend_item_box)
    ax.text(legend_x + 1.6 + i*2.3, legend_y + 0.2, text,
            ha='center', va='center', fontsize=8, fontweight='bold')

# Use Case Recommendations
usecase_x = 15
usecase_y = 8
usecase_box = Rectangle((usecase_x, usecase_y-7), 4, 8,
                       facecolor='lightyellow', edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(usecase_box)

usecase_text = """USE CASE
RECOMMENDATIONS

CLOUD COMPUTING:
• Big Data Analytics
• Enterprise Applications
• Global Web Services
• Backup & Storage
• ML Model Training

FOG COMPUTING:
• Smart Cities
• Industrial IoT
• Video Analytics
• Content Delivery
• Regional Processing

EDGE COMPUTING:
• Autonomous Vehicles
• AR/VR Applications
• Industrial Control
• Real-time Gaming
• Healthcare Monitoring
• Drone Operations"""

ax.text(usecase_x + 2, usecase_y - 3.5, usecase_text, ha='center', va='center',
        fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

# Key Insights Panel
insights_x = 2
insights_y = 0.5
insights_box = Rectangle((insights_x, insights_y-0.3), 12, 0.8,
                        facecolor='lightcoral', edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(insights_box)

insights_text = """KEY INSIGHTS: Cloud excels in processing power and scalability but suffers from latency. Edge provides ultra-low latency and privacy but has limited resources. Fog offers balanced performance across most parameters."""

ax.text(insights_x + 6, insights_y, insights_text, ha='center', va='center',
        fontsize=10, fontweight='bold', color='white')

# Performance radar chart indicators
radar_centers = [(16, 6), (17, 4.5), (18, 3)]
radar_labels = ['Cloud', 'Fog', 'Edge']
radar_colors = ['#2196F3', '#FF9800', '#4CAF50']

for i, (center, label, color) in enumerate(zip(radar_centers, radar_labels, radar_colors)):
    circle = plt.Circle(center, 0.3, facecolor=color, edgecolor='black', linewidth=2, alpha=0.8)
    ax.add_patch(circle)
    ax.text(center[0], center[1], label[0], ha='center', va='center', 
            fontsize=12, fontweight='bold', color='white')

# Set title
ax.set_title('Comparative Analysis: Cloud vs Fog vs Edge Computing Models', 
             fontsize=18, fontweight='bold', pad=20)

# Configure axes
ax.set_xlim(0, 20)
ax.set_ylim(0, 9)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('/workspace/diagram_5_comparative_analysis.png', dpi=300, bbox_inches='tight')
plt.savefig('/workspace/diagram_5_comparative_analysis.pdf', bbox_inches='tight')
plt.show()