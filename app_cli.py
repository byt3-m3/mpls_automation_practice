from app.models.node import Node
from app.models.interface import Interface
import os
import platform
import json
import argparse

import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)


def main(*args, **kwargs):
    parser = kwargs.get("parser")

    cli_args = parser.parse_args()

    method = cli_args.method
    json_file_name = cli_args.json_file_name

    if method == "base_router":
        with open(json_file_name, "r") as json_file:
            node_data = json.load(json_file)

        TEMPLATE_FILE = "base_router.j2"
        template = templateEnv.get_template(TEMPLATE_FILE)
        # node_data = json.load(json_raw)
        outputText = template.render(node=node_data)
        print(outputText)

        with open(f"./configs/base_router_{node_data.get('hostname')}.txt", "w") as f:
            f.writelines(outputText)



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
