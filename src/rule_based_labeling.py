# --- Rule-based labeling function ---
def label_risk(text, label_dict):
    for phrase, label in label_dict.items():
        if phrase in text:
            return label
    return "low"  # Default label if no phrase matches


# --- Function to find matching phrases in text ---
def find_matched_phrases(text, phrase_dict):
    matches = []
    lowered_text = text.lower()
    for phrase in phrase_dict:
        if phrase.lower() in lowered_text:
            matches.append(phrase)
    return matches
