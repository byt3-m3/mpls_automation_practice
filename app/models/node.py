from app.models.interface import Interface
from schema import Use, Schema, Optional


NodeSchema = Schema(
    {
        "hostname": str,
        "router_id": str,
        Optional("ldp_id"): str,

    }
)



class Node:

    def __init__(self, *args, **kwargs):
        self.hostname = kwargs.get("hostname", "")
        self.mgmt_ip = kwargs.get("mgmt_ip")
        self.interfaces = kwargs.get("interfaces", [])

    def add_interface(self, interface: Interface):
        for link in self.interfaces:
            if link.id == interface.id:
                return False
            else:
                self.interfaces.append(interface)
                return True

