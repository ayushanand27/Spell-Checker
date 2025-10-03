import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np
import math

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(16, 12))

# Define colors for different challenge categories
colors = {
    'center': '#2E2E2E',
    'scalability': '#F44336',
    'security': '#9C27B0',
    'networking': '#2196F3',
    'heterogeneity': '#FF9800',
    'energy': '#4CAF50',
    'cost': '#795548',
    'mobility': '#E91E63'
}

# Central node
center_x, center_y = 8, 6
center_circle = Circle((center_x, center_y), 1.2, facecolor=colors['center'], 
                      edgecolor='white', linewidth=3)
ax.add_patch(center_circle)
ax.text(center_x, center_y, 'EDGE\nCOMPUTING\nCHALLENGES', ha='center', va='center', 
        fontsize=14, fontweight='bold', color='white')

# Main challenge categories with positions
main_challenges = [
    {'name': 'SCALABILITY &\nRESOURCE MGMT', 'color': colors['scalability'], 
     'angle': 0, 'distance': 4},
    {'name': 'SECURITY &\nPRIVACY', 'color': colors['security'], 
     'angle': 51.4, 'distance': 4},
    {'name': 'NETWORKING &\nRELIABILITY', 'color': colors['networking'], 
     'angle': 102.8, 'distance': 4},
    {'name': 'HETEROGENEITY', 'color': colors['heterogeneity'], 
     'angle': 154.2, 'distance': 4},
    {'name': 'ENERGY\nEFFICIENCY', 'color': colors['energy'], 
     'angle': 205.6, 'distance': 4},
    {'name': 'COST\nOPTIMIZATION', 'color': colors['cost'], 
     'angle': 257, 'distance': 4},
    {'name': 'MOBILITY\nSUPPORT', 'color': colors['mobility'], 
     'angle': 308.4, 'distance': 4}
]

# Sub-challenges for each main category
sub_challenges = {
    'SCALABILITY &\nRESOURCE MGMT': [
        'Container Orchestration',
        'Dynamic Scaling',
        'Load Balancing',
        'Resource Allocation'
    ],
    'SECURITY &\nPRIVACY': [
        'Distributed Authentication',
        'Data Encryption',
        'Trust Management',
        'Attack Surface Expansion'
    ],
    'NETWORKING &\nRELIABILITY': [
        'Intermittent Connectivity',
        'Bandwidth Limitations',
        'QoS Guarantees',
        'Network Latency'
    ],
    'HETEROGENEITY': [
        'Device Diversity',
        'Protocol Standards',
        'Hardware Variations',
        'Software Compatibility'
    ],
    'ENERGY\nEFFICIENCY': [
        'Battery Optimization',
        'Thermal Management',
        'Power-Aware Scheduling',
        'Green Computing'
    ],
    'COST\nOPTIMIZATION': [
        'Infrastructure Investment',
        'Operational Expenses',
        'Maintenance Costs',
        'ROI Calculation'
    ],
    'MOBILITY\nSUPPORT': [
        'Service Migration',
        'Handoff Management',
        'Location Awareness',
        'Dynamic Discovery'
    ]
}

# Draw main challenge nodes and connections
for challenge in main_challenges:
    # Calculate position
    angle_rad = math.radians(challenge['angle'])
    x = center_x + challenge['distance'] * math.cos(angle_rad)
    y = center_y + challenge['distance'] * math.sin(angle_rad)
    
    # Draw main challenge node
    main_box = FancyBboxPatch((x-1.2, y-0.6), 2.4, 1.2, boxstyle="round,pad=0.1",
                             facecolor=challenge['color'], edgecolor='black', 
                             linewidth=2, alpha=0.9)
    ax.add_patch(main_box)
    ax.text(x, y, challenge['name'], ha='center', va='center', 
            fontsize=10, fontweight='bold', color='white')
    
    # Draw connection to center
    connection = FancyArrowPatch((center_x + 1.2 * math.cos(angle_rad), 
                                 center_y + 1.2 * math.sin(angle_rad)),
                                (x - 1.2 * math.cos(angle_rad), 
                                 y - 1.2 * math.sin(angle_rad)),
                                arrowstyle='-', mutation_scale=20, 
                                color=challenge['color'], linewidth=3, alpha=0.8)
    ax.add_patch(connection)
    
    # Draw sub-challenges
    sub_list = sub_challenges[challenge['name']]
    for i, sub_challenge in enumerate(sub_list):
        # Calculate sub-challenge position
        sub_angle = challenge['angle'] + (i - 1.5) * 15  # Spread around main node
        sub_angle_rad = math.radians(sub_angle)
        sub_distance = 2.5
        sub_x = x + sub_distance * math.cos(sub_angle_rad)
        sub_y = y + sub_distance * math.sin(sub_angle_rad)
        
        # Draw sub-challenge node
        sub_box = FancyBboxPatch((sub_x-0.8, sub_y-0.3), 1.6, 0.6, 
                                boxstyle="round,pad=0.05",
                                facecolor='white', edgecolor=challenge['color'], 
                                linewidth=2, alpha=0.9)
        ax.add_patch(sub_box)
        ax.text(sub_x, sub_y, sub_challenge, ha='center', va='center', 
                fontsize=8, fontweight='bold', color=challenge['color'])
        
        # Draw connection to main challenge
        sub_connection = FancyArrowPatch((x + 1.2 * math.cos(sub_angle_rad), 
                                        y + 1.2 * math.sin(sub_angle_rad)),
                                       (sub_x - 0.8 * math.cos(sub_angle_rad), 
                                        sub_y - 0.8 * math.sin(sub_angle_rad)),
                                       arrowstyle='-', mutation_scale=15, 
                                       color=challenge['color'], linewidth=2, alpha=0.6)
        ax.add_patch(sub_connection)

# Add severity indicators
severity_legend_x = 1
severity_legend_y = 10.5
severity_box = FancyBboxPatch((severity_legend_x-0.5, severity_legend_y-1), 4, 2,
                             boxstyle="round,pad=0.1", facecolor='lightgray',
                             edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(severity_box)

severity_text = """CHALLENGE SEVERITY

🔴 Critical Impact
🟡 Moderate Impact  
🟢 Manageable Impact

INTERCONNECTED NATURE:
Most challenges are
interdependent and require
holistic solutions"""

ax.text(severity_legend_x + 1.5, severity_legend_y, severity_text, ha='center', va='center',
        fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

# Add solution approaches panel
solution_x = 13
solution_y = 10.5
solution_box = FancyBboxPatch((solution_x-0.5, solution_y-1), 4, 2,
                             boxstyle="round,pad=0.1", facecolor='lightblue',
                             edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(solution_box)

solution_text = """SOLUTION APPROACHES

• AI-Driven Orchestration
• Standardization Efforts
• Hybrid Architectures
• Edge-Native Security
• Green Computing
• Cost-Benefit Analysis
• Mobility Protocols"""

ax.text(solution_x + 1.5, solution_y, solution_text, ha='center', va='center',
        fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

# Add impact indicators around the center
impact_indicators = [
    {'text': 'Performance\nImpact', 'x': center_x-2.5, 'y': center_y+2.5, 'color': '#FF5722'},
    {'text': 'Cost\nImpact', 'x': center_x+2.5, 'y': center_y+2.5, 'color': '#795548'},
    {'text': 'Security\nRisk', 'x': center_x-2.5, 'y': center_y-2.5, 'color': '#9C27B0'},
    {'text': 'Adoption\nBarrier', 'x': center_x+2.5, 'y': center_y-2.5, 'color': '#607D8B'}
]

for indicator in impact_indicators:
    impact_circle = Circle((indicator['x'], indicator['y']), 0.6, 
                          facecolor=indicator['color'], edgecolor='white', 
                          linewidth=2, alpha=0.8)
    ax.add_patch(impact_circle)
    ax.text(indicator['x'], indicator['y'], indicator['text'], ha='center', va='center',
            fontsize=8, fontweight='bold', color='white')

# Add research priorities
research_x = 1
research_y = 1.5
research_box = FancyBboxPatch((research_x-0.5, research_y-1), 15, 2,
                             boxstyle="round,pad=0.1", facecolor='lightyellow',
                             edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(research_box)

research_text = """RESEARCH PRIORITIES: Developing intelligent orchestration systems, creating standardized protocols, implementing zero-trust security models, optimizing energy consumption algorithms, and designing cost-effective deployment strategies for sustainable edge computing ecosystems."""

ax.text(research_x + 7, research_y, research_text, ha='center', va='center',
        fontsize=10, fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

# Set title
ax.set_title('Edge Computing Challenges: Comprehensive Mind Map Analysis', 
             fontsize=18, fontweight='bold', pad=20)

# Configure axes
ax.set_xlim(-1, 17)
ax.set_ylim(-1, 12)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('/workspace/diagram_6_challenges_mindmap.png', dpi=300, bbox_inches='tight')
plt.savefig('/workspace/diagram_6_challenges_mindmap.pdf', bbox_inches='tight')
plt.show()