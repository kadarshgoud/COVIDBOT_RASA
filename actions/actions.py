# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
import logging, json

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

logger = logging.getLogger(__name__)

## action class for faq_spread_disease

class ActionFaqSpread(Action):
    def name(self) -> Text:
        return "action_faq_spread_disease"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_spread"]:
            message = {
                "type": "video",
                "payload": {
                    "title": "6 Steps to Prevent COVID-19",
                    "src": "https://www.youtube.com/embed/9Ay4u7OYOhA",
                },
            }
            dispatcher.utter_message(
                text="Take steps to lower your risk of getting sick with COVID-19. Here are some things you should do.",
                attachment=message,
            )
        return []