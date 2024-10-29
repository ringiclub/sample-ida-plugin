import idaapi
import idautils
import idc

class SamplePlugin(idaapi.plugin_t):
    flags = 0
    comment = "Sample IDA Plugin"
    help = "This plugin demonstrates a basic IDA plugin structure."
    wanted_name = "Sample Plugin"
    wanted_hotkey = "Ctrl-Shift-S"

    def init(self):
        return idaapi.PLUGIN_OK

    def run(self, arg):
        for func_ea in idautils.Functions():
            print(f"Function at 0x{func_ea:X}")

    def term(self):
        print("Sample Plugin Terminated")

def PLUGIN_ENTRY():
    return SamplePlugin()
