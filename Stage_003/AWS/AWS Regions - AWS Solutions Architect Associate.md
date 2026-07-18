## Date: 07/2/2026

**Topic:** AWS Regions, Availability Zones, Edge Locations + IAM (Section 4)

**Notes:**

**Choosing an AWS Region — 4 factors:**

- **Compliance** — data governance/legal requirements; data never leaves the region without explicit permission
- **Proximity** — closer to customers = reduced latency
- **Service availability** — new services/features don't launch in every region simultaneously
- **Pricing** — varies region to region

**Availability Zones (AZs):**

- Example naming: `ap-southeast-2a`, `ap-southeast-2b`, `ap-southeast-2c`
- Minimum 3 AZs per region, max 6
- Each AZ = one or more discrete data centers with redundant power, networking, and connectivity
- AZs within a region are connected via high-bandwidth, ultra-low-latency links

**Edge Locations (Points of Presence):**

- 400+ locations across 90+ cities in 40+ countries
- Used for content delivery (CloudFront) — get content physically closer to end user