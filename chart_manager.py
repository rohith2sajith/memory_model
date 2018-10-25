import matplotlib.pyplot as plt
import rundata
import config
from scipy.stats import gaussian_kde
import numpy as np
import os

class ChartManager(object):
    CHART_COLOR_LIST = ['#FF0000','#00FF00','#0000FF','#FFFF00','#FF00FF','#00FFFF','#F00000','#00F000','#0000F0','#F0F0F0']
    CHART_LINE_STYLE = ['-', '--', '-.', ':']

    REPORT_FILE_NAME_GAMMA = os.path.join(config.REPORT_FOLDER, "gamma_variations.csv")
    REPORT_FILE_NAME_GAMMA_STABLE = os.path.join(config.REPORT_FOLDER, "gamma_variations_stable.csv")
    REPORT_FILE_NAME_SEARCH_LENGTH = os.path.join(config.REPORT_FOLDER, "search_length.csv")
    REPORT_FILE_NAME_SEARCH_LENGTH_STABLE = os.path.join(config.REPORT_FOLDER, "search_length_stable.csv")


    def get_color(self,index):
        index = index%len(self.CHART_COLOR_LIST)
        return self.CHART_COLOR_LIST[index]

    def save_path_for_gamma_variations(self,run_time_data_set:rundata.RunDataSet):
        """
        Save as csv
        :param run_time_data_set:
        :return:
        """
        data_over = False
        index = 0
        # get the gamma

        with open(self.REPORT_FILE_NAME_GAMMA, "w+") as f:
            line = ""
            for ds in run_time_data_set.data_set:
                line = f"{line}gamma_{ds.gamma:>12},"
            f.write(f"{line}\n")
            while not data_over:
                at_least_one = False
                # gamma first

                line = ""
                for ds in run_time_data_set.data_set:
                    if index < len(ds.paths):
                        line = f"{line}{ds.paths[index]:>12.6f},"
                        at_least_one = True
                    else:
                        line = f"{line}{' ':>12.6},"
                index +=1
                f.write(f"{line}\n")
                data_over = not at_least_one

    def plot_path_for_gamma_variations(self,run_time_data_set:rundata.RunDataSet):
        """
        Plot the path
        :return:
        """
        self.save_path_for_gamma_variations(run_time_data_set)
        index = 0

        for ds in run_time_data_set.data_set:
            x_cords = [i for i in range(len(ds.paths))]
            density = gaussian_kde(ds.paths)
            density.covariance_factor = lambda: .25
            density._compute_covariance()
            xs = np.linspace(0, 100, 200)
            plt.plot(xs, density(xs), color=self.get_color(index), label=f"{ds.gamma}")
            #plt.plot(x_cords,ds.paths,color=self.get_color(index),label=f"{ds.gamma}")
            index +=1

        plt.xlabel('gamma')
        plt.ylabel('weight')
        plt.title("Weight Plot")
        plt.legend()
        plt.show()

    def save_search_length(self,steps,special,omnicient):
        index =0
        with open(self.REPORT_FILE_NAME_SEARCH_LENGTH, "w+") as f:
            for x in steps:
                str = f"{x},{special[index]},{omnicient[index]}"
                f.write(f"{str}\n")
                index +=1



    def plot_search_length(self,steps,special,omnicient):
        """
        Plot chart length
        :param steps:
        :param special:
        :param omnicient:
        :return:
        """
        self.save_search_length(steps,special,omnicient)

        plt.plot(steps, special, color=self.get_color(0), label=f"special")
        plt.plot(steps, omnicient, color=self.get_color(1), label=f"omnicient")
        plt.xlabel('# of Learning Steps')
        plt.ylabel('Search Length')
        plt.title("Comparing Special and Omnicient")
        plt.legend()
        plt.show()




