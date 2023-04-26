$(function () {
    function BedTempMonitorViewModel(parameters) {
        var self = this;
        self.onDataUpdaterPluginMessage = function (plugin, data) {
            if (plugin !== "bed_temperature_monitor") {
                return;
            }

            if (data.type === "notification") {
                new PNotify({
                    title: "Bed Temperature Monitor",
                    text: data.message,
                    type: "info",
                    hide: false
                });
            }
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: BedTempMonitorViewModel,
        dependencies: [],
        elements: []
    });
});
