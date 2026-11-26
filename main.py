#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry.

Writes one original funny line to /output/entry.txt.
Pure standard library, deterministic: the same line every run.

Candidate one-liners, all written fresh for this entry and scored against
the judge's brief (instantly gettable, surprise, tight, fresh, clean read):

1. "My smart fridge just filed for divorce - it says I keep opening it at
   2 a.m. just to stare, and that's not a relationship, that's
   surveillance."  (Good twist, but the punchline needs a beat to land.)
2. "My doctor said I need more iron, so I started dating a blacksmith -
   the relationship is going well, but the hugs are a workplace hazard."
   (Clean literal-take twist, but "dating the X" is a familiar setup.)
3. "My houseplant died, so I replaced it with a plastic one - it thrives
   on neglect, asks for nothing, and honestly, it's the healthiest
   relationship I have."  (Relatable, but the ending is predictable
   halfway through.)
4. "I bought a self-help book, but it just sits on the shelf judging me -
   which, to be fair, is the most honest help anyone's ever given me."
   (Nice, but the laugh is gentle, not a surprise.)
5. "My Wi-Fi died during a job interview, so I finished it by carrier
   pigeon - the pigeon got the job, and honestly, it had better
   references."  (CHOSEN: the setup is ordinary, the twist is absurd and
   lands twice - the bird gets hired, then it beats me on references.
   Every word earns its place and the last clause is the laugh.)
6. "I tried to teach my dog to fetch my slippers, but he unionised the
   other pets instead - now I fetch the slippers, and he supervises."
   (Strong, but one twist only; the pigeon line's double twist wins.)
7. "I told my smart speaker a secret, and it replied, 'I've heard
   worse' - which is exactly what my grandmother used to say, and now
   I'm worried they're related."  (Funny, but the grandmother turn
   muddies the read-aloud.)

The chosen line avoids stock puns and office/meeting/resignation jokes
entirely: a dead Wi-Fi connection escalates to a bird out-qualifying the
applicant, and the punchline lands on the final word.
"""

import os

LINE = (
    "My Wi-Fi died during a job interview, so I finished it by carrier "
    "pigeon \u2014 the pigeon got the job, and honestly, it had better "
    "references."
)


def validate_line(line: str) -> str:
    """Enforce the gate: 1-200 characters, not whitespace-only, valid UTF-8."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    return line


def main() -> None:
    line = validate_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
