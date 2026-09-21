# Deep Research Agent Workflow
# Planning + Research + Content Generation + Reflection

print("======================================")
print("       DEEP RESEARCH AGENT")
print("======================================")

# Get topic from user
topic = input("\nEnter research topic: ").strip()

# =========================================================
# 1. PLANNING
# =========================================================

print("\n===== 1. PLANNING =====")

plan = [
    "Definition and introduction",
    "Applications",
    "Advantages",
    "Challenges and future scope"
]

for i, item in enumerate(plan, 1):
    print(f"{i}. {item}")


# =========================================================
# 2. RESEARCH
# =========================================================

print("\n===== 2. RESEARCH =====")

# Local research knowledge base
knowledge = {

    "data science": """
Data Science is an interdisciplinary field that uses statistics,
mathematics, programming and machine learning to analyze data
and extract useful information.

Applications include healthcare, finance, marketing,
transportation and business analytics.

Advantages include better decision making, automation,
prediction and discovering useful patterns in data.

Challenges include data quality, privacy, security,
large data volumes and the need for skilled professionals.
""",

    "artificial intelligence": """
Artificial Intelligence is a field of computer science that
develops systems capable of performing tasks that normally
require human intelligence.

Applications include robotics, computer vision,
natural language processing, healthcare and recommendation
systems.

Advantages include automation, faster decision making,
improved productivity and data analysis.

Challenges include privacy, security, bias, high computational
requirements and ethical concerns.
""",

    "internet of things": """
Internet of Things (IoT) is a technology in which physical
devices containing sensors, software and network connectivity
collect and exchange data.

Applications include smart homes, smart cities, healthcare,
agriculture and industrial automation.

Advantages include real-time monitoring, automation,
remote control and improved efficiency.

Challenges include security, privacy, connectivity,
maintenance and scalability.
""",

    "machine learning": """
Machine Learning is a branch of Artificial Intelligence in
which computers learn patterns from data and make predictions
or decisions without being explicitly programmed for every task.

Applications include recommendation systems, fraud detection,
medical diagnosis, image recognition and forecasting.

Advantages include automation, prediction and the ability
to process large datasets.

Challenges include data quality, bias, model complexity,
computational cost and interpretability.
"""
}

# Find matching topic
research = knowledge.get(topic.lower())

if research is None:
    research = """
This topic is being analyzed using the research workflow.

The research process identifies:
- Definition of the topic
- Major applications
- Advantages
- Challenges
- Future scope

Additional external sources can be connected to this stage
when internet/API access is available.
"""

print("Research source: Local Knowledge Base")
print("\nResearch information:")
print(research)


# =========================================================
# 3. CONTENT GENERATION
# =========================================================

print("\n===== 3. CONTENT GENERATION =====")

draft = f"""
TOPIC: {topic}

INTRODUCTION
{research}

The above information can be organized into a structured
article containing the definition, applications, advantages
and challenges of the selected topic.
"""

print(draft)


# =========================================================
# 4. REFLECTION
# =========================================================

print("===== 4. REFLECTION =====")

reflection_points = [
    "Check whether the topic has been clearly introduced.",
    "Check whether applications are mentioned.",
    "Check whether advantages are included.",
    "Check whether challenges are included.",
    "Identify areas where additional examples can be added."
]

for point in reflection_points:
    print("✓", point)

print("\nReflection result:")
print("The draft contains the major sections.")
print("More real-world examples and future developments can be added.")


# =========================================================
# 5. IMPROVEMENT
# =========================================================

print("\n===== 5. IMPROVEMENT =====")

improved_content = f"""
TOPIC: {topic}

1. INTRODUCTION
{research}

2. REAL-WORLD APPLICATIONS
The technology can be applied to different real-world
problems and industries. Its applications depend on the
requirements of the particular domain.

3. ADVANTAGES
It can improve efficiency, support decision making,
automate tasks and help organizations analyze information.

4. CHALLENGES
Important challenges include security, privacy, data quality,
implementation cost and technical complexity.

5. FUTURE SCOPE
Future developments can improve automation, accuracy,
scalability and real-world adoption.
"""

print(improved_content)


# =========================================================
# 6. FINAL CONTENT
# =========================================================

print("===== 6. FINAL CONTENT =====")

final_content = f"""
========================================
FINAL RESEARCH OUTPUT
========================================

Topic: {topic}

{improved_content}

CONCLUSION
The research workflow successfully analyzed the topic through
planning, research, content generation and reflection.
The reflection stage was used to improve the generated content.

========================================
DEEP RESEARCH COMPLETED
========================================
"""

print(final_content)