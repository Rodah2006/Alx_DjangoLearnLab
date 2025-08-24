from pyngrok import ngrok

# Connect ngrok to port 8000
public_url = ngrok.connect(8000)
print("Public URL:", public_url)

# Keep the tunnel open
ngrok_process = ngrok.get_ngrok_process()
ngrok_process.proc.wait()
