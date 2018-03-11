# -*- coding: utf-8 -*-
import pygame.midi

pygame.init()
pygame.midi.init()
input_id = pygame.midi.get_default_input_id()
output_id = pygame.midi.get_default_output_id()
print("input MIDI:%d" % input_id)
print("output MIDI:%d" % output_id)
i = pygame.midi.Input(input_id)
o = pygame.midi.Output(output_id)

print ("starting")
print ("full midi_events:[[[status,data1,data2,data3],timestamp],...]")

going = True
count = 0
while going:
    if i.poll():
        midi_events = i.read(10)
        if midi_events[0][0][0] == 144:
            o.note_on(midi_events[0][0][1],99,9)
        print "full midi_events:" + str(midi_events)
        count += 1
    if count >= 100:
        going = False

i.close()
o.close()
pygame.midi.quit()
pygame.quit()
exit()
