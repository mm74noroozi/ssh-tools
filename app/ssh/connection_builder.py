from subprocess import Popen,PIPE
from .models import Host

class ConnectionBuilder:
    def __init__(self) -> None:
        self.connection = None
    def up(self,host_id):
        if self.connection:
            self.down()
        host = Host.objects.get(id=host_id)
        self.connection = Popen(f"ssh -D1080 -N root@{host.address} -p {host.port} ping",shell=True,stdout=PIPE)

    def down(self):
        self.connection.close()