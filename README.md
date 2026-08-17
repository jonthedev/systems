# Systems

Public record of a move from **frontend engineering** into **platform and infrastructure** work.

I have spent six years shipping production UI — JavaScript, TypeScript, Vue, Nuxt, React, and Next.js. That work is at [j-dev.online](https://j-dev.online/). The next step is the layer under that UI: how machines run, how services talk, and how that work gets shipped.

Work lives in this repo as I go — local exercises and git history.

## Why this, in this order

Hands first, then names for what those hands are building.

1. **[Boot.dev](https://www.boot.dev/dashboard) — DevOps Engineer Path**  
   The full path, in their order. The platform is the syllabus and the grader. Each exercise is also reproduced locally — real shell, real toolchain, git history — so the work is not trapped in a browser tab.

   | | Course |
   |---|---|
   | 1 | Learn Python for Beginners |
   | 2 | Learn Linux |
   | 3 | Build a BookBot |
   | 4 | Learn Git |
   | 5 | Learn Object Oriented Programming |
   | 6 | Build Asteroids |
   | 7 | Personal Project 1 |
   | 8 | Learn Go |
   | 9 | Learn HTTP Clients |
   | 10 | Learn SQL |
   | 11 | Learn HTTP Servers |
   | 12 | Learn Docker |
   | 13 | Learn Logging and Observability |
   | 14 | Learn AWS |
   | 15 | Learn CI/CD |
   | 16 | Learn Kubernetes |
   | 17 | Capstone Project |

2. **[Algoroq](https://algoroq.io/learn/introduction-to-system-design/fundamentals-of-computing/) — Introduction to System Design**  
   After Boot.dev is in motion.

   | | Section |
   |---|---|
   | 1 | Fundamentals of Computers |
   | 2 | Computer Networking Fundamentals |
   | 3 | Fundamentals of Storage |
   | 4 | Fundamentals of REST APIs |
   | 5 | Database Fundamentals |
   | 6 | Caching Fundamentals |
   | 7 | Foundations of System Design |

Homelab, model serving, and intermediate design studies come later, when this foundation is real.

## Layout

```
systems/
  boot.dev/     DevOps Engineer Path — local exercises
  algoroq/      Introduction to System Design
```

Python files under `boot.dev/python-sandbox/` use normal `#` comments. A `*` or `?` right after `#` is a local note convention (general vs important) for the editor; it is not extra Python syntax. The interpreter ignores the whole line either way.
