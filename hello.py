# Section one of variables. 
# Define the variables BOOK, AUTHOR, RELEASE YEAR AND RATING ON GOOD READS
# Each variable is defined individually and then it is printed individually. 

# def main():
#     book = 'Dracula'
#     author = 'Bram Stoker'
#     release_year = 1897
#     goodreads_rating = 4.01

#     print(book)
#     print(author)
#     print(release_year)
#     print(goodreads_rating)

#     if __name__ == '__main__':
#         main()

# Section two of variables.
# Define the variables BOOK, AUTHOR, RELEASE YEAR AND RATING ON GOOD READS
# Instead of defining each variable individually you can define them all at once using commas as the delimiter
# def main():
#     book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01

#     print(book, author, release_year, goodreads_rating)

# if __name__ == '__main__':
#     main()

#Section three of variables. This begins the use of strings. Pring can be done using strings so that python doesn't see the + in front of a variable
#and try to apply arithmtic.
# def main():
#     book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01

#     print(book + ' is a novel by ' + author + ', published in ' + str(release_year) + '. It has a rating of ' + str(goodreads_rating) + ' on goodreads.')

# if __name__ == '__main__':
#     main()

# Section four of variables introduces the f string. You add a f in front of a string and then you can call variables inside a curly bracket. 
# You can also split long lines of code by having two f strings indside of one set of ().
# def main():
#     book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01

#     print(f'{book} is a novel by {author}, published in {release_year}.'
#           f' It has a rating of {goodreads_rating} on good reads.')

# if __name__ == '__main__':
#     main()

#Python can represent integers in four different bases. You can use decimal, hex, octal, and binary. You differienate them with the prefixes below. 
#Use 0x(number) for hex
#Use 0o(number) for octal 
#Use 0b(number) for binary
#Floats can be represented with a precision of up to 15. Anything after 15 digits may not be accurate. 
def main():
    num_1 = 15
    num_2 = 12
    float_variable = 1.25
    integer_variable = 55

    print(f'sum of num_1 and num_2 is: {num_1 + num_2}')
    print(f'difference of num_1 and num_2 is:{num_1 - num_2}')
    print(f'product of num_1 and num_2 is: {num_1 * num_2}')
    print(f'quotient of num_1 and num_2 is: {num_1 / num_2}')
    print(f'floored quotient of num_1 and num_2 is: {num_1 // num_2}') #Floored quotient is when the quotient is rounded down to the nearest whole number. It is expressed with a '//' operator.
    print(f'remainder of num_1 / num_2 is: {num_1 % num_2}') #Remainders are done with modulus operation. 15/2=1 with a remainder of 3. The three is the result of the operation.
    print(f'{float_variable} converted to an integer is: {int(float_variable)}') #Changes a float to an int. Ex is 1.25 is changed to 1.
    print(f'{integer_variable} converted to a float is: {float(integer_variable)}') #Changes a int to a float. Ex is 55 is changed to 55.0. 
    #Careful here with the float and int conversions. There could be data loss if used incorrectly.


if __name__ == '__main__': #messed up here. I didn't have the indentation correct. The 'if' was indented with the print statement above. The output then didn't work.
        main()