import pandas as pd
import os

# Function to generate Cypher queries
def generate_cypher_queries():
    
    # Load data from CSV files
    nodes_df = pd.read_csv(os.path.join(os.getcwd(), 'Data', '03 Processed', 'nodes.csv'))
    links_df = pd.read_csv(os.path.join(os.getcwd(), 'Data', '03 Processed', 'links.csv'))

    # Print data to verify
    print(nodes_df.head())
    print(links_df.head())

    cypher_queries = []

    cypher_queries.append(f"MATCH (n) DETACH DELETE n;")

    # Generate Cypher queries for creating nodes
    for index, row in nodes_df.iterrows():
        cypher_queries.append(f"CREATE (:System {{SystemID: {row['SystemID']}, Name: '{row['Systems']}'}})")

    #nothing important here

    # Generate Cypher queries for creating relationships
    for index, row in links_df.iterrows():
        cypher_queries.append(f"MATCH (from:System {{SystemID: {row['FromSystemID']}}}), "
                              f"(to:System {{SystemID: {row['SystemID']}}}) "
                              f"CREATE (from)-[:LINKED_TO {{Group_Count: {row['Group_Count']}}}]->(to);")
        #cypher_queries.append(f"CREATE (System ({row['FromSystemID']})) - [:LINKED_TO] -> (System ({row['SystemID']}))")

    return cypher_queries

# Generate Cypher queries
#cypher_queries = generate_cypher_queries(nodes, links)

def write_cypher():
    cypher_queries = generate_cypher_queries()
    # Write Cypher queries to a file
    with open(os.path.join(os.getcwd(), 'Docs','neo4j_queries.cypher'), 'w') as f:
        for query in cypher_queries:
            #print(query)
            f.write(query + '\n')

    print("Cypher queries generated and saved to 'neo4j_queries.cypher' file.")
