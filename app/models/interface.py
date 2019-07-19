from schema import Optional, Schema
import ipaddress

from app.models.ospf import OSPFv2InterfaceBaseSchema

InterfaceSchema = Schema(
    {
        "id": str,
        "ipv4_address": lambda x: ipaddress.IPv4Address(x),
        "ipv4_netmask": lambda x: ipaddress.IPv4Address(x),
        "bandwidth": str,
        Optional("desc"): str,
        Optional("mtu"): str,
        Optional("ldp_enabled"): bool,
        Optional("ospfv2"): lambda x: OSPFv2InterfaceBaseSchema.validate(x),

    }
)


def test_model():
    model = {
        "id": "Ethernet0/0",
        "desc": "Link to R3-PE",
        "ipv4_address": "10.1.3.1",
        "ipv4_netmask": "255.255.255.252",
        "mtu": "9000",
        "bandwidth": "20",
        "ldp_enabled": True
    }

    print(InterfaceSchema.validate(model))
