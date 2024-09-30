#live Fx

use_bpm 150

#sample :vinyl_backspin, rate: 1, amp: 1.5

sample :misc_cineboom, rate: 1, amp: 3


live_loop :cabina do
  sleep 5
  sample "C:/Users/julia/Downloads/Lenguajes_y_Paradigmas_PEC1/EN-CABINA-ADRIAN-LM.wav", rate: 1, amp: 1.5
  sleep 100
end