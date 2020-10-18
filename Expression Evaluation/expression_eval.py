from stack_array import *
       
def postfix_eval(input_str):
    """ Evaluates a postfix expression
    Attributes:
      input_str (string): expression to be evaluated
    """
    input_str = input_str.split()
    stack_array = StackArray()
    postfix_eval_exceptions(input_str)
    for char in input_str:
        if char in "+-*/^":
            val_1 = stack_array.pop()
            val_2 = stack_array.pop()
            if char == "+":
                to_add = float(val_1) + float(val_2)
                stack_array.push(to_add)
            if char == "-":
                to_sub = float(val_2) - float(val_1)
                stack_array.push(to_sub)
            if char == "*":
                to_mult = float(val_1) * float(val_2)
                stack_array.push(to_mult)
            if char == "/":
                to_div = float(val_2) / float(val_1)
                stack_array.push(to_div)
            if char == "^":
                to_power = float(val_2)**float(val_1)
                stack_array.push(to_power)
        else:
            stack_array.push(char)
    return float(stack_array.arr[0])


class PostfixFormatException(Exception):
    """ Defines the postfix format exception
    """
    pass


def postfix_eval_exceptions(input_str):
    """ Helper function for the postfix format exception
    Attributes:
      input_str (string): expression to be evaluated by postfix_eval
    """
    num_operands = 0
    num_operators = 0
    for char in input_str:
        if char in "+-*/^":
            num_operators += 1
        else:
            num_operands += 1
        if char not in "+-*/^":
            try:
                float(char)
            except:
                raise PostfixFormatException("Invalid token")
    if num_operands - 1 < num_operators:
        raise PostfixFormatException("Insufficient operands")
    if num_operands - 1 > num_operators:
        raise PostfixFormatException("Too many operands")


def infix_to_postfix(infix_str):
    """ Converts an infix expression to a postfix expression
    Attributes:
      infix_str (string): infix expression to be converted
    """
    infix_str = infix_str.split()
    rpn_exp = ""
    stack_array = StackArray()
    for char in infix_str:
        if char == "(":
            stack_array.push(char)
        elif char == ")":
            while stack_array.peek() != "(":
                opr_to_append = stack_array.pop()
                rpn_exp = rpn_exp + " " + opr_to_append
            stack_array.pop()
        elif char in "+-*^/":
            if stack_array.is_empty() == False:
                if stack_array.peek() in "+-*^/(":
                    if char == "^":
                        stack_array.push(char)
                    if char in "*/" and stack_array.peek() in "*/":
                        opr_to_append = stack_array.pop()
                        rpn_exp = rpn_exp + " " + opr_to_append
                        stack_array.push(char)
                    if char in "+-" and stack_array.peek() in "+-":
                        opr_to_append = stack_array.pop()
                        rpn_exp = rpn_exp + " " + opr_to_append
                        stack_array.push(char)
                    if char in "+-" and stack_array.peek() in "*/^":
                        opr_to_append = stack_array.pop()
                        rpn_exp = rpn_exp + " " + opr_to_append
                        stack_array.push(char)
                    if char in "*/" and stack_array.peek() in "+-":
                        stack_array.push(char)
                    if stack_array.peek() == "(":
                        stack_array.push(char)                   
            else:
                stack_array.push(char)
        else:
            if len(rpn_exp) == 0:
                rpn_exp = rpn_exp + char
            else:
                rpn_exp = rpn_exp + " " + char
    while stack_array.is_empty() == False:
        rpn_exp = rpn_exp + " " + stack_array.pop()
    return rpn_exp


def prefix_to_postfix(input_str):
    """ Converts an prefix expression to a postfix expression
    Attributes:
      input_str (string): prefix expression to be converted
    """
    input_str = input_str.split()
    input_str = input_str[::-1] 
    rpn_exp = ""
    stack_array = StackArray()
    for char in input_str:
        if char in "+-*^/":
            val_1 = stack_array.pop()
            val_2 = stack_array.pop()
            rpn_exp = val_1 + " " + val_2 + " " + char
            stack_array.push(rpn_exp)
        else:
            stack_array.push(char)       
    return stack_array.arr[0]
