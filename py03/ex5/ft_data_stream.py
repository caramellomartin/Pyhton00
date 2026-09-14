#!/usr/bin/env python3
import random
from typing import Generator


PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = [
    "run", "eat", "sleep", "grab", "move",
    "climb", "swim", "use", "release"
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(events: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        yield events.pop(index)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()
    for i in range(1000):
        player, action = next(event_stream)
        print(f"Event {i}: Player {player} did action {action}")

    event_list = []
    for _ in range(10):
        event_l = next(event_stream)
        event_list.append(event_l)
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
