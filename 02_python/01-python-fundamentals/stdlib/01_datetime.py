"""
Demonstrates datetime in Python.
Covers: date arithmetic, timezones with zoneinfo
"""
from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo

def main():
    now = datetime.now()
    print(f"Current local time: {now}")

    # Arithmetic
    tomorrow = now + timedelta(days=1)
    print(f"Tomorrow: {tomorrow}")

    # Formatting
    print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

    # Timezones
    utc_now = datetime.now(ZoneInfo("UTC"))
    tokyo_now = utc_now.astimezone(ZoneInfo("Asia/Tokyo"))
    print(f"UTC: {utc_now}")
    print(f"Tokyo: {tokyo_now}")

    # Specific date
    bday = date(1990, 5, 20)
    print(f"Birthday: {bday}")
    delta = date.today() - bday
    print(f"Days since birth: {delta.days}")

if __name__ == "__main__":
    main()
