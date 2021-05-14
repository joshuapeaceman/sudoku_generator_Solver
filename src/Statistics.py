class Statistics:
    def __init__(self, app_ctrl):
        self.app_ctrl = app_ctrl
        self.empty_fields_cnt = 0

        self.game_creation_start_time = 0
        self.game_creation_end_time = 0

        self.game_start_time = 0
        self.game_end_time = 0
        self.game_played_time = 0

    def calculate_game_creation_time(self):
        self.app_ctrl.mainWindow.generation_time.setText(str(round(self.game_creation_end_time-self.game_creation_start_time, 3)))


    def calculate_game_played_time(self):
        self.game_played_time = self.game_end_time - self.game_start_time
        print('You played this game for:', self.game_played_time)

    def how_many_fields_are_empty(self):
        self.app_ctrl.mainWindow.empty_fields.setText(str(self.empty_fields_cnt))
