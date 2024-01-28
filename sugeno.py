import tkinter as tk
from tkinter import ttk
from skfuzzy import control as ctrl
import skfuzzy as fuzz
import numpy as np

def evaluate_kinerja():
    # Mengambil nilai dari entry widgets
    orientasi_value = float(orientasi_entry.get())
    integritas_value = float(integritas_entry.get())
    kedisiplinan_value = float(kedisiplinan_entry.get())
    kerjasama_value = float(kerjasama_entry.get())

    # Mengatur nilai input pada sistem fuzzy
    evaluasi_kinerja.input['orientasi_pelayanan'] = orientasi_value
    evaluasi_kinerja.input['integritas'] = integritas_value
    evaluasi_kinerja.input['kedisiplinan'] = kedisiplinan_value
    evaluasi_kinerja.input['kerjasama'] = kerjasama_value

    # Fuzzy Inference
    evaluasi_kinerja.compute()

    # Mendapatkan hasil evaluasi kinerja
    hasil_evaluasi = evaluasi_kinerja.output['kompeten']

    # Menampilkan hasil pada label
    hasil_label.config(text=f"Hasil Evaluasi Kinerja: {hasil_evaluasi:.2f}", font=('Arial', 13))

    # Menampilkan keterangan
    if hasil_evaluasi >= 70:
        keterangan_label.config(text="Pegawai Kompeten", font=('Arial', 13))
    elif hasil_evaluasi >= 50:
        keterangan_label.config(text="Pegawai Cukup Kompeten", font=('Arial', 13))
    else:
        keterangan_label.config(text="Pegawai Tidak Kompeten", font=('Arial', 13))

# Membuat antarmuka grafis menggunakan Tkinter
root = tk.Tk()
root.title("Evaluasi Kinerja Pegawai")

# Style GUI
style = ttk.Style()

# Background Frame
style.configure("TFrame", background="#97cdfc")

# Membuat frame utama
main_frame = ttk.Frame(root, style="TFrame", padding=(30, 20))
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Membuat input dan label untuk setiap variabel input
orientasi_label = ttk.Label(main_frame, text="Orientasi Pelayanan:", font=('Arial', 13),background="#97cdfc")
orientasi_label.grid(row=0, column=0, pady=10, sticky=tk.W) 
orientasi_entry = ttk.Entry(main_frame)
orientasi_entry.grid(row=0, column=1, pady=10, sticky=tk.W)

integritas_label = ttk.Label(main_frame, text="Integritas:", font=('Arial', 13),background="#97cdfc")
integritas_label.grid(row=1, column=0, pady=10, sticky=tk.W) 
integritas_entry = ttk.Entry(main_frame)
integritas_entry.grid(row=1, column=1, pady=10, sticky=tk.W)

kedisiplinan_label = ttk.Label(main_frame, text="Kedisiplinan:", font=('Arial', 13),background="#97cdfc")
kedisiplinan_label.grid(row=2, column=0, pady=10, sticky=tk.W) 
kedisiplinan_entry = ttk.Entry(main_frame)
kedisiplinan_entry.grid(row=2, column=1, pady=10, sticky=tk.W)

kerjasama_label = ttk.Label(main_frame, text="Kerjasama:", font=('Arial', 13),background="#97cdfc")
kerjasama_label.grid(row=3, column=0, pady=10, sticky=tk.W) 
kerjasama_entry = ttk.Entry(main_frame)
kerjasama_entry.grid(row=3, column=1, pady=10, sticky=tk.W)

# Tombol untuk mengevaluasi kinerja
evaluate_button = ttk.Button(main_frame, text="Evaluasi Kinerja", command=evaluate_kinerja)
evaluate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil evaluasi kinerja
hasil_label = ttk.Label(main_frame, text="Hasil Evaluasi Kinerja:", font=('Arial', 13),background="#97cdfc")
hasil_label.grid(row=5, column=0, columnspan=2, pady=5)

# Label untuk menampilkan keterangan
keterangan_label = ttk.Label(main_frame, text="",background="#97cdfc")
keterangan_label.grid(row=6, column=0, columnspan=2, pady=5)

# Fuzzyfikasi
orientasi_pelayanan = ctrl.Antecedent(np.arange(0, 101, 1), 'orientasi_pelayanan')
integritas = ctrl.Antecedent(np.arange(0, 101, 1), 'integritas')
kedisiplinan = ctrl.Antecedent(np.arange(0, 101, 1), 'kedisiplinan')
kerjasama = ctrl.Antecedent(np.arange(0, 101, 1), 'kerjasama')

kompeten = ctrl.Consequent(np.arange(0, 101, 1), 'kompeten')

# Fungsi keanggotaan
orientasi_pelayanan['tidak_baik'] = fuzz.trimf(orientasi_pelayanan.universe, [0, 0, 50])
orientasi_pelayanan['baik'] = fuzz.trimf(orientasi_pelayanan.universe, [0, 50, 100])
orientasi_pelayanan['sangat_baik'] = fuzz.trimf(orientasi_pelayanan.universe, [50, 100, 100])

integritas['tidak_baik'] = fuzz.trimf(integritas.universe, [0, 0, 50])
integritas['baik'] = fuzz.trimf(integritas.universe, [0, 50, 100])
integritas['sangat_baik'] = fuzz.trimf(integritas.universe, [50, 100, 100])

kedisiplinan['tidak_disiplin'] = fuzz.trimf(kedisiplinan.universe, [0, 0, 50])
kedisiplinan['disiplin'] = fuzz.trimf(kedisiplinan.universe, [0, 50, 100])
kedisiplinan['sangat_disiplin'] = fuzz.trimf(kedisiplinan.universe, [50, 100, 100])

kerjasama['tidak_bisa'] = fuzz.trimf(kerjasama.universe, [0, 0, 50])
kerjasama['bisa'] = fuzz.trimf(kerjasama.universe, [0, 50, 100])

kompeten['kompeten'] = fuzz.trimf(kompeten.universe, [70, 80, 100])
kompeten['cukup'] = fuzz.trimf(kompeten.universe, [63, 70, 70])
kompeten['tidak_kompeten'] = fuzz.trimf(kompeten.universe, [0, 0, 50])

# Rules 
rule1 = ctrl.Rule(orientasi_pelayanan['sangat_baik'] & integritas['sangat_baik'] & kedisiplinan['sangat_disiplin'] & kerjasama['bisa'], kompeten['kompeten'])
rule2 = ctrl.Rule(orientasi_pelayanan['baik'] & integritas['baik'] & kedisiplinan['disiplin'] & kerjasama['bisa'], kompeten['cukup']) 
rule3 = ctrl.Rule(orientasi_pelayanan['tidak_baik'] | integritas['tidak_baik'] | kedisiplinan['tidak_disiplin'] | kerjasama['tidak_bisa'], kompeten['tidak_kompeten'])

# Rule System 
evaluasi_kinerja_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
evaluasi_kinerja = ctrl.ControlSystemSimulation(evaluasi_kinerja_ctrl)

# Menjalankan loop utama Tkinter
root.mainloop()
