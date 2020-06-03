import random
#---------------generated password variable--------------------------
generatedPassword = ''

def toGenerate(len_of_pass,state):
    #---------Variable initialization----------------
    pass_len = len_of_pass
    pass_state = state
    medium_secure = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    strong_secure = "!@#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    password = ''

    #------------------password generating----------------------
    #------------------ for Medium secure-----------------------
    if pass_state == 0:
        for _ in range(0,pass_len):
            password = password + random.choice(medium_secure)
        return password
    #------------------ for Strong secure--------------------------------
    else:
         for _ in range(0,pass_len):
            password = password + random.choice(strong_secure)
    return password

len_of_password = int(input("Length of the password : "))
state_of_password = int(input("Password for Medium_secure 0 Strong_secure 1 : "))

#------------function takes 2 arguments one is length another is password state-------------
generatedPassword = toGenerate(len_of_password,state_of_password)
#------------password prints on the console-----------------------------------------------
print(generatedPassword)