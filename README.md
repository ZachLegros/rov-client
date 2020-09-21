# rov-client

This is the client code written in python and running on a laptop for my underwater remotely operated vehicule (ROV).
Once a connection is established with the main computer (Raspberry Pi Server), the client reads the inputs comming from a Xbox One controller and maps the wanted values
to bytes. Then, the bytes representing the controls of the ROV are sent to the server and the bytes from the server containing the telemetry data are read.

The index.html file is displaying the livestream from the main computer and the telemetry data from the Arduino. 
