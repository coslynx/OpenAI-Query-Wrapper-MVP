<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
OpenAI-Query-Wrapper-MVP
</h1>
<h4 align="center">A Python backend service for simplifying OpenAI API interactions.</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-blue" alt="Framework: FastAPI" />
  <img src="https://img.shields.io/badge/Language-Python-red" alt="Language: Python" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue" alt="Database: PostgreSQL" />
  <img src="https://img.shields.io/badge/LLMs-OpenAI-black" alt="LLMs: OpenAI" />
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/OpenAI-Query-Wrapper-MVP?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/OpenAI-Query-Wrapper-MVP?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/OpenAI-Query-Wrapper-MVP?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors

## 📍 Overview
This repository contains a Minimum Viable Product (MVP) for an AI wrapper designed to streamline interactions with the OpenAI API. Built with Python, FastAPI, and PostgreSQL, it aims to simplify integration with OpenAI's powerful language models for developers and businesses.

## 📦 Features
|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular architectural pattern with separate directories for different functionalities, ensuring easier maintenance and scalability.             |
| 📄 | **Documentation**  | The repository includes a README file that provides a detailed overview of the MVP, its dependencies, and usage instructions.|
| 🔗 | **Dependencies**   | The codebase relies on various external libraries and packages such as `fastapi`, `openai`, `pyjwt`, `sqlalchemy`, and `psycopg2`, which are essential for building the API, handling OpenAI API calls, implementing JWT authentication, and interacting with the PostgreSQL database. |
| 🧩 | **Modularity**     | The modular structure allows for easier maintenance and reusability of the code, with separate directories and files for different functionalities such as services, models, utils, and configurations.|
| 🧪 | **Testing**        | Implements unit tests using `pytest` to ensure the reliability and robustness of the codebase.       |
| ⚡️  | **Performance**    | The performance of the system is optimized using techniques such as asynchronous programming, caching, and efficient database queries. |
| 🔐 | **Security**       | Enhances security by implementing measures such as input validation, API key handling, and secure database connections.|
| 🔀 | **Version Control**| Utilizes Git for version control with GitHub Actions workflow files for automated build and release processes.|
| 🔌 | **Integrations**   | Interacts with external services like OpenAI API and PostgreSQL database.|
| 📶 | **Scalability**    | Designed to handle increased user load and data volume, utilizing efficient coding practices, caching, and database optimization techniques.           |

## 📂 Structure
```text
├── src
│   ├── services
│   │   └── openai_service.py
│   ├── models
│   │   └── models.py
│   ├── utils
│   │   └── logger.py
│   └── config
│       └── config.py
├── main.py
├── requirements.txt
├── commands.json
├── startup.sh
├── .env
└── .gitignore
```

## 💻 Installation
### 🔧 Prerequisites
- Python 3.9+
- pip
- PostgreSQL (optional)

### 🚀 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/coslynx/OpenAI-Query-Wrapper-MVP.git
   cd OpenAI-Query-Wrapper-MVP
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database (optional):
   - Install and configure PostgreSQL.
   - Create a database and a user with appropriate permissions.
   - Update the `DATABASE_URL` in the `.env` file with your database connection string. 
4. Configure environment variables:
   ```bash
   cp .env.example .env
   # Update the environment variables in .env with your OpenAI API key and database connection string (if applicable).
   ```

## 🏗️ Usage
### 🏃‍♂️ Running the MVP
1. Start the development server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## 🌐 Hosting
### 🚀 Deployment Instructions
1. **Containerize with Docker:**
   - Create a Dockerfile and docker-compose.yml file to define your application's container environment.
   - Build the Docker image and run the container using docker-compose.
2. **Deploy to a Cloud Platform:**
   - Choose a cloud provider like AWS, GCP, or Azure.
   - Create a virtual machine or container instance.
   - Deploy your containerized application using the cloud provider's tools.
3. **Set Up Environment Variables:**
   - Set environment variables (like OpenAI API key and database connection string) within your cloud provider's environment.

### 🔑 Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key.
- `DATABASE_URL`:  PostgreSQL database connection string (if applicable).
- `PORT`:  The port for running the application (default: 8000).

## 📜 API Documentation
### 🔍 Endpoints
- **POST /v1/query/**: Sends a request to OpenAI's API for text generation.
  - **Request Payload:**
    ```json
    {
      "model": "text-davinci-003",  // OpenAI model to use
      "prompt": "Write a short story about a cat.",  // Prompt for the model
      "temperature": 0.7,  // Controls the creativity of the output (optional)
      "max_tokens": 2048,  // Maximum number of tokens in the output (optional)
      "top_p": 1.0,  // Controls the randomness of the output (optional)
      "frequency_penalty": 0.0,  // Penalty for repeating words (optional)
      "presence_penalty": 0.0  // Penalty for including specific words (optional)
    }
    ```
  - **Response:** JSON object containing the generated text and relevant metadata.

## 📜 License & Attribution

### 📄 License
This Minimum Viable Product (MVP) is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) license.

### 🤖 AI-Generated MVP
This MVP was entirely generated using artificial intelligence through [CosLynx.com](https://coslynx.com).

No human was directly involved in the coding process of the repository: OpenAI-Query-Wrapper-MVP

### 📞 Contact
For any questions or concerns regarding this AI-generated MVP, please contact CosLynx at:
- Website: [CosLynx.com](https://coslynx.com)
- Twitter: [@CosLynxAI](https://x.com/CosLynxAI)

<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="Developers: Drix10, Kais Radwan" />
  <img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="Website: CosLynx.com" />
  <img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="Backed by: Google, Microsoft & Amazon for Startups" />
  <img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="Finalist: Backdrop Build v4, v6" />
</div>