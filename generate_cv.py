import json

with open("../cv/cv.json") as f:
    cv = json.load(f)

print(f"""
{cv['name']}
{cv['role']}

Skills:
- {', '.join(cv['skills'])}

Experiência:
""")

for exp in cv["experience"]:
    print(f"- {exp['company']} | {exp['role']} → {exp['results']}")
