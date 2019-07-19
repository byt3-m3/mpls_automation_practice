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

def test_model():
    model = {
        "hostname": "R1-BITS",
        "ldp_id": "loopback0",
        "router_id": "1.1.1.1",
        "loopbacks": [
            {
                "id": "loopback0",
                "desc": "RouterID and MGMT Interface",
                "ipv4_address": "1.1.1.1"
            }
        ],
        "interfaces": [
            {
                "id": "Ethernet0/0",
                "desc": "Link to R3-PE",
                "ipv4_address": "10.1.3.1",
                "ipv4_netmask": "255.255.255.252",
                "mtu": "9000",
                "bandwidth": "20",
                "ldp_enabled": True
            }
        ]
    }

    print(NodeSchema.validate(model))
