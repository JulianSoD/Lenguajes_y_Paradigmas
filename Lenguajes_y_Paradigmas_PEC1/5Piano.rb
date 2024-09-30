# PIANO

use_bpm 150
sync :inicio
sleep 65

live_loop :chorus_loop do
  use_synth :piano
  
  notes = [
    #Sweet dreams are made of this
    [:eb4, 1], [:eb4, 1], [:c4, 1], [:eb4, 0.5], [:eb4, 1], [:d4, 2.5],
    
    #Who am I to disagree?
    [:eb4, 0.5], [:eb4, 0.5], [:c4, 1], [:eb4, 1], [:c4, 1], [:eb4, 0.5], [:f4, 1.5], [:d4, 2],
    
    #I've traveled the world and the seven seas
    [:eb4, 0.5], [:eb4, 0.5], [:c4, 1], [:eb4, 0.5], [:eb4, 0.5], [:c4, 0.5], [:eb4, 1], [:f4, 1], [:d4, 2],
    
    #Everybody's looking for something
    [:eb4, 1], [:c4, 1], [:eb4, 1], [:c4, 0.5], [:eb4, 1], [:f4, 1], [:eb4, 1], [:c4, 1.5],
    
    #Some of them want to use you
    [:eb4, 0.5], [:eb4, 0.5], [:c4, 1], [:eb4, 0.5], [:eb4, 0.5], [:c4, 0.5], [:f4, 1], [:c4, 3],
    
    #Some of them want to get used by you
    [:eb4, 0.5], [:eb4, 0.5],[:c4, 1], [:eb4, 0.5], [:eb4, 0.5], [:c4, 0.5], [:eb4, 1], [:f4, 1], [:d4, 2.5],
    
    #Some of them want to abuse you
    [:eb4, 0.5], [:eb4, 0.5], [:c4, 1],[:eb4, 0.5], [:eb4, 0.5], [:c4, 0.5], [:f4, 1], [:c4, 3.25],
    
    #Some of them want to be abused
    [:eb4, 0.5], [:eb4, 0.5], [:c4, 1], [:eb4, 0.5], [:eb4, 0.5],[:c4, 0.5], [:eb4, 1], [:f4, 1.5], [:d4, 3]
  ]
  
  with_fx :reverb, room: 0.8, mix: 0.6 do
    with_fx :echo, phase: 0.025, decay: 0.25 do
      1.times do
        notes.each do |note, duration|
          play note, release: duration
          sleep duration
        end
      end
    end
  end
  sleep 32.25
end

