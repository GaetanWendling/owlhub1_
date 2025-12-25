#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
force_push.py
Force le push depuis owlhub_
"""

import subprocess
from pathlib import Path
import time

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

def run_cmd(cmd, description):
    """Exécute une commande Git"""
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
    if result.stderr and "warning" not in result.stderr.lower():
        print(f"⚠️ {result.stderr}")

    return result.returncode == 0

print("🦉 FORCE PUSH - owlhub_")
print("="*50)

# 1. Vérifier l'état
run_cmd("git status", "État du dépôt")

# 2. Ajouter tous les fichiers
if run_cmd("git add .", "Ajout des fichiers"):
    print("✅ Fichiers ajoutés")

# 3. Commit
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
commit_msg = f"Force update: rouge + header + burger + code M - {timestamp}"

if run_cmd(f'git commit -m "{commit_msg}" --allow-empty', "Commit"):
    print("✅ Commit créé")

# 4. Force push
print("\n" + "="*50)
print("🚀 FORCE PUSH vers GitHub")
print("="*50)

if run_cmd("git push origin main --force", "Push forcé"):
    print("\n✅ DÉPLOIEMENT RÉUSSI !")
    print("\n⏱️ Attendre 2-3 minutes pour la mise à jour")
    print("\n🌐 URL du site :")
    print("   https://gaetanwendling.github.io/owlhub1_/")
    print("\n💡 VIDER LE CACHE :")
    print("   • Ctrl + Shift + R")
else:
    print("\n❌ ÉCHEC - Tentative alternative...")
    run_cmd("git push origin main --force-with-lease", "Push avec --force-with-lease")

print("\n🦉 Script terminé")
