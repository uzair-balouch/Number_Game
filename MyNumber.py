
import FriendNumber
import time

def HelloMax():
    print('Hello Max! How are you.?')
    time.sleep(4)
    FriendNumber.MFine()

def Nothing():
    time.sleep(4)
    print('Nothing Max, You know its a very long and bore day...')
    time.sleep(4)
    FriendNumber.SameHere()
def Wanna_Play():
    time.sleep(4)
    print('Hey Max, You wanna play a number game.. ?')
    time.sleep(4)
    FriendNumber.YeahSure()

def StarTheGame():
    result1 = int(input(('Ok Max you have to write a number between 1000-9999.. OK.. '
                     'Lets star,. Common write a number  ::  ')))
    while len(str(result1)) != 4:
        print('Not a 4 digit number')
        result1 = input(('Enter again a number between 1000-9999  ::  '))
    print(FriendNumber.OkIWillChoose(), result1 , end='\n')
    result2 = int(input('Ok Max now again choose another number between 1000-9999...  ::  '))
    while len(str(result2)) != 4:
         print('Not a 4 digit number')
         result2 = input(('Enter again a number between 1000-9999  ::  '))
    print(FriendNumber.AgainSecondNumber(), result2, end='\n')
    time.sleep(4)
    print('Ok Max now I am going to write a number on paper I will show you the number'
           'and I will fold the paper and never going to touch this paper for the rest of the game'
           'Ok,. Does this make sense to you..??')
    print(FriendNumber.Ok_Makes_Sense())

    My_Number_End_Result = '2'+str(result1-2)
    print('Ok I will write this number remember this number ..Remember this Number,, OK >>>>>>',My_Number_End_Result ,'<<<<<<')
    time.sleep(4)

    My_Second_Number =  ('Now again  I will enter a number  ::  ')
    result3 = 9999 - result2
    time.sleep(4)
    print('I am going to gain enter the number....and Here is my number',result3)

    result4 = int(input('Ok Now the Last time you need to enter a number between 1000-8999..On Your own Choice Whatever you like..  ::  '))
    while len(str(result4)) != 4:
        print('Not a 4 digit number')
        result4 = input(('Enter again a number between 1000-9999  ::  '))
    time.sleep(4)
    print('Ok Jimmy here is my last number  ::  ', result4)

    My_Third_and_Last_Number = ('Now again  I will enter a number which will be my last number  ::  ')
    result5 = (result2 + result3) - result4
    print('Here is my number', result5)


    print('And Now ITs for the Magic....Remember the number which I have Told to be remember BEFORE..Now LEt\'s SEE  :: ')
    a = result1 + result2 + result3 + result4 + result5
    print()
    print('\n>>>>>>>>>>>>>>>>>>>>>>>', a ,'<<<<<<<<<<   <<<<<<<<<<<<')


HelloMax()
Nothing()
Wanna_Play()

#Max (your friend's input starts from here)
StarTheGame()
