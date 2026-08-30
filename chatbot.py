import json
import re
import string

class StudentChatbot:
    def __init__(self, intents_path="intents.json", responses_path="responses.json"):
        self.intents = self._load_json(intents_path)
        self.responses = self._load_json(responses_path)

    def _load_json(self, file_path):
        """JSON files ko safely load karne ke liye exception handling."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from '{file_path}'.")
            return {}

    def clean_text(self, text):
        """
        Text Preprocessing:
        1. Lowercase conversion
        2. Punctuation removal
        3. Space stripping
        """
        if not text:
            return ""
        text = text.lower().strip()
        text = text.translate(str.maketrans("", "", string.punctuation))
        return text

    def detect_intent(self, user_input):
        """Keyword matching aur query comparison se intent match karna."""
        cleaned_input = self.clean_text(user_input)
        if not cleaned_input:
            return None

        words = cleaned_input.split()

        # Direct pattern matching
        for intent, patterns in self.intents.items():
            for pattern in patterns:
                pattern_clean = self.clean_text(pattern)
                if pattern_clean in cleaned_input or any(word == pattern_clean for word in words):
                    return intent

        return "fallback"

    def get_response(self, user_input):
        """Intent ke basis par response deliver karna."""
        try:
            intent = self.detect_intent(user_input)
            if intent is None:
                return "Please enter a valid message."
            return self.responses.get(intent, self.responses.get("fallback"))
        except Exception as e:
            return "Bot Error: Something went wrong while processing your request."
