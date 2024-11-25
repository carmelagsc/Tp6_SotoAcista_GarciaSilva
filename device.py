import requests
from fhir.resources.device import Device
from fhir.resources.identifier import Identifier
from fhir.resources.extension import Extension

def check_device_approval_fda(device_name):
    """
    Consulta la API pública de OpenFDA y verifica si un dispositivo coincide exactamente con el nombre buscado.
    """
    api_url = f"https://api.fda.gov/device/510k.json?search=device_name:{device_name}&limit=5"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if "results" in data:
                print(f"Dispositivos encontrados para '{device_name}':")
                for result in data["results"]:
                    # Mostrar todos los resultados
                    print(f"- Nombre: {result.get('device_name')}")
                    print(f"  Número de aprobación: {result.get('k_number')}")
                    print(f"  Fecha de decisión: {result.get('decision_date')}\n")

                    # Verificar si el nombre coincide exactamente
                    if result.get("device_name").lower() == device_name.lower():
                        print(f"¡Coincidencia exacta encontrada para {device_name}!")
                        return True
                return False  # No hay coincidencias exactas
            else:
                print(f"No se encontraron dispositivos con el nombre '{device_name}' en la base de datos de FDA.")
                return False
        else:
            print(f"Error al consultar la API: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error al conectar con la API: {str(e)}")
        return False


# Función para crear el recurso FHIR de tipo Device
def create_device_resource(identifier_value, device_type, manufacturer, device_name, authority):
    """
    Crea un recurso FHIR de tipo Device, incluyendo información sobre su aprobación.
    """
    # Verificar la aprobación del dispositivo utilizando la API de OpenFDA
    is_approved = check_device_approval_fda(device_name)

    # Crear el recurso Device
    device = Device()

    # Agregar identificador
    identifier = Identifier()
    identifier.use = "official"
    identifier.value = identifier_value
    device.identifier = [identifier]

    # Agregar tipo de dispositivo
    device.type = {"text": device_type}

    # Agregar fabricante
    device.manufacturer = manufacturer

    # Agregar el nombre del dispositivo
    device.deviceName = [{"name": device_name, "type": "model-name"}]

    # Agregar una extensión con el resultado de la verificación
    approval_extension = Extension(
        url="http://example.org/fhir/StructureDefinition/device-approval",
        extension=[
            {"url": "approval-status", "valueString": "aprobado" if is_approved else "no aprobado"},
            {"url": "approval-authority", "valueString": authority}
        ]
    )
    device.extension = [approval_extension]

    return device