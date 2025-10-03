import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 10))

# Define colors
colors = {
    'user': '#4CAF50',
    'internet': '#2196F3', 
    'cloud': '#FF9800',
    'service': '#9C27B0',
    'infrastructure': '#607D8B'
}

# Draw Users section
user_y = 8.5
users = ['Desktop', 'Mobile', 'Tablet', 'IoT Device']
for i, user in enumerate(users):
    x_pos = 1 + i * 2
    # User device
    device = Circle((x_pos, user_y), 0.3, facecolor=colors['user'], edgecolor='black', linewidth=2)
    ax.add_patch(device)
    ax.text(x_pos, user_y, user.split()[0][0], ha='center', va='center', fontweight='bold', color='white')
    ax.text(x_pos, user_y-0.7, user, ha='center', va='center', fontsize=9, fontweight='bold')

# Draw Internet Cloud
internet_box = FancyBboxPatch((0.5, 6), 8, 1.5, boxstyle="round,pad=0.1",
                             facecolor=colors['internet'], edgecolor='black', 
                             linewidth=2, alpha=0.8)
ax.add_patch(internet_box)
ax.text(4.5, 6.75, 'INTERNET', ha='center', va='center', fontsize=16, 
        fontweight='bold', color='white')

# Draw arrows from users to internet
for i in range(4):
    x_pos = 1 + i * 2
    ax.annotate('', xy=(x_pos, 7.5), xytext=(x_pos, 8.2),
                arrowprops=dict(arrowstyle='<->', lw=2, color='red'))

# Draw Cloud Data Center
cloud_box = FancyBboxPatch((0.5, 0.5), 8, 5, boxstyle="round,pad=0.2",
                          facecolor=colors['cloud'], edgecolor='black', 
                          linewidth=3, alpha=0.9)
ax.add_patch(cloud_box)

# Cloud Data Center Title
ax.text(4.5, 5.2, 'CLOUD DATA CENTER', ha='center', va='center', 
        fontsize=16, fontweight='bold', color='white')

# Service Models Layer
service_y = 4.5
service_models = ['SaaS', 'PaaS', 'IaaS']
service_colors = ['#E91E63', '#673AB7', '#3F51B5']

for i, (service, color) in enumerate(zip(service_models, service_colors)):
    service_box = Rectangle((1 + i*2.2, service_y-0.3), 2, 0.6, 
                           facecolor=color, edgecolor='black', linewidth=1)
    ax.add_patch(service_box)
    ax.text(2 + i*2.2, service_y, service, ha='center', va='center', 
            fontsize=12, fontweight='bold', color='white')

# Service descriptions
descriptions = [
    'Software as\na Service',
    'Platform as\na Service', 
    'Infrastructure\nas a Service'
]

for i, desc in enumerate(descriptions):
    ax.text(2 + i*2.2, service_y-0.7, desc, ha='center', va='center', 
            fontsize=8, style='italic')

# Virtualization Layer
virt_box = Rectangle((1, 3.2), 6.5, 0.8, facecolor='#795548', 
                    edgecolor='black', linewidth=2)
ax.add_patch(virt_box)
ax.text(4.25, 3.6, 'VIRTUALIZATION LAYER', ha='center', va='center', 
        fontsize=12, fontweight='bold', color='white')

# Physical Infrastructure
infra_components = ['Compute Servers', 'Storage Systems', 'Network Equipment']
infra_colors = ['#F44336', '#4CAF50', '#2196F3']

for i, (comp, color) in enumerate(zip(infra_components, infra_colors)):
    comp_box = Rectangle((1 + i*2.2, 1.5), 2, 1.2, facecolor=color, 
                        edgecolor='black', linewidth=2)
    ax.add_patch(comp_box)
    ax.text(2 + i*2.2, 2.1, comp, ha='center', va='center', 
            fontsize=10, fontweight='bold', color='white')

# Add server icons in compute section
for j in range(3):
    server = Rectangle((1.2 + j*0.5, 1.7), 0.3, 0.8, facecolor='white', 
                      edgecolor='black', linewidth=1)
    ax.add_patch(server)

# Add storage icons
for j in range(3):
    storage = Circle((3.4 + j*0.4, 2.1), 0.15, facecolor='white', 
                    edgecolor='black', linewidth=1)
    ax.add_patch(storage)

# Add network icons
for j in range(2):
    for k in range(2):
        network = Rectangle((5.3 + j*0.6, 1.8 + k*0.4), 0.4, 0.2, 
                           facecolor='white', edgecolor='black', linewidth=1)
        ax.add_patch(network)

# Arrow from internet to cloud
ax.annotate('', xy=(4.5, 5.5), xytext=(4.5, 6),
            arrowprops=dict(arrowstyle='<->', lw=3, color='red'))

# Add side panel with characteristics
char_box = Rectangle((9.5, 1), 4, 7.5, facecolor='lightgray', 
                    edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(char_box)

characteristics_text = """CLOUD COMPUTING
CHARACTERISTICS

✓ On-Demand Self-Service
✓ Broad Network Access  
✓ Resource Pooling
✓ Rapid Elasticity
✓ Measured Service

ADVANTAGES:
• Unlimited Scalability
• Global Accessibility
• Cost Optimization
• Professional Management
• High Availability

CHALLENGES:
• Network Latency
• Bandwidth Limitations
• Security Concerns
• Regulatory Compliance
• Internet Dependency"""

ax.text(11.5, 4.75, characteristics_text, ha='center', va='center', 
        fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

# Add multi-tenancy illustration
tenant_y = 0.8
for i in range(3):
    tenant = Circle((2 + i*2, tenant_y), 0.2, facecolor='yellow', 
                   edgecolor='black', linewidth=1)
    ax.add_patch(tenant)
    ax.text(2 + i*2, tenant_y, f'T{i+1}', ha='center', va='center', 
            fontsize=8, fontweight='bold')

ax.text(4, 0.3, 'Multi-Tenant Architecture', ha='center', va='center', 
        fontsize=10, fontweight='bold')

# Set title
ax.set_title('Cloud-Only Architecture: Centralized Computing Model', 
             fontsize=18, fontweight='bold', pad=20)

# Configure axes
ax.set_xlim(0, 14)
ax.set_ylim(0, 9.5)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('/workspace/diagram_2_cloud_architecture.png', dpi=300, bbox_inches='tight')
plt.savefig('/workspace/diagram_2_cloud_architecture.pdf', bbox_inches='tight')
plt.show()