"""
This is a sample IDA plugin demonstrating a basic structure.
"""

import idaapi  # pylint: disable=import-error
import idautils  # pylint: disable=import-error
import idc  # pylint: disable=import-error


class SamplePlugin(idaapi.plugin_t):
    """
    Sample IDA Plugin that demonstrates plugin creation and basic API usage.
    """

    flags = 0
    comment = "Sample IDA Plugin"
    help = "This plugin demonstrates a basic IDA plugin structure."
    wanted_name = "Sample Plugin"
    wanted_hotkey = "Ctrl-Shift-S"

    def init(self):
        """Initializes the plugin."""
        return idaapi.PLUGIN_OK

    def run(self, arg):  # pylint: disable=unused-argument
        """
        Runs the plugin.
        Args:
            arg: Argument passed to the plugin on run.
        """
        for func_ea in idautils.Functions():
            print(f"Function at 0x{func_ea:X}")

    def term(self):
        """Terminates the plugin."""
        print("Sample Plugin Terminated")

def PLUGIN_ENTRY():  # pylint: disable=invalid-name
    """Entry point for the IDA plugin."""
    return SamplePlugin()