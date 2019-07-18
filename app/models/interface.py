class Interface:

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.desc = kwargs.get("desc")
        self.ipv4_address = kwargs.get("ipv4_address")
        self.ipv4_netmask = kwargs.get("ipv4_netmask")
        self.mtu = kwargs.get("mtu", "1518")
        self.bandwidth = kwargs.get("bandwidth")

    @staticmethod
    def new(data: dict):
        return Interface(**data)
