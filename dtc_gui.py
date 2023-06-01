# Made by TyDev lmao
import tkinter as tk
import discord

class DiscordClient(discord.Client):
    def __init__(self, token):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.token = token

    async def on_ready(self):
        print(f"Logged in as {self.user.name} ({self.user.id})")

    async def send_message(self, channel_id, message):
        channel = self.get_channel(channel_id)
        if channel:
            await channel.send(message)
            print("Message sent successfully.")
        else:
            print("Error: Channel not found.")

class DTCGUI(tk.Tk):
    def __init__(self, token):
        tk.Tk.__init__(self)
        self.title("Discord Token Control")
        self.token = token

        self.create_widgets()

        self.client = DiscordClient(self.token)
        self.client.run(self.token)

    def create_widgets(self):
        self.info_label = tk.Label(self, text="Connecting to Discord...", padx=10, pady=10)
        self.info_label.pack()

        self.input_entry = tk.Entry(self, width=50)
        self.input_entry.pack()

        self.send_button = tk.Button(self, text="Send", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        message = self.input_entry.get()

        # Replace CHANNEL_ID_HERE with the desired channel ID (USE DISCORD WEB OR ENABLE DEV TOOLS IN SETTINGS)
        channel_id = CHANNEL_ID_HERE
        self.client.loop.create_task(self.client.send_message(channel_id, message))

        self.info_label.config(text="Message sent successfully.")

if __name__ == "__main__":
    # Add your Discord token here
    token = "DISCORD_TOKEN_HERE"

    app = DTCGUI(token)

    app.mainloop()