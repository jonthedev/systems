# Permissions

## Users

Unix is multi-user even if you are the only person at the keyboard. Each account has a home (`~`), files, and permissions. `root` is the superuser. It can change anything.

```bash
whoami          # this account
echo $HOME      # this account’s home
```

## sudo / root

`root` is the superuser. It can read, write, and delete anything. `sudo` runs **one command** as root (unless the box is set up differently). The next prompt is still you.

```bash
sudo <command>
sudo apt update
sudo whoami     # root, because this command ran as root
```

Use it when you understand the command. Do not paste a `sudo` line you cannot read.

The classic foot-gun is `rm -r -f /` (or `rm -rf /`): recursive + force on the disk root. Most systems refuse that unless you also pass `--no-preserve-root`. With `sudo`, those safeguards are easier to bypass. Do not run it. On the studio VM, ask before you use `sudo` at all.

Ctrl+C / `kill` stop a process. `sudo` is the opposite problem: too much power, not too little.

## The 10-character string

`ls -l` prints who can do what. Ten characters.

```text
drwxr-xr-x
│└┬┘└┬┘└┬┘
│ │  │  └ others (everyone else)
│ │  └──── group
│ └─────── owner (usually who created it)
└───────── type: d = directory, - = regular file
```

Each trio is `rwx`: read, write, execute. A dash means that bit is off.

| Bits | Meaning |
| --- | --- |
| `rwx` | all |
| `rw-` | read + write |
| `r-x` | read + execute |
| `---` | nothing |

On a **file**: read = open it, write = change it, execute = run it as a program.

On a **directory** the words mean different things:

- **read** = `ls` the names inside
- **write** = create / rename / delete inside
- **execute** = `cd` into it (and use a path through it)

Without directory `x`, you cannot enter the folder even if you can read the listing.

Symbolic is the letters. Octal is the same bits as numbers: `r=4`, `w=2`, `x=1`. Add them. `7` = `rwx`, `5` = `r-x`. So `755` is `rwxr-xr-x`.

On your own machine you mostly care about **owner**. That is usually you.

## chmod

Change mode. Sets those `rwx` bits. You need to own the file, or be root.

Who: `u` owner, `g` group, `o` others, `a` all three.

How: `=` set exactly, `+` add bits, `-` remove bits.

```bash
chmod u=rwx,g=,o= file.txt    # owner all, everyone else nothing
chmod g+w file.txt            # add write for the group, leave the rest
chmod -R u=rwx,g=,o= DIR      # same bits on DIR and everything inside
chmod u=rwx,g=rwx,o= .        # current directory only (no -R)
```

`.` is this directory. `-R` walks the tree. Same danger class as `rm -R`: one wrong path and a lot of files change.

Octal is the same command with numbers. `770` is `rwxrwx---`. `chmod 770 file` and `chmod u=rwx,g=rwx,o= file` are the same bits.

## chmod +x

A script you can read is not always a script you can run. New files are often `644` (`rw-r--r--`): read/write for you, read for everyone, **no execute**.

```bash
./conquerworld.sh
# bash: ./conquerworld.sh: Permission denied

chmod +x conquerworld.sh
./conquerworld.sh
```

`+` adds bits and leaves the rest. `chmod +x` adds execute for owner, group, and others. It does not take away read or write.

`Permission denied` here means the file exists. The execute bit is off. “No such file or directory” is a different error: wrong path or name.

## chown

Change owner. Needs root, so you prefix `sudo`. `chmod` is enough when **you** already own the file. `chown` is for when you need to hand ownership to someone else (often `root`).

`ls -l` shows owner and group as the two names after the permission string:

```text
drwxr-xr-x  2  root  staff  4096  contacts
            │   │      │
            │   │      └ group
            │   └ owner
            └ link count (ignore for now)
```

```bash
sudo chown -R root contacts
```

`-R` is the same recursive idea as `chmod -R`: the directory **and** everything inside. After this, `root` is the owner. Your account is now “group” or “others” for that tree, so `chmod` on it may fail until you use `sudo` again.

## Using sudo

After `chown` to `root` and mode `drwx------`, only the owner can enter or list that folder. You are not root (`whoami` is still you). A plain `ls` or `cat` inside `contacts` is **Permission denied**.

`sudo ls` / `sudo cat` works because that one command runs as root, and root is the owner.

Check the setup with `ls -l` from the parent: owner column `root`, permissions `drwx------`, and you are not signed in as root.

