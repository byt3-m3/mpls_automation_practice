from schema import Optional, Schema

from app.models.interface import InterfaceSchema

VRFSchema = Schema(
    {
        "service_id": str,
        "customer_name": str,
        "customer_id": str,
        "bgp_as": str,
        "cx_bgp_as": str,
        "pe_router": str,
        "uplink": lambda x: InterfaceSchema.validate(x),
        "downlink": lambda x: InterfaceSchema.validate(x),
    }
)