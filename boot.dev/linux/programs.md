# Programs

A program is a set of instructions. An **executable** is a file that holds one. People use the words interchangeably.

## bash / sh / zsh

`sh` is the original Unix shell (Bourne). POSIX, basic. `bash` and `zsh` can run `.sh` scripts **and** extra features.

| Shell | Typical home |
| --- | --- |
| `sh` | Scripts (`#!/bin/sh`) — lowest common denominator |
| `bash` | Linux interactive |
| `zsh` | macOS interactive |

This course works in bash and zsh. `echo $SHELL` prints yours.

## Compiled vs interpreted

| | Compiled (Go, C, Rust) | Interpreted (Python, JS, Ruby, `.sh`) |
| --- | --- | --- |
| What you run | Machine code the CPU executes | Source text another program reads |
| Need installed? | Usually just the binary | The **interpreter** (`python3`, `node`, `sh`) |
| `cat` the file | Garbage (binary) | Readable text |

Frontend parallel: a Vue app in the browser is interpreted (JS engine). A Go CLI on a server is compiled — copy the binary, no runtime language install.

`.sh` scripts are interpreted by the **shell**. `/bin/sh` itself is a compiled program (often C). Both are “executables”; only the binary runs without a helper.

## env / export

Local `name=Lane` is this shell only. **Export** copies it into the environment so child programs (`./script.sh`) can read `$NAME`. Session only — close the terminal, it’s gone.

```bash
env                       # list environment
export NAME="Lane"
echo $NAME
./introduce.sh            # script sees $NAME
unset NAME
WARN_MESSAGE="once" ./warn.sh    # this command only, not the session
```

JS parallel: `process.env.NAME`. Same bag of key/value the parent process handed you.

## PATH

Colon-separated list of directories. Bare commands (`ls`, `python3`) are found by walking this list. First match wins.

```bash
echo $PATH
# /usr/local/bin:/usr/bin:/bin
export PATH="$PATH:/some/new/directory"   # append — don't drop the old list
```

`command not found` after an install: the binary is probably in a dir that isn’t on PATH. The installer usually prints that path.

`$PATH` is the current list; `:` adds another directory. This session only (same as other `export`s).

That’s why `ls` works and `program.sh` in this folder does not — `.` is usually **not** on PATH. Use `./program.sh` or a path with a `/`.

JS parallel: `npx` / `node_modules/.bin` is a mini-PATH for project binaries.

## Running a file

Type the **path** to run it. In the current directory you need `./` so the shell does not look for an installed command (`ls`, `mkdir`, …).

```bash
mydir/program.sh      # path with a slash — fine
./program.sh          # here: . = this directory
program.sh            # shell searches PATH, usually "command not found"
```

`./program.sh` and `program.sh` are the same *path* (`.` is this dir). The `./` is a signal: run **this file**, not a program from PATH.

JS parallel: `./script.sh` is like `./node_modules/.bin/vite` — a file here, not a global `vite`.

## Shebang

First line of a script. Tells the system which interpreter to use when you run the **file** (`./script.py`), not when you call `python3 script.py` yourself.

```bash
#!/usr/bin/python3
#!/bin/sh
```

Format: `#! interpreter [optional-arg]`. Compiled binaries don’t need this — the CPU already knows how to run them.

## which

Where an installed command actually lives.

```bash
which sh          # usually /bin/sh
which python3
```

`cat /bin/sh` looks like junk — compiled. `cat script.sh` is text — interpreted.
