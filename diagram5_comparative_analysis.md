# Diagram 5: Comparative Analysis of Computing Models

```mermaid
graph TB
    subgraph "Computing Models Comparison"
        subgraph "Cloud Computing"
            CC[Cloud Computing<br/>📍 Centralized Data Centers<br/>⚡ High Processing Power<br/>💾 Massive Storage<br/>📈 Excellent Scalability<br/>⏱️ High Latency (100-500ms)<br/>💰 Pay-per-use Model<br/>🔒 Centralized Security<br/>📱 Web Applications<br/>📧 Email Services<br/>🗄️ Data Analytics]
        end
        
        subgraph "Fog Computing"
            FC[Fog Computing<br/>📍 Network Edge Devices<br/>⚡ Medium Processing Power<br/>💾 Moderate Storage<br/>📈 Good Scalability<br/>⏱️ Medium Latency (10-100ms)<br/>💰 Moderate Cost<br/>🔒 Distributed Security<br/>🏭 Industrial IoT<br/>🚦 Smart Traffic<br/>🏥 Healthcare Monitoring]
        end
        
        subgraph "Edge Computing"
            EC[Edge Computing<br/>📍 Device/Node Level<br/>⚡ Limited Processing Power<br/>💾 Small Storage<br/>📈 Limited Scalability<br/>⏱️ Ultra-low Latency (1-10ms)<br/>💰 High Initial Cost<br/>🔒 Local Security<br/>🚗 Autonomous Vehicles<br/>🎮 AR/VR Gaming<br/>⚡ Real-time Control]
        end
    end
    
    subgraph "Comparison Matrix"
        subgraph "Performance Metrics"
            PM[Performance Comparison<br/>┌─────────────┬─────────┬─────────┬─────────┐<br/>│ Metric      │ Cloud   │ Fog     │ Edge    │<br/>├─────────────┼─────────┼─────────┼─────────┤<br/>│ Latency     │ High    │ Medium  │ Ultra-low│<br/>│ Processing  │ Excellent│ Good   │ Limited │<br/>│ Storage     │ Massive │ Moderate│ Small   │<br/>│ Scalability │ Excellent│ Good   │ Limited │<br/>│ Cost        │ Low     │ Medium  │ High    │<br/>│ Security    │ Central │ Dist.   │ Local   │<br/>└─────────────┴─────────┴─────────┴─────────┘]
        end
        
        subgraph "Use Case Suitability"
            UC[Use Case Mapping<br/>🟢 Excellent  🟡 Good  🔴 Limited<br/><br/>📊 Big Data Analytics<br/>Cloud: 🟢 Fog: 🟡 Edge: 🔴<br/><br/>🏭 Industrial Automation<br/>Cloud: 🟡 Fog: 🟢 Edge: 🟢<br/><br/>🚗 Autonomous Vehicles<br/>Cloud: 🔴 Fog: 🟡 Edge: 🟢<br/><br/>📱 Mobile Applications<br/>Cloud: 🟢 Fog: 🟢 Edge: 🟡<br/><br/>🎮 Real-time Gaming<br/>Cloud: 🔴 Fog: 🟡 Edge: 🟢]
        end
    end
    
    CC -.-> PM
    FC -.-> PM
    EC -.-> PM
    
    CC -.-> UC
    FC -.-> UC
    EC -.-> UC
    
    style CC fill:#e3f2fd
    style FC fill:#fff3e0
    style EC fill:#f1f8e9
    style PM fill:#fce4ec
    style UC fill:#e8f5e8
```

**Figure 5: Comparative Analysis of Cloud, Fog, and Edge Computing Models**

This diagram provides a comprehensive comparison of the three computing paradigms, highlighting their characteristics, performance metrics, and suitability for different use cases. The comparison matrix shows the trade-offs between latency, processing power, storage capacity, scalability, cost, and security across the three models.