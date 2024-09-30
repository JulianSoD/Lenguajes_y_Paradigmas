# HI-HATS

use_bpm 150
sync :inicio
sleep 16

live_loop :hihats do
  16.times do
    sleep 0.5
    with_fx :reverb, room: 0.1, mix: 0.5 do
      sample :drum_cymbal_closed, amp: 1
      sample :drum_cymbal_soft, amp: 0.3
    end
    sleep 0.5
  end
end