import argparse
import logging
import os
import subprocess
from typing import Dict



def Arguments() -> argparse.Namespace:

    parser = argparse.ArgumentParser()


    parser.add_argument('-yml', '--yaml_path', type=str, required=False, default=None,
                        help='path of github workflow to execute')

    parser.add_argument('-yp', '--yaml_payload', type=str, required=False, default=None,
                        help='path of json payload for github workflow to execute')

    parser.add_argument('-gt', '--github_token', type=str, required=True,
                        help='token for github')

    args = parser.parse_args()
    return args

def main():
    args = Arguments()

    secrets = {'GITHUB_TOKEN': args.github_token}

    cmd = f"act"
    cmd = cmd + f" -W .github/workflows/{args.yaml_path}"
    for key, value in secrets.items():
        cmd += f' -s {key}={value}'
    cmd += f' -e {args.yaml_payload}'

    logging.debug(f'act command: "{cmd}"')

    try:
        proc = subprocess.run(cmd, shell=True)
    except Exception as e:
        print(f'CLI Check returned exception: {e}')
        return False
    if (proc.returncode):
        return False
    return True

if __name__ == '__main__':
    main()
