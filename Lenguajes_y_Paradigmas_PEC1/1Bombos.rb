# BOMBOS

use_bpm 150
cue :inicio
contador = 0

live_loop :techno_loop do
  16.times do |i|
    if (i == 7 || i == 15) && contador < 4
      with_fx :reverb, room: 0.1, mix: 0.5 do
        with_fx :distortion, distort: 0.5 do
          sample :bd_tek, rate: 0.8
          sleep 0.5
          sample :bd_tek, rate: 0.8
          sleep 0.5
        end
      end
    else
      with_fx :reverb, room: 0.1, mix: 0.5 do
        with_fx :distortion, distort: 0.5 do
          sample :bd_tek, rate: 0.8
          sleep 1
        end
      end
    end
  end
  contador += 1
end
