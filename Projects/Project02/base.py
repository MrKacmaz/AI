import plotly.express as px

# Do not modify the line below.
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay",
             "Peru", "Suriname", "Uruguay", "Venezuela"]

# Do not modify the line below.
colors = ["orange", "blue", "green", "red", "yellow"]

emptyDict = {}


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)]
                      for _ in range(vertices)]

    # is safe for vertex v
    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    # A recursive utility function to solve m
    # coloring  problem
    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, colour, c):
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1):
                    return True
                colour[v] = 0

    def graphColouring(self, m, mColours):
        colour = [0] * self.V
        if not self.graphColourUtil(m, colour, 0):
            return False

        # Print the solution
        print("Solution exist and Following are the assigned colours:")
        for c in range(len(colour)):
            print(str(c + 1) + ".index is " + countries[c] + " colour = " + str(mColours[colour[c] - 1]))
            emptyDict.update({str(countries[c]): str(mColours[colour[c] - 1])})
        return True


# Do not modify this method, only call it with an appropriate argument.
# colormap should be a dictionary having countries as keys and colors as values.
def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


def main():
    # (ecuador)---(colombia)---(venezuela)---(guyana)---(suriname)
    # | ____________|           |               |           |
    # | |           |           |               |           |
    # (peru)---(brazil)_________|_______________|___________|
    # |          | | |_____
    # |          | |____  |____
    # |          |     |      |
    # |___(bolivia)__  |      |________________
    # |     |  |    |  |            |         |
    # |     |  | (paraguay)---(uruguay)       |
    # |     |  |______  |___________|         |
    # |     |         | |   __________________|
    # |     |         | |   |
    # |___(chili)---(argentina)     (FI)
    g = Graph(13)
    g.graph = [
        [0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    ]

    colors.reverse()
    g.graphColouring(len(colors), colors)
    colorMap = emptyDict
    plot_choropleth(colorMap)


# Implement main to call necessary functions
if __name__ == "__main__":
    main()
