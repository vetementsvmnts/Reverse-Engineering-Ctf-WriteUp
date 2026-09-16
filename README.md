<div align="center">

```
 ██████╗██████╗  █████╗  ██████╗██╗  ██╗███╗   ███╗███████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝████╗ ████║██╔════╝
██║     ██████╔╝███████║██║     █████╔╝ ██╔████╔██║█████╗  
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██║╚██╔╝██║██╔══╝  
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗██║ ╚═╝ ██║███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
        R E V E R S E   E N G I N E E R I N G   C T F
```

**Static and dynamic analysis writeups for reverse-engineering challenges sourced from crackme.one**

[![Ghidra](https://img.shields.io/badge/Ghidra-1A1A1A?style=for-the-badge&logo=ghidra&logoColor=00FF41)](https://ghidra-sre.org/)
[![x64dbg](https://img.shields.io/badge/x64dbg-2E7D32?style=for-the-badge&logoColor=white)](https://x64dbg.com/)
[![IDA](https://img.shields.io/badge/IDA%20Pro-0078D4?style=for-the-badge&logoColor=white)](https://hex-rays.com/ida-pro/)
[![crackmes.one](https://img.shields.io/badge/crackmes.one-181717?style=for-the-badge&logoColor=00FF41)](https://crackmes.one/)
[![License: MIT](https://img.shields.io/badge/License-MIT-00FF41?style=for-the-badge)](LICENSE)

</div>

---

## `~$ cat abstract.md`

This repository is a growing collection of writeups for reverse-engineering challenges pulled from
**crackmes.one**, spanning multiple architectures, languages, and protection schemes. Each entry documents
the full analysis path — static disassembly, dynamic debugging, and either a keygen, a patch, or an
extracted algorithm — rather than just a "flag found" screenshot.

Methodology per challenge: **triage → static analysis → dynamic analysis → solve → document**, with
difficulty, language, and platform tagged for each entry so the index stays browsable.

---

## `~$ cat brief.md`

**Objective:** Build reverse-engineering proficiency across binary formats and protection schemes by solving
crackmes ranging from beginner to hard difficulty, documenting the exact static/dynamic technique that
cracked each one.

**Environment:** Challenges downloaded directly from crackmes.one, analyzed in an isolated VM — no
production systems, licensed software, or real vendor binaries involved.



## `~$ cat structure.md`

```
Reverse-Engineering-CTF/
├── 01-<challenge-name>/
│   ├── README.md                # Writeup: approach, tools, solution
│   ├── binary/                  # Original challenge binary (where redistribution allowed)
│   └── images/                  # Disassembly / debugger screenshots
├── 02-<challenge-name>/
│   └── ...
├── keygens/                     # Standalone keygen scripts, where applicable
├── patches/                     # Binary patches / patched binaries
├── notes/                       # Cross-challenge technique notes (anti-debug, packers, etc.)
├── README.md                    # This file — master index
└── LICENSE
```

---

## `~$ cat methodology.md`

- **Triage** — Identify file type, architecture, packer/protector presence, and language/runtime (native, .NET, Java) before opening a disassembler
- **Static Analysis** — Disassemble/decompile in Ghidra or IDA, trace string references and imports, map out validation logic without executing the binary
- **Dynamic Analysis** — Step through execution in x64dbg/GDB, set breakpoints on comparison/validation routines, inspect registers and memory at the decision point
- **Unpacking** — Identify and unpack common packers (UPX and custom) when static analysis is obstructed
- **Solving** — Produce either a keygen (full algorithm reversal), a binary patch (jump/flag flip), or a documented bypass, depending on what the challenge calls for
- **Documentation** — Every solve is written up with the reasoning trail, not just the final key — tool output, key decision points, and screenshots included

---

## `~$ cat tools.md`

| Tool | Purpose |
|---|---|
| **Ghidra** | Static disassembly and decompilation (primary, free) |
| **IDA Free / IDA Pro** | Static disassembly, cross-referencing |
| **x64dbg / x32dbg** | Dynamic analysis and debugging on Windows targets |
| **GDB + GEF/pwndbg** | Dynamic analysis and debugging on Linux/ELF targets |
| **dnSpy / ILSpy** | Decompilation and patching of .NET binaries |
| **Cutter (Radare2)** | Cross-platform static/dynamic analysis, quick triage |
| **UPX / Detect It Easy (DiE)** | Packer identification and unpacking |
| **HxD / 010 Editor** | Hex editing for binary patching |

---

## `~$ contact --info`

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](#)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/vetementsvmnts)

---

<div align="center">

*All challenges in this repository are sourced from crackmes.one and solved strictly for educational and
skill-building purposes. No copyrighted commercial software or unauthorized targets were reverse engineered.*

</div>
