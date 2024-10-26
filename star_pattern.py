user_input=int(input("please enter a number :"))
output=0
spacing=0
# Loop through numbers up to the user's number
for i in range(user_input*2 -1):
    if i<user_input:
        if i==0:
            spacing=user_input-1
            print(" "*spacing,"*")
            output=1
        else:
                output+=2
                spacing-=1
                print(" "*spacing ,"*"*output)
                
    else:
            output-=2
            spacing+=1
            print(" "*spacing,"*"*output)