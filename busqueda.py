import requests

# Buscar pacientes por número de documento
def search_patient_by_document(document_number):
    url = f"http://hapi.fhir.org/baseR4/Patient?identifier=http://hospital.example.org/patients|{document_number}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        results = response.json()
        if results.get("entry"):
            print(f"Pacientes encontrados: {len(results['entry'])}")
            for entry in results['entry']:
                print(entry['resource'])
        else:
            print("No se encontró ningún paciente con ese documento.")
    else:
        print(f"Error en la búsqueda: {response.status_code}")
        print(response.json())
