import json
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(PROJECT_ROOT)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import pygame

from turnset import Game


OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imitation_data.jsonl')


def main():
    game = Game(50, 50)
    try:
        game.run_by_AI(view_lock=False, collect_data=True)
    finally:
        try:
            if game.imitation_data:
                with open(OUTPUT_PATH, 'a', encoding='utf-8') as output_file:
                    for sample in game.imitation_data:
                        output_file.write(json.dumps(sample) + '\n')
                print('Saved {} samples to {}'.format(len(game.imitation_data), OUTPUT_PATH))
            else:
                print('No samples collected.')
        finally:
            pygame.quit()


if __name__ == '__main__':
    main()
