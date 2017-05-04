import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

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


def plot(trajectory_time, trajectory_numerical,trajectory_analytical,error):
  fig=plt.figure()
  ax=fig.add_subplot(211)
  fig.tight_layout()
  ax.set_title("trajectory")
  ax.plot(np.array(trajectory_numerical)[:,0],np.array(trajectory_numerical)[:,1], label="numerical")
  ax.plot(np.array(trajectory_analytical)[:,0],np.array(trajectory_analytical)[:,1], label="analytical")
  ax.legend()
  ax.set_ylabel("y")
  ax.set_xlabel("x")


  plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)

  ax=fig.add_subplot(212)
  ax.set_title("Error")
  ax.plot(trajectory_time,np.array(error)[:,0], label="Error in x")
  ax.plot(trajectory_time,np.array(error)[:,1], label="Error in y")
  ax.plot()
  ax.legend()
  ax.set_ylabel("error")
  ax.set_xlabel("time")
  plt.show()