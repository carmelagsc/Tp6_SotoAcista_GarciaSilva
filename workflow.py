from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir
from busqueda import search_patient_by_document

if __name__ == "__main__":
    # Parámetros del paciente (se puede dejar algunos vacíos)
    family_name = "Mouse"
    given_name = "Mini"
    document_number = "49535470"
    birth_date = "1990-01-01"
    gender = "female"
    phone = None 

    while True:
        print("\n")
        print("Seleccione una opción:")
        print("1. Crear un nuevo paciente")
        print("2. Buscar un paciente por DNI")
        print("3. Salir")
        option = input("Ingrese el número de la opción seleccionada: ")

        if option == "1":
            # Crear y enviar el recurso de paciente
            patient = create_patient_resource(family_name, given_name, document_number, birth_date, gender, phone)
            patient.identifier = [{"use": "official", "system": "http://hospital.example.org/patients", "value": document_number}]
            patient_id = send_resource_to_hapi_fhir(patient, 'Patient')

            print("\n")
            # Ver el recurso de paciente creado
            if patient_id:
                get_resource_from_hapi_fhir(patient_id,'Patient')
                print("\n")

        elif option == "2":
            # Buscar paciente por DNI
            dni_to_search = input("Ingrese el DNI del paciente a buscar: ")
            search_patient_by_document(dni_to_search)

        elif option == "3":
            print("Saliendo del progrma.")
            break


        else:
            print("Opción no válida. Intente nuevamente.")