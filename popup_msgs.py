# ba_meta require api 7
import ba, _ba
from bastd.ui.party import PartyWindow
from bastd.actor import popuptext

#   Примечание: у хоста должен быть открыт чат 

old__init__ = PartyWindow.on_chat_message
def chat_handler(self, msg: str) -> None:
        old__init__(self, msg)
        if _ba.get_foreground_host_activity():
            player_name = msg.split(': ')[0]
            last_msg = msg.split(': ')[-1]
            PopupMsg().show_popup(player_name, last_msg)
PartyWindow.on_chat_message = chat_handler

class PopupMsg:
    def __init__(self):
        pass

    def get_pos(self, name):
        activity = _ba.get_foreground_host_activity()
        for player in activity.players:
            if player.getname(False, False) == name:
                position = player.position
                return position
        return None

    def show_popup(self, player_name, text):
        activity = _ba.get_foreground_host_activity()
        position = self.get_pos(player_name)
        if position:
            with ba.Context(activity):
                self.popup = popuptext.PopupText(
                    text=text,
                    position=position,
                    color=(1.0, 1.0, 1.0),
                    scale=1.5
                ).autoretain()

# ba_meta export plugin
class ByFlou(ba.Plugin):
    pass
