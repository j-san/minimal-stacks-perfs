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

    servers = [{
        "name": "node",
        "addr": "http://localhost:3001",
    }, {
        "name": "go",
        "addr": "http://localhost:3002",
    }, {
        "name": "rust",
        "addr": "http://localhost:3003",
    }, {
        "name": "java spr",
        "addr": "http://localhost:3004",
    }, {
        "name": "python",
        "addr": "http://localhost:3005",
    }, {
        "name": "java vrtx",
        "addr": "http://localhost:3006",
    }]

    first = True
    for srv in servers:
        if not first:
            print()
            print("-" * 10)
            # make sure the processor is idle
            time.sleep(10)
        else:
            first = False

        print(f"\n\n### Running load test for {srv["name"]}:\n")

        if args.verbose:
            cmd = f"curl -s -D - {srv["addr"]}"
            print(cmd)
            results = os.popen(cmd).read()
            print(results)
            print("\n\n")

        cmd = f"hey -n 1000000 -c 100 {srv["addr"]}"
        results = os.popen(cmd).read()

        print(cmd)
        total = float(re.search(r"Total:\s+([0-9.]+)\s+secs", results).group(1))
        avg = float(re.search(r"Average:\s+([0-9.]+)\s+secs", results).group(1))

        if args.verbose:
            print(results)

        print(f"Total time: {total}")
        print(f"Avg response time: {avg}")
        srv["total"] = total
        srv["avg"] = avg

    print("\n")

    print("-" * 120)
    max_total_time = max(srv["total"] for srv in servers)
    servers = sorted(servers, key=lambda srv: srv["total"])

    for srv in servers:
        srv["ratio"] = srv["total"] / max_total_time
        print(f"{srv["name"]:<9}", f"{srv["total"]:<9}", "#" * int(srv["ratio"] * 100))
    print("-" * 120)


if __name__ == "__main__":
    main()
