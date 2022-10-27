def validator(method, error_message):
    def receiver(function):
        def wrapper(*args, **kwargs):
            if 'g_t' in func:
                if method < function(*args, **kwargs):
                    return function(*args, **kwargs)
                else:
                    return error_message

            if 'l_t' in func:
                if method > function(*args, **kwargs):
                    return function(*args, **kwargs)
                else:
                    return error_message

            if 'a_i' in func:
                if function(*args, **kwargs) in method:
                    return function(*args, **kwargs)
                else:
                    return error_message

            if 's_w' in func:
                if function(*args, **kwargs)[0] == method:
                    return function(*args, **kwargs)
                else:
                    return error_message
        return wrapper
    return receiver


func = set()


def greater_than(minimum_value):
    func.add('g_t')
    return minimum_value


def less_than(maximum_value):
    func.add('l_t')
    return maximum_value


def arg_in(possible_value):
    func.add('a_i')
    return possible_value


def starts_with(start_of_argument):
    func.add('s_w')
    return start_of_argument
