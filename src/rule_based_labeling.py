# --- Function to find matching phrases in text ---
import re
def find_matched_phrases(text, phrase_dict):
    """
    Finds which phrases from a dictionary are present in a given text.
    
    The phrases in the dictionary are treated as regular expression patterns,
    allowing for flexible matching (e.g., handling gendered pronouns).
    """
    matches = []
    # No need to lower the text here, as re.search can do it case-insensitively
    
    for phrase_pattern in phrase_dict:
        # The use of \b for word boundaries is an excellent practice!
        pattern = r'\b' + phrase_pattern + r'\b'
        
        if re.search(pattern, text, flags=re.IGNORECASE):
            # Append the original pattern from the dictionary if a match is found
            matches.append(phrase_pattern)
            
    return matches

# --- Function to score the list of flags with a clear hierarchy ---

def find_highest_risk_label(flag_list, phrase_dict):
    # Default to 'Low' if there are no flags, or if only low-risk flags are found
    final_risk = 'low'

    for phrase in flag_list:
        risk = phrase_dict.get(phrase)
        if risk == 'high':
            return 'high' # If we find any High risk flag, we're done. It's High.
        if risk == 'medium':
            final_risk = 'medium' # If we find a Medium, we note it, but keep looking for a High.

    return final_risk # Will be 'Medium' if a medium was found, otherwise 'Low'

