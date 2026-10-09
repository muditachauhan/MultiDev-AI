from agents.planner import PlannerAgent


planner = PlannerAgent()

requirement = """
Build a simple library management system where users can
add books, search for books, borrow books, and return books.
"""

plan = planner.create_plan(requirement)

print("\n===== PLANNER AGENT OUTPUT =====\n")
print(plan)