def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    list_result = []
    for val in parens:
        if val == '(':
            list_result.append(val)
        elif val == ')':
            if list_result :
                list_result.pop(len(list_result) - 1)
            else: return False

    if list_result:
        return False
    else:
        return True
    
print(valid_parentheses("()"))
print(valid_parentheses("()()"))
print(valid_parentheses("(()())"))
print(valid_parentheses(")()"))
print(valid_parentheses("())"))
print(valid_parentheses(")()("))