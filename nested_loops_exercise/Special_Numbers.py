# my prototype
# number = int(input())
# concatenation =
#
# for special_number in range(1111, 10000):
#     parsing_to_str = str(special_number) # parsing the number to str data type
#     for string_number in parsing_to_str:
#         str_to_int = int(string_number) # parsing again each element from string to integer
#         if str_to_int == 0:
#             break
#         elif number % str_to_int == 0:
#             concatenation =


number = int(input())
magic_number = False

for special_number in range(1111, 10000):
    parsing_to_str = str(special_number)
    for string_number in parsing_to_str:
        if int(string_number) == 0:
            #magic_number = False
            break
        elif number % int(string_number) == 0:
            magic_number = True
        else:
            magic_number = False
            break

    if magic_number:
        print(special_number, end=" ")

# important - How the second for loop concatenate all even divisible digits? He not concatenate them! The if-else
# statements are checking first if the digit is zero it break the execution of the code. Is useless because on zero
# cannot be divide nothing. So automatically break and turn back to iterate another number. But if the digit is even
# divisible on zero, it means that this digit is a magic digit. And in this way checking digit by digit if each digit
# is even divisible till the last one included, it means that you check all digits one by one, that they are even
# divisible. When one by one each digit has a True value and also the value of the last digit is True, it means that
# all the number(all digits) are True, so the number is magic. So it means that all this number is magic. At the end
# you ask, if the variable magic_number is True print me the current number. The code do not concatenate the digits
# or collect them each by each to print them together at the end. No. The loop simple is checking if each digit is
# even divisible or not. If all=yes so print the current number, if even one no so do not print this number.
# Practically the loop is checking digit by digit is the number magic or not. We can explain it with percentage
# example. 4 digit = 100%, so each digit is 25%. On each iteration we are covering 25% from the number. So on some
# iteration if the value of the digit is not even divisible on the number it means that this digit is not covering
# his 25% from the job, so automatically all process stop because is useless to check the rest of the digits if one
# of them cannot cover his own 25%.

# Този код с флагови променливи учи как да изградиш крайния резултат без да използваш аритметика. Събиране, изваждане и т.н.
# Само с флагови променливи като превключватели събираш резултата и го изграждаш напълно.

# Is printing all number in consequence because after one time the flag variable is switched to True, the value remain True.
# And after this digit if come a digit not even divisible on zero the code automatically go on the bottom and execute the last two line.
# The first line contain condition if magic_number is true print the number. And is true because the previous digit was even divisible and set up the value of hte magic_number on True.
# Because there is no alternative to say stop do not execute and print this number. That`s why is the last case else, to switch the value of magic_number
# on False and doing that stop the printing of the current number. Try with number 1117 and see what`s happen.

# Find out why eliminating line 22 the code is not working correctly.


