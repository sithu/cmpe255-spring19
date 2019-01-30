from matplotlib import pyplot

# https://tradingeconomics.com/united-states/gdp
years= [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
gdp = [14964.37, 15517.93, 16155.26, 16691.52, 17427.61, 18120.71, 18624.48, 19390.6]

def line_chart():
    pyplot.plot(years, gdp, color='green', marker='o', linestyle='solid')
    pyplot.title("Nominal GDP of United States")
    pyplot.ylabel("$ in Billions")
    pyplot.show()

def bar_chart():
    pyplot.bar(years, gdp)
    pyplot.title("Nominal GDP of United States")
    pyplot.ylabel("$ in Billions")
    pyplot.show()

bar_chart()