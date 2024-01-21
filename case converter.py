#Tutorial version of a program that take aLongAndComplexString and converts it to snake case
def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

    

if __name__ == '__main__':
    main()

#Now, without tutorial, let's modify it to covert from snake case to camelCase
def convert_to_camel_case(pascal_or_snake_cased_string):

    camel_cased_char_list = [
        char.lower() if char.isupper()
        else char 
        for char in pascal_or_snake_cased_string
    ]