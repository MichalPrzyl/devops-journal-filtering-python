import matplotlib.pyplot as plt 
import matplotlib
import json

FILE_TO_READ_DATA = 'data_string.json'

def draw_charts():
    with open(FILE_TO_READ_DATA) as json_file:
        data = json.load(json_file)

    primivite_func_times = data['primitive_func_times']
    x1 = [index for index in range(len(primivite_func_times))] 
    y1 = [float(x) for x in primivite_func_times]
    
    filter_func_times = data['filter_func_times']
    x2 = [index for index in range(len(filter_func_times))] 
    y2 = [float(x) for x in filter_func_times]

    filter_lambda_func_times = data['filter_lambda_func_times']
    x3 = [index for index in range(len(filter_lambda_func_times))] 
    y3 = [float(x) for x in filter_lambda_func_times]

    list_comp_func_times = data['list_comp_func_times']
    x4 = [index for index in range(len(list_comp_func_times))] 
    y4 = [float(x) for x in list_comp_func_times]

    generator_func_times = data['generator_func_times']
    x5 = [index for index in range(len(generator_func_times))] 
    y5 = [float(x) for x in generator_func_times]
    
    fig, ax = plt.subplots(figsize=(10, 8)) 

    # font size on Y axis labels
    plt.yticks(fontsize=6)

    # grid
    ax.grid(True, linestyle='--', alpha=0.2)

    # labels
    ax.set_xlabel('Sample No.', fontsize=20)
    ax.set_ylabel('Time in seconds', fontsize=20)

    # plots
    plt.plot(x1, y1, label = "primitive function", linewidth=1.0, marker='o', color='black') 
    plt.plot(x2, y2, label = "filter", linewidth=1.0, marker='o', color='blue') 
    plt.plot(x3, y3, label = "filter with lambda", linewidth=1.0, marker='o', color='red') 
    plt.plot(x4, y4, label = "list comprehension", linewidth=1.0, marker='o', color='green') 
    plt.plot(x5, y5, label = "generator", linewidth=1.0, marker='o', color='purple') 

    plt.title('Filtering in python') 
    plt.legend()
    plt.ylabel = "time in seconds"
    plt.show() 

if __name__ == "__main__":
    draw_charts()
