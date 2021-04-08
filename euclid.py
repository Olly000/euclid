#!/usr/bin/env python3

# import midi object library and set backend to pygame to allow access to midi ports.

import mido
import pygame.midi as pym
from time import sleep

mido.set_backend('mido.backends.pygame')
pym.init()

class MidiOptions:
    def __init__(self):
        self.port = self.get_port()
        self.channel = self.get_channel()

    def get_port(self):
        port_list = mido.get_output_names()

    def get_channel(self):
        return int(input('Choose MIDI channel to output on (1-16): ')) - 1


class SeqOptions:
    def __init__(self):
        self.bpm = self.get_bpm()
        self.bars = self.get_bars()
        self.divisions = self.get_divisions()

    def get_bpm(self):
        pass

    def get_bars(self):
        pass

    def get_divisions(self):
        pass


class Process:
    def __init__(self, options):
        self.duration = self.calculate_duration(options.bpm, options.bars)
        self.division_length = self.calculate_division_length(options.divisions)
        self.note_length = self.calculate_note_length(options.bpm) # this should check vs division_length
        self.gap_length = self.calculate_gap()

    def calculate_duration(self, bpm, bars):
        pass

    def calculate_division_length(self, divisions):
        pass

    def calculate_note_length(self, bpm):
        pass

    def calculate_gap(self):
        return self.division_length - self.note_length


class Output:
    def __init__(self):



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    midi = MidiOptions()
    sequence = SeqOptions()


    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
