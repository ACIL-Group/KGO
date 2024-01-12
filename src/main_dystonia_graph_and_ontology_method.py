"""
    NetworkX Graph Generation Script

# Description
This script imports data from CSV files, creates a NetworkX graph, and performs operations on the graph.

# Usage
- Make sure to run this file from the top of the repository directory.
- Ensure that the required data files are in the specified directory.

# Attribution
Author: Daniel B. Hier MD
"""

############################
# Import needed libraries  #
############################

import pandas as pd
import networkx as nx
from rdflib import Graph, Namespace, RDF, RDFS, OWL, XSD, Literal
import matplotlib.pyplot as plt
from pathlib import Path

from typing import (
    List,
)

########################################################
# Data Files                                           #
########################################################

# Point to the location where the data is located
data_dir = Path("data")
out_dir = Path("out")

# Ouptut files
out_graph_file = out_dir.joinpath("dystonia_graph.graphml")
out_graph_image = out_dir.joinpath("low_resolution_dystonia_graph.png")
out_ontology = out_dir.joinpath("dystonia.owl")

# Declare all of the data files used
node_files_raw = [
    'dystonia_nodes.csv',
    'dystonia_proteins_nodes.csv',
    'dystonia_genes_nodes.csv',
    'dystonia_diseases_nodes.csv',
    'dystonia_phenotypes_nodes.csv',
    'dystonia_inheritance_nodes.csv',
    'dystonia_proteins_GO_CC.csv',
    'dystonia_proteins_GO_MF.csv',
    'dystonia_proteins_GO_BP.csv',
]

edge_files_raw = [
    'dystonia_edges.csv',
    'dystonia_phenotypes_edges.csv',
    'dystonia_gene_to_protein_edges.csv',
    'dystonia_disease_caused_by_gene_edges.csv',
    'dystonia_diseases_is_a_disease_edges.csv',
    'dystonia_inheritance_edges.csv',
    'dystonia_protein_GO_edges.csv',
]

# Get the full path for each data file
node_files = [data_dir.joinpath(node_file) for node_file in node_files_raw]
edge_files = [data_dir.joinpath(edge_file) for edge_file in edge_files_raw]


########################################################
# Procedures go here                                   #
########################################################


def add_data_properties(g: Graph):
    # Define the namespaces
    ex = Namespace("http://example.org/")
    g.bind("ex", ex)
    # Define individual URIs for data properties
    gene_MIM_uri = ex['gene_MIM']
    disease_MIM_uri = ex['disease_MIM']
    chromosome_location_uri = ex['chromosome_location']

    # Declare data properties
    g.add((gene_MIM_uri, RDF.type, OWL.DatatypeProperty))
    g.add((gene_MIM_uri, RDFS.domain, ex.gene))
    g.add((gene_MIM_uri, RDFS.range, XSD.string))

    g.add((disease_MIM_uri, RDF.type, OWL.DatatypeProperty))
    g.add((disease_MIM_uri, RDFS.domain, ex.gene))
    g.add((disease_MIM_uri, RDFS.range, XSD.string))

    g.add((chromosome_location_uri, RDF.type, OWL.DatatypeProperty))
    g.add((chromosome_location_uri, RDFS.domain, ex.gene))
    g.add((chromosome_location_uri, RDFS.range, XSD.string))

    # Define individual URIs for data properties
    protein_MW_uri = ex['protein_MW']
    protein_length_uri = ex['protein_length']
    protein_name_uri = ex['protein_name']

    # Declare data properties
    g.add((protein_MW_uri, RDF.type, OWL.DatatypeProperty))
    g.add((protein_MW_uri, RDFS.domain, ex.protein))
    g.add((protein_MW_uri, RDFS.range, XSD.string))

    g.add((protein_length_uri, RDF.type, OWL.DatatypeProperty))
    g.add((protein_length_uri, RDFS.domain, ex.protein))
    g.add((protein_length_uri, RDFS.range, XSD.string))

    g.add((protein_name_uri, RDF.type, OWL.DatatypeProperty))
    g.add((protein_name_uri, RDFS.domain, ex.protein))
    g.add((protein_name_uri, RDFS.range, XSD.string))

    # Define individual URI for the 'hpo_id' data property
    hpo_id_uri = ex['hpo_id']

    # Declare the 'hpo_id' data property
    g.add((hpo_id_uri, RDF.type, OWL.DatatypeProperty))
    g.add((hpo_id_uri, RDFS.domain, ex.phenotype))
    g.add((hpo_id_uri, RDFS.range, XSD.string))  # Assuming 'hpo_id' is a string

    # Define individual URIs for data properties
    disease_name_uri = ex['disease_name']
    gene_name_uri = ex['gene_name']
    gene_MIM_uri = ex['gene_MIM']

    # Declare data properties
    g.add((disease_name_uri, RDF.type, OWL.DatatypeProperty))
    g.add((disease_name_uri, RDFS.domain, ex.disease))
    g.add((disease_name_uri, RDFS.range, XSD.string))

    g.add((gene_name_uri, RDF.type, OWL.DatatypeProperty))
    g.add((gene_name_uri, RDFS.domain, ex.disease))
    g.add((gene_name_uri, RDFS.range, XSD.string))

    g.add((gene_MIM_uri, RDF.type, OWL.DatatypeProperty))
    g.add((gene_MIM_uri, RDFS.domain, ex.disease))
    g.add((gene_MIM_uri, RDFS.range, XSD.string))

    return (g)


def add_object_properties(g: Graph):
    ex = Namespace("http://example.org/")
    # Define an object property
    object_property_uri = ex['causes']
    g.add((object_property_uri, RDF.type, RDF.Property))
    g.add((object_property_uri, RDFS.domain, ex['gene']))
    g.add((object_property_uri, RDFS.range, ex['disease']))

    obj_property_uri = ex['located_in']
    # Declare the object property
    g.add((obj_property_uri, RDF.type, OWL.ObjectProperty))
    # Declare the domain and range of the object property
    g.add((obj_property_uri, RDFS.domain, ex['protein']))
    g.add((obj_property_uri, RDFS.range, ex['CC']))

    obj_property_uri = ex['has_phenotype']
    # Declare the object property
    # Declare the domain and range of the object property
    g.add((obj_property_uri, RDFS.domain, ex['disease']))
    g.add((obj_property_uri, RDFS.range, ex['phenotype']))

    obj_property_uri = ex['has_inheritance']
    g.add((obj_property_uri, RDF.type, OWL.ObjectProperty))
    g.add((obj_property_uri, RDFS.domain, ex['disease']))
    g.add((obj_property_uri, RDFS.range, ex['inheritance']))

    object_property_uri = ex['enables']
    g.add((object_property_uri, RDF.type, RDF.Property))
    g.add((object_property_uri, RDFS.domain, ex['protein']))
    g.add((object_property_uri, RDFS.range, ex['MF']))

    object_property_uri = ex['codes_for']
    g.add((object_property_uri, RDF.type, RDF.Property))
    g.add((object_property_uri, RDFS.domain, ex['gene']))
    g.add((object_property_uri, RDFS.range, ex['protein']))

    object_property_uri = ex['is_active_in']
    g.add((object_property_uri, RDF.type, RDF.Property))
    g.add((object_property_uri, RDFS.domain, ex['protein']))
    g.add((object_property_uri, RDFS.range, ex['MF']))

    g.add((object_property_uri, RDF.type, RDF.Property))
    g.add((object_property_uri, RDFS.domain, ex['protein']))
    g.add((object_property_uri, RDFS.range, ex['BP']))

    object_property_uri = ex['is_involved_in']
    g.add((object_property_uri, RDF.type, RDF.Property))
    g.add((object_property_uri, RDFS.domain, ex['protein']))
    g.add((object_property_uri, RDFS.range, ex['BP']))

    return g


def create_networkx_graph(
    node_files: List[Path],
    edge_files: List[Path],
    G: nx.Graph
):
    """
    Create a NetworkX graph from data files.

    Parameters:
    - node_files (list): List of CSV files containing node data.
    - edge_files (list): List of CSV files containing edge data.

    Returns:
    - G (NetworkX Graph): The generated graph.
    """
    # Iterate through the node files and add all nodes to the NetworkX graph G
    for node_file in node_files:
        df = pd.read_csv(node_file)
        for index, row in df.iterrows():
            node_name = row['node_name']
            node_attributes = {}
            for col_name in df.columns[1:]:
                attribute_value = row[col_name]
                node_attributes[col_name] = attribute_value
            G.add_node(node_name, **node_attributes)

    # Add edges from edge files to the NetworkX graph G
    for edge_file in edge_files:
        df_edges = pd.read_csv(edge_file)
        for index, row in df_edges.iterrows():
            source = row['source']
            target = row['target']
            if target in G.nodes() and source in G.nodes():
                edge_name = row.get('edge_name', None)
                G.add_edge(source, target, edge_name=edge_name)
            else:
                print(edge_file, source, target)

    return G


def plot_graph(G: nx.Graph):
    # Specify the figure size (adjust the values as needed)
    plt.figure(figsize=(15, 15))
    # Get the 'supernode' attribute values for all nodes
    supernode_values = nx.get_node_attributes(G, 'supranode').values()
    # Define node colors based on the 'supernode' attribute
    # Assign a unique color to each 'supernode' value
    node_colors = []
    for value in supernode_values:
        if value == 'gene':
            node_colors.append('red')
        elif value == 'protein':
            node_colors.append('blue')
        elif value == 'disease':
            node_colors.append('orange')
        elif value == 'phenotype':
            node_colors.append('green')
        elif value == 'BP':
            node_colors.append('cyan')
        elif value == 'CC':
            node_colors.append('cyan')
        elif value == 'inheritance':
            node_colors.append('green')
        elif value == 'MF':
            node_colors.append('cyan')
        else:
            node_colors.append('gray')  # Default color for unknown values
    # Write the graph to a GraphML file
    nx.write_graphml(G, out_graph_file)
    # Draw a low-resolution graph on the console with node colors
    nx.draw(G, node_color=node_colors)
    # Save the low-resolution graph to disk
    plt.savefig(out_graph_image)

    return


def add_data_properties_to_nodes(g: Graph, G: nx.Graph):
    # Define the namespaces
    ex = Namespace("http://example.org/")
    g.bind("ex", ex)
    # Iterate through the 'disease' nodes and add 'disease_name' data property
    for node_data in G.nodes(data=True):
        node_name = node_data[0]
        node_attributes = node_data[1]

        if 'supranode' in node_attributes and node_attributes['supranode'] == 'disease':
            disease_name = node_attributes.get('disease_name', None)
            node_name = str(node_name)
            disease_name = str(disease_name)
            if disease_name:
                individual_uri = ex[node_name]
                data_property_uri = ex['disease_name']
                g.add((individual_uri, data_property_uri, Literal(disease_name, datatype=XSD.string)))

    for node_data in G.nodes(data=True):
        node_name = node_data[0]
        node_attributes = node_data[1]
        if 'supranode' in node_attributes and node_attributes['supranode'] == 'protein':
            protein_length = node_attributes.get('protein_length', None)
            protein_weight = node_attributes.get('protein_weight', None)
            protein_name = node_attributes.get('protein_name', None)
            node_name = str(node_name)
            protein_length = str(protein_length)
            protein_weight = str(protein_weight)
            protein_name = str(protein_name)
            # print(node_name, protein_length, protein_weight, protein_name)
            individual_uri = ex[node_name]
            data_property_uri = ex['protein_length']
            g.add((individual_uri, data_property_uri, Literal(protein_length, datatype=XSD.string)))
            data_property_uri = ex['protein_weight']
            g.add((individual_uri, data_property_uri, Literal(protein_weight, datatype=XSD.string)))
            data_property_uri = ex['protein_name']
            g.add((individual_uri, data_property_uri, Literal(protein_name, datatype=XSD.string)))

    # Iterate through the 'phenotype' nodes and add 'hpo_id' data property
    for node_data in G.nodes(data=True):
        node_name = node_data[0]
        node_attributes = node_data[1]
        if 'supranode' in node_attributes and node_attributes['supranode'] == 'phenotype':
            hpo_id = node_attributes.get('hpo_id', None)
            if hpo_id:
                individual_uri = ex[node_name]
                data_property_uri = ex['hpo_id']
                g.add((individual_uri, data_property_uri, Literal(hpo_id, datatype=XSD.string)))
    for node_data in G.nodes(data=True):
        node_name = node_data[0]
        node_attributes = node_data[1]
        if 'supranode' in node_attributes and node_attributes['supranode'] == 'gene':
            gene_MIM = node_attributes.get('gene_MIM', None)
            chromosome_location = node_attributes.get('chromosome_location', None)
            node_name = str(node_name)
            gene_MIM = str(gene_MIM)
            chromosome_location = str(chromosome_location)
            individual_uri = ex[node_name]
            data_property_uri = ex['gene_MIM']
            g.add((individual_uri, data_property_uri, Literal(gene_MIM, datatype=XSD.string)))
            data_property_uri = ex['chromosome_location']
            g.add((individual_uri, data_property_uri, Literal(chromosome_location, datatype=XSD.string)))

    return g


def add_edges_to_RDF_graph(g: Graph, G: nx.Graph):
    # Define the namespaces
    ex = Namespace("http://example.org/")
    g.bind("ex", ex)

    # Add object relationships
    start_nodes_set = set()
    end_nodes_set = set()
    all_edges_set = set()
    for e in G.edges.data():
        start_node = e[0]
        start_nodes_set.add(start_node)
        end_node = e[1]
        end_nodes_set.add(end_node)
        edge_name = e[2].get('edge_name', 0)

    # Define a namespace for your object properties
    obj_property_ns = Namespace("http://example.org/object_properties#")
    g.bind("objprop", obj_property_ns)
    source_node_set = set()
    target_node_set = set()

    # Iterate through the edges in your NetworkX graph G
    for edge in G.edges(data=True):
        source_node = str(edge[0])
        target_node = str(edge[1])
        edge_name = str(edge[2].get('edge_name', None))
        all_edges_set.add(edge_name)
        source_node_set.add(source_node)
        target_node_set.add(target_node)

        # Create URIs for the source, target, and object property
        source_uri = ex[source_node]
        target_uri = ex[target_node]
        obj_property_uri = obj_property_ns[edge_name]

        # Add the edge as a triple in the RDF graph
        g.add((source_uri, obj_property_uri, target_uri))

    return g


def add_nodes_to_RDF_graph(g: Graph, G: nx.Graph):
    # Define the namespaces
    ex = Namespace("http://example.org/")
    g.bind("ex", ex)
    supranodes = [
        ex["phenotype"],
        ex["gene"],
        ex["protein"],
        ex['CC'],
        ex['BP'],
        ex['MF'],
        ex['inheritance'],
        ex['disease'],
    ]

    # Add supranodes
    for c in supranodes:
        if c != '':
            g.add((c, RDF.type, OWL.Class))
    for n in G.nodes.data():
        category = ''
        category = n[1].get('category', 0)
        if category == 'instance':
            supranode = n[1].get('supranode', 0)
            individual_name = str(n[0])
            # print(individual_name)
            individual_name_uri = ex[individual_name]
            supranode_uri = ex[supranode]
            g.add((individual_name_uri, RDF.type, supranode_uri))

    return g


def main():
    # G is networkX graph
    # g is an RDF graph
    # Declare a NetworkX graph
    G = nx.Graph()

    # Call the procedure to add nodes and edges to the graph G
    G = create_networkx_graph(node_files, edge_files, G)
    plot_graph(G)

    # Declare an RDF graph
    g = Graph()
    g = add_object_properties(g)
    g = add_data_properties(g)
    g = add_data_properties_to_nodes(g, G)
    g = add_nodes_to_RDF_graph(g, G)
    g = add_edges_to_RDF_graph(g, G)

    # Serialize the updated RDF graph to an OWL file
    g.serialize(out_ontology, format="turtle")
    print('Graph and Ontology complete.')
    print(f'- {out_graph_file} has been written to file as a GraphML file')
    print(f'- {out_graph_image} has been written to file as a PNG file')
    print(f'- {out_ontology} has been written to file as an ontology')

    return


########################################################
# Main Program Starts here                             #
########################################################

if __name__ == "__main__":

    main()
