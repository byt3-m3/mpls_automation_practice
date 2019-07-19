from schema import Optional, Schema
import ipaddress

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

BGPPeerSessionSchema = Schema({
    "policy_name": str,
    Optional("description "): str,
    Optional("password"): str,
    Optional("timers"): lambda x: x <= 65535,
    Optional("shutdown"): bool,
    Optional("shutdown_graceful"): lambda x: x <= 65535,
    Optional("disable_connected_check"): bool,
    Optional("ebgp_multihop"): lambda x: x <= 255,
    Optional("remote_as"): str,
    Optional("update_source"): str,
    Optional("ttl_security"): lambda x: x <= 254,
    Optional("log_neighbor_changes"): bool,
})

BGPSessionOptionSchema = Schema({
    "peer_address": str,
    "remote_as": int,
    Optional("password"): str,
    Optional("peer_session"): str,
    Optional("peer_policy"): str,
    Optional("description"): str,
    Optional("ebgp_multihop"): lambda x: x <= 255,
    Optional("peer_group"): str,
    Optional("shutdown"): bool,
    Optional("shutdown_graceful"): lambda x: x <= 65535,
    Optional("ttl_security"): lambda x: x <= 254,
    Optional("update_source"): str,
    Optional("version"): str,
    Optional("disable_connected_check"): bool,
    Optional("ipv4_enabled"): bool,
    Optional("vpnv4_enabled"): bool,
    Optional("ipv6_enabled"): bool,
    Optional("ipv4_networks"): lambda x: [BGPIPV4NetworkSchema.validate(network) for network in x],
    Optional("ipv4_labled_unicast_enabled"): bool,
    Optional("timers"): lambda x: x <= 65535,
})

BGPIPV4NetworkSchema = Schema(
    {
        "network_id": lambda x: ipaddress.IPv4Network(x),
        "netmask": lambda x: ipaddress.IPv4Address(x),
        Optional("route_map"): str,
        Optional("backdoor"): bool
    }
)

BGPSessionSchema = Schema({
    "asn": int,
    "sessions": lambda x: [BGPSessionOptionSchema.validate(session) for session in x]
}
)
