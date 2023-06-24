import plantweb

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
    
    # Generate the UML diagram
    uml_code = plantweb.generate_uml(diagram_code, format='png')
    
    # Save the UML diagram to a file
    with open("uml_diagram.png", "wb") as file:
        file.write(uml_code)
    
    print("UML diagram generated and saved as uml_diagram.png")

# Generate the UML diagram
generate_uml_diagram()
