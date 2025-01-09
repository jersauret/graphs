from diagrams import Diagram, Cluster, Edge
from diagrams.aws.storage import Backup
from diagrams.generic.database import SQL
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.onprem.analytics import Tableau
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Nginx
from diagrams.programming.language import Python

with Diagram("Organisation du SI de K-ElectroniK", show=True, direction="TB"):
    # Utilisateurs
    clients = Users("Clients")
    entrepots = Users("Entrepôts")
    prod_teams = Users("Équipes production")
    marketing = Users("Marketing")
    madrid_team = Users("Équipe Madrid")

    # Systèmes actuels
    with Cluster("Systèmes existants"):
        with Cluster("Applications métiers"):
            order_mgmt = Server("Gestion des commandes")
            client_mgmt = Server("Gestion des clients (CRM basique)")
            prod_planning = Server("Planning de production (obsolète)")
            e_commerce = Nginx("Site e-commerce")
            excel_tools = Tableau("Tableaux Excel avec macros")
            dashboards = Tableau("Tableaux de bord (Excel)")

        with Cluster("Infrastructure"):
            onprem_servers = Server("Serveurs internes")
            backups = Backup("Sauvegardes hebdomadaires")

        with Cluster("ERP SaaS"):
            erp = Tableau("ERP RH & Finance (SaaS)")

    # Nouveaux besoins
    with Cluster("Nouvelle entité à Madrid"):
        madrid_legacy = Server("Systèmes Madrid (obsolètes)")

    with Cluster("Projets et synergies à venir"):
        crm = Server("CRM amélioré")
        campaign_tool = Server("Outil de campagnes marketing")
        data_integration = Python("Intégration des données")
        unified_branding = Docker("Refonte marque & SI unifié")

    # Relations
    clients >> e_commerce
    entrepots >> order_mgmt >> prod_planning >> prod_teams
    prod_planning >> excel_tools >> dashboards
    client_mgmt >> dashboards
    marketing >> crm >> campaign_tool
    crm >> data_integration
    madrid_team >> madrid_legacy >> data_integration
    data_integration >> unified_branding
    backups >> onprem_servers >> [order_mgmt, client_mgmt, prod_planning]
    erp >> [dashboards, backups]

    # Représentation des entrepôts et flux internationaux
    with Cluster("Flux internationaux"):
        suppliers = Users("Fournisseurs (Asie)")
        madrid_warehouse = Users("Entrepôt Madrid")
        production = Users("Production & Personnalisation")
        suppliers >> madrid_warehouse >> production >> entrepots
