import csv
from pickle import TRUE

def main():
    sentence = input("Enter a sentence with abbreviations (no punctuations):\n> ")
    list1 = sentence.split()

    try:
        with open('file.csv', 'r') as file:
            reader = csv.reader(file)
            list2 = []
            list3 = []
            for row in reader:
                list2.append(row[0])
                list3.append(row[1])

            replaceAbr(list1,list2,list3)

            finalPrint(list1)

    except FileNotFoundError:
        print("File not found. Please check the file path.")

def replaceAbr(list1,list2,list3):
    for i in range(len(list1)):
            if list1[i].upper() in list2:
                index = list2.index(list1[i].upper())
                list1[i] = list3[index]
    return list1

def finalPrint(list1):
    final_sentence = " ".join(list1)
    print("So, your message is: \n> "+final_sentence)

print("Welcome to this program!")
runLoop=True
while runLoop:
    i=input("Do you wanna write a message? 1. Yes 2. No\nAns: ")
    if i=='1':
        main()
    elif i=='2':
        runLoop=False
        print("Thanks for using this program!")
    else:
        print("Wrong input!")
