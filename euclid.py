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

    @staticmethod
    def get_port():
        port_list = mido.get_output_names()
        print('Available MIDI ports are \n')
        for name in range(0, len(port_list)):
            print('%s' % name, port_list[name])
        return port_list[int(input('\nChoose port by number: '))]

    @staticmethod
    def get_channel():
        return int(input('Choose MIDI channel to output on (1-16): ')) - 1


class SeqOptions:
    def __init__(self):
        self.bpm = self.get_bpm()
        self.bars = self.get_bars()
        self.notes = self.get_notes()

    @staticmethod
    def get_bpm():
        return int(input('Choose BPM: '))

    @staticmethod
    def get_bars():
        return int(input('Choose number of bars: '))

    @staticmethod
    def get_notes():
        return int(input('Choose number of notes: '))


class Process:
    def __init__(self, options):
        self.duration = self.calculate_duration(options.bpm, options.bars)
        self.division_length = self.calculate_division_length(options.notes)
        self.note_length = self.calculate_note_length(options.bpm)
        self.gap = self.calculate_gap()

    @staticmethod
    def calculate_duration(bpm, bars):
        return float(60/bpm) * 4 * bars

    def calculate_division_length(self, notes):
        return self.duration/notes

    def calculate_note_length(self, bpm):
        note_length = (60/bpm)/4
        while note_length >= self.division_length:
            note_length = note_length/2
        return note_length

    def calculate_gap(self):
        return self.division_length - self.note_length

    def check_calculations(self):
        print(f'{self.duration}\n{self.division_length}\n{self.note_length}\n{self.gap}')


class MidiOutput:
    def __init__(self):
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    output_port = MidiOptions.get_port()
    output_channel = MidiOptions.get_channel()
    sequence = SeqOptions()
    calculate = Process(sequence)

    calculate.check_calculations()
    print('Completed')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
