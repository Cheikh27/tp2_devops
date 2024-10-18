import http.server
import socketserver

PORT = 8080  # Le port sur lequel le serveur écoutera

# Définir le gestionnaire qui va servir le fichier HTML
handler = http.server.SimpleHTTPRequestHandler

# Crée un serveur avec le gestionnaire et le port spécifiés
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serveur démarré à l'adresse http://localhost:{PORT}")
    print("Appuyez sur Ctrl+C pour arrêter le serveur.")
    httpd.serve_forever()
