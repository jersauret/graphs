from diagrams import Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.generic.blank import Blank

with Diagram("Custom Workflow Example", show=True):
    start = Blank("Start")
    web = ELB("Web Server")
    app = EC2("Application")
    db = RDS("Database")
    end = Blank("End")

    # Workflow connections
    start >> web >> app >> db >> end
