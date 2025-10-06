import os
import json

output_path = os.path.join("build", "api", "v1", "plugins.json")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

data = {
    "name": "",
    "plugins": []
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"Generated plugin manifest at {output_path}")