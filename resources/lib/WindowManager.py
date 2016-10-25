# -*- coding: utf8 -*-

from Utils import *
import xbmcaddon

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_ICON = ADDON.getAddonInfo('icon')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_PATH = ADDON.getAddonInfo('path').decode("utf-8")
HOME_XML = "script-Main.xml"
SCHEDULE_DETAIL_XML = "script-ScheduleDetail.xml"
MATCH_SCHEDULE_XML = "script-MatchSchedule.xml"
MATCH_SCHEDULE_TIME_XML = "script-MatchScheduleTime.xml"
MATCH_FILTER_XML = "script-MatchFilterDialog.xml"


class WindowManager(object):

    def __init__(self):
        self.window_stack = []

    def add_to_stack(self, window):
        """
        add window / dialog to global window stack
        """
        self.window_stack.append(window)

    def pop_stack(self):
        """
        get newest item from global window stack
        """
        if self.window_stack:
            dialog = self.window_stack.pop()
            xbmc.sleep(300)
            dialog.doModal()

    def open_main_window(self, prev_window=None):
        """
        open main window, deal with window stack
        """
        import MainWindow
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        dialog = MainWindow.MainWin(HOME_XML, ADDON_PATH)
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        self.open_dialog(dialog, prev_window)

    def open_schedule_detail_window(self, prev_window=None):
        """
        open schedule detail window, deal with window stack
        """
        import ScheduleDetailWindow
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        dialog = ScheduleDetailWindow.ScheduleDetailWin(SCHEDULE_DETAIL_XML, ADDON_PATH)
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        self.open_dialog(dialog, prev_window)

    def open_match_schedule_window(self, name, channel, competitionId, prev_window=None):
        """
        open match schedule window, deal with window stack
        """
        import MatchScheduleWindow
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        dialog = MatchScheduleWindow.MatchScheduleWin(MATCH_SCHEDULE_XML, ADDON_PATH, name=name, channel=channel, competitionId=competitionId)
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        self.open_dialog(dialog, prev_window)

    def open_match_schedule_time_window(self, prev_window=None):
        """
        open match schedule time window, deal with window stack
        """
        import MatchScheduleTimeWindow
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        dialog = MatchScheduleTimeWindow.MatchScheduleTimeWin(MATCH_SCHEDULE_TIME_XML, ADDON_PATH)
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        self.open_dialog(dialog, prev_window)

    def show_match_filter_dialog(self, prev_window=None):
        """
        open match filter dialog, deal with window stack
        """
        from dialogs.DialogMatchFilter import MatchFilter
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        dialog = MatchFilter(MATCH_FILTER_XML, ADDON_PATH)
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        self.open_dialog(dialog, prev_window)

    def open_dialog(self, dialog, prev_window):
        if dialog:
            if prev_window:
                self.add_to_stack(prev_window)
                prev_window.close()
            dialog.doModal()
            self.pop_stack()
        else:
            notify(LANG(32143))

wm = WindowManager()
