import json

def get_patient_details():
    """Function to get patient details from the user"""
    patient_details = {}
    print("Enter patient details:")
    patient_details['name'] = input("Name: ")
    patient_details['age'] = int(input("Age: "))
    patient_details['condition'] = input("Condition: ")
    patient_details['symptoms'] = input("Symptoms (comma-separated): ").split(',')

    return patient_details

def analyze_patient_data(patient_details):
    """Function to analyze patient data and generate a report"""
    report = {
        "Patient Name": patient_details['name'],
        "Age": patient_details['age'],
        "Condition": patient_details['condition'],
        "Symptoms": ', '.join(patient_details['symptoms']),
        "Recommendations": generate_recommendations(patient_details['condition'])
    }
    return report

def generate_recommendations(condition):
    """Function to generate recommendations based on the patient's condition"""
    recommendations = {
        "Flu": "Rest and hydration. Consider over-the-counter medications.",
        "Diabetes": "Monitor blood sugar levels. Follow dietary recommendations.",
        "Hypertension": "Reduce salt intake. Regular exercise is recommended."
    }
    return recommendations.get(condition, "Consult a specialist for further advice.")

def generate_report(report):
    """Function to print the report in a formatted manner"""
    print("\n--- Patient Report ---")
    for key, value in report.items():
        print(f"{key}: {value}")
    print("-----------------------")

def main():
    """Main function to run the application"""
    patient_details = get_patient_details()
    report = analyze_patient_data(patient_details)
    generate_report(report)

if __name__ == "__main__":
    main()
