from pyngrok import ngrok

# Port your Django server runs on
port = 8000

# Open a tunnel
public_url = ngrok.connect(port)
print("Public URL:", public_url)

# Keep the tunnel running
input("Press ENTER to exit...")
