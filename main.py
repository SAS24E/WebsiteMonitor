"""
Website Monitoring Tool
----------------------
Checks the LuxLine website for outages and sends notifications to a Discord channel using a webhook.
"""

import os
import logging
import requests
import time
# --- Configuration ---
WEBSITE_URL = "https://luxlinerefinishing.com"  # The website to monitor
CHECK_INTERVAL = 300  # Time between checks in seconds (5 minutes)
last_status = "UNKNOWN"
DISCORD_WEBHOOK_URL = os.getenv(
    "DISCORD_WEBHOOK_URL",
    "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL" # For security, set your actual Discord webhook URL as an environment variable or replace the placeholder here.
) 

# Global logger 
logger = logging.getLogger(__name__)

def setup_logger():
    """
    Set up logging to a file with timestamps.
    """
    logging.basicConfig(
        filename="luxline_monitor.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s"
        )
    logger.setLevel(logging.INFO)


def send_discord_notification(message):
    """
    Send a message to a Discord channel using a webhook.
    """
    data = {"content": message}
    try:
        resp = requests.post(DISCORD_WEBHOOK_URL, json=data, timeout=10)
        log_status(f"Discord response status: {resp.status_code}", "info")
        if resp.status_code != 204:
            log_status(f"Failed to send Discord notification: {resp.status_code} {resp.text}", "error")

    except Exception as e:
        log_status(f"Error sending Discord notification: {e}", "error")

def check_website():
    global last_status

    log_status("Checking LuxLine website for updates...", "info")
    try:
        response = requests.get(WEBSITE_URL, timeout=10)
        status = response.status_code
        speed = response.elapsed.total_seconds()

        log_status(f"Website responded with status {status} in {speed:.2f} seconds", "info")

        if speed > 2:
            log_status(f"Slow response time ({speed:.2f} seconds)", "warning")

        if status == 200:
            log_status(f"Website is up", "info")

            if last_status != "UP":
                send_discord_notification(f"Website UP: {WEBSITE_URL}")
                last_status = "UP"

        else:
            log_status(f"Website returned status {status}", "error")

            if last_status != "DOWN":
                send_discord_notification(f"Website DOWN: {WEBSITE_URL}\nStatus code: {status}")
                last_status = "DOWN"

    except Exception as e:
        log_status(f"Error checking website: {e}", "error")

        if last_status != "DOWN":
            send_discord_notification(f"Website DOWN: {WEBSITE_URL}\nError: {e}")
            last_status = "DOWN"

    log_status("Finished checking LuxLine website.", "info")
    

def log_status(message, level="info"):
    """
    Log a status message.
    """
    if level == "info":
        logger.info(message)
    elif level == "error":
        logger.error(message)
    elif level == "warning":
        logger.warning(message)

def main():
    """
    Main loop: checks the website at regular intervals.
    """
    setup_logger()
    log_status("Starting website monitor...", "info")
    while True:
        check_website()
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()