from mycroft import MycroftSkill, intent_file_handler


class RoverController(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('controller.rover.intent')
    def handle_controller_rover(self, message):
        self.speak_dialog('controller.rover')


def create_skill():
    return RoverController()

