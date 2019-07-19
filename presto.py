import os
import platform
import json
import argparse
import re
import jinja2

from app.models.node import NodeSchema
from app.models.vrf import VRFSchema
from app.models.bgp import BGPPeerPolicySchema
from app.constants import METHODS

templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)


def process_template_output(outputText: str):
    formated_data = []
    for line in outputText.split("\n"):
        if line:
            formated_data.append(line)

    return formated_data


def main(*args, **kwargs):
    parser = kwargs.get("parser")

    cli_args = parser.parse_args()

    method = cli_args.method
    json_file_name = cli_args.json_file_name

    if not METHODS.count(method):
        raise BaseException(f"Invalid Method Supplied, Please Choose from the following: {METHODS}")


    if method == "base_router":
        with open(json_file_name, "r") as json_file:
            node_data = json.load(json_file)

        NodeSchema.validate(node_data)

        TEMPLATE_FILE = "base_router.j2"
        template = templateEnv.get_template(TEMPLATE_FILE)
        # node_data = json.load(json_raw)
        outputText = template.render(node=node_data)
        print(outputText)

        with open(f"./output/base_router/{node_data.get('hostname')}.txt", "w") as f:
            f.writelines(outputText)

    if method == "vrf":
        with open(json_file_name, "r") as json_file:
            data = json.load(json_file)

            VRFSchema.validate(data)

            TEMPLATE_FILE = "vrf_vpn.j2"
            template = templateEnv.get_template(TEMPLATE_FILE)
            # node_data = json.load(json_raw)
            outputText = template.render(sp=data)
            print(outputText)

            with open(f"./output/vrf/{data.get('policy_name')}.txt", "w") as f:
                f.writelines(outputText)

    if method == "bgp_policy":
        with open(json_file_name, "r") as json_file:
            data = json.load(json_file)
        BGPPeerPolicySchema.validate(data)

        TEMPLATE_FILE = "bgp_peer_policy.j2"
        template = templateEnv.get_template(TEMPLATE_FILE)

        outputText = template.render(policy=data)

        result_data = process_template_output(outputText)

        with open(f"./output/bgp_policy/{data.get('policy_name')}.txt", "w") as f:
            for line in result_data:
                f.write(line)
                f.write("\n")
        print(data)


def clear_screen():
    _platform = platform.system()

    if 'Windows' in _platform:
        os.system('cls')

    if 'Darwin' in _platform:
        os.system('clear')


if __name__ == '__main__':
    clear_screen()
    parser = argparse.ArgumentParser(
        description='CLI Tool for Generating Lab Configs for MPLS Lab',
    )

    parser.add_argument(
        '-j',
        '--json_file_name',
        help="JSON model"
    )

    parser.add_argument(
        '-m',
        '--method',
        help="Specify an action to preform"
    )

    main(parser=parser)
