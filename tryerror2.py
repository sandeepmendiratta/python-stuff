def ask():

    while True:
        try:
            a = int(input("Please enter an intger"))


        except:
            print("Some error happened")
            continue

        else:
            break

        finally:
            print("here")
    b = a **2
    print(b)
#         finally:
#             print("i always run")
ask()
