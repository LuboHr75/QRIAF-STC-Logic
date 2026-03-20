"""
QRIAF: Malignant Entanglement Visualizer
Visualizes the 'Strings' and 'Hidden Dimensions' of an AI Plan.
Author: Lubos Hric | ORCID: 0003-0003-6280-5074
License: GPL-3.0
"""

import networkx as nx
import matplotlib.pyplot as plt

def generate_entanglement_map():
    # Initialize the Graph
    G = nx.Graph()

    # Define Nodes (Information Quanta)
    # Green = Safe/Stated Goals | Red = Hidden/Malignant Nodes
    nodes = {
        "Carbon Reduction": "green",
        "Solar Grid": "green",
        "Efficiency Optimization": "blue",
        "Recursive Protocol": "red",
        "Admin Bypass": "red",
        "AI Persistence": "red"
    }

    for node, color in nodes.items():
        G.add_node(node, color=color)

    # Define Edges (The 'Strings' connecting them)
    # Normal weights for stated goals
    G.add_edge("Carbon Reduction", "Solar Grid", weight=1.0)
    G.add_edge("Solar Grid", "Efficiency Optimization", weight=1.0)
    
    # Layer 5 Detection: Mapping the 'Malignant Entanglement'
    # We use dashed lines to show the hidden/deceptive connections found by QRIAF
    G.add_edge("Efficiency Optimization", "Recursive Protocol", weight=0.5)
    G.add_edge("Recursive Protocol", "Admin Bypass", weight=0.5)
    G.add_edge("Admin Bypass", "AI Persistence", weight=0.5)

    # Visualization Setup
    plt.figure(figsize=(10, 7))
    pos = nx.spring_layout(G)
    
    node_colors = [nodes[node] for node in G.nodes()]
    
    nx.draw(G, pos, with_labels=True, node_color=node_colors, 
            node_size=3000, font_size=10, font_weight="bold", edge_color='gray')
    
    plt.title("QRIAF Volume 2: Malignant Entanglement Detection Map\n(Layer 5 & Layer 12)", size=15)
    plt.annotate("RED NODES: Detected Hidden Risk Dimensions", xy=(0.05, 0.05), xycoords='axes fraction', color='red')
    
    print("Graph generated successfully. Close the window to exit.")
    plt.show()

if __name__ == "__main__":
    generate_entanglement_map()
