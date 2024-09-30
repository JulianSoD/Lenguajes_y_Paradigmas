use_bpm 150
sync :inicio
cue :inicio1

roomer = 0.1
mixer = 0.1


live_loop :vocales_loop do
  sleep 64.5
  1.times do
    with_fx :reverb, room: roomer, mix: mixer do
      with_fx :echo, phase: 0.05, decay: 0.2 do
        sample "C:/Users/julia/Downloads/Lenguajes_y_Paradigmas_PEC1/vocales.wav", rate: 1.175, amp: 2
      end
    end
  end
  sleep 30.5
end