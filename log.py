import sys
import os
from datetime import datetime

# --- CONFIGURATION ---
# The script will save your logs to this file.
LOG_FILE = r"E:\tools\activity_log.txt"

def main():
    args = sys.argv[1:]
    
    if not args:
        print("Usage:")
        print("  log [activity]       - Logs a new entry")
        print("  log --view           - Shows the last 10 entries")
        print("  log --search [word]  - Searches for a specific word")
        return

    # COMMAND: --view
    if args[0] == "--view":
        display_logs(limit=10)
        return

    # COMMAND: --search
    if args[0] == "--search" and len(args) > 1:
        search_term = args[1].lower()
        display_logs(search=search_term)
        return

    # DEFAULT: Log an activity
    activity = " ".join(args)
    # UPDATED: Format is now YYYY-MM-DD HH:MM:SS
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {activity}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    print(f"✅ Logged: {activity}")

def display_logs(limit=None, search=None):
    if not os.path.exists(LOG_FILE):
        print("Error: No log file found yet.")
        return

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
        if search:
            print(f"--- Search Results for '{search}' ---")
            results = [l.strip() for l in lines if search in l.lower()]
            for r in results:
                print(r)
            if not results:
                print("No matches found.")
        else:
            print(f"--- Recent Activity (Last {limit}) ---")
            for line in lines[-limit:]:
                print(line.strip())

if __name__ == "__main__":
    main()
  
