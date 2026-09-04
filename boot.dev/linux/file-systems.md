# Filesystems

## cat

Print file(s) to the terminal.

```bash
cat file1.txt
cat file1.txt file2.txt
```

## cd / paths

`/` = from the root (absolute). Anything else = from `pwd` (relative). `.` = this directory. `..` = parent.

```bash
cd /home/lane             # absolute
cd worldbanc              # relative
cd ..                     # parent
```

## cp

Copy. Original stays. `-R` for directories.

```bash
cp source_file.txt destination/
cp -R my_dir new_dir
```

## find

Files and dirs by **name**, not contents (`grep` is contents).

```bash
find some_directory -name hello.txt
find some_directory -name "*.txt"
find some_directory -name "*chad*"
```

Quote the pattern so the shell doesn't expand `*`.

## grep

Print lines that contain a string. Case-sensitive.

```bash
grep "hello" words.txt
grep "hello" hello.txt hello2.txt
grep -r "hello" .         # this dir and all subdirs
```

## head / tail

First or last *n* lines. Default 10.

```bash
head -n 10 file1.txt
tail -n 10 file1.txt
tail -f /var/log/syslog   # follow as it grows
```

## home

Where you land at login. `~` and `$HOME` are the same path.

```bash
cd ~
cd $HOME
echo $HOME
```

Do project work here. Leave `/bin`, `/etc`, `/var` alone unless you mean to.

## less

Page through a file. Use instead of `more`.

```bash
less file1.txt
```

`space` page down · `b` page up · `/` search · `q` quit

## mkdir

```bash
mkdir my_directory
mkdir -p a/b/c            # parents too; no error if it exists
```

## mv

Move or rename. Can't move the directory you're in.

```bash
mv draft.md final.md
mv photo.png images/      # into images/, keep the name
mv invoice.pdf ../
```

## pwd

Where this shell is.

```bash
pwd
```

## rm

Delete. No trash.

```bash
rm some_file.txt
rm -r some_directory      # directory and everything inside
```

## touch

Create empty file if missing. If it exists, only timestamps change — content stays.

```bash
touch new_file.txt
touch a.txt b.txt
```
