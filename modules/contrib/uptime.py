# pylint: disable=C0111,R0903

"""Displays the system uptime."""

from datetime import timedelta

import core.module
import core.widget

class Module(core.module.Module):
    def __init__(self, config):
        super().__init__(config, core.widget.Widget(self.output))
        self.__uptime = ''

    def output(self, _):
        return '{}'.format(self.__uptime)

    def update(self):
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = int(float(f.readline().split()[0]))
            self.__uptime = timedelta(seconds = uptime_seconds)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
