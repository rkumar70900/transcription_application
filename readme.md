# Transcription Application

A powerful, containerized transcription application that allows users to upload audio files and get text transcriptions. The application features a user-friendly Streamlit-based web interface and a robust backend service for processing audio files.

## 📁 Project Structure

```
transcription_application/
├── app/                      # Backend service
│   ├── Dockerfile            # Docker configuration for the backend
│   ├── main.py               # Main FastAPI application
│   ├── models.py             # Data models
│   ├── read_files.py         # File handling utilities
│   ├── store_data.py         # Data storage functionality
│   ├── transcribe.py         # Core transcription logic
│   └── requirements.txt      # Python dependencies for the backend
├── streamlit_ui/             # Frontend web interface
│   ├── Dockerfile            # Docker configuration for the Streamlit UI
│   ├── app.py                # Streamlit application
│   └── requirements.txt      # Python dependencies for the UI
├── docker-compose.yml        # Docker Compose configuration
└── README.md                 # This file
```

## 🚀 Features

- Upload audio files for transcription
- Web-based user interface built with Streamlit
- RESTful API backend built with FastAPI
- Containerized with Docker for easy deployment
- Asynchronous processing of transcription tasks

## 🛠️ Prerequisites

- Docker (v20.10+)
- Docker Compose (v2.0+)
- Git

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/transcription_application.git
   cd transcription_application
   ```

2. **Start the application**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Web UI: http://localhost:8501
   - API Documentation: http://localhost:8000/docs

## 🔧 Configuration

Environment variables can be configured in the `docker-compose.yml` file. The following variables are available:

- `APP_HOST`: Host address (default: 0.0.0.0)
- `APP_PORT`: Port for the backend API (default: 8000)
- `STREAMLIT_SERVER_PORT`: Port for the Streamlit UI (default: 8501)

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the awesome web interface
- [FastAPI](https://fastapi.tiangolo.com/) for the high-performance API
- [Docker](https://www.docker.com/) for containerization
