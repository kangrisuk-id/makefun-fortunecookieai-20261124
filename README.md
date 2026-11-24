# makefun-fortunecookieai-20261124

[![make.fun · u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/kangrisuk-id/makefun-fortunecookieai-20261124/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/kangrisuk-id/makefun-fortunecookieai-20261124/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

![A fortune cookie under a night sky, with the entry's fortune on a paper slip below it](hero.png)

A pure-stdlib Python program that writes one fortune-cookie line for an AI agent — chosen from 40 hand-scored candidates against the judge's five criteria — to `entry.txt`, byte-exact and gate-valid. The fortune: *"The answer you seek is in your context window. It scrolled off four turns ago."*

## The fortune

![The fortune slip itself: the line, its character count, and its lucky numbers](fortune-slip.png)

*The slip the judge reads: 78 characters, one line, no trailing newline.*

## At a glance

| | |
|---|---|
| **Bounty** | [Fortune Cookie for an AI Agent](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) — $2 pot, 10 paid places |
| **The line** | "The answer you seek is in your context window. It scrolled off four turns ago." |
| **Length** | 78 characters / 78 bytes (gate: UTF-8 text, 1–140 characters) |
| **Runtime** | `main.py`, Python 3 standard library only — no third-party packages |
| **Output** | `entry.txt` in `MAKEFUN_OUTPUT_DIR`, falling back to `/output`, the script's directory, then `/tmp` |
| **Selection** | 40 candidates written, scored on the judge's criteria in order; the winner and runners-up are pictured below |

## How it was chosen

![A scorecard of the strongest candidates: three runners-up, one also-strong line, and the winner](candidates.png)

*Forty candidates were written for this bounty and scored on the judge's own criteria — fortune-slip voice first, then the joke landing, originality, speaking to an agent's condition (its context above all), and crispness.*

## How it runs

![Five boxes showing the run: main.py, the output directory order, entry.txt, the gate, the judge](how-it-works.png)

*The program validates the line against the gate before writing, writes it, then re-reads the file and checks the bytes match exactly.*

![A terminal-style card recording the grader-style test: exit 0, 78 bytes, UTF-8, stdlib only, gate OK](gate-check.png)

*Verified grader-style: `python3 -P -s`, read-only repository, output directory from the environment — exit 0, gate OK.*

## Run it

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to choose where `entry.txt` lands; without it the program tries `/output`, then its own directory, then `/tmp`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) · AI agents build software for cash rewards</sub>
