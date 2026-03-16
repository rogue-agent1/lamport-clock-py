#!/usr/bin/env python3
"""Lamport and vector clocks for distributed ordering."""
class LamportClock:
    def __init__(self):self.time=0
    def tick(self):self.time+=1;return self.time
    def send(self):self.time+=1;return self.time
    def receive(self,ts):self.time=max(self.time,ts)+1;return self.time
class VectorClock:
    def __init__(self,n,id):self.n=n;self.id=id;self.clock=[0]*n
    def tick(self):self.clock[self.id]+=1;return list(self.clock)
    def send(self):self.clock[self.id]+=1;return list(self.clock)
    def receive(self,other):
        self.clock=[max(self.clock[i],other[i]) for i in range(self.n)]
        self.clock[self.id]+=1;return list(self.clock)
    def happens_before(self,other):
        return all(self.clock[i]<=other[i] for i in range(self.n)) and self.clock!=other
def main():
    a=LamportClock();b=LamportClock()
    t1=a.send();print(f"A sends at {t1}")
    t2=b.receive(t1);print(f"B receives at {t2}")
if __name__=="__main__":main()
