# LuxLine Website Monitor

A Python script that monitors your website for outages and sends Discord notifications via Docker.

## Features

- Checks website status every 5 minutes
- Logs all checks and response times
- Sends Discord alerts when the website goes down
- Tracks CPU usage
- Runs 24/7 in a Docker container

## Installation

### Prerequisites

- Docker and Docker Compose installed
- Discord webhook URL

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/WebsiteMonitor.git
cd WebsiteMonitor
```

2. Create a `.env` file with your Discord webhook:
```bash
echo "DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/..." > .env
```

3. Build and run with Docker Compose:
```bash
docker-compose up -d
```

## Commands

View logs:
```bash
docker-compose logs -f
```

Stop the container:
```bash
docker-compose down
```

Restart the container:
```bash
docker-compose restart
```

## Configuration

Edit `main.py` to change:
- `WEBSITE_URL`: The website to monitor
- `CHECK_INTERVAL`: How often to check (in seconds)

## Logs

Logs are written to `luxline_monitor.log` in the project directory.

## Security

**Never commit your Discord webhook URL to GitHub!**

Always use the `.env` file (which is in `.gitignore`) for secrets.

