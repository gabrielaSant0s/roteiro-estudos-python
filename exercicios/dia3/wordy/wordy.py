def answer(question):

    replace_question = question.replace('?','')
    split_question = replace_question.split()
    result = 0

    postfix(split_question)
    duplicated_operation(split_question)
    no_operators(split_question)
    two_numbers(split_question)
    
    for (index,item) in enumerate(split_question):
        if item == 'divided':
            if result != 0:
                result /= int(split_question[index+2])
            else:
                try:
                    result = int(split_question[index-1]) / int(split_question[index+2])
                except ValueError:
                    raise ValueError("syntax error")

        elif item == 'multiplied':
            if result != 0:
                result *= int(split_question[index+2])
            else:
                try:
                    result = int(split_question[index-1]) * int(split_question[index+2])
                except ValueError:
                    raise ValueError("syntax error")

        elif item == 'minus':
            if result != 0:
                result -= int(split_question[index+1])
            else:
                try:
                    result = int(split_question[index-1]) - int(split_question[index+1])
                except ValueError:
                    raise ValueError("syntax error")

        elif item == 'plus':
            if result != 0:
                result += int(split_question[index+1])
            else:
                try:
                    result = int(split_question[index-1]) + int(split_question[index+1])
                except ValueError:
                    raise ValueError("syntax error")
        
        elif item == 'raised':
            split_raised = split_question[index+3]
            if result != 0:
                result **= int(split_raised[0])
            else:
                try:
                    result = int(split_question[index-1]) ** int(split_raised[0])
                except ValueError:
                    raise ValueError("syntax error")
    try:
        if 'What' in split_question and result == 0:
            number = int(replace_question[-1])
            return number
    except ValueError:
        raise ValueError("unknown operation")

    else:
        no_math(split_question)
        return result
    

def duplicated_operation(question_list):
    operations = ['divided', 'multiplied', 'minus', 'plus', 'raised']
    for (index,item) in enumerate(question_list):
        if (item in operations) and (question_list[index+1] in operations):
            raise ValueError("syntax error")

def no_operators(question_list):
     if len(question_list)< 3:
        raise ValueError("syntax error") 

def no_math(question_list):
    operations = ['divided', 'multiplied', 'minus', 'plus', 'raised']
    cont = 0
    for item in question_list:
        if item in operations:
            cont +=1
    if (question_list[3] not in operations) and (len(question_list)==6):
        raise ValueError("syntax error")
    elif cont==0:
        raise ValueError("unknown operation")

def postfix(question_list):
    operations = ['divided', 'multiplied', 'minus', 'plus', 'raised']
    if question_list[-1] in operations:
        raise ValueError("syntax error")
    
def two_numbers(question_list):
    if question_list[-1].isnumeric() and question_list[-2].isnumeric():
        raise ValueError("syntax error")
    









