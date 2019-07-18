#!/usr/bin/env bash

# Generates Base Router Configs
python app_cli.py -m base_router -j devices\r1_core.json
python app_cli.py -m base_router -j devices\r2_core.json
python app_cli.py -m base_router -j devices\r3_pe.json
python app_cli.py -m base_router -j devices\r4_pe.json
python app_cli.py -m base_router -j devices\r5_pe.json
python app_cli.py -m base_router -j devices\r6_pe.json
