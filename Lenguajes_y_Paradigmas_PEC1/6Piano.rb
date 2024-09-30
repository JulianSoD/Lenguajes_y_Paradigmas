# PIANO FINAL

use_bpm 150
sync :inicio1
sleep 127



use_synth :piano

with_fx :reverb, room: 0.8, mix: 0.6 do
  with_fx :echo, phase: 0.025, decay: 0.25 do
    notes = [
      [:c4, 1], [:c4, 0.5], [:c4, 0.5], [:eb4, 0.5], [:eb4, 0.5],
      [:c4, 0.5], [:c4, 0.5], [:ab3, 0.5], [:ab3, 0.5],
      [:ab3, 0.5], [:c4, 0.5], [:g3, 0.5], [:g3, 0.5],
      [:bb3, 0.5], [:c4, 0.5]
    ]
    
    4.times do
      notes.each do |note, duration|
        play note, release: duration
        sleep duration
      end
    end
  end
end