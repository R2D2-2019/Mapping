from client.comm import BaseComm
from common.frame_enum import FrameType
from common.base_module import BaseModule

class Module(BaseModule):

    def __init__(self, comm: BaseComm):
        super(Module, self).__init__(comm)
        #self.comm.listen_for([FrameType.>geef_frametype<])

    def process(self):
        while self.comm.has_data():
            frame = self.comm.get_data()

            if frame.request:
                continue

            if frame["state"]:
               
            else:
                