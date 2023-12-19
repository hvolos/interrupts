#!/usr/bin/env python3

import sys

def aggregate_interrupts(file_path="/proc/interrupts"):
    interrupts_data = []
    ncores = 0

    with open(file_path, "r") as file:
        for line in file:
            if line.strip().startswith("CPU"):
                fields = line.strip().split()
                ncores = len(fields)
                # Skip the header line
                continue

            # Split the line into fields
            fields = line.strip().split()

            if not fields:
                # Skip empty lines
                continue

            interrupt_number = fields[0]
            interrupts = [int(value) for value in fields[1:ncores+1]]
            interrupt_desc = fields[ncores+1:]

            interrupts_data.append([interrupt_number, interrupts, interrupt_desc])

    return interrupts_data

def diff_interrupts(interrupts_data1, interrupts_data2):
    for (a,b) in zip(interrupts_data1, interrupts_data2):
        diff = []
        for (val1, val2) in zip(a[1], b[1]):
            diff.append(val2 - val1)
        print(a[0], diff, ' '.join(a[2]))


def print_interrupts(interrupts_data):
    print("Interrupt\tInterrupts")
    for interrupt, interrupts in interrupts_data.items():
        print(f"{interrupt}\t{interrupts}")

if __name__ == "__main__":
    interrupts_data1 = aggregate_interrupts(sys.argv[1])
    interrupts_data2 = aggregate_interrupts(sys.argv[2])
    diff_interrupts(interrupts_data1, interrupts_data2)
