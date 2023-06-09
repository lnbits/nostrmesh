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


![mesh1](https://github.com/lnbits/nostrmesh/assets/33088785/e62b090f-b6b2-4e9a-afda-8f330c6c2f35)

![mesh2](https://github.com/lnbits/nostrmesh/assets/33088785/99f115c0-18d9-425f-ad7a-747bed39928a)

![mesh3](https://github.com/lnbits/nostrmesh/assets/33088785/323bfbd9-7b9b-4810-8026-0b43e51d17e8)

![mesh4](https://github.com/lnbits/nostrmesh/assets/33088785/9b5f9837-b509-4ca9-84d9-c860577cbc9a)

![mesh5](https://github.com/lnbits/nostrmesh/assets/33088785/3be3f3e7-aa8c-49b7-a0b5-7b9522f3930d)
