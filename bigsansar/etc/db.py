import subprocess
import psycopg2

def connectposgres(database_name, username, password):

    con = psycopg2.connect(
    database="%s"  % (database_name) ,
    user="%s" % (username) ,
    password="%s" % (password) ,
    host="localhost",
    port= ""
    )

    cursor_obj = con.cursor()
    print(cursor_obj)

    if cursor_obj:
         # Open a file with access mode 'a'
            with open("www/settings.py", "a") as append_posgre:
                # Append 'postgres' at the end of file
                append_posgre.write(""
                                    "\n"
                                    "\n"
                                "DATABASES = {"
                                "\n"
                                "     'default': {"
                                "\n"
                                "         'ENGINE': 'django.db.backends.postgresql',"
                                "\n"
                                "         'NAME': '%s'," 
                                "\n"
                                "         'USER': '%s'," 
                                "\n"
                                "         'PASSWORD': '%s',"
                                "\n"
                                "         'HOST': 'localhost',"
                                "\n"
                                "         'PORT': '',"
                                "\n"
                                "     }"
                                 "\n"
                                  "}" % (database_name, username, password)
                                )
                                
                # Close the file
                append_posgre.close()

            print('postgresql: connection to server at "localhost" (127.0.0.1) successfully')
    else:
        print('connection to server at "localhost" (127.0.0.1) failed')

def execute_command(command, database_name=None, username=None, password=None):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Error: {error.decode('utf-8')}")
    else:
        print(output.decode('utf-8'))

        if database_name == None and username == None and password == None:
            pass
        else:

            # Open a file with access mode 'a'
            with open("www/settings.py", "a") as append_posgre:
                # Append 'postgres' at the end of file
                append_posgre.write(""
                                    "\n"
                                    "\n"
                                "DATABASES = {"
                                "\n"
                                "     'default': {"
                                "\n"
                                "         'ENGINE': 'django.db.backends.postgresql',"
                                "\n"
                                "         'NAME': '%s'," 
                                "\n"
                                "         'USER': '%s'," 
                                "\n"
                                "         'PASSWORD': '%s',"
                                "\n"
                                "         'HOST': 'localhost',"
                                "\n"
                                "         'PORT': '',"
                                "\n"
                                "     }"
                                 "\n"
                                  "}" % (database_name, username, password)
                                )
                                
                # Close the file
                append_posgre.close()


def create_database_and_user(database_name, username, password):

    
    create_db_command = f"sudo -u postgres psql -c 'CREATE DATABASE {database_name};'"
    create_user_command = f"sudo -u postgres psql -c \"CREATE USER {username} WITH PASSWORD '{password}';\""
    #alter_uff = f"sudo -u postgres psql -c \"ALTER ROLE {username} SET client_encoding TO 'utf8';\""
    grant_privileges_command = f"sudo -u postgres psql -c 'GRANT ALL PRIVILEGES ON DATABASE {database_name} TO {username};'"

    execute_command(create_db_command)
    execute_command(create_user_command)
    execute_command(grant_privileges_command, database_name, username, password)


print(' we are configuring postgresql for you ......................')

user_input = input('Do you have a already postgresql account (yes/no): ')

if user_input.lower() == 'yes':

    # Replace these with your desired values
    database_name = input("Enter the database name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    connectposgres(database_name, username, password)

elif user_input.lower() == 'no':
    # Replace these with your desired values
    database_name = input("Enter the database name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    create_database_and_user(database_name, username, password)

else:
    exit()
