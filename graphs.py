import matplotlib.pyplot as plt
import numpy as np
import chart_manager

from scipy.stats import gaussian_kde

class PathLengthChart(object):
    learning_steps = [
            1000,
            2000,
            5000,
            10000,
            15000,
            20000,
            30000,
            40000,
            50000]
    special_search_length=[
            5722.642191,
            3980.78778,
            2040.89876,
            1830.16543,
            1213.618833,
            932.8131334,
            928.1863914,
            914.7487733,
            500.56756,
        ]
    omnicient_search_length=[
            496.3015266,
            198.263664,
            68.65110178,
            531.6355216,
            698.8292312,
            361.3836572,
            712.4156666,
            697.834569,
            497.0785766
    ]
    def __init__(self,filename):
        load_from_file = True
        if load_from_file:
            self.load(filename)

    def load(self,filename):
        with open(filename, "r") as f:
            self.learning_steps = []
            self.special_search_length = []
            self.omnicient_search_length = []
            for line in f:
                line = line.strip("\n")
                parts = line.split(',')
                if parts[0].strip():
                    self.learning_steps.append(float(parts[0].strip()))
                    self.special_search_length.append(float(parts[1].strip()))
                    self.omnicient_search_length.append(float(parts[2].strip()))

    def plot(self,):
        delta = []
        for i in range(len(self.learning_steps)):
            delta.append(self.special_search_length[i]-self.omnicient_search_length[i])

        plt.plot(self.learning_steps,delta,color="#000000",linestyle="--")
        plt.legend()
        plt.title("Diff between special and omnicient")
        plt.xlabel("Number of steps")
        plt.ylabel("Search length(special - omnicient)")
        plt.show()



class GammaVariationsChart(object):
    weights_for_gamma=[]

    weights_for_gamma.append([33.3334,
              33.3335,
              33.3338,
              33.3351,
              33.3394,
              33.3527,
              33.3889,
              33.4277,
              33.5874,
              33.7794,
              36.1240,
              39.5728,
              44.2498,
              51.9131,
              76.6195,
              247.8414,
              5236.4749])
    weights_for_gamma.append([
        20.0000,
        20.0000,
        20.0000,
        20.0000,
        20.0000,
        20.0002,
        20.0006,
        20.0023,
        20.0085,
        20.0301,
        20.1191,
        20.4632,
        21.3571,
        28.0278,
        52.6064,
        1965.0504,
        4292.4050
    ])
    weights_for_gamma.append([
        10.0000,
        10.0000,
        10.0000,
        10.0000,
        10.0000,
        10.0000,
        10.0000,
        10.0000,
        10.0001,
        10.0005,
        10.0039,
        10.0244,
        10.2397,
        11.8327,
        21.6224,
        3264.5460
    ])
    weights_for_gamma.append([
        7.6923,
        7.6923,
        7.6923,
        7.6923,
        7.6923,
        7.6923,
        7.6923,
        7.6923,
        7.6923,
        7.6925,
        7.6942,
        7.7001,
        7.7141,
        7.7555,
        9.1086,
        494.8194,
        2929.6041
    ])
    weights_for_gamma.append([
        6.6667,
        6.6667,
        6.6667,
        6.6667,
        6.6667,
        6.6667,
        6.6667,
        6.6667,
        6.6667,
        6.6667,
        6.6667,
        6.6671,
        6.6712,
        6.7235,
        9.1817,
        770.3576,
        2756.6738
    ])
    weights_for_gamma.append([
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0000,
        5.0001,
        5.0012,
        5.0044,
        5.0720,
        5.7215,
        567.8894,
        2427.5174
    ])
    weights_for_gamma.append([
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0000,
       4.0008,
       4.0038,
       4.2311,
     197.7042,
    2187.9453
    ])
    weights_for_gamma.append([
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3333,
         3.3334,
         3.3335,
         3.3385,
         5.7399,
      2001.9615
    ])
    gamma_value = [0.97, 0.95, 0.9, 0.87, 0.85, 0.8, 0.77, 0.75, 0.7]
    def __init__(self,filename):
        self.init(filename)

    def init(self,filename):
        load_from_file = True
        if load_from_file:
            self.load(filename)

    def load(self,filename):
        self.weights_for_gamma = []
        header = True
        with open(filename, "r") as f:
            self.gamma_value  = []
            for line in f:
                line = line.strip("\n")
                parts = line.split(',')
                values = []
                if header:
                    # header get the gamma values
                    for g in parts:
                        if g:
                            ps = g.split('_')
                            self.gamma_value.append(float(ps[1]))
                            self.weights_for_gamma.append([])
                    header = False
                else:
                    index = 0
                    for g in parts:
                        g = g.strip()
                        if g:
                            self.weights_for_gamma[index].append(float(g))
                        index +=1

    def plot(self):
        cm = chart_manager.ChartManager()
        index = 0
        for g in self.weights_for_gamma:
            x_cords = [i for i in range(len(g))]
            density = gaussian_kde(g)
            density.covariance_factor = lambda: .25
            density._compute_covariance()
            xs = np.linspace(0, 100, 200)
            plt.plot(xs, density(xs), color=cm.get_color(index), linestyle=f"{cm.get_linestyle(index)}",label=f"{self.gamma_value[index]}")
            index +=1

        plt.legend()
        plt.title("Density distribution for various gamma")
        plt.xlabel('Weight buckets')
        plt.ylabel('density')
        plt.show()


class ImpactOfDamage(object):
    def __init__(self,filename):
        self.damage_degree_ratio = []
        self.damage_path_ratio = []
        self.load(filename)

    def load(self,filename):
        with open(filename, "r") as f:
            for line in f:
                line = line.strip("\n")
                parts = line.split(',')
                if parts[0].strip():
                    self.damage_degree_ratio.append(float(parts[0].strip()))
                    self.damage_path_ratio.append(float(parts[1].strip()))

    def plot(self,damage_type):
        ax = plt.plot(self.damage_degree_ratio, self.damage_path_ratio, color="#000000", linestyle="--")
        #plt.legend()
        plt.title(f"Path Length v.s. {damage_type} Damage Proportion")
        plt.xlabel("Damage Propotion (%)")
        plt.ylabel("Damage Length/Control Length)")
        plt.show()