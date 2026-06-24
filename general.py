class General:
    def __init__(self, general_id, is_traitor=False):
        self.general_id = general_id
        self.is_traitor = is_traitor

    def __str__(self):
        status = "Traitor" if self.is_traitor else "Loyal"
        return f"General {self.general_id} ({status})"