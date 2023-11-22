import time
import random
import string
from draw_charts import draw_charts
from utils import write_to_file


SIZE = 5000000
TIMES = 10
OUTPUT_FILE = 'data_string.json'
POSTFIX = 'kc'
STRING_LENGTH = 5

def generate_random_string(length: int):
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))

def prepare():
    initial_list = [generate_random_string(STRING_LENGTH) for _ in range(SIZE)]
    return initial_list


def filter_lambda_func():
    initial_list = prepare()
    start = time.time()
    # filtering
    filtered = list(filter(lambda x: x.endswith(POSTFIX), initial_list))
    end = time.time()
    # print("filter lambda functime: {:.5f}s".format(end-start))
    return "{:.5f}".format(end-start)


def filter_func():
    initial_list = prepare()
    
    start = time.time()

    def custom_filtering_func(element):
        if element.endswith(POSTFIX):
            return True
        else:
            return False

    odds = list(filter(custom_filtering_func, initial_list))
    end = time.time()
    # print("filter func time: {:.5f}s".format(end-start))
    return "{:.5f}".format(end-start)

def list_comp_func():
    initial_list = prepare()

    start = time.time()
    # filtering
    odds = [x for x in initial_list if x.endswith(POSTFIX)]
    end = time.time()
    # print("list compr time: {:.5f}s".format(end-start))
    return "{:.5f}".format(end-start)

def generator_func():
    initial_list = prepare()

    start = time.time()
    # filtering
    output = []
    odds = (x for x in initial_list if x.endswith(POSTFIX))
    for el in odds:
        output.append(el)
    end = time.time()
    # print("generator time: {:.5f}s".format(end-start))
    return "{:.5f}".format(end-start)


def primitive_func():
    initial_list = prepare()

    start = time.time()
    # filtering
    odds = []
    for element in initial_list:
        if element.endswith(POSTFIX):
            odds.append(element)
    end = time.time()
    # print("primitive func time: {:.5f}s".format(end-start))
    return "{:.5f}".format(end-start)


def main():
    primitive_func_times = []
    filter_func_times = []
    filter_lambda_func_times = []
    list_comp_func_times = []
    generator_func_times = []

    iteration = 0
    
    for _ in range(TIMES):
        # print(f"ITERATION: {iteration}/{TIMES}")
        print(f"ITERATION: {iteration/TIMES*100}%")
        filter_func_times.append(filter_func())
        primitive_func_times.append(primitive_func())
        filter_lambda_func_times.append(filter_lambda_func())
        list_comp_func_times.append(list_comp_func())
        generator_func_times.append(generator_func())
        iteration += 1


    write_to_file(OUTPUT_FILE, {
        "primitive_func_times": primitive_func_times,
        "filter_func_times": filter_func_times,
        "filter_lambda_func_times": filter_lambda_func_times,
        "list_comp_func_times": list_comp_func_times,
        "generator_func_times": generator_func_times,
    })

if __name__ == "__main__":
    main()
