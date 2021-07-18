from load_data import *
from auto_complete_funcs import *

if __name__ == '__main__':
    data = Data()
    data.insert_data_to_dict()
    while True:
        user_query = ignore(input())
        while not user_query[-1] == '#':
            i = 0
            for sentence in get_best_k_completions(data, user_query):
                i += 1
                print(str(i) + '. ', sentence)
            if i < 5:
                pass
            user_query = user_query+input(user_query)
