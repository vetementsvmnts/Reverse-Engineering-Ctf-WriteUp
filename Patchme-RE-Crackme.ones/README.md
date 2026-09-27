<div align="center">

```
 ██████╗ ███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ 
██╔════╝ ██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ 
██║  ███╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗
██║   ██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║
╚██████╔╝███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝
 ╚═════╝ ╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
        S T A R T E D   —   P A T C H M E
```

**Static and dynamic analysis writeup for a beginner patch-the-binary crackme sourced from crackmes.one**

[![Ghidra](https://img.shields.io/badge/Ghidra-1A1A1A?style=for-the-badge&logo=ghidra&logoColor=00FF41)](https://ghidra-sre.org/)
[![Linux ELF](https://img.shields.io/badge/Linux%20x64%20ELF-2E7D32?style=for-the-badge&logoColor=white)](#)
[![crackmes.one](https://img.shields.io/badge/crackmes.one-181717?style=for-the-badge&logoColor=00FF41)](https://crackmes.one/)
[![Difficulty: Beginner](https://img.shields.io/badge/Difficulty-Beginner-00FF41?style=for-the-badge)](#)

</div>

---

## `~$ cat challenge-info.md`

| Field | Value |
|---|---|
| **Name** | `getting_started_patchme` |
| **Source** | crackmes.one |
| **Platform** | Linux x64, ELF |
| **Language / Runtime** | C++ (`std::cin` / `std::cout` present, stack canary enabled) |
| **Objective** | Patch the binary so it always reports success (`Good job patcher! :3`), regardless of the validation routine's verdict on the input |
| **Tooling used** | Ghidra (static analysis + patch), Kali terminal (dynamic verification) |

---

## `~$ cat abstract.md`

`getting_started_patchme` is an entry-level "patch-me" style crackme: the binary reads an integer
from `stdin`, runs it through a validation routine, and only prints the success banner if that
routine is satisfied. Rather than reverse the exact validation algorithm to find a "correct" key,
the goal of a patchme challenge is to alter the binary's control flow directly so the success path
is always taken — a classic warm-up in conditional-jump patching.

---

## `~$ cat static-analysis.md`

Loaded the binary into Ghidra (`CodeBrowser: re/getting_started_patchme`) and let auto-analysis run.

The entry logic decompiles to (post-patch shown here):

```c
undefined8 FUN_00101120(void)
{
  ostream *poVar1;
  long in_FS_OFFSET;
  int local_14;
  long local_10;

  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  std::istream::operator>>((istream *)std::cin, &local_14);
  FUN_00101320(local_14);
  poVar1 = std::operator<<((ostream *)std::cout, "Good job patcher! :3");
  FUN_001012a0(poVar1);
  if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
    return 0;
  }
  __stack_chk_fail();
}
```

Key observations from the Listing view:

- **`FUN_00101320(local_14)`** — the validation routine. It receives the user's input and is
  responsible for deciding pass/fail.
- **`LAB_00101188`** (the success block: `LEA RSI, [DATA]` → `cout <<` → success string) is only
  reached via a jump from **`0x00101154`**, immediately after the call into the validation routine.
  That jump is the actual gate the challenge hinges on — originally a conditional branch (`JE`/`JNZ`)
  testing the validation routine's result, deciding whether execution fell through to a failure path
  or jumped into the success block at `LAB_00101188`.
- The `JNZ` visible at `0x0010117f` → `LAB_001011a5` is unrelated to the challenge logic — it's the
  standard stack-canary check (`__stack_chk_fail`), not the validation gate.

Used **Search → Go To** (`0x00101188`) to jump straight to the success label once it was identified
from the cross-reference (`XREF[1]: 00101154(j)`), confirming exactly which instruction controls
entry into the success branch.

---

## `~$ cat the-patch.md`

With the gating jump at `0x00101154` identified, the fix is a one-instruction patch: flip the
conditional jump that depended on `FUN_00101320`'s return value into an **unconditional jump**
(`JMP`) straight into `LAB_00101188`. This forces the success block to execute no matter what the
validation routine returns — the input value itself becomes irrelevant.

Patched directly in Ghidra's Listing view (Patch Instruction), then exported the modified binary
as `patched_patchme`.

---

## `~$ cat dynamic-verification.md`

```
┌──(vetementsvmnts㉿kali)-[~]
└─$ cd ~/Downloads

┌──(vetementsvmnts㉿kali)-[~/Downloads]
└─$ chmod +x patched_patchme

┌──(vetementsvmnts㉿kali)-[~/Downloads]
└─$ ./patched_patchme
45
Good job patcher! :3

┌──(vetementsvmnts㉿kali)-[~/Downloads]
└─$ 
```

Ran the patched binary and supplied an arbitrary value (`45`) at the prompt. The success banner
printed unconditionally, confirming the patch bypasses validation entirely rather than merely
guessing a correct input.

---

## `~$ cat takeaways.md`

- Confirming *which* jump gates the success path (via XREFs) before patching anything is what
  turns this from guesswork into a targeted, one-instruction fix.
- Distinguishing challenge logic from compiler-inserted scaffolding (stack canary checks) early
  avoids wasting time patching the wrong branch.
- A patchme doesn't require fully reversing the validation algorithm — only understanding enough
  of the control flow to redirect it.

---

## `~$ ls screenshots/`

- `Ghidra-Analysis.png` — decompiled `FUN_00101120` and disassembly around the success branch
- `Path-Direction.png` — Go To dialog confirming the success label address
- `Program-Execution.png` — patched binary run, forcing success on arbitrary input

---

<div align="center">

*Solved strictly for educational and skill-building purposes as part of ongoing reverse-engineering
practice. Binary sourced from crackmes.one — no copyrighted commercial software or unauthorized
targets were reverse engineered.*

</div>
