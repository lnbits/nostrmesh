![nostrmeshlogo](https://github.com/lnbits/nostrmesh/assets/33088785/8634277b-79ab-4a96-b8d1-3fbe44f35fd4)

## Self-Heaing ESP32 <a href="https://github.com/lnbits/arduino-nostr">Nostr-Arduino</a> Based Mesh-Network

The similicty of the <a href="https://github.com/nostr-protocol/nostr">nostr-protocol</a>, makes it ieal for use with mesh-networking.

While utilizing WiFi for node connections imposes a range limitation of less than 200 meters, it significantly boosts bandwidth, thereby enabling the sharing of internet access across the mesh network.

ESP32 microcontrollers are both highly affordable and widely accessible. With a mere $1 cost for the basic controller, nodes can be effortlessly integrated into passive electronics such as light bulbs, facilitating the creation of a robust mesh network.

##### Each nostrmesh node has the ability to:
* Establish a WiFi station
* Set up a websocket server
* Connect to a websocket
* Run a stateless nostr relay for sending and receiving events using <a href="https://github.com/lnbits/arduino-nostr">Nostr-Arduino</a>
* Run a nostr client using <a href="https://github.com/lnbits/arduino-nostr">Nostr-Arduino</a>

## Comparison with Current Systems

<a href="https://github.com/espressif/esp-mdf">ESP-MDF</a> (ESP Mesh Development Framework) and <a href="https://mqtt.org/">MQTT</a>  (Message Queuing Telemetry Transport) are the two popular approaches to creating mesh networks with ESP32 microcontrollers.

* *ESP-MDF (ESP Mesh Development Framework):* ESP-MDF is a comprehensive mesh development framework provided by Espressif Systems specifically for ESP32 microcontrollers. It is built on top of the ESP-IDF (ESP32 IoT Development Framework) and provides a high-level API for creating and managing mesh networks. ESP-MDF supports the ESP-MESH protocol, which is based on the IEEE 802.11s standard, enabling devices to form self-healing and self-organizing mesh networks. The framework includes features such as automatic topology construction, network management, and remote configuration. ESP-MDF simplifies the development process by providing a set of tools and APIs to handle mesh network operations, allowing developers to focus on the application logic rather than the underlying mesh infrastructure.

* *MQTT (Message Queuing Telemetry Transport) Protocol:* MQTT is a lightweight and efficient messaging protocol commonly used in IoT applications. It can also be leveraged to create mesh networks with ESP32 microcontrollers. In this approach, each ESP32 node in the mesh network can act as both a publisher and a subscriber. The nodes connect to a central MQTT broker, which manages the message distribution across the network. MQTT's publish-subscribe model enables easy communication between nodes, allowing data to be efficiently shared. MQTT supports topics, which act as message channels, enabling data organization and efficient filtering of relevant messages. This approach provides flexibility in terms of network architecture and allows for the integration of other MQTT-enabled devices in the mesh network.

## Nostrmesh

### Connecting to a node

![mesh2](https://github.com/lnbits/nostrmesh/assets/33088785/e6298f00-27c9-4952-bf83-73b8b9312043)

To connect to a peer a node must: 
* Be in close enough proximity
* Share a "similar" SSID and identical WiFi password

```
WiFi station format:
SSID: <shared-mesh-key>-<node-id>
Password: <shared-mesh-password>
```

Once connected to a node a node will subscribe to the other nodes nostr relay (hosted at `127.0.0.1:4545`)

The opening event request-header `User-Agent` must be set as a `"nostrmesh node"`

### Scaling

![mesh3](https://github.com/lnbits/nostrmesh/assets/33088785/323bfbd9-7b9b-4810-8026-0b43e51d17e8)

The nodes will continue to look for other nodes to connect to. Each node will connect to the 3 nodes with the strongest WiFi signal

### Separating/healing

![mesh4](https://github.com/lnbits/nostrmesh/assets/33088785/9b5f9837-b509-4ca9-84d9-c860577cbc9a)

the mesh can be separated into multiple networks.

If networks sharing the same `<shared-mesh-key>` are in close enough they will heal.

### Mapping, Unicast, broadcast

![mesh5](https://github.com/lnbits/nostrmesh/assets/33088785/3be3f3e7-aa8c-49b7-a0b5-7b9522f3930d)

External devices can connect to any node using the nodes `SSID`, `WiFi password` and then the nodes relay on `127.0.0.1:4545`. 

To share data through the network `tag: r` proposed here https://github.com/nostr-protocol/nips/pull/594, or something similar will used.

##### Mapping: 
When a device connects to a node that is not `User-Agent: nostrmesh node`, the node being connected publishes `NIP-01` event with content simply set as `"content": "map"`, all nodes then publish from there clients a `NIP-01` event listing the nodes they are directly connected to 
```
{"node-id": <node-id>, "friends": "<node-id>,<node-id>,<node-id>"}
```
Each node builds a json map of the netork from the data. 
```
[
{"node-id": <node-id>, "pubkey": <nodes-public-key>, "friends": "<node-id>,<node-id>,<node-id>"}, 
{"node-id": <node-id>, "pubkey": <nodes-public-key>, "friends": "<node-id>,<node-id>,<node-id>"}
]
```
##### Broadcast/unicast:

Using <a href="https://github.com/lnbits/nostrmesh/blob/main/README.md#mapping">mapping</a>, and something like `tag: r`, a client can send data in a unicast or broadcast way through the relay network.
