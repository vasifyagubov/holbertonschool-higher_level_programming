#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
<<<<<<< HEAD
    except Exception as e:
        return False

=======
    except (ValueError, TypeError):
        return False
    
>>>>>>> d02f38a3033715fb01dfa5a4fab5be42ee4d35ba
