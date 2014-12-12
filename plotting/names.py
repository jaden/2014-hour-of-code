import matplotlib.pyplot as plt
import sys

def get_name_popularity(name, year):
    f = open('names/yob%s.txt' % year)
    for line in f.readlines():
        fname, gender, count = line.split(',')
        if fname == name:
            return count
    return 0

def plot_chart(years, occurrences, years2=None, occurrences2=None):

    plt.figure(figsize=(20,5))
    
    if years2 and occurrences2:
        lines = plt.plot(years, occurrences, 'ro', years2, occurrences2, 'go')
    else:
        lines = plt.plot(years, occurrences, 'ro')
    
    for line in lines:
        line.set_antialiased(True)
        line.set_linestyle('-')
        line.set_linewidth(2)
        
    if len(names) > 1:
        lines[0].set_label(names[0])
        lines[1].set_label(names[1])
        plt.legend(shadow=True, loc='best', framealpha=.5)

    plt.xlabel('Year')
    plt.ylabel('Occurrences')
    plt.title(r'Popularity of %s by Year' % ' and '.join(names))    
    plt.show()
    
def graph_names(names):
    if len(names) == 1:
        years, occurrences = graph_name(names[0])
        plot_chart(years, occurrences)
        return
    years, occurrences = graph_name(names[0])
    years2, occurrences2 = graph_name(names[1])
    plot_chart(years, occurrences, years2, occurrences2)
    
def graph_name(name):
    sys.stdout.write("Calculating popularity of %s..." % name)
    years = [year for year in range(1880, 2013 + 1)]
    occurrences = [get_name_popularity(name, year) for year in years]
    sys.stdout.write("Done\n")
    return years, occurrences

if len(sys.argv) == 1:    
    names = raw_input('Enter one or two names (e.g. Frank Sally): ')
    if len(names) == 0:
        names = ['Frank', 'Sally']
    else:
        # Split names list, ignoring spaces
        names = [name.strip() for name in names.split(' ')]
    
else:
    names = sys.argv[1:]

graph_names(names)
