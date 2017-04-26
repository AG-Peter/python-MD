import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(trajectory, speed):
    fig, ax = plt.subplots()
    head, = ax.plot([], [], lw=2, marker='o', color='y')
    trace, = ax.plot([], [], lw=2, color='y')
    lines = [head, trace]
    x_data = []
    y_data = []

    def init():
        ax.set_ylim(0, 1)
        ax.set_xlim(0, 1)
        fig.canvas.set_window_title('tennis ball simulation')
        del x_data[:]
        del y_data[:]
        for line in lines:
            line.set_data(x_data, y_data)
        return lines,

    def run(data):
        x, y = data
        x_data.append(x)
        y_data.append(y)
        lines[0].set_data(x_data[-1], y_data[-1])
        lines[1].set_data(x_data, y_data)
        return lines
    ani = animation.FuncAnimation(fig, run, iter(trajectory), blit=False, interval=speed,
                                  repeat=False, init_func=init)
    return ani
