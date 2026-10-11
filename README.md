# 🧪 OrangeHRM Automated Test Suite

<div align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1400/1*_sRXtPteUX0_Bzl68FX_YA.png" width="400" alt="OrangeHRM Logo">
  
  <p><em>🎯 A comprehensive end-to-end test automation suite for OrangeHRM using modern tools and best practices</em></p>

  ![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
  [![Python](https://img.shields.io/badge/Python-3.15-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
  [![Pytest](https://img.shields.io/badge/Pytest-Test_Framework-green.svg?style=for-the-badge&logo=pytest)](https://docs.pytest.org/)
  [![Allure](https://img.shields.io/badge/Allure-Reports-9249A7.svg?style=for-the-badge&logo=allure)](https://docs.qameta.io/allure/)
  [![Live Report](https://img.shields.io/badge/Allure--Live--Report-ff6f00?style=for-the-badge&logo=allure)](https://shlomi10.github.io/OrangeHRM/)
  [![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg?style=for-the-badge&logo=docker)](https://docs.docker.com/compose/)
  [![Docker Pulls](https://img.shields.io/docker/pulls/shlomi10/orangehrm?style=for-the-badge)](https://hub.docker.com/r/shlomi10/orangehrm)
  [![Docker Image Size](https://img.shields.io/docker/image-size/shlomi10/orangehrm/002?style=for-the-badge)](https://hub.docker.com/r/shlomi10/orangehrm)

  **[🚀 View Live Reports](https://shlomi10.github.io/OrangeHRM/) • [📚 Documentation](https://github.com/shlomi10/OrangeHRM/wiki) • [🐳 Docker Hub](https://hub.docker.com/r/shlomi10/orangehrm)**

</div>

---

## 🌟 Overview

This test automation suite provides comprehensive coverage for OrangeHRM's core functionality, combining API and UI testing with modern DevOps practices. The suite demonstrates a complete user lifecycle: creating users via API and managing them through the web interface.

### 🎯 Key Features

- **🔄 End-to-End Testing** - Complete user lifecycle from creation to deletion
- **🌐 Cross-Browser Support** - Chrome, Firefox, Safari, and Edge
- **📱 Multi-Platform** - Windows, macOS, and Linux compatibility
- **🔀 Hybrid Approach** - API for setup, UI for business logic validation
- **📊 Rich Reporting** - Detailed Allure reports with screenshots and traces
- **🐳 Containerized** - Ready for local development and CI/CD pipelines

---

## 🔧 Tech Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| 🎭 **Playwright** | Cross-browser UI automation | Latest |
| 🐍 **Python** | Core language | 3.15 |
| 🧪 **Pytest** | Testing framework | Latest |
| 🔐 **REST API** | User management & data setup | - |
| 🧱 **Page Object Model** | Clean, maintainable test structure | - |
| 📊 **Allure** | Rich HTML reporting | Latest |
| 🐳 **Docker** | Containerization & CI/CD | Latest |
| ☁️ **GitHub Actions** | Continuous Integration | - |

---

## 🚀 Quick Start

### 📋 Prerequisites

- Python 3.15 or higher
- Docker & Docker Compose (optional)
- Git

### 🛠️ Local Installation

```bash
# Clone the repository
git clone https://github.com/shlomi10/OrangeHRM.git
cd OrangeHRM

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate    # Linux/macOS
# or
.venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### 🧪 Running Tests

```bash
# Run all tests with Allure reporting
pytest --alluredir=allure-results

# Run specific test file
pytest tests/test_user_flow.py --alluredir=allure-results

# Run with verbose output
pytest -v --alluredir=allure-results

# Generate and serve Allure report
allure serve allure-results
```

---

## 🐳 Docker Usage

### 🏃‍♂️ Quick Run (Using Docker Hub Image)

```bash
# Pull and run the latest image
docker run --rm -v "${PWD}/allure-results:/app/allure-results" shlomi10/orangehrm:latest

# Run specific tag
docker run --rm -v "${PWD}/allure-results:/app/allure-results" shlomi10/orangehrm:v1.0.0
```

### 🔨 Build Local Image

```bash
# Build the image
docker build -t orangehrm-tests .

# Run tests in container
docker run --rm -v "${PWD}/allure-results:/app/allure-results" orangehrm-tests
```

### 🐳 Docker Compose (Full Stack)

```bash
# Start the complete testing environment
docker-compose up --build

# Run in detached mode
docker-compose up -d --build

# View logs
docker-compose logs -f tests

# Re-run tests without rebuilding
docker-compose run tests

# Clean up
docker-compose down
```

#### 📊 Accessing Reports

After running with Docker Compose, access the Allure report at:
```
http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html
```

> 💡 **Tip**: If you see a blank page, ensure the `allure-results/` directory exists in your project root.

---

## 🤖 CI/CD Pipeline

### GitHub Actions Workflow

This project includes a comprehensive CI/CD pipeline that:

1. **🔄 Triggers** - Runs on every push and pull request
2. **🐳 Docker Integration** - Uses the pre-built image from Docker Hub
3. **🧪 Test Execution** - Runs all tests in a containerized environment
4. **📊 Report Generation** - Creates detailed Allure reports
5. **🚀 Deployment** - Publishes reports to GitHub Pages

#### 🏷️ Docker Tags

Available on Docker Hub: [shlomi10/orangehrm](https://hub.docker.com/r/shlomi10/orangehrm)

- `latest` - Most recent stable build
- `v1.0.0` - Tagged releases
- `main` - Latest from main branch

---

## 📂 Project Architecture

```
OrangeHRM/
├── 🐳 Dockerfile                    # Container configuration
├── 🐳 docker-compose.yml           # Multi-service setup
├── 📦 requirements.txt             # Python dependencies
├── 📄 README.md                    # Documentation
├── 🧪 tests/
│   └── test_user_flow.py           # Main test scenarios
├── 📄 pages/                       # Page Object Model
│   ├── basePage.py                 # Base page class
│   ├── login_page.py               # Login functionality
│   └── admin_page.py               # Admin panel operations
├── 🔌 api/
│   └── users_api.py                # REST API interactions
├── ⚙️ utils/
│   ├── conftest.py                 # Pytest configuration
│   └── .env                        # Environment variables
├── 📊 allure-results/              # Test results (generated)
├── 🎭 trace/                       # Playwright traces (generated)
└── 📁 .github/
    └── workflows/
        └── ci.yml                  # GitHub Actions workflow
```

---

## 🧪 Test Scenarios

### ✅ Current Test Coverage

- **System User Creation** - Create users via REST API
- **Admin Panel Navigation** - Navigate and manage users through UI
- **User Management** - Complete CRUD operations
- **Data Validation** - Ensure data integrity and error handling
- **Cross-Step Integration** - Share data between API and UI tests

### 🔍 Test Architecture

The test suite follows a **hybrid approach**:

1. **API Layer** - Fast data setup and teardown
2. **UI Layer** - Business logic validation and user experience testing
3. **Data Layer** - Shared test data management
4. **Reporting Layer** - Comprehensive test execution reporting

---

## 📊 Reporting & Debugging

### 📈 Allure Reports

Generate comprehensive HTML reports:

```bash
# Generate report
allure generate allure-results --clean -o allure-report

# Serve report locally
allure serve allure-results

# Open generated report
allure open allure-report
```

### 🔍 Debugging with Playwright

```bash
# Show trace files
npx playwright show-trace trace/trace.zip

# Debug mode
pytest --headed --slowmo=1000

# Generate trace on failure
pytest --tracing=on
```

### 📝 Logging

Logs are automatically generated and include:
- Test execution details
- API request/response data
- Browser console logs
- Screenshots on failure

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **🍴 Fork** the repository
2. **🌿 Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **💾 Commit** your changes: `git commit -m 'Add amazing feature'`
4. **📤 Push** to the branch: `git push origin feature/amazing-feature`
5. **🔄 Open** a Pull Request

### 📋 Development Guidelines

- Follow PEP 8 style guidelines
- Write comprehensive tests for new features
- Update documentation for any changes
- Ensure all tests pass before submitting PR
- Use meaningful commit messages

---

## 📄 License

MIT License

Copyright (c) 2025 Shlomi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## 🆘 Support & Issues

- **📋 Issues**: [GitHub Issues](https://github.com/shlomi10/OrangeHRM/issues)
- **📖 Documentation**: [Project Wiki](https://github.com/shlomi10/OrangeHRM/wiki)
- **💬 Discussions**: [GitHub Discussions](https://github.com/shlomi10/OrangeHRM/discussions)

---

## 🙏 Acknowledgments

- **OrangeHRM** - For providing the demo application
- **Playwright Team** - For the excellent automation framework
- **Allure Framework** - For beautiful test reporting
- **Docker Community** - For containerization support

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by [Shlomi](https://github.com/shlomi10)

</div>