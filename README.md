# RESO Organizations Search App

A modern web application for searching and exploring RESO (Real Estate Standards Organization) organization data. Built with Flask and Docker for easy deployment.

![RESO Search](https://img.shields.io/badge/RESO-Organizations%20Search-blue)
![Docker](https://img.shields.io/badge/docker-ready-green)
![Python](https://img.shields.io/badge/python-3.11-blue)

## ✨ Features

- 🔍 **Smart Search** - Search organizations by name, type, state, and country
- 🏢 **Visual Icons** - Organization type icons for quick identification
- 📋 **Copy IDs** - One-click copy of Organization Unique IDs
- 📄 **Pagination** - 25 results per page with smart navigation
- ⌨️ **Keyboard Shortcuts** - Press Escape to clear filters, Enter to search
- 🔄 **Real-time Data** - Fetches live data from https://services.reso.org/orgs
- 🐳 **Docker Ready** - Easy deployment with Docker/Docker Compose
- 📱 **Responsive Design** - Works on desktop and mobile

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)
```bash
git clone <your-repo-url>
cd reso_ouid
docker-compose up -d
```

### Option 2: Docker
```bash
git clone <your-repo-url>
cd reso_ouid
docker build -t reso-search .
docker run -p 7766:5000 reso-search
```

### Option 3: Local Development
```bash
git clone <your-repo-url>
cd reso_ouid
pip install -r requirements.txt
python app.py
```

🌐 **Access the app at:** http://localhost:7766

## 🎮 How to Use

1. **Search Organizations** - Type in the search box or use dropdown filters
2. **Copy Organization IDs** - Click the 📋 button next to any ID
3. **Navigate Pages** - Use pagination controls for large result sets
4. **Clear Filters** - Click "Clear Filters" or press `Escape`
5. **Quick Search** - Press `Enter` from any field to search

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Web interface |
| `/api/organizations` | GET | Search organizations |
| `/api/stats` | GET | Dataset statistics |

### Query Parameters for `/api/organizations`:
- `query` - Search by organization name
- `type` - Filter by organization type  
- `state` - Filter by state/province
- `country` - Filter by country
- `page` - Page number (default: 1)
- `per_page` - Results per page (default: 25)

### Example API Call:
```bash
curl "http://localhost:7766/api/organizations?type=MLS&state=CA&page=1"
```

## 📊 Organization Types

The app recognizes these organization types with visual icons:

| Type | Icon | Description |
|------|------|-------------|
| Local Association | 🏘️ | Local real estate associations |
| MLS | 🏢 | Multiple Listing Services |
| Brokerage | 🏪 | Real estate brokerages |
| Commercial | 🏬 | Commercial real estate |
| Technology Company | 💻 | PropTech companies |
| State/Provincial Association | 🏛️ | State-level associations |
| National Association | 🌟 | National organizations |
| Pooled Platform | 🔗 | Shared platforms |

## 🗂️ Data Fields

Each organization includes:
- **Organization Name & Unique ID**
- **Type & Classification**
- **Complete Address** (street, city, state, postal code, country)
- **Geographic Coordinates** (latitude/longitude)
- **Website & Contact Information**
- **Certification Details**

## 🛠️ Tech Stack

- **Backend:** Python 3.11, Flask 2.3.3
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Data Source:** RESO Organizations API
- **Deployment:** Docker, Docker Compose
- **Features:** Pagination, Real-time search, Copy-to-clipboard

## 🐳 Docker Configuration

The app runs on port 5000 inside the container and can be mapped to any host port:

```yaml
# docker-compose.yml
services:
  reso-search:
    build: .
    ports:
      - "7766:5000"  # Host:Container
    environment:
      - FLASK_ENV=production
```

## 📝 Development

### Project Structure
```
reso_ouid/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── docker-compose.yml # Multi-container setup
├── templates/
│   └── index.html     # Web interface
└── README.md          # This file
```

### Adding Features
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker
5. Submit a pull request

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📄 License

This project is open source. Feel free to use it for your real estate data needs.