from schema import Optional, Schema
from app.constants import OSPF_NETWORK_TYPES


OSPFv2InterfaceBaseSchema = Schema({
    "pid": int,
    "network_type": lambda x: OSPF_NETWORK_TYPES.count(x),
    "area_id": int,
})


# model = {
#     "pid": "1",
#     "network_type": "point-to-point",
#     "area_id": 100
# }
#
# print(OSPFv2InterfaceBaseSchema.validate(model))