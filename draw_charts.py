import matplotlib.pyplot as plt 
# from matplotlib import rcParams
import matplotlib
import json




def draw_charts():
    with open('data.json') as json_file:
        data = json.load(json_file)


    fig, ax = plt.subplots(figsize=(10, 8)) 
    ax.set_xlabel('Sample', fontsize=20)
    ax.set_ylabel('Time in seconds', fontsize=20)
    plt.yticks(fontsize=6)
    primivite_func_times = data['primitive_func_times']
    x1 = [index for index in range(len(primivite_func_times))] 
    y1 = primivite_func_times
    print(f"x1: {x1}")
    print(f"y1: {y1}")
    # plotting the line 1 points  
    plt.plot(x1, y1, label = "primitive function", linewidth=1.0, marker='o', color='black') 
    plt.rc('ytick', labelsize=1)    # fontsize of the tick labels
    ax.grid(True, linestyle='--', alpha=0.7)
    # 2nd
    filter_func_times = data['filter_func_times']
    x2 = [index for index in range(len(filter_func_times))] 
    y2 = filter_func_times
    plt.plot(x2, y2, label = "filter", linewidth=1.0, marker='o', color='blue') 

    filter_lambda_func_times = data['filter_lambda_func_times']
    x3 = [index for index in range(len(filter_lambda_func_times))] 
    y3 = filter_lambda_func_times
    plt.plot(x3, y3, label = "filter with lambda", linewidth=1.0, marker='o', color='red') 

    list_comp_func_times = data['list_comp_func_times']
    x4 = [index for index in range(len(list_comp_func_times))] 
    y4 = list_comp_func_times
    plt.plot(x4, y4, label = "list comprehension", linewidth=1.0, marker='o', color='green') 

    generator_func_times = data['generator_func_times']
    x5 = [index for index in range(len(generator_func_times))] 
    y5 = generator_func_times
    plt.plot(x5, y5, label = "generator", linewidth=1.0, marker='o', color='purple') 

    plt.title('Some cool customizations!') 
    plt.legend()
    plt.ylabel = "time in seconds"
    plt.rc('font', size=1)          # controls default text sizes
    plt.show() 

if __name__ == "__main__":
    draw_charts()