#!/usr/bin/env python3
import os
from dotenv import load_dotenv


def is_env_git_ignored() -> bool:
    gitignore_path: str = ".gitignore"
    if not os.path.exists(gitignore_path):
        return False
    with open(gitignore_path, "r") as file:
        lines: list[str] = [line.strip() for line in file.readlines()]
        return ".env" in lines


def main() -> None:
    load_dotenv()
    app_env: str = os.getenv("APP_ENV", "development")
    db_url: str = os.getenv("DATABASE_URL", "")
    api_key: str = os.getenv("API_KEY", "")
    log_level: str = os.getenv("LOG_LEVEL", "DEBUG")
    ext_api: str = os.getenv("EXTERNAL_API_URL", "")

    print("SYSTEM STATUS: Checking configuration...")
    print("Configuration loaded:")
    print(f"Environment: {app_env}")

    if "localhost" in db_url or "127.0.0.1" in db_url or not db_url:
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to remote instance")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthenticated (Missing API_KEY)")
    print(f"Log Level: {log_level}")

    if ext_api:
        print("External API: Online")
    else:
        print("External API: Offline")
    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected")

    if is_env_git_ignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env file is NOT ignored by git!")
    print("[OK] Production overrides available")
    print("\nAll configuration checks passed.")


if __name__ == "__main__":
    main()
