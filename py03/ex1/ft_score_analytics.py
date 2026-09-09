#!/usr/bin/env python3
import sys


def score_analytics() -> None:
    print("=== Player Score Analytics ===")
    tot_args = len(sys.argv)
    scores: list[int] = []
    if tot_args > 1:
        for arg in sys.argv[1:]:
            try:
                score = int(arg)
                scores.append(score)
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        tot_player = len(scores)
        if tot_player >= 1:
            print(f"Scores processed: {scores}")
            print(f"Total players: {tot_player}")
            print(f"Total score: {sum(scores)}")
            average = (sum(scores)) / (tot_player)
            print(f"Average score: {average}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        else:
            print(
                "No scores provided. Usage: python3 "
                "ft_score_analytics.py <score1> <score2> ..."
            )
    else:
        print(
                "No scores provided. Usage: python3 "
                "ft_score_analytics.py <score1> <score2> ..."
            )


if __name__ == "__main__":
    score_analytics()
    print()
