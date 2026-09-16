Sygil Binary Reverse Engineering & Keygen
This repository contains the analysis notes, binary reconnaissance artifacts, and custom Python key generator (keygen.py) developed to reverse engineer and generate valid sigils for the stripped ELF binary sygil.

Overview of the Process
The workflow followed a standard reverse engineering and cryptographic key derivation analysis methodology:

Reconnaissance & File Analysis (Screenshot 2026-09-16 192617.png):

Extracted the binary from the challenge archive (6aa9e8b1dbb3353b7539688c.zip).

Ran file to inspect binary characteristics, identifying it as a 64-bit LSB dynamically linked, stripped ELF executable (ELF 64-bit LSB pie executable, x86-64).

Ran strings to inspect embedded text fragments, revealing references to standard input/output functions, libc versions, and format indicators.

Disassembly & Behavioral Analysis (Screenshot 2026-09-16 192642.png):

Granted execution permissions using chmod +x and tested the binary execution, noting the initial behavior ("the ritual begins...", "the spirit rejects.").

Used objdump -d to disassemble the .text section of the binary and grepped for specific format strings and offset markers (such as 2023) to locate the core validation and formatting logic.

Key Derivation Implementation (Screenshot 2026-09-16 192709.png):

Developed a custom Python key generator (keygen.py) implementing an FNV-1a hashing function combined with custom bitwise operations and XOR transformations matching the binary's internal validation routine.

Implemented length checks ensuring input names are at least 4 characters long.

Verification & Execution (Screenshot 2026-09-16 192732.png):

Verified the assembly instructions against the script logic, ensuring the transformation offsets match the binary's expectations.

Executed the Python keygen with a test string (test) to produce a valid sigil format (syg-f69738a9-de35-f6c4bfdb), which successfully passed the ritual verification check upon runtime execution.

Usage
To generate a valid sigil for any given name (minimum 4 characters), run the Python key generator script:

Bash
python3 keygen.py <name>
Or run it interactively:

Bash
python3 keygen.py
