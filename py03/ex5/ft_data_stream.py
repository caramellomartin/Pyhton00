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
    while len(events) > 0:
        index = random.randrange(len(events))
        chosen_event = events.pop(index)
        yield chosen_event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()
    for i in range(1000):
        curr_event = next(event_stream)
        player_name = curr_event[0]
        player_action = curr_event[1]
        print(f"Event {i}: Player {player_name} did action {player_action}")

    event_list: list[tuple[str, str]] = []
    for _ in range(10):
        new_event = next(event_stream)
        event_list.append(new_event)
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
