# How computers work

Algoroq: [How Computers Work](https://algoroq.io/learn/introduction-to-system-design/fundamentals-of-computing/)

Write below in your own words. Short is fine. If it still sounds like their city metaphor, rewrite.

## CPU

What does it actually do?

Kind of like the person running the orchestra, except the CPU is also _playing_ — it fetches, decodes, and actually runs the instructions. The OS is closer to the conductor (who gets the CPU next).

## RAM

What is it for? What happens when you power off?

The work desk. Open an app and it takes RAM to run. RAM is fast (nanoseconds) but limited and expensive. Fill it up and the machine crawls.

Power off and RAM is empty. That's why IT support may suggest you to restart your computer.

## Storage (disk / SSD)

How is it different from RAM?

The warehouse. Bigger than RAM, slower to get at, but it survives power-off.

When you save, the file lives in RAM first (the desk). The CPU / OS then writes a copy to disk. RAM doesn't "save" the file by itself.

## Input / output

One example of a request going through the machine.

How you talk to the box. Keyboard in → CPU does something with it → pixels on the display (output).

## Why this matters for servers (and later, models)

One or two sentences. Not “more RAM always = faster.”

RAM is the work desk. If an LLM is bigger than RAM, the machine starts using swap (disk pretending to be RAM) and everything gets slow. That's why I had to drop to smaller Qwen models so the computer could still do other stuff. Extra RAM wouldn't help if the CPU is the bottleneck anyway.
