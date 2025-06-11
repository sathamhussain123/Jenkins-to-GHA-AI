from fastapi import FastAPI
from convert import parse_jenkinsfile
import os, yaml

app = FastAPI()

@app.post("/convert/")
async def convert(payload: dict):
    path = payload.get('path')
    if not path:
        return {"error": "No path provided"}

    with open(path, 'r') as f:
        jenkinsfile = f.read()

    output_yaml = parse_jenkinsfile(jenkinsfile)

    service_dir = os.path.dirname(path)
    wf_dir = os.path.join(service_dir, ".github", "workflows")
    os.makedirs(wf_dir, exist_ok=True)

    wf_path = os.path.join(wf_dir, "generated.yml")
    with open(wf_path, "w") as f:
        f.write(output_yaml)

    manifest = {"source": path, "generated": wf_path}
    with open(os.path.join(service_dir, "manifest.yml"), "w") as mf:
        yaml.dump(manifest, mf)

    return {"status": "converted", "workflow_path": wf_path}
