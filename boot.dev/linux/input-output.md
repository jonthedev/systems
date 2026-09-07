# Input/Output

## exit codes

`0` = success. Anything else = fail (usually `1`). `$?` is the last command’s code.

```bash
echo $?
command1 ; command2      # always run both
command1 && command2     # second only if first succeeded
```

CI, Docker, systemd all use this. JS: `process.exit(0)` / `&&` in npm scripts.

## flags

Options that change a command. `-` short, `--` long. Combine shorts: `-al` is `-a` and `-l`.

```bash
ls -l                 # long listing
ls -a                 # include hidden (dotfiles)
ls -al
ls --help
```

What exists is up to that program — `--help` lists them.

## help

How to use a CLI tool. Try these in order:

```bash
grep --help
grep -h
grep help
```

Shorter than a man page — enough to run the command. `--help` is the reliable one; `-h` is sometimes a different flag (e.g. `grep -h`).

## pipe

`|` — left program’s **stdout** becomes the right program’s **stdin**. No temp file.

```bash
echo "Have you heard the tragedy of Darth Plagueis the Wise?" | wc -w
```

Works because `wc` (and most CLI tools) can read stdin, not only a filepath. JS: `.then` / a stream pipeline — output of one step is input to the next.

## positional arguments

The values — order matters, like function parameters. Flags change *how*; these are *what*.

```bash
cd /home/wagslane
mv file.txt dest/file.txt
```

JS: `printPlayer(100, 2)` vs `{ verbose: true }`. Same split as args vs flags.

## redirect

`>` stdout to a file. `2>` stderr to a file. `<` a file into stdin.

```bash
echo "Hello world" > hello.txt
cat doesnotexist.txt 2> error.txt
wc < input.txt
```

## stderr

Error stream. Same terminal as stdout unless you `2>` it. JS: `console.error`.

```bash
cat doesnotexist.txt 2> error.txt
```

## stdin

Default place a program **reads**. Keyboard, unless you `<` a file into it. Python `input()`, JS stdin.

```bash
wc < input.txt          # stdin — wc never sees the filename
wc input.txt            # argument — wc opens the file itself
```

## stdout

Default print stream — the terminal unless you `>` it. Python `print`, JS `console.log`.

```bash
echo "Hello world"
echo "Hello world" > hello.txt
```

## unix philosophy

1. One job, done well (`ls`, `grep`, `less`).
2. Work together (`grep "hello" some_file.txt | less`).
3. Text streams as the shared interface — that’s why `|` and `>` work.



