import os 

def create_file(filename):             # file create function
    try:
        with open(filename,'x') as f :
            print(f"File Name {filename} : Created successfully!!" )
    except FileExistsError:            # file exists
        print(f'File Name {filename} already exists!')    
        
    except Exception as E:              # files 
        print('An error occurred !')
        
def view_all_files():            # view all files function
    files = os.listdir()
    if not files:
        print('No file found')
    else:
        print('Files in directory!')
        for file in files:            # loop through all files
            print(file)   
        
def delete_file(filename):          # delete file function
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully!')     
    except FileNotFoundError:
        print('File not found')  
        
    except Exception as E:
        print('An error occurred !')
        
def read_file(filename):              # read file function
    try: 
        with open('sample.txt','r') as f:
            content = f.read()
            print(f"content of '{filename}' :\n{content}")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")   
                      
    except Exception as e:   
        print('An error occurred !')
    
def edit_file(filename):               # edit file function            
    try:
        with open('sample.txt','a') as f:
            content = input('Enter data to add = ')   
            f.write(content + "\n")
            print('content added to {filename} Successfully!')
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")   
                      
    except Exception as e:   
        print('An error occurred !')        
            
def main():
    while True:
        print("FILE MANAGEMENT APP")  
        print('1:Create file')
        print('2:View all files')  
        print('3:Delete file')
        print('4:read file')
        print('5:edit file')
        print('6:Exit')
        
        choice = input('Enter your choice(1-6) = ')
        if choice == '1':
            filename = input('Enter the file-name to create = ')
            create_file(filename)
            
             
        elif choice == '2':
            view_all_files()
            
        elif choice == '3':
            filename = input("Enter the name of file you want yo delete :")
            delete_file(filename) 
            
        elif choice == '4':
            filename = input("enter file name to read = ")
            read_file(filename) 
               
        elif choice == '5':
            filename = input("Enter the name to edit")
            edit_file(filename)         
            
        elif choice == '6':
           print("Closing th qpp.....")
           break
        else:
            print("In-valid syntax")
            
if __name__ == '__main__':
        main()
                
                        
                  
     
                    
                
              
                      
                             