#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_github_remote.py
Met à jour l'URL du dépôt GitHub après changement de username
Ancien : GaetanWendling → Nouveau : hibwho
"""

import subprocess
from pathlib import Path

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

def run_cmd(cmd, description):
    print(f"\n{'='*50}")
    print(f"🔧 {description}")
    print(f"{'='*50}")

    result = subprocess.run(
        cmd,
        cwd=BASE_DIR,
        shell=True,
        capture_output=True,
        text=True
    )

    print(result.stdout)
    if result.stderr:
        print(f"⚠️ {result.stderr}")

    return result.returncode == 0

print("🦉 MISE À JOUR GITHUB USERNAME")
print("=" * 50)

# 1. Vérifier l'URL actuelle
print("\n📍 URL actuelle du remote :")
run_cmd("git remote -v", "Vérification remote")

# 2. Supprimer l'ancien remote
run_cmd("git remote remove origin", "Suppression ancien remote")

# 3. Ajouter le nouveau remote
new_url = "https://github.com/hibwho/owlhub1_.git"
if run_cmd(f'git remote add origin {new_url}', "Ajout nouveau remote"):
    print(f"\n✅ Nouveau remote configuré : {new_url}")

# 4. Vérifier la configuration
print("\n📍 Nouvelle configuration :")
run_cmd("git remote -v", "Vérification")

# 5. Fetch pour vérifier la connexion
if run_cmd("git fetch origin", "Test connexion"):
    print("\n✅ Connexion réussie au nouveau dépôt")
else:
    print("\n❌ Échec de connexion")
    print("\n💡 Vérifie que le dépôt existe :")
    print("   https://github.com/hibwho/owlhub1_")

print("\n🦉 Script terminé")
