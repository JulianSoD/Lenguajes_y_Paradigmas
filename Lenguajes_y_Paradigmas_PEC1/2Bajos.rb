#BAJOS
use_bpm 150

sync :inicio
sleep 16

live_loop :bass_loop do
  with_fx :lpf, cutoff: 80, amp: 1 do
    play :e2, release: 8
    sleep 8
    play :d2, release: 8
    sleep 8
    play :g2, release: 8
    sleep 8
    play :c2, release: 8
    sleep 8
  end
end