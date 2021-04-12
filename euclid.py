#!/usr/bin/env python3

# import midi object library and set backend to pygame to allow access to midi ports.

import mido
import pygame.midi as pym
from time import sleep

mido.set_backend('mido.backends.pygame')
pym.init()


class UserOptions:
    def __init__(self):
        self.port = self.get_port()
        self.channel = self.get_channel()
        self.bpm = self.get_bpm()
        self.bars = self.get_bars()
        self.notes = self.get_notes()

    @staticmethod
    def get_port():
        port_list = mido.get_output_names()
        print('Available MIDI ports are \n')
        for name in range(0, len(port_list)):
            print('%s' % name, port_list[name])
        return port_list[int(input('Choose port by number: '))]

    @staticmethod
    def get_channel():
        return int(input('Choose MIDI channel to output on (1-16): ')) - 1

    @staticmethod
    def get_bpm():
        return int(input('Choose BPM: '))

    @staticmethod
    def get_bars():
        return int(input('Choose number of bars: '))

    @staticmethod
    def get_notes():
        return int(input('Choose number of notes: '))


class Calculate:
    def __init__(self, options):
        self.options = options
        self.duration = self.calculate_duration()
        self.division_length = self.calculate_division_length()
        self.note_length = self.calculate_note_length()
        self.gap = self.calculate_gap()

    def calculate_duration(self):
        return float(60/self.options.bpm) * 4 * self.options.bars

    def calculate_division_length(self):
        return self.duration/self.options.notes

    def calculate_note_length(self):
        note_length = (60 / self.options.bpm) / 4
        while note_length >= self.division_length:
            note_length /= 2
        return note_length

    def calculate_gap(self):
        return self.division_length - self.note_length

    def check_calculations(self):
        print(f'{self.duration}\n{self.division_length}\n{self.note_length}\n{self.gap}')


class MidiOutput:
    def __init__(self):
        self.parameters = UserOptions()
        self.durations = Calculate(self.parameters)

    def send_start(self):
        self.parameters.out_port.open()
        self.parameters.out_port.send(mido.Message('record'))

    def send_note(self):
        on_msg = mido.Message('note_on', channel=self.parameters.channel, note=60)
        self.parameters.out_port.send(on_msg)
        sleep(self.durations.note_length)
        off_msg = mido.Message('note_off', channel=self.parameters.channel, note=60)
        self.parameters.out_port.send(off_msg)

    def note_controller(self):
        for note in range(1, self.parameters.notes):
            self.send_note()
            sleep(self.durations.gap)

    def end_process(self):  # closes port and sends user confirmation sequence ended
        self.out_port.close()
        print('Sequence ended successfully')

    def sequence_controller(self):
        self.send_start()
        self.note_controller()
        self.end_process()


if __name__ == '__main__':

    sequence = MidiOutput()
    sequence.sequence_controller()

    print('Completed')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
