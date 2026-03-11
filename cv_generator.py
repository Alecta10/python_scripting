import customtkinter as ctk
from tkinter import messagebox
import yaml
import os

# Variables para que cualquiera pueda cambiar los datos que son fijos facilmente
headline='Android Developer | Cybersecurity'
nombre='nombre completo'
location='lugar de residencia'
email='correo@gmail.com'
phone='numero'
linkedin='nombre linkedin'
github='nombre github'

job1 = {
    'name': 'Alten Spain',
    'puesto': 'Android Developer',
    'ubicación': 'Sevilla',
    'start_date': 'YYYY-MM',
    'end_date': 'YYYY-MM'
}

job2 = {
    'name': 'job2',
    'puesto': 'Administrativo',
    'ubicación': 'lugar',
    'start_date': 'YYYY-MM',
    'end_date': 'YYYY-MM'
}

education = {
    "institution": "CES Juan Pablo II",
    "location": "lugar",
    "degree": "FP",
    "area": "Técnico Superior en Desarrollo de Aplicaciones Multiplataforma (DAM)",
    "start_date": "YYYY-MM",
    "end_date": "YYYY-MM"
}

proyects = [
    "**Home_Lab**: Deployment of a lab on Raspberry Pi with Pi-hole and Unbound.",
    "**telegram_offer_job**: Envia por telegram ofertas de trabajo establecidas con filtros.",
    "**bash_scripting**: Scripts en bash que ayudan a automatizar acciones en el sistema.",
    "**python_scripting**: Scripts en python que ayudan a automatizar acciones del sistema y ciberseguridad."
]

language = [
    {"label": "English", "details": "Intermediate (B1-B2)"},
    {"label": "Español", "details": "Nativo"}
]

class CVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RenderCV - Adaptador Profesional")
        self.root.geometry("750x850")

        # Título
        ctk.CTkLabel(self.root, text="Adaptar CV a Oferta de Empleo", font=("Arial", 20, "bold")).pack(pady=10)

        # Tabview
        self.tabview = ctk.CTkTabview(self.root, width=700, height=650)
        self.tabview.pack(padx=20, pady=10)

        self.tab_perfil = self.tabview.add("Perfil e Intro")
        self.tab_job1 = self.tabview.add(f"Highlights {job1['name']}")
        self.tab_isg = self.tabview.add(f"Highlights {job2['name']}")
        self.tab_skills = self.tabview.add("Skills")
        self.tab_certs = self.tabview.add("Certificaciones")

        self.setup_tabs()

        # Botón Generar
        self.btn_generate = ctk.CTkButton(self.root, text="🚀 Generar CV Adaptado", 
                                         command=self.click_generar, fg_color="green", hover_color="darkgreen", height=40)
        self.btn_generate.pack(pady=20)

    def setup_tabs(self):
        # TAB PERFIL: Headline e Introducción
        ctk.CTkLabel(self.tab_perfil, text="Titular del CV (Headline):").pack(pady=(10,0))
        self.entry_headline = ctk.CTkEntry(self.tab_perfil, width=500)
        self.entry_headline.insert(0, headline)
        self.entry_headline.pack(pady=5)

        ctk.CTkLabel(self.tab_perfil, text="Introducción (Summary - una frase por línea):").pack(pady=(10,0))
        self.txt_summary = ctk.CTkTextbox(self.tab_perfil, width=600, height=200)
        initial_summary = "Software Developer specialized in Cybersecurity and automation (Bash/Python).Expert in log analysis and triage optimization.Extensive experience in Native Android development.Currently training for eJPT certification."
        self.txt_summary.insert("0.0", initial_summary)
        self.txt_summary.pack(pady=5)

        # TAB Job1: Logros en primer empleo
        ctk.CTkLabel(self.tab_job1, text=f"Logros en {job1['name']} (una frase por línea):").pack(pady=(10,0))
        self.txt_highlights_job1 = ctk.CTkTextbox(self.tab_job1, width=600, height=350)
        job1_defaults = "Developed native Android apps using Kotlin and Java for clients like Vodafone and Iberdrola.\nImplemented modern UIs with Jetpack Compose.\nStructured code under Clean Architecture and MVVM/MVP.\nAutomated CI/CD pipelines with Jenkins and Gradle."
        self.txt_highlights_job1.insert("0.0", job1_defaults)
        self.txt_highlights_job1.pack(pady=5)

        # TAB job2: Logros en segundo empleo
        ctk.CTkLabel(self.tab_job2, text=f"Logros en {job2['name']}:").pack(pady=(10,0))
        self.txt_highlights_job2 = ctk.CTkTextbox(self.tab_job2, width=600, height=350)
        job2_defaults = "Optimized supply chain and invoicing flow.\nManaged inventory control systems."
        self.txt_highlights_job2.insert("0.0", job2_defaults)
        self.txt_highlights_job2.pack(pady=5)

        # TAB SKILLS: Dinámicas 
        ctk.CTkLabel(self.tab_skills, text="Habilidades (Formato: Categoría: Detalles):").pack(pady=(10,0))
        self.txt_skills = ctk.CTkTextbox(self.tab_skills, width=600, height=400)
        skills_defaults = "Languages: Kotlin, Java, Python, Bash, SQL\nAndroid: Jetpack Compose, Coroutines, Dagger Hilt, Room, Retrofit\nCybersecurity: Nmap, Wireshark, Vulnerability Analysis"
        self.txt_skills.insert("0.0", skills_defaults)
        self.txt_skills.pack(pady=5)

        # TAB CERTIFICACIONES 
        ctk.CTkLabel(self.tab_certs, text="Certificaciones (una por línea):").pack(pady=(10,0))
        self.txt_certs = ctk.CTkTextbox(self.tab_certs, width=600, height=400)
        certs_defaults = "Azure Specialist (Professional Path) - Microsoft & LinkedIn (2026)\nCybersecurity for Vehicles (IFCD101) - Focus on Pentesting\nMicrosoft Security Essentials - SIEM, Sentinel, Defender XDR"
        self.txt_certs.insert("0.0", certs_defaults)
        self.txt_certs.pack(pady=5)

    def click_generar(self):
        try:
            # Procesar Skills: Convertir "Label: Details" en diccionario 
            raw_skills = self.txt_skills.get("1.0", "end-1c").strip().split("\n")
            processed_skills = []
            for line in raw_skills:
                if ":" in line:
                    label, details = line.split(":", 1)
                    processed_skills.append({"label": label.strip(), "details": details.strip()})

            # Creación de la plantilla en yaml para poder crear el pdf con renderCV
            cv_data = {
                "cv": {
                    "name": nombre,
                    "headline": self.entry_headline.get(),
                    "location": location,
                    "email": email,
                    "phone": phone,
                    "social_networks": [
                        {"network": "LinkedIn", "username": linkedin},
                        {"network": "GitHub", "username": github}
                    ],
                    "sections": {
                        "summary": self.txt_summary.get("1.0", "end-1c").strip().split("\n"),
                        "experience": [
                            {
                                "company": job1['name'],
                                "position": job1['puesto'],
                                "location": job1['ubicación'],
                                "start_date": job1['start_date'],
                                "end_date": job1['end_date'],
                                "highlights": self.txt_highlights_job1.get("1.0", "end-1c").strip().split("\n")
                            },
                            {
                                "company": job2['name'],
                                "position": job2['puesto'],
                                "location": job2['ubicación'],
                                "start_date": job2['start_date'],
                                "end_date": job2['end_date'],
                                "highlights": self.txt_highlights_job2.get("1.0", "end-1c").strip().split("\n")
                            }
                        ],
                        "education": [
                            {
                                "institution": education['institution'],
                                "location": education['location'],
                                "degree": education['degree'],
                                "area": education['area'],
                                "start_date": education['start_date'],
                                "end_date": education['end_date']
                            }
                        ],
                        "projects": proyects,
                        "skills": processed_skills,
                        "certifications": self.txt_certs.get("1.0", "end-1c").strip().split("\n"),
                        "languages": language
                    }
                },
                "design": {"theme": "classic"}
            }

            # Escritura del yml
            file_name = "CV_Adaptado.yaml"
            with open(file_name, 'w', encoding='utf-8') as f:
                yaml.dump(cv_data, f, allow_unicode=True, sort_keys=False)
            
            # Una vez con el yaml creado podemos ejecutar rendercv
            os.system(f"rendercv render {file_name}")
            messagebox.showinfo("Éxito", "CV generado con éxito.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = ctk.CTk()
    CVApp(app)
    app.mainloop()