#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        # Only a number
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        # A list (not empty)
        if isinstance(data, list) and len(data) > 0:
            for i in data:
                if not isinstance(i, (int, float)) or isinstance(i, bool):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data.")
        if isinstance(data, list):
            for i in data:
                self.storage.append((self.rank, str(i)))
                self.rank += 1
        else:
            self.storage.append((self.rank, str(data)))
            self.rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and len(data) > 0:
            for i in data:
                if not isinstance(i, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data.")
        if isinstance(data, list):
            for i in data:
                self.storage.append((self.rank, i))
                self.rank += 1
        else:
            self.storage.append((self.rank, data))
            self.rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        # Dict
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True
        # List (not empty)
        if isinstance(data, list) and len(data) > 0:
            for i in data:
                if not isinstance(i, dict):
                    return False
                # Check all dicts
                for key, value in i.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data.")
        if isinstance(data, list):
            for i in data:
                text = f"{i['log_level']}: {i['log_message']}"
                self.storage.append((self.rank, text))
                self.rank += 1
        else:
            text = f"{data['log_level']}: {data['log_message']}"
            self.storage.append((self.rank, text))
            self.rank += 1


if "__main__" == __name__:
    pass
