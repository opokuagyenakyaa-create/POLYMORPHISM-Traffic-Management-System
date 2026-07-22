class TrafficDevice:
    def __init__(self, name):
        self.name = name

    def activate(self):
        print(f"{self.name} activated")


class TrafficLight(TrafficDevice):
    def __init__(self, name):
        super().__init__(name)

    def activate(self):
        print(f"{self.name}: Switching lights - Red, Yellow, Green")


class SpeedCamera(TrafficDevice):
    def __init__(self, name):
        super().__init__(name)

    def activate(self):
        print(f"{self.name}: Scanning vehicles and recording speed")


class PedestrianSignal(TrafficDevice):
    def __init__(self, name):
        super().__init__(name)

    def activate(self):
        print(f"{self.name}: Walk signal ON - Safe to cross")


class EmergencySiren(TrafficDevice):
    def __init__(self, name):
        super().__init__(name)

    def activate(self):
        print(f"{self.name}: EMERGENCY - All vehicles stop immediately")


light = TrafficLight("Main Street Light")
camera = SpeedCamera("Highway Camera")
signal = PedestrianSignal("Junction Signal")
siren = EmergencySiren("Emergency Siren")

devices = [light, camera, signal, siren]

for device in devices:
    device.activate()
