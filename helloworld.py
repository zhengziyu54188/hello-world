#!/usr/bin/env python3
"""A cinematic typewriter with scrolling character effects."""

import sys
import time
import random


def typewrite(
    text: str,
    delay: float = 0.05,
    flicker: bool = True,
) -> None:
    """
    Print text character by character with a glitch-scroll effect.

    Each character:
      1. Flashes a random bright color briefly (the "ghost" frame)
      2. Settles into its final color after a tiny delay
    """
    RESET = "\033[0m"
    PALETTE = [
        "\033[92m",  # bright green
        "\033[96m",  # bright cyan
        "\033[94m",  # bright blue
        "\033[95m",  # bright magenta
        "\033[93m",  # bright yellow
    ]

    for ch in text:
        if flicker and ch != " ":
            ghost = random.choice(PALETTE)
            sys.stdout.write(f"{ghost}{ch}{RESET}")
            sys.stdout.flush()
            time.sleep(delay * 0.4)
            # Erase the ghost character and print the final one
            sys.stdout.write(f"\b{RESET}{ch}")
        else:
            sys.stdout.write(ch)

        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write("\n")
    sys.stdout.flush()


def scroll_reveal(
    text: str,
    speed: float = 0.08,
) -> None:
    """
    Reveal text character by character, building it up in place.

    Each new character lights up bright-yellow as it lands,
    then fades to dim — but all characters stay on screen.
    """
    DISCOVERED = "\033[2m"   # dim — already revealed
    LANDING = "\033[1;93m"   # bright-yellow — just landed
    RESET = "\033[0m"

    for i, ch in enumerate(text):
        # Build the line: already-revealed (dim) + current (bright) + cursor
        revealed = DISCOVERED + text[:i] + RESET if i > 0 else ""
        landing = LANDING + ch + RESET
        sys.stdout.write(f"\r{revealed}{landing}")
        sys.stdout.flush()
        time.sleep(speed)

    # Final: all characters in normal color, stay on screen
    sys.stdout.write(f"\r{RESET}{text}\n")
    sys.stdout.flush()


def main() -> None:
    message = "Hello, World!"

    # --- Act 1: typewriter glitch effect ---
    typewrite(message, delay=0.06, flicker=True)
    time.sleep(0.3)

    # --- Act 2: scroll-reveal the same message ---
    scroll_reveal(message, speed=0.08)
    time.sleep(0.3)
if __name__ == "__main__":
    main()
