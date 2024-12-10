import os
import yaml

# 源文件目录和目标文件
source_dir = "provider/direct"
target_file = "provider/direct.yaml"

# 初始化合并的 payload 列表
combined_payload = []

# 遍历 source_dir 下的所有 YAML 文件
for filename in sorted(os.listdir(source_dir)):
    if filename.endswith(".yaml"):
        filepath = os.path.join(source_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if "payload" in data:
                combined_payload.extend(data["payload"])

# 写入到目标文件
with open(target_file, "w", encoding="utf-8") as f:
    yaml.dump({"payload": combined_payload}, f, allow_unicode=True)

print(f"Combined {len(combined_payload)} rules into {target_file}")
