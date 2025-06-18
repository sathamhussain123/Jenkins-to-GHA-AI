def parse_jenkinsfile(jenkinsfile: str) -> str:
    # Placeholder conversion logic
    return """name: Converted CI

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Run sample
        run: echo 'Converted from Jenkinsfile'
"""