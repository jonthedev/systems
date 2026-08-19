# Basics of CPU

Algoroq: [Basics of CPU](https://algoroq.io/learn/introduction-to-system-design/cpu-basics/)

Study sheet — say this to a junior. Algoroq is the textbook.

This chapter feels dense because it is three ideas, not one: **how one instruction runs**, **how many workers**, **how fast the clock ticks**. You do not need the restaurant game or the GHz arithmetic.

## One core

A **core** is one worker that runs **one stream of instructions** at a time. Fetch → decode → execute → write the result. Then the next instruction. That loop is the pipeline. “Billions of times a second” is just that loop on a clock.

## Cores vs GHz

- **More cores** = more workers. Helps if the program can split work (video export, compiling, some servers).
- **Higher GHz** = each worker chops faster. Helps if the work is stuck on **one** thread (a lot of games, a lot of old code).
- A 5 GHz 4-core box can beat an 8-core on a single-thread job and lose on a parallel job. More GHz is not automatically faster. Cache and waiting on disk/RAM still win a lot of the time (last chapter).

Frontend parallel: the JS main thread is basically one core. Extra cores do not speed up a `for` loop on that thread. Web workers / extra Node processes are how you use more cores.

## CPU-bound vs I/O-bound

This is the line you keep.

- **CPU-bound:** the box is busy *thinking* (encode, compress, run a model that already fits in RAM). Faster/more cores help.
- **I/O-bound:** the box is busy *waiting* (disk, network, swap). A fancier CPU barely helps. Fix the wait — RAM, disk, network, async.

Qwen that fits in RAM can be CPU-bound (the chip is chewing tokens). Qwen that does not fit and hits swap is I/O-bound (the chip is waiting on disk). Same program, different bottleneck.

## Why this matters for servers

When something is slow, ask: is the CPU pegged, or is it idle waiting on disk/network? `htop` later. Wrong fix is “buy a faster CPU” when the machine is swapping.
