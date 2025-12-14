import os
import sys
from pathlib import Path

from  malla.database.repositories import NodeRepository
from  malla.mqtt_capture import update_node_cache

def main() -> None:
    if len(sys.argv) < 3:
        print(
            "Usage: python scripts/set_as_infrastructure_node.py <node_id> <True|False>"
        )
        sys.exit(1)

    node_id = sys.argv[1];
    value = sys.argv[2];

    if not isinstance(value, str) or value not in ['True', 'False']:
        print("Value must be True or False")
        sys.exit(1);

    value = value == "True"

    node = NodeRepository.get_node_details(node_id=node_id)

    if node is None:
        print(f"Node {node_id} not found")
        sys.exit(1)

    update_node_cache(
        node_id=node_id,
        is_infrastructure_node=value
    )

    print(f"Marked {node_id} as infrastructure node={value}")

if __name__ == "__main__":
    main()
