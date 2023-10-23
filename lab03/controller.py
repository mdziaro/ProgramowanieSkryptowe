from model import MoveDirection

class OptionsParser:
    @staticmethod
    def parse(args):
        valid_directions = {
            "FORWARD": MoveDirection.FORWARD,
            "BACKWARD": MoveDirection.BACKWARD,
            "LEFT": MoveDirection.LEFT,
            "RIGHT": MoveDirection.RIGHT
        }
        parsed_directions = []

        for arg in args:
            if arg in valid_directions:
                parsed_directions.append(valid_directions[arg])

        return parsed_directions
