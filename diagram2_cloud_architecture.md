# Diagram 2: Cloud-Only Architecture

```mermaid
graph TB
    subgraph "Users"
        U1[User 1]
        U2[User 2]
        U3[User 3]
        U4[User N]
    end
    
    subgraph "Internet"
        I[Internet Connection]
    end
    
    subgraph "Cloud Data Center"
        subgraph "Frontend Layer"
            LB[Load Balancer]
            API[API Gateway]
        end
        
        subgraph "Virtualization Layer"
            VM1[Virtual Machine 1]
            VM2[Virtual Machine 2]
            VM3[Virtual Machine 3]
            VM4[Virtual Machine N]
        end
        
        subgraph "Service Models"
            IaaS[Infrastructure as a Service<br/>• Compute<br/>• Storage<br/>• Networking]
            PaaS[Platform as a Service<br/>• Development Tools<br/>• Runtime Environment<br/>• Database Services]
            SaaS[Software as a Service<br/>• Applications<br/>• Email Services<br/>• Office Suites]
        end
        
        subgraph "Physical Infrastructure"
            S1[Server 1]
            S2[Server 2]
            S3[Server 3]
            ST[Storage Systems]
            NW[Network Equipment]
        end
    end
    
    U1 --> I
    U2 --> I
    U3 --> I
    U4 --> I
    
    I --> LB
    LB --> API
    API --> VM1
    API --> VM2
    API --> VM3
    API --> VM4
    
    VM1 --> IaaS
    VM2 --> PaaS
    VM3 --> SaaS
    VM4 --> IaaS
    
    IaaS --> S1
    PaaS --> S2
    SaaS --> S3
    
    S1 --> ST
    S2 --> ST
    S3 --> ST
    
    ST --> NW
    
    style U1 fill:#e1f5fe
    style U2 fill:#e1f5fe
    style U3 fill:#e1f5fe
    style U4 fill:#e1f5fe
    style I fill:#fff3e0
    style LB fill:#f3e5f5
    style API fill:#f3e5f5
    style VM1 fill:#e8f5e8
    style VM2 fill:#e8f5e8
    style VM3 fill:#e8f5e8
    style VM4 fill:#e8f5e8
    style IaaS fill:#fff8e1
    style PaaS fill:#fff8e1
    style SaaS fill:#fff8e1
    style S1 fill:#ffebee
    style S2 fill:#ffebee
    style S3 fill:#ffebee
    style ST fill:#ffebee
    style NW fill:#ffebee
```

**Figure 2: Cloud-Only Architecture with Centralized Data Centers**

This diagram illustrates a traditional cloud-only architecture where all computing resources are centralized in data centers, accessed by users through the Internet. The architecture demonstrates virtualization layers, service models (IaaS, PaaS, SaaS), and multi-tenancy capabilities.