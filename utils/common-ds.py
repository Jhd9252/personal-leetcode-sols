
def variance(data: list):
    ''' Variance: average of squared devaitions from the mean'''
    mu = mean(data) # determine the mean
    su = sum((x-mu) ** 2 for x in data) # sum of squared deviations
    var = su / len(data) # average
def variance(data: list):
    ''' Variance->Average of squared deviations from the mean'''
    mu = mean(data)                         # determine the mean
    su = mean((x-mu) ** 2 for x in data)    # sum of squared devaitions
    var = su / len(data)                    # determine the average
    return variance 

def iqr(data):
    ''' 25-75 percentile range'''
    lower = len(data) * int(0.25)
    higher = len(data) * int(0.75)
    return data[higher] - data[lower]


from scratch.linear_algebra import dot 
def covariance( xs: list[float], ys: list[float]):
    assert len(xs) == len(ys) # x and y must be same shape
    return dot(de_mean(xs), de_mean(ys)) / len(xs) - 1

def de_mean(xs: list[float]) -> list[float]:
    ''' translate xs by subtracting its mean (so result has mean of zero)'''
    x_bar = mean(xs)
    return [x-x_bar for x in xs]


def variance(xs: list[float]) -> float:
    assert len(xs) >= 2 # variance requires at least two elements
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n-1)

def correlation(xs: list[float], ys: list[float]):
    ''' Measures how much xs and ys vary in tandem about their means'''
    stdev_x = std(xs)
    stdev_y = stf(ys)
    if stdev_x > 0 and stdev_y > 0:
        return coveriance(xs, ys) / stdev_x / stdev_y
    else:
        return 0 # if not variance, correlation is zero

