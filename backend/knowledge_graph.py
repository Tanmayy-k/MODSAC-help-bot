import pandas as pd  # Make sure pandas is installed
import networkx as nx  # Make sure networkx is installed

# Function to load knowledge graph from CSV
def load_knowledge_graph(csv_file):
    try:
        # Load CSV into DataFrame
        df = pd.read_csv(csv_file)

        # Create a directed graph
        G = nx.DiGraph()

        # Iterate over each row and add nodes/edges
        for index, row in df.iterrows():
            question = row['question']
            answer = row['answer']

            # Add nodes
            G.add_node(question, type='question')
            G.add_node(answer, type='answer')

            # Add edge from question to answer
            G.add_edge(question, answer, relation='answers')

        print(f"✅ Knowledge graph created with {len(G.nodes)} nodes and {len(G.edges)} edges.")
        return G

    except Exception as e:
        print(f"❌ Error loading knowledge graph: {e}")
        return None
