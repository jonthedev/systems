# Computer memory hierarchy

Algoroq: [Computer Memory Hierarchy](https://algoroq.io/learn/introduction-to-system-design/memory-hierarchy/)

Study sheet — say this to a junior. Algoroq is the textbook.

## The pyramid

Fast and tiny at the top. Slow and huge at the bottom. Same data, different shelves:

```
registers   tiny, inside the CPU, this cycle
L1 / L2 / L3 cache   still on the chip, nanoseconds
RAM         the work desk  (you already know this)
SSD         warehouse, persists, slower
HDD         even slower warehouse (spinning disk)
```

You do not pick one. The machine uses all of them. Hot data stays close to the CPU. Cold data lives on disk.

Do not memorise “L1 is 32KB.” Remember the order and that each step down is *a lot* slower (RAM vs SSD is the one you will actually feel).

## Cache in one sentence

The CPU checks the small fast shelves first. If the bytes are there, that is a **hit** (cheap). If not, a **miss** — walk down to RAM or disk, then copy the bytes upward so the next time is a hit.

That is why opening an app the second time feels snappier. Not magic. The data is already on a closer shelf.

Caches work because of **locality**: you tend to reuse the same bytes soon (temporal), and you tend to need the next bytes nearby (spatial — a loop over a list). Sequential beats random. Databases and disks care about that later.

## Why you cannot have “infinite L1”

Bigger cache is slower to search and costs a fortune. Small and close beats huge and sluggish. Same idea as “more RAM is not always faster” from chapter 1.

## Why this matters for servers (and later, models)

A Qwen file on disk is the warehouse. Loading it into RAM is the desk. If it does not fit, the OS uses **swap** (disk pretending to be RAM) and everything crawls. Cache is the even faster shelf *above* RAM — you do not manage it by hand; you feel it when the working set fits.

Ops takeaway: fit the hot working set in RAM. Disk is for keeping stuff, not for running it.
