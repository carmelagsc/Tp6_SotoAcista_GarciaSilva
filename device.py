from fhir.resources.device import Device
from fhir.resources.identifier import Identifier

# Crear un recurso Device
def create_device_resource(identifier_value, device_type, manufacturer, device_name):
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

    return device
