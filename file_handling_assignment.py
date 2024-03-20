try:

    with open("my_file.txt","w") as myfile:
        
        myfile.write("My Name is Jevinarlys, \nI love coding 24/7. \nNo code no life.")


    with open("my_file.txt","r") as myfile:
        
        content=myfile.read()
        print(content)

    with open("myfile.txt","a") as myfile:

        myfile.write("\nI am back again.\n It feels awesome to be here,\n I am not leaving any time soon")

except:

    if FileNotFoundError:

        print("The file is not available")
    else:
        print ("You don't have permission to perform that!!")
