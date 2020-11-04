"""
    Read files in python
"""

with open("./example.txt","r") as f_read:
    # f_content = f_read.read()
    # print(f_content)

    # lines = f_read.readlines()
    # #print(lines)
    # for line in lines:
    #     print(line,end='\n')
    # print(f_read.tell())
    # f_read.seek(0)
    # print("+++++++++++++++++")
    # f_content = f_read.read()
    # print(f_content)

    myChunk = f_read.read(100)
    while len(myChunk) > 0:
        print(myChunk)
        print()