from medical import Patient, Procedure

def main():
	Patient.load_patients()
	print(Patient.all_patients)
	# Main menu loop
	patients = None
	while True:
		print("\nMenu:")
		print("1. Look up a patient by ID number")
		print("2. Add a new patient")
		print("3. Quit")

		choice = input("Enter your choice: ")

		if choice == '1':
			# Look up a patient by ID number
			patient_id = int(input("Enter patient ID number: "))
			patient = Patient.get_patient(patient_id)
			if patient:
				print("Patient found:")
				print(patient.__str__())
			else:
				print("Patient not found.")

		elif choice == '2':
			# Add a new patient
			first_name = input("Enter patient's first name: ")
			last_name = input("Enter patient's last name: ")
			address = input("Enter patient's address: ")
			phone = input("Enter patient's phone number: ")
			emergency_contact_name = input("Enter emergency contact name: ")
			emergency_contact_phone = input("Enter emergency contact phone number: ")
			patients = Patient(first_name, last_name, address, phone, emergency_contact_name, emergency_contact_phone)
			print(patients.all_patients)
			print("Patient added successfully.")

		elif choice == '3':
			# Quit the program
			if patients:
				patients.save_patients()	
			print("Exiting program.")
			break

		else:
			print("Invalid choice. Please enter a valid option.")
main()
