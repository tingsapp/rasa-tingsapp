# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# import arrow
# import dateparser
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
# from rasa_sdk.executor import CollectingDispatcher

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# city_db={
#     'brussels': 'Europe/Brussels',
#     'zagreb': 'Europe/Zagreb',
#     'london': 'Europe/London',
#     'lisbon': 'Europe/Lisbon',
#     'amsterdam': 'Europe/Amsterdam',
#     'seattle': 'US/Pacific'
# }

# class ActionTellTime(Action):
#     def name(self)->Text:
#         return 'action_tell_time'

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         current_place = next(tracker.get_latest_entity_values('place'),None)
#         utc = arrow.utcnow()

#         if not current_place:
#             msg = f"It's {utc.format('HH:mm')} utc now. You can also give me a place."
#             dispatcher.utter_message(text=msg)
#             return [SlotSet('place', None)]  # Reset the slot
        
#         tz_string = city_db.get(current_place, None)
#         if not tz_string:
#             msg = f"It's I didn't recognize {current_place}. Is it spelled correctly?"
#             dispatcher.utter_message(text=msg)
#             return [SlotSet('place', None)]  # Reset the slot
        
#         msg = f"It's {utc.to(city_db[current_place]).format('HH:mm')} in {current_place} now."
#         dispatcher.utter_message(text=msg)
#         return [SlotSet('place', None)]  # Reset the slot
