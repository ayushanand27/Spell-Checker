# Diagram 4: Hybrid Cloud-Edge Architecture

```mermaid
graph TB
    subgraph "Device Layer"
        subgraph "IoT Devices"
            D1[Sensors]
            D2[Cameras]
            D3[Mobile Devices]
            D4[Smart Appliances]
        end
    end
    
    subgraph "Edge/Fog Layer"
        subgraph "Edge Nodes"
            EN1[Edge Node 1<br/>• Real-time Processing<br/>• Data Filtering<br/>• Local Storage]
            EN2[Edge Node 2<br/>• Real-time Processing<br/>• Data Filtering<br/>• Local Storage]
        end
        
        subgraph "Fog Computing"
            FN1[Fog Node 1<br/>• Intermediate Processing<br/>• Data Aggregation<br/>• Protocol Translation]
            FN2[Fog Node 2<br/>• Intermediate Processing<br/>• Data Aggregation<br/>• Protocol Translation]
        end
        
        subgraph "Edge Servers"
            ES1[Edge Server 1<br/>• High Performance<br/>• AI/ML Processing<br/>• Data Analytics]
            ES2[Edge Server 2<br/>• High Performance<br/>• AI/ML Processing<br/>• Data Analytics]
        end
    end
    
    subgraph "Cloud Layer"
        subgraph "Private Cloud"
            PC[Private Cloud<br/>• Secure Processing<br/>• Sensitive Data<br/>• Compliance]
        end
        
        subgraph "Public Cloud"
            subgraph "Cloud Services"
                CS1[Compute Services<br/>• Virtual Machines<br/>• Containers<br/>• Serverless]
                CS2[Storage Services<br/>• Object Storage<br/>• Database Services<br/>• Backup]
                CS3[AI/ML Services<br/>• Model Training<br/>• Inference<br/>• Analytics]
            end
        end
        
        subgraph "Cloud Data Centers"
            CDC1[Data Center 1]
            CDC2[Data Center 2]
            CDC3[Data Center 3]
        end
    end
    
    subgraph "Network Connectivity"
        N1[5G/4G Networks]
        N2[Fiber Optic]
        N3[Internet]
    end
    
    subgraph "Orchestration Layer"
        ORCH[AI-Driven Orchestration<br/>• Workload Distribution<br/>• Resource Management<br/>• Dynamic Scaling]
    end
    
    D1 --> EN1
    D2 --> EN1
    D3 --> EN2
    D4 --> EN2
    
    EN1 --> FN1
    EN2 --> FN2
    
    FN1 --> ES1
    FN2 --> ES2
    
    ES1 --> N1
    ES2 --> N1
    
    N1 --> PC
    N1 --> CS1
    N2 --> CS2
    N3 --> CS3
    
    CS1 --> CDC1
    CS2 --> CDC2
    CS3 --> CDC3
    
    PC --> CDC1
    
    ORCH -.-> EN1
    ORCH -.-> EN2
    ORCH -.-> FN1
    ORCH -.-> FN2
    ORCH -.-> ES1
    ORCH -.-> ES2
    ORCH -.-> PC
    ORCH -.-> CS1
    ORCH -.-> CS2
    ORCH -.-> CS3
    
    style D1 fill:#e3f2fd
    style D2 fill:#e3f2fd
    style D3 fill:#e3f2fd
    style D4 fill:#e3f2fd
    style EN1 fill:#fff3e0
    style EN2 fill:#fff3e0
    style FN1 fill:#f1f8e9
    style FN2 fill:#f1f8e9
    style ES1 fill:#fce4ec
    style ES2 fill:#fce4ec
    style PC fill:#e8f5e8
    style CS1 fill:#fff8e1
    style CS2 fill:#fff8e1
    style CS3 fill:#fff8e1
    style CDC1 fill:#ffebee
    style CDC2 fill:#ffebee
    style CDC3 fill:#ffebee
    style N1 fill:#f3e5f5
    style N2 fill:#f3e5f5
    style N3 fill:#f3e5f5
    style ORCH fill:#e1f5fe
```

**Figure 4: Hybrid Cloud-Edge Architecture with Three-Tier System**

This diagram illustrates a comprehensive hybrid cloud-edge architecture that integrates device, edge/fog, and cloud layers. The architecture demonstrates dynamic workload distribution, AI-driven orchestration, and seamless connectivity between distributed edge nodes and centralized cloud infrastructure.