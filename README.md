![nostrmeshlogo](https://github.com/lnbits/nostrmesh/assets/33088785/8634277b-79ab-4a96-b8d1-3fbe44f35fd4)

## Self-Heaing ESP32 Nostr-Arduino Based Mesh-Network

The similicty of the nostr-protocol, makes it ieal for use with mesh-networking.

While utilizing WiFi for node connections imposes a range limitation of less than 200 meters, it significantly boosts bandwidth, thereby enabling the sharing of internet access across the mesh network.

ESP32 microcontrollers are both highly affordable and widely accessible. With a mere $1 cost for the basic controller, nodes can be effortlessly integrated into passive electronics such as light bulbs, facilitating the creation of a robust mesh network.

##### Each node has the ability to:
* Establish a WiFi station
* Set up a web server
* Initialize a websocket connection
* Connect to a websocket
* Enable a stateless relay for sending and receiving events
* Act as a nostr client (optional: applicable when the microcontroller is utilized in an IoT device, such as a weather station for data posting)

## Comparison with Current Systems

ESP-MDF (ESP Mesh Development Framework) and MQTT (Message Queuing Telemetry Transport) are the two popular approaches to creating mesh networks with ESP32 microcontrollers.

* *ESP-MDF (ESP Mesh Development Framework):* ESP-MDF is a comprehensive mesh development framework provided by Espressif Systems specifically for ESP32 microcontrollers. It is built on top of the ESP-IDF (ESP32 IoT Development Framework) and provides a high-level API for creating and managing mesh networks. ESP-MDF supports the ESP-MESH protocol, which is based on the IEEE 802.11s standard, enabling devices to form self-healing and self-organizing mesh networks. The framework includes features such as automatic topology construction, network management, and remote configuration. ESP-MDF simplifies the development process by providing a set of tools and APIs to handle mesh network operations, allowing developers to focus on the application logic rather than the underlying mesh infrastructure.

* *MQTT (Message Queuing Telemetry Transport) Protocol:* MQTT is a lightweight and efficient messaging protocol commonly used in IoT applications. It can also be leveraged to create mesh networks with ESP32 microcontrollers. In this approach, each ESP32 node in the mesh network can act as both a publisher and a subscriber. The nodes connect to a central MQTT broker, which manages the message distribution across the network. MQTT's publish-subscribe model enables easy communication between nodes, allowing data to be efficiently shared. MQTT supports topics, which act as message channels, enabling data organization and efficient filtering of relevant messages. This approach provides flexibility in terms of network architecture and allows for the integration of other MQTT-enabled devices in the mesh network.

## Nostrmesh Examples

### Single node

The node will wait and search for other nodes to connect to.

![mesh1](https://github.com/lnbits/nostrmesh/assets/33088785/e62b090f-b6b2-4e9a-afda-8f330c6c2f35)

### Connecting to a node

To connect to a peer a node must: 
* be in close enough proximit
* share a similar SSID and identical WiFi password

```
WiFi station format:
SSID: <shared-mesh-key>-<node-id>
Password: <shared-mesh-password>
```

Once connected to a peer the node will subscribe to the other nodes stateless nostr relay, hosted at `127.0.0.1:4545`

The opening event request-header `User-Agent` must be set as a `nostrmesh node`

![mesh2](https://github.com/lnbits/nostrmesh/assets/33088785/e6298f00-27c9-4952-bf83-73b8b9312043)

### Scaling

The node will continue to look for other nodes to connect to.

![mesh3](https://github.com/lnbits/nostrmesh/assets/33088785/323bfbd9-7b9b-4810-8026-0b43e51d17e8)

### Seperating and self-healing

If a mesh is seperated by a noe failing or being seperated by too great a distane, the mesh will turn into multiple networks.

With the nodes always looking for peers to connevct to, the mesh will self-heal.

![mesh4](https://github.com/lnbits/nostrmesh/assets/33088785/9b5f9837-b509-4ca9-84d9-c860577cbc9a)

### Mapping, Unicast, broadcast

External devices can connect to any node using the nodes `SSID`, `WiFi password` and then the nodes relay on `127.0.0.1:4545`. 

**Mapping:** 
When a device connects to a node that is not `User-Agent: nostrmesh node`, the node being connected to publishes `NIP-01` event with content simply set as `"content": "map"`, all nodes then publish a `NIP-01` event listing the nodes they are directly connected to 
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

**Broadcast:** 
Every node has a client so can publish events to be shared by the mesh as a whole

**Unicast:** 
Using the network map and a 


![mesh5](https://github.com/lnbits/nostrmesh/assets/33088785/3be3f3e7-aa8c-49b7-a0b5-7b9522f3930d)
