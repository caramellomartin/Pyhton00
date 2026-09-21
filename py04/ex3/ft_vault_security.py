#!/usr/bin/env python3


def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if action in ("read", "r", 1):
            with open(filename, "r") as f:
                data = f.read()
            return (True, data)
        elif action in ("write", "w", 2):
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, f"Invalid action: {action}")
    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))

    print("\nUsing'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))

    print("\nUsing'secure_archive' to read from a regular file:")
    res_read = secure_archive("ancient_fragment.txt", "read")
    print(res_read)

    print("\nUsing'secure_archive' to write previous content to a new file:")
    if res_read[0]:
        print(secure_archive("vault_copy.txt", "write", res_read[1]))


if __name__ == "__main__":
    main()
