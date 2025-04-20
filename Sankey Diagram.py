
# Sankey Diagram Generator
# Version: 1.3.6  
# Author: Arash Yoosefdoost

# Description:
# This tool reads a CSV matrix of Source-Target relationships and generates a practical, colorful, and interactive Sankey diagram using Plotly. It is ideal for visualizing flows between categories like keyword trends, resource allocations, or system mappings.
#
# - Visually represent flows between different sources and targets.
# - Perform keyword analysis or thematic distribution reviews.
# - Simplify complex relationships in an intuitive, colorful way.

# Inputs
Data_File = 'INPUT.csv'

# Sankey diagram properties
Sankey_Diagram_Title = 'Sankey Diagram'
Font_Size = 8
Auto_Color = 3 # 0: Gray Mode, 1: Black & Gray, 2: Color Box, 3: # Colorful 
Links_Color = '#d3d3d3' # Will be automatically ignored if Auto_Color = 1
Boxes_Color = 'orange'
Links_Thickness = 0.01
Nodes_Thickness = 25
Spacing = 15


# %% Preparing the data
import csv

# Open the CSV file (DATA) and read its contents into a list of lists
with open(Data_File, 'r') as f:
    reader = csv.reader(f)
    table = list(reader)

# Create empty lists to store the SOURCE, TARGET, and VALUE data
SOURCE = []
TARGET = []
VALUE = []


# Loop over each row in the table, skipping the first row (header)
for row in table[1:]:
    # Loop over each column in the row, skipping the first column (row label)
    for i, val in enumerate(row[1:]):
        # Append the row label (SOURCE), column header (TARGET), and VALUE to the appropriate lists
        SOURCE.append(row[0])
        TARGET.append(table[0][i+1])
        VALUE.append(val)

Number_of_Actual_Targets = i+1

# Create a list of all unique row and column LABELS
LABELS = table[0][1:] + [row[0] for row in table[1:]]

# Create dictionaries to map row and column LABELS to IDs
label_to_id = {label: i for i, label in enumerate(LABELS)}
row_to_id = {row[0]: label_to_id[row[0]] for row in table[1:]}
col_to_id = {col: label_to_id[col] for col in table[0][1:]}

# Create lists of IDs corresponding to the SOURCE and TARGET LABELS
SOURCE_ID = [row_to_id[label] for label in SOURCE]
TARGET_ID = [col_to_id[label] for label in TARGET]

# Create a list of label IDs
LABEL_ID = list(range(len(LABELS)))

# Print all lists
print('SOURCE:', SOURCE)
print('TARGET:', TARGET)
print('VALUE:', VALUE)
print('LABEL:', LABELS)
print('LABEL_ID:', LABEL_ID)
print('SOURCE_ID:', SOURCE_ID)
print('TARGET_ID:', TARGET_ID)

# %% Auto color
## Links Color
if Auto_Color > 2:
    COLOR_BANK = [
        '#f8a3a8', '#f3c6a5', '#e5e1ab', '#9cdcaa', '#96caf7', '#bfb2f3', 
        '#FCEE9E', '#92CEA8', '#F6C6C7', '#8BD2EC', '#c4c263',
        '#f94144', '#0057e9', '#ff00bd', '#87e911', '#f2ca19', '#8931ef', '#3498db', '#e11845', '#2ab7ca', '#7fdbda', '#011f4b', '#95a5a6', '#ff595e', '#48b1bf', '#c0392b', '#83c5be', '#f9c74f', '#90be6d', '#283149', '#a8e063', '#57506d', '#2c3e50', '#9ed2ff', '#f38b4a', '#006d77', '#fed766', '#023e8a', '#27ae60', '#bdc3c7', '#f3722c', '#34495e', '#f8961e', '#1b262c', '#2f4b7c', '#7f8c8d', '#e67e22', '#4ecdc4', '#0f4c5c', '#474787', '#a6dcef', '#0a2463', '#e74c3c', '#1abc9c', '#2980b9', '#ff6b6b', '#357ded', '#f1c40f', '#002d40', '#ff6b81', '#d35400', '#1e3799', '#5de5ff', '#283747', '#b71540', '#c8d6e5', '#fdcb6e', '#576574', '#ff9ff3', '#a29bfe', '#ff8c00', '#fd79a8', '#00b894', '#6c5ce7', '#ff7675', '#70a1ff', '#fab1a0', '#fd7272', '#1dd1a1', '#e84393', '#3c40c6', '#ffa502', '#ff6348', '#3742fa', '#fd79a8', '#2d3436', '#fdcb6e', '#8c7ae6', '#fd7272', '#74b9ff', '#feca57', '#7bed9f', '#6ab04c', '#e17055', '#e84393']

    n_colors = Number_of_Actual_Targets
    COLOR_LIST = []

    for i in range(n_colors):
        if i >= len(COLOR_BANK):
            COLOR_LIST.append(COLOR_BANK[i % len(COLOR_BANK)])
        else:
            COLOR_LIST.append(COLOR_BANK[i])

    No_Same_Color_Links = int(len(TARGET)/Number_of_Actual_Targets)        
    Links_Color = COLOR_LIST * No_Same_Color_Links

## Nodes Color
if Auto_Color == 0: # Gray Mode
        NODE_COLOR = Links_Color
elif Auto_Color == 1: # Black & Gray
        NODE_COLOR = []
elif Auto_Color == 2: # Just Box
    NODE_COLOR = Boxes_Color
elif Auto_Color == 3: # Color Target
    NODE_COLOR = COLOR_LIST

# %% Making Sankey Diagram
import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = Spacing,
      thickness = Nodes_Thickness,
      #line = dict(color = 'black', width = Links_Thickness),
      label = LABELS,
      #color = COLOR_LIST
      #color = Boxes_Color
      color = NODE_COLOR
    ),
    link = dict(
      source = SOURCE_ID, 
      target = TARGET_ID,
      value = VALUE,
      color = Links_Color
  ))])

fig.update_layout(title_text= Sankey_Diagram_Title , font_size= Font_Size)
fig.show()
