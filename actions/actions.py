
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class Actionlocationlink(Action):

    def name(self) -> Text:
        return "action_location_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        loc = next(tracker.get_latest_entity_values("location"), None)
         
        if loc=="India":
            msg = f"India Openings - https://kanini.com/open-positions/#india-openings/"
        elif loc=="USA":
            msg = "US Openings - https://kanini.com/open-positions/#us-openings"
        elif loc=="Ukraine":
            msg = "Ukraine Openings - https://kanini.com/open-positions/#ukraine-openings"
        
        dispatcher.utter_message(text=msg)

        return []
