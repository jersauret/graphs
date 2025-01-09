from diagrams import Diagram, Edge
from diagrams.generic.blank import Blank
from diagrams.generic.place import Datacenter

with Diagram("Workflow Chart Example", show=True):
    start = Blank("Start")
    task1 = Datacenter("Task 1")
    decision = Blank("Decision")
    task2 = Datacenter("Task 2")
    task3 = Datacenter("Task 3")
    end = Blank("End")

    # Define the workflow
    start >> task1 >> decision
    decision >> Edge(label="Yes") >> task2 >> end
    decision >> Edge(label="No") >> task3 >> end
