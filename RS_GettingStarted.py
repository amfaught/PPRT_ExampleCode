# Connect w/ the RayStation API
from connect import *

# For making GUIs
import tkinter as tk

patient = get_current('Patient')
case = get_current('Case')
beam_set = get_current('BeamSet')

# Print the information to screen
print('Patient Name: {name_variable}\n'.format(name_variable=patient.Name))
print('Patient MRN: {mrn_variable}\n'.format(mrn_variable=patient.PatientID))
print('Planning Image: {exam_name}\n'.format(exam_name=beam_set.GetPlanningExamination().Name))
for beam in beam_set.Beams:
    print('{beam_name}: {mu_in_beam} MU\n'.format(beam_name=beam.Name, mu_in_beam=beam.BeamMU))

# Write information to file
with open("output_file.txt", "w", encoding="utf-8") as file:
    file.write('Patient Name: {name_variable}\n'.format(name_variable=patient.Name))
    file.write('Patient MRN: {mrn_variable}\n'.format(mrn_variable=patient.PatientID))
    file.write('Planning Image: {exam_name}\n'.format(exam_name=beam_set.GetPlanningExamination().Name))
    for beam in beam_set.Beams:
        file.write('{beam_name}: {mu_in_beam} MU\n'.format(beam_name=beam.Name, mu_in_beam=beam.BeamMU))