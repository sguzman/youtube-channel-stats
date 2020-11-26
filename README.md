# Youtube Channel Statistics

### Summary
This is the Youtube Channels Stat Collection project. It will
collect statistics on youtube channels and store them in a 
database

### Technologies
- Python/Rust
- Docker
- Kubernetes

## Topology
All components in this project will be either database tables
or microservices acting on them.

### Databases

- Channel Serials
- Channel Metadata
- Channel Timeseries

### Microservices

- Initial channel serial inserter
- Channel serial aggregation policy
- Weighted channel select
- Youtube API query
- Youtube site scraper
- Timeseries storage policy
- Timeseries prune
- Process Scheduler
