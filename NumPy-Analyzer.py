import os
import numpy as np

def first():
    while True:
        print("\n Select the type of Array to create :-")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        print("4. Back to Main Menu")

        choice = int(input("\n ~ Select The Type of Array to Create :- "))

        match choice:

            case 1:
                print("\n 1D Array ----------")
                start=int(input("\n Enter the Starting Number :- "))
                end=int(input("\n Enter the Ending Number :- "))

                arr=list(range(start,end + 1 ))
                print("1D Array :- ", arr)

                index=int(input("\n Enter the Index of Element to Access :- "))
                print("\n Element at Index", index, "is :- ",arr[index])

                x=int(input("\n Enter the Starting value for slicing :- "))
                y=int(input("\n Enter the Ending value for slicing :- "))
                print("\n Scliced Array :- ", arr[x:y])

            case 2:
                print("\n 2D Array -------------")
                row=int(input("Enter the Number of Rows :- "))
                col=int(input("Enter the Number of Columns :-"))

                arr=np.array(list(map(int, input("\n Enter the Elements for 2D Array Saparated by Space :- ").split())))
                if len(arr) != row * col:
                    print("\n Error: Please enter exactly", row * col, "elements...")
                else:
                    arr=arr.reshape(row,col)
                    print("\n Array Created Successfully :- \n",arr)

                    print("\n1. Indexing ")
                    print("2. slicing ")
                    print("3. Go Back ")

                    choice=int(input("\n Enter Your Choice :- "))

                    if choice == 1:
                        r=int(input("\n Enter the Row Index :-"))
                        c=int(input("\n Enter the Column Index :-"))

                        print("\n Element :- ", arr[r, c])

                    elif choice == 2:
                        r_start=int(input("\n Enter the Row Starting Index :-"))
                        r_end=int(input("\n Enter the Row Ending Index :-"))

                        c_start=int(input("\n Enter the Column Starting Index :-"))
                        c_end=int(input("\n Enter the Column Ending Index :-"))

                        print("\n Scliced Array :- \n", arr[r_start:r_end, c_start:c_end])

                    elif choice == 3:
                        print("\n Go Back..")
                        break

                    else:
                        print("\n invalid Choice... Please try Again... Enter only Shown Options...")

            case 3:
                print("\n 3D Array ---------------")
                row=int(input("Enter The Number of Rows :- "))
                col=int(input("Enter The Number of Columns :- "))
                depth=int(input("Enter The Number of Depth :- "))

                arr=np.array(list(map(int, input("\n Enter the Elements for 3D Array Saprated by Space :- ").split())))
                if len(arr) != row * col * depth:
                    print("\n Error: Please enter Exactly", row*col*depth, "elements...")
                else:
                    arr=arr.reshape(row,col,depth)
                    print("\n Array Created Successfully :- \n",arr)

                    print("\n ---------- Operations on 3D Array -----------")
                    print("\n1. Indexing ---- ")
                    print("2. Slicing ----")
                    print("3. Go Back ----")

                    choice = int(input("\n Enter Your Choice :- "))

                    if choice == 1:
                        r=int(input("\n Enter the Row Index :- "))
                        c=int(input("\n Enter the Column Index :- "))
                        d=int(input("\n Enter the Depth Index :- "))

                        print("\n Value at Index =", arr[r, c, d])

                    elif choice == 2:
                        print("\n--- Slicing Options ---")
                        print("1. First Row Block")
                        print("2. All Rows First Column")
                        print("3. First Depth Values")
                        print("4. Reverse Rows")

                        s=int(input("\n Enter your Choice :- "))

                        if s == 1:
                            print(arr[0])

                        elif s == 2:
                            print(arr[:,0,:])

                        elif s == 3:
                            print(arr[:,:,0])

                        elif s == 4:
                            print(arr[::-1])

                        else:
                            print("Invalid Slicing Choice...")

                    else:
                        print("Invalid Choice...")

                    

            case 4:
                print("\n Back to Main Menu...")
                break
                        
            case _:
                print("\n Invalid Choice... Please try Again... Enter only Shown Options...")



def second():
    while True :
        print("\n Choose The Mathematical Opration :- ")
        print("1. Addition ")
        print("2. Subtraction ")
        print("3. Multiplication ")
        print("4. Dicision ")
        print("5. Go Back ")

        choice = int(input("\nEnter Your Choice :-"))

        match choice :

            case 1:
                print("\n Addition... ")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the number of Columns :- "))

                arr=np.array(list(map(int,input("\n Enter the Elements for Array A Saparated By Space :- ").split())))
                arr2=np.array(list(map(int,input(f"\n Enter the same size Array elements ({row * col} Elements) Saparated by Space :- ").split())))
                if len(arr) != row * col:
                    print("\n Error: Please Enter Exatcly",row * col, "Elements...")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array :- \n",arr)

                    
                    if len(arr2) != row * col:
                        print("\n Error: Please Enter Exactly", row * col, "Elememnts...")
                    else:
                        arr2=arr2.reshape(row,col)
                        print("\n Second Array :- \n",arr2)

                        print("\n Result Of Addition :- \n", arr + arr2)


            case 2:
                print("\n Subtraction... ")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the number of Columns :- "))
            
                arr=np.array(list(map(int,input("\n Enter the Elements for Array A Saparated By Space :- ").split())))
                arr2=np.array(list(map(int,input(f"\n Enter the same size Array elements ({row * col} Elements) Saparated by Space :- ").split())))
                if len(arr) != row * col:
                    print("\n Error: Please Enter Exatcly",row * col, "Elements...")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array :- \n",arr)
            
                                
                    if len(arr2) != row * col:
                        print("\n Error: Please Enter Exactly", row * col, "Elememnts...")
                    else:
                        arr2=arr2.reshape(row,col)
                        print("\n Second Array :- \n",arr2)
            
                        print("\n Result Of Subtraction :- \n", arr - arr2)



            case 3:
                print("\n Multiplication... ")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the number of Columns :- "))
                            
                arr=np.array(list(map(int,input("\n Enter the Elements for Array A Saparated By Space :- ").split())))
                arr2=np.array(list(map(int,input(f"\n Enter the same size Array elements ({row * col} Elements) Saparated by Space :- ").split())))
                if len(arr) != row * col:
                    print("\n Error: Please Enter Exatcly",row * col, "Elements...")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array :- \n",arr)
                            
                                                
                    if len(arr2) != row * col:
                        print("\n Error: Please Enter Exactly", row * col, "Elememnts...")
                    else:
                        arr2=arr2.reshape(row,col)
                        print("\n Second Array :- \n",arr2)
                            
                        print("\n Result Of Multiplication :- \n", arr * arr2)


            case 4:
                print("\n Division... ")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the number of Columns :- "))
                            
                arr=np.array(list(map(int,input("\n Enter the Elements for Array A Saparated By Space :- ").split())))
                arr2=np.array(list(map(int,input(f"\n Enter the same size Array elements ( ({row * col} Elements) Saparated by Space ) :- ").split())))
                if len(arr) != row * col:
                    print("\n Error: Please Enter Exatcly",row * col, "Elements...")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array :- \n",arr)
                            
                                                
                    if len(arr2) != row * col:
                        print("\n Error: Please Enter Exactly", row * col, "Elememnts...")
                    else:
                        arr2=arr2.reshape(row,col)
                        print("\n Second Array :- \n",arr2)
                            
                        print("\n Result Of Division :- \n", arr / arr2)
                



            case 5:
                print("\n Back to Main Menu...")
                break

            case _:
                print("\n invalid choice... Please try Again... Enter only Shown Options...")



def third():
    while True :
        print("\n Combine or Split Array ---------")
        print("\n Chose the operation :- ")
        print("1. Combine Array ")
        print("2. Split Array ")
        print("3. Go Back ")

        choice=int(input("Enter Your Choice :- "))

        match choice :

            case 1:
                print("\n Combine Array... ")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the Number of Columns :- "))

                arr=np.array(list(map(int,input("\n Enter the Elements for Array Saparated By Space :- ").split())))
                arr2=np.array(list(map(int,input(f"\n Enter the Elements of another array to combine ( ({row * col} Elements) Saparated By Space ) :- ").split())))

                if len(arr) != row * col :
                    print("\nError : Please Enter Exactly ", row * col , "elements...")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array :- \n ", arr)

                    arr2=arr2.reshape(row,col)
                    print("\n Second Array :- \n ", arr2)

                    print("\n Combined Array (Vertical Stack) :- \n", np.concatenate((arr,arr2), axis=0))


            case 2:
                print("\n Split Array...")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the Number of Columns :- "))
                
                arr=np.array(list(map(int,input("\n Enter the Elements for Array Saparated By Space :- ").split())))

                if len(arr) != row * col :
                    print("\n Error : Please Enter Exactly ", row * col , "elements...")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array : \n",arr)

                    split=int(input("\n Enter the Number of Splits :- "))
                    if split <=0 or split > row :
                        print("\n Error : Invalid Number of Splits... Please Enter a valid number between 1 and",row)
                    else :
                        split=np.array_split(arr,split)
                        print("\n Split Arrays :- ")

                        for i, s in enumerate(split):
                            print(f"\n Split Array {i+1} : \n", s)


            case 3:
                print("\n Back to Main Menu...")
                break

            case _:
                print("\nInvalid Choice... Please try Again... Enter only Shown Options...")


def fourth():
    while True :
        print("\n search, Sort, or Filter Array ---------")
        print("\n Choose the operation :- ")
        print("1. Search a Value :- ")
        print("2. Sort the Array :- ")
        print("3. Filter the Array :- ")
        print("4. Go Back :- ")

        choice = int(input("\n Enter Your Choice :- "))

        match choice :

            case 1:
                print("\n Search a Value... ")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the Number of Columns :- "))

                arr=np.array(list(map(int,input("\n Enter the Elements for Array Saparated By Space :- ").split())))
                if len(arr) != row * col :
                    print("\n Error : Please Enter Exactly ", row * col , "elements... ")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array : \n ",arr)

                    value=int(input("\n Enter the value to search in the array :- "))
                    result=np.where(arr==value)
                    print("\n Value found at Index :- ", result)

            case 2: 
                print("\n Sort the Array... ")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the Number of Columns :- "))

                arr=np.array(list(map(int,input("\n Enter the Elements for Array Sapatrated By Sapce :- ").split())))
                if len(arr) != row * col:
                    print("\n Error : Please Enter Exacctly ", row * col, "elements... ")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array : \n ",arr)

                    sorted_arr=np.sort(arr,axis=None)
                    print("\n Sorted Array : \n ", sorted_arr.reshape(row,col))
                    print("\n ( Sorting Apllied row-wise. )")


            case 3:
                print("\n Filter the Array... ")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the Number of Columns :- "))

                arr=np.array(list(map(int,input("\n Enter the Elements for Array Sapatrated By Sapce :- ").split())))
                if len(arr) != row * col:
                    print("\n Error : please Enter Exactly ", row * col, "elements... ")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array : \n ",arr)

                    condition=int(input("\n Enter the Condition for Filtering (5 for greater then 5 ) :- "))
                    filtered_arr=arr[arr>condition]
                    print("\n Filtered Array (values greater then ", condition, "):\n", filtered_arr)

            case 4:
                print("\n Back to Main Menu...")
                break

            case _:
                print("\n invalid choice... Please try Again... Enter only Shown Options...")



def fifth():
    while True :
        print("\n Compute Aggregates and Statistics ------------")
        print("\n Choose the aggregate/statistics operation :- ")
        print("1. Sum :- ")
        print("2. Mean :- ")
        print("3. Median :- ")
        print("4. Standard Deviation :- ")
        print("5. Variance :- ")
        print("6. Go Back :- ")


        choice = int(input("\n Enter Your Choice :- "))

        match choice :

            case 1:
                print("\n Sum... ")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the number of Columns :- "))

                arr=np.array(list(map(int,input("\n Enter the Elements for Array Saparated By Space :- ").split())))
                if len(arr) != row * col :
                    print("\n Error : Please Enter exactly ", row * col, " elemennts.. ")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array : \n",arr)

                    print("\n Sum of Array Elements :- ", np.sum(arr))


            case 2:
                print("\n Mean...")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the Number of Columns :- "))

                arr=np.array(list(map(int, input("\n Enter the Elements for Array Saparated By Space :- ").split())))
                if len(arr) != row * col :
                    print("\n Error : Please Enter Exactly ", row * col, " elements...")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array : \n",arr)

                    print("\n Mean of Array Elements :- ", np.mean(arr))


            case 3:
                print("\n Median...")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the Number of Columns :- "))

                arr=np.array(list(map(int, input("\n Enter the Elements for Array Saparated By Space :- ").split())))
                if len(arr) != row * col :
                    print("\n Error : Please Enter Exactly ", row * col, "elements....")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array : \n", arr)

                    print("\n Median of Array Elements :-", np.median(arr))


            case 4:
                print("\n Standard Deviation...")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the Number of Columns :- "))

                arr=np.array(list(map(int, input("\n Enter the Elements for Array Saparated By Sapce :- ").split())))
                if len(arr) != row * col :
                    print("\n Error : Please Enter Exactly ", row * col, "elements... ")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array : \n",arr)

                    print("\n Standard Deviation of Array Elements :- ",np.std(arr))


            case 5:
                print("\n Variance...")
                row=int(input("\n Enter the Number of Rows :- "))
                col=int(input("\n Enter the Number of Columns :- "))

                arr=np.array(list(map(int, input("\n Enter the Elements for Array Saparated by Space :- ").split())))
                if len(arr) != row * col :
                    print("\n Error : Please Enter Exactly ", row * col, " elements... ")
                else :
                    arr=arr.reshape(row,col)
                    print("\n Original Array : \n",arr)

                    print("\n Variance of Array Elements :- ", np.var(arr))


            case 6:
                print("\n Back to Main Menu... ")
                break

            case _:
                print("\n invalid choice... Please try Again... Enter only Shown Options... ")



def main():
    while True:
        print("\n======================================================================")
        print("\n Welcome to Numpy Analyzer..")
        print("\n======================================================================")

        print("1. Create a numpy Array :~")
        print("2. Perform Mathemetical Operation :~")
        print("3. Combine or split Array :~")
        print("4. Search, Sort, or Filter Array :~")
        print("5. Computer Aggregate and Statics :~")
        print("6. Exit :~")

        choice = int(input("Enter your choice :- "))

        match choice:
            case 1:
                first()
            case 2:
                second()
            case 3:
                third()
            case 4:
                fourth()
            case 5:
                fifth()
            case 6:
                print("\n Exit...")
                print("\n Thank you for using Numpy Analyzer ! GoodBye !.. ")
                break
            case _:
                print("\nInvalid Choice... Please try Again... ")

main()
