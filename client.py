import os
import socket
import tkinter as tk

# Replace 'PC_IP_ADDRESS' and 'PC_PORT' with the actual IP address and port number of your PC
PC_IP_ADDRESS = '192.168.1.21'  # Replace with your PC's IP address
PC_PORT = 5555  # Replace with the port number you chose on the PC-side script

class StreamDeckApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stream Deck")

        # Use os.path.join for cross-platform compatibility
        image_paths = [os.path.join("Icons", "Steam.png"), os.path.join("Icons", "EpicGames.png"), os.path.join("Icons", "RazerSynapse.png"),
                       os.path.join("Icons", "Netflix.png"), os.path.join("Icons", "Youtube.png"), os.path.join("Icons", "Snapchat.png")]

        # Create buttons with icons
        for i, image_path in enumerate(image_paths):
            image = tk.PhotoImage(file=image_path)
            # Set the image as a reference to prevent it from being garbage-collected
            setattr(self, f"image_{i}", image)
            button = tk.Button(root, image=image, command=lambda idx=i: self.send_signal(idx))
            button.config(width=200, height=200, bd=0, highlightthickness=0)  # Set button size and remove borders
            button.grid(row=i // 3, column=i % 3, pady=5, padx=5)

            # Add colored spaces between the buttons
            if i % 3 != 2:
                separator = tk.Frame(root, width=5, height=50, background="black")
                separator.grid(row=i // 3, column=(i % 3) + 1)

        # Add console logging for debugging
        print("GUI initialized")

    def send_signal(self, action_index):
        try:
            # Connect to the PC
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((PC_IP_ADDRESS, PC_PORT))

            # Send the selected action to the PC (you can replace this with actual action names)
            actions = ['open_1', 'open_2', 'open_3', 'open_4', 'open_5', 'open_6']
            selected_action = actions[action_index]

            print(f"Sending signal: {selected_action}")

            client_socket.sendall(selected_action.encode())
            client_socket.close()

            print(f"Signal '{selected_action}' sent successfully")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    print("Starting Stream Deck Application")
    root = tk.Tk()
    app = StreamDeckApp(root)
    root.mainloop()
    print("Stream Deck Application closed")