from flask import Flask, render_template, jsonify
import os
import json
import requests
import zipfile
import io
import re
from pathlib import Path
from collections import defaultdict
import base64

app = Flask(__name__)

JSON_B64 = os.getenv("PROBLEMS_JSON_B64")
if JSON_B64:
    try:
        decoded = base64.b64decode(JSON_B64).decode("utf-8")
        JSON = json.loads(decoded)
        print("✅ JSON carregado da variável de ambiente (base64).")
    except Exception as e:
        print(f"❌ Erro ao decodificar JSON: {e}")
        JSON = {}
else:
    print("⚠️ Nenhum JSON definido via PROBLEMS_JSON_B64.")
    JSON = {}

JUDGE_URL = os.getenv("JUDGE_URL", "https://judge_0.darlon.com.br")
PORT = int(os.getenv("PORT", 5000))

JUDGE_URL = os.getenv("JUDGE_URL", "https://judge_0.darlon.com.br")
PORT = int(os.getenv("PORT", 5000))

@app.route("/")
def index():
    return render_template("index.html", anos=JSON)

@app.route("/<ano>/<fase>/<nivel>/<problema>")
def ir_para_problema(ano, fase, nivel, problema):
    pdf_url = JSON[ano][fase][nivel].get('pdf', '')
    zip_url = JSON[ano][fase][nivel].get(problema, '')

    return render_template(
        "problems.html",
        ano=ano, fase=fase, nivel=nivel, problema=problema,
        pdf_url=pdf_url, zip_url=zip_url, JUDGE_URL=JUDGE_URL
    )

def organize_test_files(paths: list[str]) -> list[str]:
    def extract_info(p: str):
        path = Path(p)
        name = path.name.lower()
        nums = [int(n) for n in re.findall(r'\d+', str(path))]
        test_num = nums[0] if nums else -1
        file_num = nums[-1] if nums else -1
        if any(k in name for k in ["in", "entrada", ".in"]):
            io_type = "in"
        elif any(k in name for k in ["out", "saida", ".sol", ".out"]):
            io_type = "out"
        else:
            io_type = "?"
        return test_num, file_num, io_type, str(path)

    groups = defaultdict(list)
    for p in paths:
        if p.endswith('/'):
            continue
        info = extract_info(p)
        parent = str(Path(p).parent)
        groups[parent].append(info)

    final = []
    for parent, items in sorted(groups.items()):
        items.sort(key=lambda x: (x[1], 0 if x[2] == "in" else 1))
        for _, _, _, fullpath in items:
            final.append(fullpath)
    return final

@app.route("/api/get_test_cases/<ano>/<fase>/<nivel>/<problema>")
def get_test_cases(ano, fase, nivel, problema):
    try:
        zip_url = JSON[ano][fase][nivel].get(problema, '')
        if not zip_url:
            return jsonify({"error": "ZIP URL not found"}), 404
        
        response = requests.get(zip_url, timeout=10)
        response.raise_for_status()
        
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        files_list = zip_file.namelist()
        sorted_files = organize_test_files(files_list)

        test_cases = {}
        j = 0
        for i in range(0, len(sorted_files), 2):
            file_in = sorted_files[i]
            file_out = sorted_files[i + 1]
            test_cases[j] = {
                "input": zip_file.read(file_in).decode('utf-8'),
                "output": zip_file.read(file_out).decode('utf-8'),
            }
            j += 1

        return jsonify({"success": True, "files": test_cases})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print(f"🌐 Servidor Flask iniciado em 0.0.0.0:{PORT}")
    print(f"📄 Usando JSON: {JSON}")
    print(f"⚙️  Judge URL: {JUDGE_URL}")
    app.run(host="0.0.0.0", port=PORT, debug=True)
