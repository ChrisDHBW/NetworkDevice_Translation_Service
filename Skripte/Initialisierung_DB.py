import mysql.connector

# Verbindung zur MySQL-Datenbank herstellen
connection = mysql.connector.connect(
    host="localhost",
    user="dbAdmin",
    password="translation",
    database="TranslationServiceDB"
)

cursor = connection.cursor()

# Tabellen erstellen
tables = {
    "Hersteller": """
        CREATE TABLE Hersteller (
            ID INT PRIMARY KEY,
            Name CHAR(255)
        )
    """,
    "Betriebssysteme": """
        CREATE TABLE Betriebssysteme (
            ID INT PRIMARY KEY,
            HerstellerID INT,
            Name CHAR(255),
            FOREIGN KEY (HerstellerID) REFERENCES Hersteller(ID)
        )
    """,
    "SwitchSerie": """
        CREATE TABLE SwitchSerie (
            ID INT PRIMARY KEY,
            HerstellerID INT,
            Name CHAR(255),
            Nummer INT,
            FOREIGN KEY (HerstellerID) REFERENCES Hersteller(ID)
        )
    """,
    "SwitchModel": """
        CREATE TABLE SwitchModel (
            ID INT PRIMARY KEY,
            SwitchSerieID INT,
            ProductNumber CHAR(255),
            Identifier CHAR(255),
            Airflow CHAR(3),
            Type CHAR(10),
            PowerSupplies INT,
            FanTrays INT,
            PoEBudget INT,
            FOREIGN KEY (SwitchSerieID) REFERENCES SwitchSerie(ID)
        )
    """,
    "APSerie": """
        CREATE TABLE APSerie (
            ID INT PRIMARY KEY,
            HerstellerID INT,
            Name CHAR(255),
            Type CHAR(255),
            Usage CHAR(255),
            Density CHAR(255),
            WLAN_Standard CHAR(255),
            Nummer INT,
            FOREIGN KEY (HerstellerID) REFERENCES Hersteller(ID)
        )
    """,
    "APModel": """
        CREATE TABLE APModel (
            ID INT PRIMARY KEY,
            APSerieID INT,
            Identifier CHAR(255),
            ProductNumber CHAR(255),
            AntennaType CHAR(255),
            PoEConsume INT,
            PoEDelivery INT,
            FOREIGN KEY (APSerieID) REFERENCES APSerie(ID)
        )
    """,
    "ControllerSerie": """
        CREATE TABLE ControllerSerie (
            ID INT PRIMARY KEY,
            HerstellerID INT,
            Name CHAR(255),
            Type CHAR(255),
            FOREIGN KEY (HerstellerID) REFERENCES Hersteller(ID)
        )
    """,
    "Controller": """
        CREATE TABLE Controller (
            ID INT PRIMARY KEY,
            ControllerSerieID INT,
            ProductNumber CHAR(255),
            Identifier CHAR(255),
            UsageClass CHAR(255),
            DensityClass CHAR(255),
            FOREIGN KEY (ControllerSerieID) REFERENCES ControllerSerie(ID)
        )
    """,
    "Interfaces": """
        CREATE TABLE Interfaces (
            ID INT PRIMARY KEY,
            Type CHAR(255),
            MacSecAmount INT,
            MacSecSpeed CHAR(255),
            Speeds CHAR(255),
            Amount INT,
            PoE_Class CHAR(255),
            PoE_Delivery_Class CHAR(255),
            Usage_Class CHAR(255)
        )
    """,
    "Modul": """
        CREATE TABLE Modul (
            ID INT PRIMARY KEY,
            SwitchModelID INT,
            Identifier CHAR(255),
            Type CHAR(255),
            PoEBudget INT,
            FOREIGN KEY (SwitchModelID) REFERENCES SwitchModel(ID)
        )
    """,
    "Kapazitäten": """
        CREATE TABLE Kapazitäten (
            ID INT PRIMARY KEY,
            ControllerID INT,
            BetriebssystemID INT,
            APCapacity INT,
            ClientCapacity INT,
            MaxClusterSize INT,
            FOREIGN KEY (ControllerID) REFERENCES Controller(ID),
            FOREIGN KEY (BetriebssystemID) REFERENCES Betriebssysteme(ID)
        )
    """,
    "Transceiver": """
        CREATE TABLE Transceiver (
            ID INT PRIMARY KEY,
            InterfaceID INT,
            ProductNumber CHAR(255),
            Type CHAR(255),
            ConnectorType CHAR(255),
            LWLMode CHAR(255),
            MaxRange INT,
            FOREIGN KEY (InterfaceID) REFERENCES Interfaces(ID)
        )
    """,
    "L2_Features": """
        CREATE TABLE L2_Features (
            ID INT PRIMARY KEY,
            STP BOOL,
            PVST BOOL,
            RSTP BOOL,
            RPSTP BOOL,
            MSTP BOOL,
            VLAN_Max_Count INT,
            Jumbo_Frames BOOL,
            802_1q BOOL,
            802_3ad BOOL,
            802_3az BOOL,
            IGMP_Snooping BOOL,
            ERPS BOOL,
            PFC BOOL,
            DCBX BOOL,
            ECN BOOL,
            CDP BOOL
        )
    """,
    "L3_Features": """
        CREATE TABLE L3_Features (
            ID INT PRIMARY KEY,
            StaticRouting BOOL,
            IPv4 BOOL,
            IPv6 BOOL,
            RIPv1 BOOL,
            RIPv2 BOOL,
            RIPNG BOOL,
            OSPFv2 BOOL,
            OSPFv3 BOOL,
            BGP BOOL,
            MPBGP BOOL,
            QOS BOOL,
            QOS_Max_Queues INT,
            LoopbackInterfaces BOOL,
            VRRP BOOL,
            ECMP BOOL,
            VRF BOOL,
            BFD BOOL,
            PBR BOOL,
            ARP BOOL,
            ICMP BOOL,
            mDNS BOOL,
            RouteMaps BOOL
        )
    """,
    "L4_Features": """
        CREATE TABLE L4_Features (
            ID INT PRIMARY KEY,
            TCP BOOL,
            UDP BOOL,
            VXLAN BOOL,
            EVPN BOOL
        )
    """,
    "L7_Features": """
        CREATE TABLE L7_Features (
            ID INT PRIMARY KEY,
            DHCP BOOL,
            DHCP_Relay BOOL,
            DHCP_Server BOOL,
            DNS BOOL,
            TFTP BOOL,
            SFTP BOOL,
            NTP BOOL,
            PTP BOOL
        )
    """,
    "Security_Features": """
        CREATE TABLE Security_Features (
            ID INT PRIMARY KEY,
            Radius BOOL,
            Tacacs BOOL,
            TacacsPlus BOOL,
            ACLv4 BOOL,
            ACLv6 BOOL,
            802_1x_Auth BOOL,
            802_1x_Supplicant BOOL,
            Arp_Inspection BOOL,
            STP_Root_Guard BOOL,
            STP_BPDU_Guard BOOL
        )
    """,
    "Physics": """
        CREATE TABLE Physics (
            ID INT PRIMARY KEY,
            Height INT,
            Width INT,
            Depth INT,
            Weight INT,
            Min_Temp INT,
            Max_Temp INT
        )
    """
}

# Tabellen in der Datenbank erstellen
for table_name, table_sql in tables.items():
    cursor.execute(table_sql)
    print(f"Tabelle '{table_name}' erfolgreich erstellt.")

# Verbindung schließen
cursor.close()
connection.close()