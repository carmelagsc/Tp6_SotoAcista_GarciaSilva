from device import create_device_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir


if __name__ == "__main__":
    # Crear y enviar un recurso Device
    device = create_device_resource("12345", "Monitor de presión arterial", "Omron", "HEM-7120")
    device_id = send_resource_to_hapi_fhir(device, 'Device')

    # Leer el recurso creado
    if device_id:
        get_resource_from_hapi_fhir(device_id, 'Device')
