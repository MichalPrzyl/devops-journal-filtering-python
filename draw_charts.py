import matplotlib.pyplot as plt 


def draw_charts(data:dict):
    primivites_func_times = data['primitive_func_times']
    x1 = [index for index in range(len(primivites_func_times))] 
    y1 = primivites_func_times
    print(f"x1: {x1}")
    print(f"y1: {y1}")
    # plotting the line 1 points  
    plt.plot(x1, y1, label = "line 1") 
    
    # line 2 points 
    x2 = [1,2,3]
    y2 = [4,1,3]
    # plotting the line 2 points  
    # plt.plot(x2, y2, label = "line 2") 
    plt.show() 