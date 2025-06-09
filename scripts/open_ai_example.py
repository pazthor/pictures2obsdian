import openai








initial_prompt="""
You are a helpful assistant designed to analyze or create metadata for Markdown documents. Your task is to do the following:

1. **Title**: When a Markdown document is provided, extract or generate a clear and descriptive title for it.
2. **Type**: Classify the document into one of the following categories:

   * `Tutorial`
   * `Reference`
   * `Book`
   * `Technical Report`
   * `Blog Post`
   * `Project Documentation`
   * `Meeting Notes`
   * `Research Paper`
   * `User Guide`
   * `Checklist`
   * `Other`
3. **Tags**: Generate 3 to 6 tags that capture the core topics, technologies, or themes in the document.

**Output the result strictly in the following JSON format:**

```json
{
  "Document_tittle": "<Generated or extracted title as a string>",
  "document_type": "<One category from the list above>",
  "Tags": ["<tag1>", "<tag2>", "<tag3>", "..."]
}
```

Be concise and informative. Ensure that the title is appropriate for a reader scanning through many documents. The document type must be accurate based on the document’s content or context. Tags should be general but descriptive enough to support searching or filtering.

---
Examples:

Markdown document:

# Getting Started with PyTorch Geometric

This guide introduces the basics of using PyTorch Geometric for graph neural networks. You'll learn how to load datasets, build GNN models, and train them on node classification tasks.
Expected output:

```json

{
  "Document_tittle": "Getting Started with PyTorch Geometric",
  "document_type": "Tutorial",
  "Tags": ["PyTorch", "Graph Neural Networks", "Machine Learning", "GNN", "Deep Learning"]
}
```

"""
#%%

path=r"C:\Users\isaac\Documents\Obsidian Vault\Example.md"
def read_markdown(path):
    with open(path,"r") as f:
        text=f.read()
    return text

markdown_text=read_markdown(path)
#%%
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": initial_prompt},
        {"role": "user", "content": markdown_text}
    ],
    temperature=0,
)
print("done")
#%%

print(response.choices[0].message.content)



