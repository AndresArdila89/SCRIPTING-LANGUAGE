"""
    Binary files in Python 

"""
with open("./test.jpg","rb") as rfb:
    with open("./cp_test.jpg","wb") as wfb:
        chunk = 4096
        rf_content = rfb.read(chunk)
        while len(rf_content) > 0:
            wfb.write(rf_content)
            rf_content = rfb.read(chunk)



            