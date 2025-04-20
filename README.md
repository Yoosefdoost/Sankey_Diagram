
# 🔗 Sankey Diagram Generator

**Version:** 1.3.6  
**Author:** Arash Yoosefdoost

## 📘 Overview

This tool reads a CSV matrix of Source-Target relationships and generates a practical, colorful, and interactive Sankey diagram using Plotly. It is ideal for visualizing flows between categories like keyword trends, resource allocations, or system mappings.

---

## 🎯 Purpose

- Visually represent flows between different sources and targets.
- Perform keyword analysis or thematic distribution reviews.
- Simplify complex relationships in an intuitive, colorful way.

---

## 📥 Input

A CSV file like `INPUT.csv` with:
- Column headers: Targets
- Row headers: Sources
- Cell values: Flow amounts

Example:
```
,Target A,Target B
Source A,10,5
Source B,3,7
```

---

## 📤 Output

An interactive Sankey diagram launched in the browser with custom:
- Colors
- Link thickness
- Node spacing
- Labels and titles

---

## ⚙️ Parameters

You can adjust the following in the script:

```python
Sankey_Diagram_Title = 'Sankey Diagram'
Font_Size = 8
Auto_Color = 3  # Modes: 0 = Gray, 1 = Gray+Black, 2 = Custom Box, 3 = Colorful
Links_Thickness = 0.01
Nodes_Thickness = 25
Spacing = 15
```

---

## 💻 Usage

1. Install Plotly:
   ```bash
   pip install plotly
   ```

2. Place your CSV file in the same directory and ensure it matches the required format.

3. Run the script:
   ```bash
   python "Sankey Diagram.py"
   ```

---

## 📊 Custom Color Modes

- `Auto_Color = 0`: All links gray
- `Auto_Color = 1`: Black & gray
- `Auto_Color = 2`: All boxes same color
- `Auto_Color = 3`: Each target flow gets a unique color

