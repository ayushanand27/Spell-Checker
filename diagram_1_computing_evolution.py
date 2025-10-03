import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(16, 10))

# Define timeline data
timeline_data = [
    {"period": "1950-1970", "name": "Mainframe\nComputing", "color": "#8B4513", "y": 0.8, "key_tech": "IBM System/360\nTime-sharing\nBatch Processing"},
    {"period": "1970-1980", "name": "Distributed\nSystems", "color": "#4169E1", "y": 0.7, "key_tech": "ARPANET\nEthernet\nClient-Server"},
    {"period": "1980-1990", "name": "Cluster\nComputing", "color": "#32CD32", "y": 0.6, "key_tech": "Beowulf Clusters\nHigh-Performance\nComputing"},
    {"period": "1990-2000", "name": "Grid\nComputing", "color": "#FF6347", "y": 0.5, "key_tech": "Globus Toolkit\nResource Sharing\nVirtual Organizations"},
    {"period": "2000-2010", "name": "Cloud\nComputing", "color": "#20B2AA", "y": 0.4, "key_tech": "AWS EC2\nVirtualization\nSaaS/PaaS/IaaS"},
    {"period": "2010-Present", "name": "Edge\nComputing", "color": "#FF1493", "y": 0.3, "key_tech": "IoT Integration\n5G Networks\nAI at Edge"}
]

# Set up the plot
ax.set_xlim(1945, 2030)
ax.set_ylim(0.2, 0.9)

# Draw timeline arrow
arrow = patches.FancyArrowPatch((1950, 0.25), (2025, 0.25),
                               arrowstyle='->', mutation_scale=20, 
                               color='black', linewidth=3)
ax.add_patch(arrow)

# Add timeline markers and labels
for i, data in enumerate(timeline_data):
    start_year = int(data["period"].split("-")[0])
    end_year = int(data["period"].split("-")[1]) if data["period"].split("-")[1] != "Present" else 2025
    
    # Draw era box
    era_box = FancyBboxPatch((start_year, data["y"]-0.05), end_year-start_year, 0.1,
                            boxstyle="round,pad=0.01", 
                            facecolor=data["color"], 
                            edgecolor='black',
                            alpha=0.8,
                            linewidth=2)
    ax.add_patch(era_box)
    
    # Add era name
    ax.text((start_year + end_year)/2, data["y"], data["name"], 
            ha='center', va='center', fontsize=12, fontweight='bold', color='white')
    
    # Add period label
    ax.text((start_year + end_year)/2, data["y"]-0.08, data["period"], 
            ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Add key technologies
    ax.text((start_year + end_year)/2, data["y"]+0.08, data["key_tech"], 
            ha='center', va='center', fontsize=9, style='italic',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    # Draw connection line to timeline
    ax.plot([(start_year + end_year)/2, (start_year + end_year)/2], 
            [data["y"]-0.05, 0.27], 'k--', alpha=0.5, linewidth=1)

# Add decade markers on timeline
for year in range(1950, 2030, 10):
    ax.plot([year, year], [0.23, 0.27], 'k-', linewidth=2)
    ax.text(year, 0.21, str(year), ha='center', va='top', fontsize=10, fontweight='bold')

# Add title and labels
ax.set_title('Evolution of Computing Paradigms: From Mainframes to Edge Computing', 
             fontsize=18, fontweight='bold', pad=20)

# Add evolution arrows between eras
arrow_y = 0.15
for i in range(len(timeline_data)-1):
    start_year = int(timeline_data[i]["period"].split("-")[1]) if timeline_data[i]["period"].split("-")[1] != "Present" else 2025
    end_year = int(timeline_data[i+1]["period"].split("-")[0])
    
    if i < len(timeline_data)-1:
        arrow = patches.FancyArrowPatch((start_year-5, arrow_y), (end_year+5, arrow_y),
                                       arrowstyle='->', mutation_scale=15, 
                                       color='red', linewidth=2, alpha=0.7)
        ax.add_patch(arrow)

# Add legend for key characteristics
legend_text = """
Key Evolutionary Drivers:
• Processing Power Requirements
• Geographic Distribution
• Resource Sharing Needs
• Latency Sensitivity
• Cost Optimization
• Scalability Demands
"""

ax.text(1950, 0.45, legend_text, fontsize=11, 
        bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.8),
        verticalalignment='top')

# Remove axes
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.savefig('/workspace/diagram_1_computing_evolution.png', dpi=300, bbox_inches='tight')
plt.savefig('/workspace/diagram_1_computing_evolution.pdf', bbox_inches='tight')
plt.show()