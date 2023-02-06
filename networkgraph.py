#code to generate network graph visualisation

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
import math;
from scipy import stats
import networkx as nx
from pyvis.network import Network

df = pd.read_csv("SFlow_Data_1.csv", names = ['Type', 'sflow_agent_address','inputPort','outputPort','src_MAC','dst_MAC','ethernet_type','in_vlan','out_vlan','src_IP','dst_IP','IP_protocol','ip_tos','ip_ttl','src_port_addr','dest_port_addr','tcp_flags','packet_size','IP_size','sampling_rate','isCNTR'])
df1 = df.loc[df['Type'] != 'CNTR']
dfpairs = df1[['src_IP', 'dst_IP', 'IP_protocol','IP_size']]

dfgraph = dfpairs[['src_IP', 'dst_IP', 'IP_size']]

# result = dfgraph[dfgraph['packet_size'] > 1426]
# result

g = nx.from_pandas_edgelist(dfgraph, source='src_IP', target='dst_IP', edge_attr='IP_size')
net = Network(select_menu=True)
net.force_atlas_2based()
net.from_nx(g)
net.show_buttons(filter_=['physics',"nodes", "edges"])
# net.set_options("""

# """)
net.show('egforceatlas.html')