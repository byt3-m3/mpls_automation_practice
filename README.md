# Presto Configuration Generator

This tool is designed to generate Cisco style configurations.This tool is aimed to aide in the agility when labeling or
simulating high level networks. 


## Schemas
base_router schema.
```python
from schema import Use, Schema, Optional
from app.models.interface import InterfaceSchema

NodeSchema = Schema(
    {
        "hostname": str,
        "router_id": str,
        Optional("ldp_id"): str,
        Optional("loopbacks"): list,
        Optional("interfaces"): lambda x: [InterfaceSchema.validate(interface) for interface in x],

    }
)
```

BGP Peer Policy Schama
### Method : -m bgp_policy
```python
from schema import Optional, Schema

BGPPeerPolicySchema = Schema({
    "policy_name": str,
    "bgp_asn": int,
    Optional("allowas_in"): lambda x: x <= 10,
    Optional("as_override"): bool,
    Optional("as_override_split_horizon"): bool,
    Optional("next_hop_self"): bool,
    Optional("next_hop_self_all"): bool,
    Optional("next_hop_unchanged"): bool,
    Optional("next_hop_unchanged_allpaths"): bool,
    Optional("route_reflector_client"): bool,
    Optional("route_map_in"): str,
    Optional("route_map_out"): str,
    Optional("send_label"): bool,
    Optional("send_label_explicit_null"): bool,
    Optional("prefix_list_in"): str,
    Optional("prefix_list_out"): str,
    Optional("weight"): lambda x: x <= 65535,
    Optional("soft_reconfiguration"): bool,
    Optional("maximum_prefix"): lambda x: int(x) <= 2147483647,
})
```