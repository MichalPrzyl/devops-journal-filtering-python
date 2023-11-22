import time

SIZE = 10000000

def prepare():
    initial_list = [x for x in range(SIZE)]
    return initial_list


def filter_lambda_func():
    initial_list = prepare()
    start = time.time()
    # filtering
    odds = list(filter(lambda x: x%2==0, initial_list))
    end = time.time()
    print("filter lambda functime: {:.3f}s".format(end-start))


def filter_func():
    initial_list = prepare()
    
    start = time.time()

    def custom_filtering_func(element):
        if element%2 == 0:
            return True
        else:
            return False

    odds = list(filter(custom_filtering_func, initial_list))
    end = time.time()
    print("filter func time: {:.3f}s".format(end-start))

def list_comp_func():
    initial_list = prepare()

    start = time.time()
    # filtering
    odds = [x for x in initial_list if x%2==0]
    end = time.time()
    print("list compr time: {:.3f}s".format(end-start))

def generator_func():
    initial_list = prepare()

    start = time.time()
    # filtering
    output = []
    odds = (x for x in initial_list if x%2==0)
    for el in odds:
        output.append(el)
    end = time.time()
    print("generator time: {:.3f}s".format(end-start))


def primitive_func():
    initial_list = prepare()

    start = time.time()
    # filtering
    odds = []
    for element in initial_list:
        if element %2 == 0:
            odds.append(element)
    end = time.time()
    print("primitive func time: {:.3f}s".format(end-start))


def main():
    primitive_func()
    filter_func()
    filter_lambda_func()
    list_comp_func()
    generator_func()

if __name__ == "__main__":
    main()
