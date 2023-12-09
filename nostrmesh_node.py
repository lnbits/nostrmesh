import socket
import threading
import json
import time

class NostrmeshNode:
    def __init__(self, node_id, mesh_key, mesh_password):
        self.node_id = node_id
        self.mesh_key = mesh_key
        self.mesh_password = mesh_password
        self.ssid = f"{mesh_key}-{node_id}"
        self.port = 4545
        self.neighbors = set()
        self.relay_server_address = ('127.0.0.1', self.port)
        self.mapping = []

    def start(self):
        self.start_wifi_station()
        self.start_relay_server()
        self.start_mapping_broadcast()

    def start_wifi_station(self):
        # Implement WiFi station setup here using self.ssid and self.mesh_password
        print(f"Node {self.node_id} connected to WiFi with SSID: {self.ssid}")

    def start_relay_server(self):
        server_thread = threading.Thread(target=self.relay_server)
        server_thread.start()

    def relay_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind(('0.0.0.0', self.port))

        while True:
            data, addr = server.recvfrom(1024)
            message = data.decode('utf-8')
            self.handle_message(message)

    def start_mapping_broadcast(self):
        mapping_thread = threading.Thread(target=self.broadcast_mapping)
        mapping_thread.start()

    def broadcast_mapping(self):
        while True:
            mapping_message = json.dumps({
                "node-id": self.node_id,
                "friends": ",".join(map(str, self.neighbors))
            })
            self.send_message("map", mapping_message)
            time.sleep(10)  # Adjust the frequency based on your needs

    def send_message(self, tag, content):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto(f"{tag}: {content}".encode('utf-8'), self.relay_server_address)

    def handle_message(self, message):
        # Implement message handling logic based on your protocol
        print(f"Node {self.node_id} received message: {message}")

# Example of usage
node1 = NostrmeshNode(1, "mesh_key", "mesh_password")
node2 = NostrmeshNode(2, "mesh_key", "mesh_password")

node1.neighbors.add(node2.node_id)
node2.neighbors.add(node1.node_id)

node1.start()
node2.start()

# Communication test
node1.send_message("unicast", "Hello, Node 2!")
