from typing import Set


class PortRange():
    ports: Set[int]

    def __init__(self, desc: str):
        self.ports = self.parse(desc)

    def update(self, new_desc: str):
        new_ports = self.parse(new_desc)
        self.ports = self.ports.union(new_ports)

    @staticmethod
    def parse(desc: str) -> Set[int]:
        '''
        Parse a port range description into a set of ports.

        Accept: 

        comma-separated list of ports combined with port ranges.

        Examples:

        - 80,443,8080-8090

        - 9,7070-6060,3
        '''

        ports = set()
        raw_ports = desc.split(',')
        for raw_port in raw_ports:
            if '-' in raw_port:
                start, end = raw_port.split('-')
                if int(start) > int(end):
                    start, end = end, start
                ports.update(range(int(start), int(end) + 1))
            else:
                ports.add(int(raw_port))
        return ports

    def __str__(self):
        return str(self.ports)

    def __contains__(self, port: int) -> bool:
        return port in self.ports
