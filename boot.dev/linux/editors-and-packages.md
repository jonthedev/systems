# Editors and package managers

A package manager installs, updates, and removes software, and it pulls in dependencies. You ask for a name. It fetches the official package and puts the binary on your `PATH`.

| Machine | Tool |
| --- | --- |
| Ubuntu / studio VM / remote Linux | `apt` |
| Mac | Homebrew (`brew`) |

Same job. Different catalogue. Like `npm` vs `pnpm`: the command shape is similar, the registry is not.

```bash
# Ubuntu
sudo apt update
sudo apt install neovim

# Mac
brew install neovim

nvim --version
```

`apt` needs `sudo` because it writes system packages. Homebrew installs into your user prefix, so most `brew install` lines do not need `sudo`.

`nvim` is the binary. Neovim is a modern Vim. This chapter installs it. Motions and config stay in the Udemy course / `cheatsheets/vim/vim.md`.

## Using Neovim

`nvim` opens in **normal** mode. You cannot type text yet. That is on purpose.

| Key | What it does |
| --- | --- |
| `i` | insert mode (type) |
| `Esc` | back to normal |
| `:w` Enter | write (save) |
| `:q` Enter | quit |

```bash
nvim worldbanc/public/company_info.md
# i → edit → Esc → :w → :q
cat worldbanc/public/company_info.md
```

`-- INSERT --` at the bottom means you can type. After `Esc` it goes away. `:w` then `:q` is the same as `:wq`. If it refuses to quit, you still have unsaved changes. `:q!` throws them away. That last one is in the cheatsheet, not this lesson.

## How a package manager works

`apt` and `brew` are two catalogues. Same job exists elsewhere (`dnf`, `pacman`, `apk`). When you `install neovim` it roughly:

1. Check if it is already installed
2. Download from the official repository
3. Unpack it onto the filesystem
4. Install dependencies
5. Put the binary on your `PATH` (so `nvim` works without a full path)

It also tracks **what** and **which version**, so you do not end up with ten copies of the same app.

```bash
which nvim
```

`which` prints the file the shell will run. That is where the package manager dropped the binary, not a second copy in your project folder.

On this Mac, Homebrew lands at `/opt/homebrew/bin/nvim`. On the Ubuntu server, apt lands at `/usr/bin/nvim`.

## Webi

Not a package manager you install. You paste one HTTPS command from [webinstall.dev](https://webinstall.dev) that downloads that tool’s installer and runs it. Often the binary goes in `~/.local/bin`.

That is `curl … | sh`. The script can do anything your user can do. HTTPS plus a source you actually trust is the bar. Do not paste installer pipes from random blogs.

This lesson used it for `lsd` (ls deluxe):

```bash
lsd worldbanc/private/transactions
lsd --tree worldbanc/private
lsd --tree --classic worldbanc/private/transactions
```

`--classic` is ASCII boxes (no Nerd Font icons). Icons need a Nerd Font in the terminal app, including on Windows Terminal if you use WSL.

## Code editors

Two shapes:

- **Terminal:** Neovim / Vim / Emacs. Runs in the shell. What this chapter already installed.
- **GUI:** windows, tabs, file tree, extensions. VS Code, Cursor, IntelliJ, Zed.

Boot.dev suggests Zed if you have nothing yet. You already have **Cursor** (GUI) and **Neovim** (terminal). Skip the Zed install.

Zed is a fast GUI editor written in Rust, from people who worked on Atom. Same job as VS Code, lighter process. Lane uses it. Cursor is VS Code plus the AI loop you already work in. No need to switch.
