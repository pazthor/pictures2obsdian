import requests

markdown_text = """# Getting Started with PyTorch Geometric

This guide introduces the basics of using PyTorch Geometric for graph neural networks. 
You'll learn how to load datasets, build GNN models, and train them on node classification tasks.
"""

url = "http://localhost:8000/markdown/analyze"

response = requests.post(
    url,
    json={"markdown_text": markdown_text}
)


result = response.json()
print("Status:", result["status"])
print("Content:", result["content"])
