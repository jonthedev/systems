# Local CLI

## top

Which programs are using CPU and RAM. Like Activity Monitor, in the terminal. It loops until `q`.

Mac and Linux `top` are not the same binary.

```bash
top
top -o mem    # Mac: start sorted by memory
q             # quit
```

While running:

| | Memory | CPU |
| --- | --- | --- |
| Mac | lowercase `o`, then `mem`, Enter | default |
| Ubuntu | `M` | `P` |

Capital `O` on a Mac is **secondary** sort. That is the `secondary key [-pid]:` prompt, not “sort by RAM.”

## Interrupt (Ctrl+C)

Stop a stuck or unwanted program. The kernel sends SIGINT (interrupt). Same idea as hitting stop on a hung request.

```bash
# while a command is running:
Ctrl+C
```

Typo, no network, too much data, or a hang: Ctrl+C. `top` prefers `q`.

## ps

Process status. Every running program has a PID.

```bash
ps aux
ps aux | grep malicious.sh
```

`aux` = all users, extra columns. Pipe to `grep` to find one name. You will often see two rows: the program, and grep itself. Use the PID of the program.

## kill

When SIGINT is ignored, open a **second** terminal and kill by PID.

```bash
kill <PID>
```

Default is SIGTERM. If that still fails: `kill -9 <PID>` (SIGKILL). Do not spray kill at random PIDs.
