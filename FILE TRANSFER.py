import http.server
import socketserver
import os
import time
from rich.console import Console
from rich.panel import Panel

console = Console()

PORT = 8000
handler = http.server.SimpleHTTPRequestHandler

# server start hone ka animation
def animated_startup():
    console.print(Panel.fit(" File Transfer Server Starting... ", style="bold cyan"))
    for i in range(1, 101, 10):
        time.sleep(0.1)
        console.print(f"[green]Loading: {i}%[/green]", end="\r")
    console.print("\n[bold green]Server Ready![/bold green]\n")

# dashboard dikhane ke liye
def dashboard():
    console.print(Panel.fit(f"Sharing Directory: {os.getcwd()}", style="bold magenta"))
    console.print("[blue]Recent Files in Directory:[/blue]")
    files = os.listdir('.')
    for f in files[-5:]:
        console.print(f" - {f}")

# animation aur dashboard call
animated_startup()
dashboard()

# file server start
with socketserver.TCPServer(("", PORT), handler) as http:
    console.print(f"[bold green] File Transfer Server Running on Port {PORT}[/bold green]")
    console.print("[bold cyan]Browser me kholein:[/bold cyan] http://localhost:8000\n")
    http.serve_forever()
