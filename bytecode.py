import dis
import time

def writing(task, delay):
    for item in task:
        print("Writing:", item)
        time.sleep(delay)

def reading(task, delay):
    for item in task:
        print("Reading:", item)
        time.sleep(delay)

task = "3task"
delays = 0.5

writing(task, delays)
reading(task, delays)

dis.dis(writing)
dis.dis(reading)

print("Writing instructions:", len(list(dis.get_instructions(writing))), "variable lookups:", sum(1 for i in dis.get_instructions(writing) if "LOAD" in i.opname))
print("Reading instructions:", len(list(dis.get_instructions(reading))), "variable lookups:", sum(1 for i in dis.get_instructions(reading) if "LOAD" in i.opname))

total_instructions = len(list(dis.get_instructions(writing))) + len(list(dis.get_instructions(reading)))
total_lookups = sum(1 for i in dis.get_instructions(writing) if "LOAD" in i.opname) + sum(1 for i in dis.get_instructions(reading) if "LOAD" in i.opname)
print("Total instructions:", total_instructions, "total variable lookups:", total_lookups)