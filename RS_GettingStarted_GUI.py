import tkinter as tk
from connect import *

def create_gui():
    # 1. Pull data directly from the active RayStation environment
    patient = get_current("Patient")
    beam_set = get_current("BeamSet")

    examination = beam_set.GetPlanningExamination()
    pat_name = patient.Name
    pat_mrn = patient.PatientID
    img_name = examination.Name

    # Create a comma-separated string of all beam names in the active beam set
    beam_names = ", ".join([beam.Name for beam in beam_set.Beams])

    # 2. Initialize the Tkinter root window
    root = tk.Tk()
    root.title("Plan Review Summary")
    root.geometry("450x200")

    # Forces the pop-up to stay on top of the RayStation application window
    root.attributes("-topmost", True)

    # Define standard padding for clean alignment
    padx = 10
    pady = 8

    # 3. Build the grid layout (Row by Row)

    # Patient Name
    tk.Label(root, text="Patient Name:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="e", padx=padx,
                                                                          pady=pady)
    tk.Label(root, text=pat_name, font=("Arial", 10)).grid(row=0, column=1, sticky="w", padx=padx, pady=pady)

    # MRN
    tk.Label(root, text="MRN:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="e", padx=padx, pady=pady)
    tk.Label(root, text=pat_mrn, font=("Arial", 10)).grid(row=1, column=1, sticky="w", padx=padx, pady=pady)

    # Planning Image
    tk.Label(root, text="Planning Image:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="e", padx=padx,
                                                                            pady=pady)
    tk.Label(root, text=img_name, font=("Arial", 10)).grid(row=2, column=1, sticky="w", padx=padx, pady=pady)

    # Beam Names
    tk.Label(root, text="Beam Names:", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="e", padx=padx,
                                                                        pady=pady)
    tk.Label(root, text=beam_names, font=("Arial", 10)).grid(row=3, column=1, sticky="w", padx=padx, pady=pady)

    # 4. Add an exit button
    tk.Button(root, text="Close Window", command=root.destroy, width=15).grid(row=4, column=0, columnspan=2, pady=15)

    # Execute the GUI loop
    root.mainloop()


if __name__ == "__main__":
    create_gui()