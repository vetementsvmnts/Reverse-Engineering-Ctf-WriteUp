#!/usr/bin/env python3
import sys

def fnv1a(data: bytes) -> int:
    h = 0x811c9dc5
    for c in data:
        h ^= c
        h = (h * 0x1000193) & 0xffffffff
    return h

def keygen(name: str) -> str:
    name = name.rstrip('\n')
    if len(name) < 4:
        raise ValueError("Name must be at least 4 characters long")
    h = fnv1a(name.encode())
    H = h  # not traced
    part1 = (H ^ 0x5947494c) & 0xffffffff
    part2 = ((H >> 16) ^ (H & 0xffff)) & 0xffff
    part3 = (part1 ^ part2 ^ 0x535947) & 0xffffffff
    return "syg-%08x-%04x-%08x" % (part1, part2, part3)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = input("Enter name: ")
    print(keygen(name))
