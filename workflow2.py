from device import create_device_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir

if _name_ == "_main_":
    # Datos del dispositivo
    identifier_value = "12345"
    device_type = "DIGITAL BLOOD PRESSURE MONITOR"
    manufacturer = "Omron"
    device_name = "HEM-401C"
    authority = "FDA"


    # Crear el recurso Device
    device = create_device_resource(identifier_value, device_type, manufacturer, device_name, authority)

    # Enviar el recurso al servidor HAPI FHIR
    device_id = send_resource_to_hapi_fhir(device, "Device")

    # Recuperar y mostrar el recurso creado
    if device_id:
        print(f"Recurso Device creado con ID: {device_id}")
        get_resource_from_hapi_fhir(device_id,"Device")
