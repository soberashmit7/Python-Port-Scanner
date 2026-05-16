import tkinter as tk
import socket
import threading

socket.setdefaulttimeout(0.5)

scanning = False


def run_scan(target_ip, start_port, end_port):

    global scanning

    output_text.insert(
        tk.END,
        f"Scanning {target_ip}...\n\n"
    )

    open_ports = 0
    results = []

    for port in range(start_port, end_port + 1):

        if not scanning:

            output_text.insert(
                tk.END,
                "\nSCAN STOPPED\n"
            )

            break

        output_text.insert(
            tk.END,
            f"Scanning Port {port}...\n"
        )

        output_text.see(tk.END)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        result = sock.connect_ex((target_ip, port))

        if result == 0:

            open_ports += 1

            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            result_text = f"Port {port} is OPEN ({service})"

            output_text.insert(
                tk.END,
                result_text + "\n"
            )

            results.append(result_text)

        sock.close()

    if scanning:

        output_text.insert(
            tk.END,
            f"\nSCAN COMPLETED\nTotal Open Ports Found: {open_ports}\n"
        )

        with open("scan_results.txt", "w") as file:

            for result in results:
                file.write(result + "\n")

        output_text.insert(
            tk.END,
            "\nResults saved to scan_results.txt\n"
        )


def start_scan():

    global scanning

    scanning = True

    output_text.delete(1.0, tk.END)

    target = target_entry.get()

    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())

    except:

        output_text.insert(
            tk.END,
            "Please enter valid port numbers\n"
        )

        return

    try:
        target_ip = socket.gethostbyname(target)

    except:

        output_text.insert(
            tk.END,
            "Invalid Target\n"
        )

        return

    scan_thread = threading.Thread(
        target=run_scan,
        args=(target_ip, start_port, end_port)
    )

    scan_thread.start()


def stop_scan():

    global scanning

    scanning = False


window = tk.Tk()

window.configure(bg="#1e1e1e")

window.title("Python Port Scanner")

window.geometry("700x650")


title_label = tk.Label(
    window,
    text="PYTHON PORT SCANNER",
    font=("Arial", 18),
    bg="#1e1e1e",
    fg="cyan"
)

title_label.pack(pady=20)


target_label = tk.Label(
    window,
    text="Enter Target IP or Website:",
    bg="#1e1e1e",
    fg="white"
)

target_label.pack()


target_entry = tk.Entry(
    window,
    width=40,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)

target_entry.pack(pady=10)


start_port_label = tk.Label(
    window,
    text="Start Port:",
    bg="#1e1e1e",
    fg="white"
)

start_port_label.pack()


start_port_entry = tk.Entry(
    window,
    width=20,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)

start_port_entry.pack(pady=5)


end_port_label = tk.Label(
    window,
    text="End Port:",
    bg="#1e1e1e",
    fg="white"
)

end_port_label.pack()


end_port_entry = tk.Entry(
    window,
    width=20,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)

end_port_entry.pack(pady=5)


scan_button = tk.Button(
    window,
    text="Start Scan",
    command=start_scan,
    bg="#00bcd4",
    fg="black",
    font=("Arial", 10, "bold")
)

scan_button.pack(pady=10)


stop_button = tk.Button(
    window,
    text="Stop Scan",
    command=stop_scan,
    bg="red",
    fg="white",
    font=("Arial", 10, "bold")
)

stop_button.pack(pady=10)


text_frame = tk.Frame(window)

text_frame.pack(pady=10)


scrollbar = tk.Scrollbar(text_frame)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


output_text = tk.Text(
    text_frame,
    height=20,
    width=80,
    yscrollcommand=scrollbar.set,
    bg="black",
    fg="#00ff00",
    insertbackground="white"
)

output_text.pack(side=tk.LEFT)


scrollbar.config(command=output_text.yview)


window.mainloop()