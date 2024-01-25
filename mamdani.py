# Import Library
from matplotlib import pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import ttk

# Fuzzy Variables
ujian_nasional = ctrl.Antecedent(np.arange(0, 41, 1), 'Ujian Nasional')
nilai_raport = ctrl.Antecedent(np.arange(0, 101, 1), 'Nilai Raport')
ujian_tulis = ctrl.Antecedent(np.arange(0, 101, 1), 'Ujian Tulis')
tes_psikologi = ctrl.Antecedent(np.arange(0, 101, 1), 'Tes Psikologi')
tes_wawancara = ctrl.Antecedent(np.arange(0, 101, 1), 'Tes Wawancara')
kelulusan = ctrl.Consequent(np.arange(0, 101, 1), 'Kelulusan')

# Membership Functions
ujian_nasional['Rendah'] = fuzz.trimf(ujian_nasional.universe, [0, 10, 20])
ujian_nasional['Sedang'] = fuzz.trimf(ujian_nasional.universe, [15, 22, 29])
ujian_nasional['Tinggi'] = fuzz.trimf(ujian_nasional.universe, [25, 35, 40])

nilai_raport['Rendah'] = fuzz.trimf(nilai_raport.universe, [0, 55, 65])
nilai_raport['Sedang'] = fuzz.trimf(nilai_raport.universe, [60, 72, 85])
nilai_raport['Tinggi'] = fuzz.trimf(nilai_raport.universe, [75, 88, 100])

ujian_tulis['Rendah'] = fuzz.trimf(ujian_tulis.universe, [0, 50, 60])
ujian_tulis['Sedang'] = fuzz.trimf(ujian_tulis.universe, [55, 75, 85])
ujian_tulis['Tinggi'] = fuzz.trimf(ujian_tulis.universe, [75, 88, 100])

tes_psikologi['Kurang'] = fuzz.trimf(tes_psikologi.universe, [0, 65, 75])
tes_psikologi['Baik'] = fuzz.trimf(tes_psikologi.universe, [70, 75, 100])

tes_wawancara['Kurang'] = fuzz.trimf(tes_wawancara.universe, [0, 65, 75])
tes_wawancara['Baik'] = fuzz.trimf(tes_wawancara.universe, [70, 80, 100])

kelulusan['Tidak Lulus'] = fuzz.trimf(kelulusan.universe, [0, 52, 70])
kelulusan['Lulus'] = fuzz.trimf(kelulusan.universe, [60, 75, 100])

# Rules-Based System
rule1 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Rendah'] & ujian_tulis['Rendah'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule2 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Rendah'] & ujian_tulis['Rendah'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule3 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Rendah'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule4 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Rendah'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule5 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Rendah'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule6 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Rendah'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule7 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Rendah'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule8 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Rendah'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule9 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Rendah'] & ujian_tulis['Tinggi'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule10 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Rendah'] & ujian_tulis['Tinggi'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule11 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Rendah'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule12 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Rendah'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule13 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Rendah'] & ujian_tulis['Tinggi'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule14 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Sedang'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule15 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule16 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule17 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule18 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Sedang'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule19 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Sedang'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule20 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Sedang'] & ujian_tulis['Tinggi'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule21 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Sedang'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule22 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Sedang'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule23 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Sedang'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule24 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule25 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Tinggi'] & ujian_tulis['Tinggi'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule26 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Tinggi'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule27 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Tinggi'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule28 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Tinggi'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule29 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Tinggi'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule30 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Tinggi'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule31 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Tinggi'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule32 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Tinggi'] & ujian_tulis['Tinggi'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule33 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Tinggi'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule34 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Tinggi'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule35 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Tinggi'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule36 = ctrl.Rule(ujian_nasional['Rendah'] & nilai_raport['Tinggi'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule37 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Rendah'] & ujian_tulis['Rendah'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule38 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Rendah'] & ujian_tulis['Rendah'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule39 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Rendah'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule40 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Rendah'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule41 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Rendah'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule42 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Rendah'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule43 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Rendah'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule44 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Rendah'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule45 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Rendah'] & ujian_tulis['Tinggi'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule46 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Rendah'] & ujian_tulis['Tinggi'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule47 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Rendah'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule48 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Rendah'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule49 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule50 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule51 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule52 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule53 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule54 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule55 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule56 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule57 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Tinggi'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule58 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule59 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule60 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule61 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule62 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule63 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Tinggi'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule64 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Tinggi'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule65 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Tinggi'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule66 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Tinggi'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule67 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Tinggi'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule68 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Tinggi'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule69 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Tinggi'] & ujian_tulis['Tinggi'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule70 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Tinggi'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule71 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Tinggi'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule72 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Tinggi'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule73 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Tinggi'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule74 = ctrl.Rule(ujian_nasional['Sedang'] & nilai_raport['Tinggi'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule75 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Rendah'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule76 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Rendah'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule77 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Rendah'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule78 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Rendah'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule79 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Rendah'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule80 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Rendah'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule81 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Rendah'] & ujian_tulis['Tinggi'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule82 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Rendah'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule83 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Rendah'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Tidak Lulus'])
rule84 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Rendah'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule85 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Rendah'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule86 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Rendah'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Tidak Lulus'])
rule87 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Sedang'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule88 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule89 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule90 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule91 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Sedang'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule92 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Sedang'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule93 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Sedang'] & ujian_tulis['Tinggi'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule94 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Sedang'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule95 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Sedang'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule96 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Sedang'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule97 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Sedang'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule98 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Sedang'] & ujian_tulis['Rendah'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule99 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Tinggi'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule100 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Tinggi'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule101 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Tinggi'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule102 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Tinggi'] & ujian_tulis['Sedang'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule103 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Tinggi'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule104 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Tinggi'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule105 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Tinggi'] & ujian_tulis['Tinggi'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule106 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Tinggi'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule107 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Tinggi'] & ujian_tulis['Rendah'] & tes_psikologi['Baik'] & tes_wawancara['Baik'], kelulusan['Lulus'])
rule108 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Tinggi'] & ujian_tulis['Tinggi'] & tes_psikologi['Baik'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule109 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Tinggi'] & ujian_tulis['Sedang'] & tes_psikologi['Kurang'] & tes_wawancara['Kurang'], kelulusan['Lulus'])
rule110 = ctrl.Rule(ujian_nasional['Tinggi'] & nilai_raport['Tinggi'] & ujian_tulis['Rendah'] & tes_psikologi['Kurang'] & tes_wawancara['Baik'], kelulusan['Lulus'])

# Control System
kelulusan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50,
                                    rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69, rule70, rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81, rule82, rule83, rule84, rule85, rule86, rule87, rule88, rule89, rule90, rule91, rule92, rule93, rule94, rule95, rule96, rule97, rule98, rule99,
                                    rule100, rule101, rule102, rule103, rule104, rule105, rule106, rule107, rule108, rule109, rule110])
kelulusan_system = ctrl.ControlSystemSimulation(kelulusan_ctrl)

# GUI Functions
def calculate_kelulusan():
    # Get input values from the user
    ujian_nasional_input = float(ujian_nasional_entry.get().replace(',', '.'))
    nilai_raport_input = float(nilai_raport_entry.get().replace(',', '.'))
    ujian_tulis_input = float(ujian_tulis_entry.get().replace(',', '.'))
    tes_psikologi_input = float(tes_psikologi_entry.get().replace(',', '.'))
    tes_wawancara_input = float(tes_wawancara_entry.get().replace(',', '.'))

    # Set input values in the kelulusan system
    kelulusan_system.input['Ujian Nasional'] = ujian_nasional_input
    kelulusan_system.input['Nilai Raport'] = nilai_raport_input
    kelulusan_system.input['Ujian Tulis'] = ujian_tulis_input
    kelulusan_system.input['Tes Psikologi'] = tes_psikologi_input
    kelulusan_system.input['Tes Wawancara'] = tes_wawancara_input

    # Crunch the numbers
    kelulusan_system.compute()

    # Calculate kelulusan status
    hasil_kelulusan = kelulusan_system.output['Kelulusan']
    tidak_lulus_membership = fuzz.interp_membership(kelulusan.universe, kelulusan['Tidak Lulus'].mf, hasil_kelulusan)
    lulus_membership = fuzz.interp_membership(kelulusan.universe, kelulusan['Lulus'].mf, hasil_kelulusan)

    # Display the result
    result_label.config(text=f"Hasil Kelulusan: {hasil_kelulusan}")
    if lulus_membership > tidak_lulus_membership:
        result_status.config(text="Selamat, Anda Lulus!")
    else:
        result_status.config(text="Maaf, Anda Tidak Lulus.")

# Create main window
window = tk.Tk()
window.title("Sistem Kelulusan")
window.configure(background='#e6e6e6')

# Create input fields
ujian_nasional_label = ttk.Label(window, text="Nilai Ujian Nasional (0-40):", font=('Arial', 10), background='#e6e6e6')
ujian_nasional_entry = ttk.Entry(window)
nilai_raport_label = ttk.Label(window, text="Nilai Raport (0-100):", font=('Arial', 10), background='#e6e6e6')
nilai_raport_entry = ttk.Entry(window)
ujian_tulis_label = ttk.Label(window, text="Nilai Ujian Tulis (0-100):", font=('Arial', 10), background='#e6e6e6')
ujian_tulis_entry = ttk.Entry(window)
tes_psikologi_label = ttk.Label(window, text="Nilai Tes Psikologi (0-100):", font=('Arial', 10), background='#e6e6e6')
tes_psikologi_entry = ttk.Entry(window)
tes_wawancara_label = ttk.Label(window, text="Nilai Tes Wawancara (0-100):", font=('Arial', 10), background='#e6e6e6')
tes_wawancara_entry = ttk.Entry(window)

# Create calculate button
calculate_button = ttk.Button(window, text="Hitung Kelulusan", command=calculate_kelulusan, style='TButton')

# Create result labels
result_label = ttk.Label(window, text="Hasil Kelulusan:", font=('Helvetica', 12, 'bold'), background='#e6e6e6')
result_status = ttk.Label(window, text="")

# Grid layout
ujian_nasional_label.grid(row=0, column=0, padx=10, pady=10)
ujian_nasional_entry.grid(row=0, column=1, padx=10, pady=10)
nilai_raport_label.grid(row=1, column=0, padx=10, pady=10)
nilai_raport_entry.grid(row=1, column=1, padx=10, pady=10)
ujian_tulis_label.grid(row=2, column=0, padx=10, pady=10)
ujian_tulis_entry.grid(row=2, column=1, padx=10, pady=10)
tes_psikologi_label.grid(row=3, column=0, padx=10, pady=10)
tes_psikologi_entry.grid(row=3, column=1, padx=10, pady=10)
tes_wawancara_label.grid(row=4, column=0, padx=10, pady=10)
tes_wawancara_entry.grid(row=4, column=1, padx=10, pady=10)
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)
result_label.grid(row=6, column=0, columnspan=2, pady=10)
result_status.grid(row=7, column=0, columnspan=2, pady=10)

# Run the main loop
window.mainloop()