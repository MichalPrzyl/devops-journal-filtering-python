import matplotlib.pyplot as plt 
from matplotlib import rcParams
import json




def draw_charts():
    with open('data.json') as json_file:
        data = json.load(json_file)

    rcParams.update({'font.size': 10})
    primivite_func_times = data['primitive_func_times']
    x1 = [index for index in range(len(primivite_func_times))] 
    y1 = primivite_func_times
    print(f"x1: {x1}")
    print(f"y1: {y1}")
    # plotting the line 1 points  
    plt.plot(x1, y1, label = "primitive function", linewidth=1.0) 
    plt.rc('ytick', labelsize=1)    # fontsize of the tick labels
    
    # 2nd
    filter_func_times = data['filter_func_times']
    x2 = [index for index in range(len(filter_func_times))] 
    y2 = filter_func_times
    plt.plot(x2, y2, label = "filter") 

    filter_lambda_func_times = data['filter_lambda_func_times']
    x2 = [index for index in range(len(filter_lambda_func_times))] 
    y2 = filter_lambda_func_times
    plt.plot(x2, y2, label = "filter with lambda") 

    list_comp_func_times = data['list_comp_func_times']
    x2 = [index for index in range(len(list_comp_func_times))] 
    y2 = list_comp_func_times
    plt.plot(x2, y2, label = "list comprehension") 

    generator_func_times = data['generator_func_times']
    x2 = [index for index in range(len(generator_func_times))] 
    y2 = generator_func_times
    plt.plot(x2, y2, label = "generator") 

    # # line 2 points 
    # x2 = [1,2,3]
    # y2 = [4,1,3]
    # # plotting the line 2 points  
    # # plt.plot(x2, y2, label = "line 2") 
    plt.title('Some cool customizations!') 
    plt.legend()
    plt.ylabel = "time in seconds"
    plt.rc('font', size=1)          # controls default text sizes
    plt.show() 

if __name__ == "__main__":
    draw_charts()