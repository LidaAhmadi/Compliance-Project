# --- Libraries ---
import re

# --- Phrase Matching Function ---
def find_matched_phrases(text, phrase_dict):
    """
    Finds which phrases from a dictionary are present in a given text.
    The phrases in the dictionary are treated as regular expression patterns.
    """
    # Safety check: If the input text is empty or not a string, return an empty list.
    if not text or not isinstance(text, str):
        return []

    matches = []
    for phrase_pattern in phrase_dict:
        try:
            # Use word boundaries (\b) to match whole words/phrases.
            pattern = r'\b' + phrase_pattern + r'\b'
            if re.search(pattern, text, flags=re.IGNORECASE):
                matches.append(phrase_pattern)
        except re.error:
            # This handles cases where a pattern in the CSV might be an invalid regex.
            continue
            
    return matches

# --- Triage Model Function ---
def find_highest_risk_label(matched_phrases_list, rule_lookup_dict):
    """
    Finds the single most severe risk label from a list of matched phrases.
    If the list is empty, it assumes no risk was found and returns 'low'.
    The order of severity is: high > medium > low.
    """
    # Find the unique set of labels for all phrases found in the text.
    found_labels = {rule_lookup_dict.get(phrase) for phrase in matched_phrases_list}

    # --- Triage Logic ---
    if 'high' in found_labels:
        return 'high'
    elif 'medium' in found_labels:
        return 'medium'
    elif 'low' in found_labels:
        return 'low'
    else:
        # If no phrases were found, or found phrases had no matching label, it's low risk.
        return 'low'
