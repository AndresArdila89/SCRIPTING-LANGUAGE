"""
    File Write in Python 

"""

with open("./example_1.txt", "r") as rf:
    with open("./cp_example_1.txt","w") as wf:
        for line in rf:
            wf.write(line)

with open("./cp_example_1.txt", "a") as af:
    af.write("\nThisis the EOF")