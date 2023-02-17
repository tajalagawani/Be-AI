


#Python Script 
import os

def main():
    #create root directory
    root_directory = os.mkdir("root_directory")
    
    #create main.py file
    open("main.py","w")
   
    #create config.py file
    open("config.py","w")
    
    #create request.txt file
    open("request.txt","w")
    
    #create app directory
    app_directory = os.mkdir("app")
    os.chdir("app")
    
    #create __init__.py file
    open("__init__.py","w")
    
    #create views directory
    views_directoy = os.mkdir("views")
    os.chdir("views")
    
    #Create _init_.py file
    open("__init__.py","w")
    
    #Create home.py, profile.py and post.py file
    open("home.py","w")
    open("profile.py","w")
    open("post.py","w")
    
    #Navigate one up
    os.chdir("..")
    
    #Create template and static directories 
    os.mkdir("templates")
    os.mkdir("static")
    
    #Create models and utils directories 
    os.mkdir("models")
    os.mkdir("utils")
    
    #Navigate one up 
    os.chdir("..")
    
    #Create db directory 
    os.mkdir("db")
    
if __name__ == "__main__": 
    main()

    print("Project Structure created successfully!")