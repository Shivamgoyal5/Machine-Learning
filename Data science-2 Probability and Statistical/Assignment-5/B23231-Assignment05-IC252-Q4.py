import math
import matplotlib.pyplot as plt
import numpy as np

class BivariateGaussianDistribution:
    def __init__(self, mean_x, mean_y, var_x, var_y, cov):
        self.mean_x = mean_x
        self.mean_y = mean_y
        self.var_x = var_x
        self.var_y = var_y
        self.cov = cov
    
    def calculate_pdf(self, x, y):
        return (1/(2*math.pi*self.var_x*self.var_y*math.sqrt(1-self.cov**2)))*math.exp(-1/(2*(1-self.cov**2))*(((x-self.mean_x)**2/self.var_x**2)+((y-self.mean_y)**2/self.var_y**2)-2*self.cov*(x-self.mean_x)*(y-self.mean_y)/(self.var_x*self.var_y)))
    
    def marginal_pdf_x(self, x):
        return (1/(math.sqrt(2*math.pi*self.var_x)))*math.exp(-1/(2*self.var_x)*(x-self.mean_x)**2)
    
    def marginal_pdf_y(self, y):
        return (1/(math.sqrt(2*math.pi*self.var_y)))*math.exp(-1/(2*self.var_y)*(y-self.mean_y)**2)
    
    def plot_pdf_contour(self):
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.zeros(X.shape)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                Z[i, j] = self.calculate_pdf(X[i, j], Y[i, j])
        plt.contour(X, Y, Z)
        plt.show()


# Test the class
distribution = BivariateGaussianDistribution(1.0, 1.0, 1.0, 1.0, 0.5)
pdf_value = distribution.calculate_pdf(1.5, 2.0)
marginal_pdf_x = distribution.marginal_pdf_x(1.0)
distribution.plot_pdf_contour()