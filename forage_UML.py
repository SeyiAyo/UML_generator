import plantuml

def generate_uml_diagram():
    diagram_code = """
    @startuml
    
    class Car {
        - carModel: string
        - engineType: Engine
        - batteryType: Battery
        - serviceCriteria: ServiceCriteria
    }
    
    class Engine {
        - engineType: string
        - serviceCriteria: ServiceCriteria
    }
    
    class Battery {
        - batteryType: string
        - serviceCriteria: ServiceCriteria
    }
    
    class ServiceCriteria {
        - criteriaDescription: string
    }
    
    Car "1" --> "1" Engine
    Car "1" --> "1" Battery
    Engine "1" --> "1" ServiceCriteria
    Battery "1" --> "1" ServiceCriteria
    
    @enduml
    """
    
    # Specify the PlantUML server URL
    url = "http://www.plantuml.com/plantuml"
    
    # Generate the UML diagram and save it to a file
    with open("uml_diagram.pu", "w") as file:
        file.write(diagram_code)
    
    plantuml.PlantUML(url).processes_file("uml_diagram.pu", "uml_diagram.png")

# Generate the UML diagram
generate_uml_diagram()
