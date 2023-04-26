from octoprint.plugin import Plugin, EventHandlerPlugin, AssetPlugin
import time
import threading

class BedTempMonitor(Plugin, EventHandlerPlugin, AssetPlugin):

    def __init__(self):
        self._monitor_thread = None

    def on_event(self, event, payload):
        if event == "GcodeProcessing":
            self._process_gcode(payload["gcode"])

    def _process_gcode(self, gcode):
        keyword = "WAIT_FOR_BED_TEMP"
        if keyword in gcode:
            try:
                target_temp = float(gcode.split(keyword)[-1].strip())
            except ValueError:
                self._logger.error(f"Unable to parse target temperature from GCODE: {gcode}")
                return

            self._logger.info(f"Waiting for bed temperature to reach {target_temp}°C")
            self._wait_for_bed_temp(target_temp)
            self._logger.info(f"Bed temperature reached {target_temp}°C, resuming operation")

    def _wait_for_bed_temp(self, target_temp):
        while True:
            bed_temp = self._printer.get_current_temperatures()["bed"]["actual"]
            if bed_temp <= target_temp:
                break
            self._send_notification(f"Waiting for bed temperature to reach {target_temp}°C. Current bed temperature: {bed_temp}°C")
            time.sleep(5)

    def _send_notification(self, message):
        self._plugin_manager.send_plugin_message(__plugin_name__, {"type": "notification", "message": message})

    def get_assets(self):
        return {
            "clientjs": ["bed_temp_monitor.js"]
        }

__plugin_name__ = "Bed Temperature Monitor"
__plugin_pythoncompat__ = ">=3,<4"
def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = BedTempMonitor()

    global __plugin_hooks__
    __plugin_hooks__ = {}
