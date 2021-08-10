import datetime

# Store the next available id for all new notes
last_id = 0


class Note:
    """Represent a note in the notebook. Match against a
    string in searches and store tags for each note."""

    def __init__(self, memo, tags=""):
        """initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id."""
        pass

    def match(self, filter):
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and
        tags."""
        pass


class Notebook:
    """Represent a collection of notes that can be tagged,
    modified, and searched."""

    def __init__(self):
        """Initialize a notebook with an empty list."""
        pass

    def new_note(self, memo, tags=""):
        """Create a new note and add it to the list."""
        pass

    def _find_note(self, note_id):
        """Locate the note with the given id."""
        pass


    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its
        memo to the given value."""
        pass

    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its
        tags to the given value."""
        pass

    def search(self, filter):
        """Find all notes that match the given filter
        string."""
        pass
