import os
import yaml
import argparse

def combine_yaml_files(input_dir, output_file):
    """
    Combine all YAML files in a directory into a single YAML file.

    Args:
        input_dir (str): Directory containing YAML files to combine.
        output_file (str): Path to the output YAML file.
    """
    # Ensure the input directory exists
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        return

    combined_payload = []

    # Iterate through YAML files in the input directory
    for filename in sorted(os.listdir(input_dir)):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            filepath = os.path.join(input_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    data = yaml.safe_load(f)
                    if data and "payload" in data:
                        combined_payload.extend(data["payload"])
                except yaml.YAMLError as e:
                    print(f"Error parsing {filename}: {e}")

    # Write the combined payload to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        yaml.dump({"payload": combined_payload}, f, allow_unicode=True)

    print(f"Combined {len(combined_payload)} rules from '{input_dir}' into '{output_file}'")


if __name__ == "__main__":
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Combine YAML files into one.")
    parser.add_argument(
        "input_dir",
        type=str,
        help="Directory containing YAML files to combine."
    )
    parser.add_argument(
        "output_file",
        type=str,
        help="Path to the output YAML file."
    )

    args = parser.parse_args()

    # Call the combine function with provided arguments
    combine_yaml_files(args.input_dir, args.output_file)
