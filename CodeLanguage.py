import random
import string

def Encode(letters):
    encode=input("Say something to encode:")
    print("Message:",encode)
    encoded=encode.split()
    print("Encoded Message:", end=" ")
    for i in encoded:
        for j in i:
            letters+=1
        if letters<=3:
            print(i[::-1],end=" ")
        else:
            startletters=random.sample(string.ascii_letters,3)
            endletters=random.sample(string.ascii_letters,3)
            encode_trick=i[1:]+i[:1] 
            final_encoded=startletters[:]+list(encode_trick)+endletters[:]
            print("".join(final_encoded), end=" ")
        letters=0
    print("\nDo you want to encode another message?")
    decode_choice=input("yes/no:")
    if decode_choice=="yes":
        Encode(letters=0)
    elif decode_choice=="no":
        print("Goodbye!")
    else:
        print("Invalid choice!")

def Decode(letters):
    decode=input("Say something to decode:")
    print("Message:",decode)
    decoded=decode.split()
    print("Decoded Message:", end=" ")
    for i in decoded:
        for j in i:
            letters+=1
        if letters<=3:
            print(i[::-1],end=" ")
        else:
            filter=i[3:len(i)-3]
            print("",filter[len(filter)-1]+filter[:len(filter)-1],end="")
        letters=0
    print("\nDo you want to decode another message?")
    decode_choice=input("yes/no:")
    if decode_choice=="yes":
        Decode(letters=0)
    elif decode_choice=="no":
        print("Goodbye!")
    else:
        print("Invalid choice!")

def main():
    Title="WELCOME TO SECRET LANGUAGE CODER AND DECODER"
    print(Title.center(120))
    print("Do you want to encode or decode?\n1. Encode\n2. Decode")
    choice =int(input("Enter your choice: "))

    if choice==1:
        Encode(letters=0)
    elif choice==2:    
        Decode(letters=0)
    else:
        print("Invalid choice")
        main()
main()
