averages =[[39.766972461368965, 40.42311234454947, 39.73715861137575, 41.71161208358292, 41.56841467371977]]

import statistics
for average in averages:
    new_list = []
    for nums in average:
        new_list.append(nums)
    print(new_list)
    print(round(statistics.mean(average)), round(statistics.stdev(average),3))