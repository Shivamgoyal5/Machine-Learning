import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# random sample generator - also makes textboxes and chexkboxes for stuff
def generate_samples():

    # get user input from input fields
    mean = float(mean_entry.get())
    std_dev = float(std_dev_entry.get())
    
    n = int(n_entry.get())
    l_bound = min(mean-4*std_dev, -10)
    u_bound = max(mean+4*std_dev, 10)

    # generate 5 random samples
    samples = [np.random.normal(mean, std_dev, n) for i in range(5)]
    
    # delete every widget in the samples frame
    for widget in samples_frame.winfo_children():
        widget.destroy()
    
    # checkboxes and textboxes for each sample
    checkboxes = []
    textboxes = []
    for idx, sample in enumerate(samples):
        # calculate mean and variance of the sample
        sample_mean = np.mean(sample)
        sample_var = np.var(sample)
        sample_std_dev = np.sqrt(sample_var)

        var = tk.IntVar() # <- used to keep track of the checkbox state (1=checked, 0=unchecked)
        checkbox = Checkbutton(samples_frame, text='Sample '+str(idx+1), variable=var)
        checkbox.grid(row=idx, column=0, padx=5, pady=5)
        checkboxes.append((idx, var, sample))
        
        textbox = Text(samples_frame, height=5, width=30)
        textbox.insert(tk.END, '\n'.join(map(str, sample)))
        textbox.grid(row=idx, column=1, padx=5, pady=5)
        textboxes.append((textbox, sample))

        # showing the mean and variance of the sample on textboxes beside sample
        statsbox = Text(samples_frame, height=3, width=20)
        statsbox.insert(tk.END, f'Mean: {sample_mean:.3f}\nVar.: {sample_var:.3f}\nStd. Dev.: {sample_std_dev:.3f}')
        statsbox.grid(row=idx, column=2, padx=5, pady=5)

    
    # plotting the samples
    def plot_samples():
        fig, ax = plt.subplots(1, 1, figsize=(8, 6))

        # show the actual normal distribution in background
        # print('fuck level 1')
        x = np.linspace(l_bound, u_bound, 1000)
        y = norm.pdf(x, mean, std_dev)
        ax.plot(x, y, 'k', linewidth=2)
        
        # now plot the samples
        # print('fuck level 2')
        selected_samples = [(idx, sample) for idx, var, sample in checkboxes if var.get() == 1]
        for idx, sample in selected_samples:
            ax.hist(sample, bins=50, alpha=0.6, label='Sample '+str(idx+1), density=True) # Actual index gets preserved
        
        ax.legend()
        ax.set_xlim([l_bound, u_bound])

        # canvas to display the plot inside the Tkinter window
        # print('fuck level 3')
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=3, columnspan=2, padx=10, pady=10)
    
    # plot button
    plot_button = Button(root, text="Plot", command=plot_samples)
    plot_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    plot_samples()


root = tk.Tk()
root.title("Normal Distribution Random Samples")

# input fields for mean and standard deviation
mean_label = Label(root, text="Mean:")
mean_label.grid(row=0, column=0, padx=10, pady=10)
mean_entry = Scale(root, from_=-10, to=10, orient=HORIZONTAL, resolution=0.1)
mean_entry.grid(row=0, column=1, padx=10, pady=10)

std_dev_label = Label(root, text="Standard Deviation:")
std_dev_label.grid(row=0, column=3, padx=10, pady=10)
std_dev_entry = Scale(root, from_=0, to=10, orient=HORIZONTAL, resolution=0.1)
std_dev_entry.grid(row=0, column=4, padx=10, pady=10)

# input field for the number of samples
n_label = Label(root, text="Number of samples:")
n_label.grid(row=1, column=0, padx=10, pady=10)
n_entry = Entry(root)
n_entry.insert(0, "100")
n_entry.grid(row=1, column=1, padx=10, pady=10)

# button to generate random samples
generate_button = Button(root, text="Generate Samples", command=generate_samples)
generate_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

# frame to display the samples
samples_frame = Frame(root)
samples_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Stop code execution when the Tkinter window is closed
root.protocol("WM_DELETE_WINDOW", root.quit)


# setting up defaults
try:
    print('initializing...')
    generate_samples()

except Exception as e:
    print(e)

root.mainloop()