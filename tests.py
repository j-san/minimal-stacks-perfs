import os
import re
import time
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='Performance Tests',
        description='Test performance on various minimal setup',
    )
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    servers = {
        "node": "http://localhost:3001",
        "go": "http://localhost:3002",
        "rust": "http://localhost:3003",
        "java": "http://localhost:3004",
        "python": "http://localhost:3005",
    }

    for lng, srv in servers.items():
        print(f"\n\n### Running load test for {lng}:\n")

        if args.verbose:
            cmd = f"curl -s -D - {srv}"
            print(cmd)
            results = os.popen(cmd).read()
            print(results)
            print("\n\n")

        cmd = f"hey -n 100000 -c 100 {srv}"
        results = os.popen(cmd).read()

        print(cmd)
        total = re.search(r"Total:\s+([0-9.]+)\s+secs", results).group(1)
        avg = re.search(r"Average:\s+([0-9.]+)\s+secs", results).group(1)

        if args.verbose:
            print(results)

        print(f"Total time: {total}")
        print(f"Avg response time: {avg}")
        print()
        print("-" * 10)
        time.sleep(3)


if __name__ == "__main__":
    main()
