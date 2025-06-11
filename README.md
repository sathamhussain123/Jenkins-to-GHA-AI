# Jenkins to GitHub Actions AI Converter 🚀

This repo uses **Ollama, FastAPI, Watchdog**, and **Docker** to:
- Monitor all Jenkinsfiles in your microservices repo
- Convert them to `.github/workflows/generated.yml`
- Add a `manifest.yml` per service

## 🛠️ How to Use

1. **Clone:**
   ```bash
   git clone <your repo URL>
   cd jenkins-to-gha-ai
   ```

2. **Place your services repo:**
   Inside `data/projects/`, add your monorepo (with Jenkinsfiles).

3. **Build & run:**
   ```bash
   docker-compose up --build
   ```

4. **Modify/add a Jenkinsfile:**
   The service converts it automatically and creates:
   - `.github/workflows/generated.yml`
   - `manifest.yml`
