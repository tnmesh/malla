import os
import json
import sys

from pathlib import Path

from  malla.database.repositories import NodeRepository
from  malla.mqtt_capture import update_node_cache

def main() -> None:
    if len(sys.argv) < 2:
        print(
            "Usage: python scripts/get_node.py <node_id>"
        )
        sys.exit(1)

    node_id = sys.argv[1];

    node = NodeRepository.get_node_details(node_id=node_id)

    if node is None:
        print(f"Node {node_id} not found")
        sys.exit(1)

    nodeData = node.get('node')

    print(json.dumps(nodeData, indent=4))

if __name__ == "__main__":
    main()
