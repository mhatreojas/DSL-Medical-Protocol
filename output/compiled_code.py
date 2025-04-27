# Auto-generated compiled protocol

from runtime import administer, alert

def run_protocol(patient_data):
    if patient_data['OxygenSaturation'] < 94:
        administer('Oxygen', '2L/min')

    if patient_data['Fever'] > 38:
        administer('Paracetamol', '500mg')

    if patient_data['HeartRate'] > 120:
        alert('Cardiologist')

    if patient_data['BloodPressure'] < 90:
        administer('Saline', '500ml')

