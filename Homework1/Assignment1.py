import os
import json

def parse_duration(file_path):
    try:
        with open(file_path, "r") as f:
            line = f.readline().strip()
            h, m, s = map(int, line.split(":"))
            return h * 3600 + m * 60 + s
    except Exception:
        return None

def parse_log(file_path):
    fermi = None
    total = None
    try:
        with open(file_path, "r") as f:
            for line in f:
                if "Fermi energy is" in line:
                    try:
                        fermi = float(line.split()[-2])  
                    except:
                        pass
                if "total energy" in line:
                    try:
                        total = float(line.split()[-2])
                    except:
                        pass
        return fermi, total
    except Exception:
        return None, None

def main():
    results = {}
    base_dir = os.path.join(os.path.dirname(__file__), "results")

    all_folders = []
    for root, dirs, files in os.walk(base_dir):
        for d in dirs: 
            folder_path = os.path.join(root, d)
            all_folders.append(folder_path)

    for folder_path in all_folders:
        folder_name = os.path.basename(folder_path)  
        log_file = os.path.join(folder_path, "log.txt")
        duration_file = os.path.join(folder_path, "duration.txt")

        duration, fermi, total = None, None, None
        if os.path.exists(duration_file):
            duration = parse_duration(duration_file)
        if os.path.exists(log_file):
            fermi, total = parse_log(log_file)

        results[int(folder_name)] = {
            "duration_seconds": duration if duration is not None else 0,
            "Fermi_energy": fermi if fermi is not None else 0.0,
            "total_energy": total if total is not None else 0.0,
            "error": (duration is None or fermi is None or total is None)
        }


    output_file = os.path.join(os.path.dirname(__file__), "results_summary.json")
    with open(output_file, "w") as f:
         json.dump(results, f, indent=4, sort_keys=True)

    print(f"outcome have been saved to {output_file}")

if __name__ == "__main__":
    main()





