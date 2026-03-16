#!/usr/bin/env python3
"""Lamport logical clocks."""
import sys

class LamportClock:
    def __init__(self, pid): self.pid = pid; self.time = 0
    def tick(self): self.time += 1; return self.time
    def send(self): self.tick(); return self.time
    def receive(self, ts): self.time = max(self.time, ts) + 1; return self.time
    def __repr__(self): return f"Clock({self.pid}, t={self.time})"

if __name__ == "__main__":
    a, b, c = LamportClock("A"), LamportClock("B"), LamportClock("C")
    t1 = a.send(); print(f"A sends at {t1}")
    t2 = b.receive(t1); print(f"B receives at {t2}")
    t3 = b.send(); print(f"B sends at {t3}")
    t4 = c.receive(t3); print(f"C receives at {t4}")
    a.tick(); a.tick(); print(f"A local: {a}")
    print(f"Final: {a}, {b}, {c}")
