import pygraphviz as pgv

# Create a new graph
graph = pgv.AGraph(directed=True)

# Define the cars, engines, batteries, and their respective service criteria
cars = {
    "Calliope": "Capulet Engine",
    "Glissade": "Willoughby Engine",
    "Palindrome": "Sternman Engine",
    "Rorschach": "Willoughby Engine",
    "Thovex": "Capulet Engine"
}

engines = {
    "Capulet Engine": "Once every 30,000 miles",
    "Willoughby Engine": "Once every 60,000 miles",
    "Sternman Engine": "Only when the warning indicator is on"
}

batteries = {
    "Spindler Battery": "Once every 2 years",
    "Nubbin Battery": "Once every 4 years"
}

# Add the cars, engines, and batteries as nodes to the graph
graph.add_node("Car", shape="box")
graph.add_nodes_from(cars.keys(), shape="box")
graph.add_node("Engine", shape="box")
graph.add_nodes_from(engines.keys(), shape="box")
graph.add_node("Battery", shape="box")
graph.add_nodes_from(batteries.keys(), shape="box")

# Add the relationships between the cars, engines, and batteries with their service criteria
for car, engine in cars.items():
    graph.add_edge(car, engine, label=f"criteria_for_service: {engines[engine]}")

for car, battery in cars.items():
    graph.add_edge(car, battery, label=f"criteria_for_service: {batteries[battery]}")

# Set the layout algorithm to dot
graph.layout(prog="dot")

# Save the graph as an image file
graph.draw("diagram.png")
