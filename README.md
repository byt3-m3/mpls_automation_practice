# Cisco Segment Routing Lab

This lab is designed demonstrate the use of Python and Jinja2 templates. 

![alt text](./Capture.PNG)

## Topology Info
- Nodes
    - 6 Cisco CSR 1000vs - Cisco IOS XE Software, Version 16.03.02
    - 8 Cisco IOL  - Cisco IOS Software, Linux Software (I86BI_LINUX-ADVENTERPRISEK9-M), Version 15.2(4)M1
    
    ### Methods and Schemas
    - method: base_router
        - Schema:
            ```json
             {
              "hostname": "R3-PE",
              "ldp_id": "loopback0",
              "router_id": "3.3.3.3",
              "loopbacks": [
                {
                  "id": "loopback0",
                  "desc": "RouterID and MGMT Interface",
                  "ipv4_address": "3.3.3.3",
                  "ospfv2": {
                    "pid": 1,
                    "network_type": "point-to-point",
                    "area_id": 0
                  }
                }
              ],
              "interfaces": [
                {
                  "id": "GigabitEthernet1",
                  "desc": "Link to R1-CORE",
                  "ipv4_address": "172.1.3.2",
                  "ipv4_netmask": "255.255.255.252",
                  "mtu": "9000",
                  "bandwidth": "100",
                  "ldp_enabled": true,
                  "ospfv2": {
                    "pid": 1,
                    "network_type": "point-to-point",
                    "area_id": 0
                  }
                }
              ],
              "bgp_as": "65000"
              }

            ```