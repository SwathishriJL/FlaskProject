import re
import sys
import subprocess
import importlib.util
from pathlib import Path
import openai   # pip install openai

# --- Configure your API key ---
openai.api_key = "YOUR_OPENAI_API_KEY"

def get_imports(file_path):
    """
    Extract top-level imports from a Python file.
    """
    imports = set()
    with open(file_path, "r") as f:
        code = f.read()
        matches = re.findall(r'^\s*(?:import|from)\s+([a-zA-Z0-9_\.]+)', code, re.MULTILINE)
        for m in matches:
            imports.add(m.split('.')[0])
    return list(imports)

def map_imports_to_packages(imports):
    """
    Use GenAI to map import names to pip package names.
    """
    prompt = f"""
    I have these Python imports: {imports}.
    Please map each import to the correct pip install package names.
    Reply ONLY with a Python list of package names.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",   # you can use gpt-4, gpt-3.5, etc.
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    
    # Extract response text
    packages_text = response["choices"][0]["message"]["content"].strip()
    try:
        packages = eval(packages_text)  # Convert string list → Python list
        return packages
    except:
        return imports  # fallback if parsing fails

def install_if_missing(package):
    """
    Install a package if it's missing.
    """
    if importlib.util.find_spec(package) is None:
        print(f"📦 Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def run_script(file_path):
    """
    Run the given Python script after ensuring all imports are installed.
    """
    # Step 1: Detect imports
    imports = get_imports(file_path)
    print("🔍 Detected imports:", imports)

    # Step 2: Use GenAI to map them to pip packages
    packages = map_imports_to_packages(imports)
    print("🤖 GenAI suggests these pip packages:", packages)

    # Step 3: Install missing packages
    for pkg in packages:
        try:
            install_if_missing(pkg)
        except Exception as e:
            print(f"⚠️ Could not auto-install {pkg}: {e}")

    # Step 4: Run the script
    print(f"\n🚀 Running {file_path}...\n")
    subprocess.run([sys.executable, file_path])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python auto_runner.py your_script.py")
        sys.exit(1)

    script_file = Path(sys.argv[1])
    if not script_file.exists():
        print(f"❌ File not found: {script_file}")
        sys.exit(1)

    run_script(str(script_file))
