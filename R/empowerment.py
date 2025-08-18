import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Nodes representing Kabeer's framework
nodes = ["Resources", "Agency", "Achievements", "Empowerment"]

# Edges to show the circular process
edges = [("Resources", "Agency"), 
         ("Agency", "Achievements"), 
         ("Achievements", "Resources")]

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Positioning nodes in a circular layout
pos = nx.circular_layout(G)

# Manually position "Empowerment" at the center
pos["Empowerment"] = [0, 0]

# Draw nodes
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray")

# Highlight "Empowerment" at the center
nx.draw_networkx_nodes(G, pos, nodelist=["Empowerment"], node_color="red", node_size=3500)

# Show the plot
plt.title("Kabeer’s Women Empowerment Theory")
plt.show()
