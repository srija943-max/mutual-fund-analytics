import os
from pathlib import Path

print("Creating exact folder structure based on Evaluation Rubric...")

# Create required directories
directories = [
    "data/raw",
    "data/processed",
    "data/db",
    "notebooks",
    "scripts",
    "sql",
    "dashboard",
    "reports"
]

for d in directories:
    os.makedirs(d, exist_ok=True)

# Update .gitignore to avoid committing .db files (as per evaluation guidelines)
gitignore_content = """# Data files
*.db
*.sqlite
data/db/*.db

# Python cache
__pycache__/
*.py[cod]

# Environment
.env
venv/
"""

with open(".gitignore", "w") as f:
    f.write(gitignore_content)

print("✓ Folder structure created & .gitignore updated!")