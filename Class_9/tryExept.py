try: 
    f = open("example.txt","r")
    name = file_name
except FileNotFoundError as e:
    print("Error: file name does not exist")
except Exception as e:
    print("Error: General error!!! ")
