import requests

def parse_jenkinsfile(jenkins_content: str, model='codellama') -> str:
    prompt = f"""
You are converting CI/CD for a microservice from Jenkins to GitHub Actions.
Convert this Jenkinsfile to GitHub Actions YAML:
{jenkins_content}
"""
    res = requests.post("http://ollama:11434/api/generate", json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    return res.json().get('response', '')
