#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
force_push_hibwho.py
Push avec le nouveau username hibwho
"""

import subprocess
from pathlib import Path
import time

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
    if result.stderr and "warning" not in result.stderr.lower():
        print(f"⚠️ {result.stderr}")

    return result.returncode == 0

print("🦉 DÉPLOIEMENT - hibwho/owlhub1_")
print("="*50)

# 1. Ajouter les fichiers
run_cmd("git add .", "Ajout des fichiers")

# 2. Commit
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
commit_msg = f"Fix mobile: viewport + burger menu - {timestamp}"
run_cmd(f'git commit -m "{commit_msg}" --allow-empty', "Commit")

# 3. Push vers le nouveau dépôt
if run_cmd("git push origin main --force", "Push forcé"):
    print("\n✅ DÉPLOIEMENT RÉUSSI !")
    print("\n⏱️ Attendre 2-3 minutes pour GitHub Pages")
    print("\n🌐 NOUVELLE URL DU SITE :")
    print("   https://hibwho.github.io/owlhub1_/")
    print("\n💡 TESTER :")
    print("   • F12 → Toggle device toolbar")
    print("   • Cliquer sur le burger (☰)")
    print("   • Vider le cache : Ctrl + Shift + R")
else:
    print("\n❌ ÉCHEC DU PUSH")
    print("\n🔍 Vérifications à faire :")
    print("   1. Le dépôt existe : https://github.com/hibwho/owlhub1_")
    print("   2. GitHub Pages est activé (Settings → Pages)")
    print("   3. Branch : main, Folder : / (root)")

print("\n🦉 Script terminé")
