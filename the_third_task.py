import sys
from collections import defaultdict
from typing import List, Dict

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return {}
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2].upper(),
        'message': parts[3]
    }

def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            logs = [entry for line in file if (entry := parse_log_line(line))]
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda log: log['level'] == level.upper(), logs))

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return dict(counts)

def display_log_counts(counts: Dict[str, int]):
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level in sorted(counts.keys()):
        print(f"{level:<17}| {counts[level]}")

def display_logs_by_level(logs: List[dict], level: str):
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) >= 3 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered = filter_logs_by_level(logs, level_filter)
        display_logs_by_level(filtered, level_filter)

if __name__ == "__main__":
    main()
