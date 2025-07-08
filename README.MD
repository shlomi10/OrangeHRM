# 🧪 OrangeHRM Automated Test Suite

![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
[![Python](https://img.shields.io/badge/Python-3.13.5-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-Test_Framework-green.svg?style=for-the-badge&logo=pytest)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-Reports-orange.svg?style=for-the-badge&logo=allure)](https://docs.qameta.io/allure/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg?style=for-the-badge&logo=docker)](https://docs.docker.com/compose/)
[![Docker Pulls](https://img.shields.io/docker/pulls/shlomi10/orangehrm?style=for-the-badge)](https://hub.docker.com/r/shlomi10/orangehrm)
[![Docker Image Size](https://img.shields.io/docker/image-size/shlomi10/orangehrm/001?style=for-the-badge
)](https://hub.docker.com/r/shlomi10/orangehrm)

* 🎭 **Playwright** — UI automation
* 🐍 **Python + Pytest** — test framework
* 🔐 **REST API** — user creation and management
* 🧱 **Page Object Model** — clean test structure
* 📊 **Allure Reporting** — beautiful reports
* 🐳 **Docker + Docker Compose** — local and CI support
* ☁️ **GitHub Actions** — cloud CI with Allure Report deployment

---

## 🚀 Features

* Create a system user via API
* Delete the user via UI using the Admin panel
* Cross-step data sharing
* Detailed Allure reporting
* Logging and screenshots on failure

---

## 🛠️ Installation (Local)

```bash
git clone https://github.com/shlomi10/OrangeHRM.git
cd OrangeHRM
python -m venv .venv
source .venv/bin/activate    # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🧪 Run Tests Locally

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 🐳 Docker

### Build the image

```bash
docker build -t orangehrm-tests .
```

### Run tests in container

```bash
docker run --rm -v "${PWD}/allure-results:/app/allure-results" orangehrm-tests
```

---

## 🐳 Docker Compose (with Allure UI)

### 1. Run the full stack

```bash
docker-compose up --build
```

### 2. View the report in your browser

```
http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html
```

> If you see a blank page, make sure the `allure-results/` folder exists on your host. You can create it manually before running Compose.

### 3. Re-run just the tests (without rebuilding everything)

```bash
docker-compose run tests
```

Test results will be auto-detected and updated in the Allure UI.

---

## 🤖 GitHub Actions (CI)

This project includes a fully configured GitHub Actions workflow:

* ✅ Pulls the prebuilt Docker image from Docker Hub
* ✅ Runs all tests inside the container
* ✅ Generates and uploads the Allure report
* ✅ Publishes to GitHub Pages

You can find the report at:

```
https://shlomi10.github.io/OrangeHRM/
```

---

2. Deploy report locally with:

```bash
allure generate allure-results --clean -o allure-report
```

### Playwright Traces

View detailed interaction recordings for debugging:

```bash
npx playwright show-trace trace/trace.zip
```

---

## 📂 Project Structure

```
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── utils/
│   └── .env
├── tests/
│   └── test_user_flow.py
├── pages/
│   ├── basePage.py
│   ├── login_page.py
│   └── admin_page.py
├── api/
│   └── users_api.py
└── utils/
    └── conftest.py
```

---

## 📜 License

MIT License — free to use, modify and distribute.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request