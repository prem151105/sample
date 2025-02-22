def main(args):
    print("Starting NewsPulse AI...")  # Add this line
    config = load_config()
    wordpress_config = {
        "url": config["wordpress_url"],
        "username": config["wordpress_username"],
        "password": config["wordpress_password"],
    }