# Binary system

Algoroq: [Binary System](https://algoroq.io/learn/introduction-to-system-design/binary-system/)

Study sheet — say this to a junior. Algoroq is the textbook.

## Why computers use 0 and 1

Computers only count with two digits: 0 and 1. That system is called binary. Different patterns of 0s and 1s stand for numbers, letters, images, games, model files — whatever the program agrees they mean.

## Bit vs byte vs the size names

- **Bit** — one 0 or 1. Smallest unit.
- **Byte** — 8 bits. One ASCII letter, or one colour channel (`0–255` in CSS).
- **KB / MB / GB** — bigger piles of bytes. A photo is a few MB. A Qwen GGUF on disk is a few GB. That GB number is “how many bytes is this file,” not “how smart is the model.”

Rule of thumb: bit = one digit, byte = a tiny group of eight, then the names just mean “a lot of bytes.”

## Binary to decimal

Start at the **right** with 1. Each step left, double it. That is where `8 4 2 1` comes from — not a magic list.

```
  start here ──────────────────────────┐
                                       v
  double left    8         4         2         1
                 ← ×2      ← ×2      ← ×2      (ones)
```

A `1` means “count this column.” A `0` means “skip it.”

```
  column value    8    4    2    1
  bits            1    0    1    0
                  8  + 0  + 2  + 0   = 10
```

Same three:

- `1111` → 8+4+2+1 = **15** (every column on)
- `1010` → 8+0+2+0 = **10**
- `0110` → 0+4+2+0 = **6**

Need more columns? Keep doubling left: `16 8 4 2 1`. A full byte is eight columns. All 1s (`11111111`) = 255, which is why CSS `rgb()` maxes at 255.

## Text and color

A letter is stored as a number (ASCII/Unicode), and that number is stored as bits. `"A"` is 65, which is `01000001`.

A pixel is three of those numbers: red, green, blue. You already write this in CSS: `rgb(255, 0, 0)` or `#FF0000` is “red full, green empty, blue empty.” Each channel is one byte.

## The 1000 vs 1024 thing

Drive ads count 1 GB as 1,000,000,000 bytes. The OS counts 1 GiB as 1,024×1,024×1,024 bytes. Same pile of bytes, two rulers — so a “500 GB” disk shows up as ~465 in Finder. The rest did not vanish.

## Why this matters for servers (and later, models)

You read sizes all day: disk full, Docker image too fat, model file bigger than RAM so the box swaps and dies. Knowing bit/byte/GB is so those numbers mean something. Nobody is hiring you to convert `1010` on a whiteboard.
