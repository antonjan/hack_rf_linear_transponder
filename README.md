# hack_rf_linear_transponder
This repository will have the gnuradio hack rf Linear transponder and telemetry code.<br>
The original concept was test with hackrf transmitter where after the new IQ transmiter board was made to relace hackrf.<br>
The Gnuradio tansponder will run in a Ornage Pi with an <a href="https://github.com/antonjan/IQ_Modulator>IQ_Modulator" >transmitter</a> board plug into Orange Pi.<br>
The Receiver is an rtl dongle with a front end Saw filter on the same IQ modulator board<br>
The Battery and Solar Voltage and TX power also get read from this IQ modulator board.<br>
# Software
1) Gnuradio transponder.
2) Telemetry CW and PSK1200 (1200 2200khz).<br>
Telemetry data Calsign:SolarV,BatteryV,TXPowerV,TransponderMode,UseCount,ComandEcho,Time.<br>
The telemetry was tested on <a href="https://github.com/antonjan/Bacar_Raspberry_tx"> Bacar Balloon</a> 
# Hardware
1) IQ Modulator board for TX (500mW) (The IQ modulator board replace the hackrf board.)<br>
2) RTL SDR Dongle for RX<br>
3) Orange PI zero<br>
# Todo
1) Solar and Battery mangement and the battery.<br>
2) Permanent magnet Orieantation controle board.<br>
3) Space frame<br>
4) Antenna and ded_microswitch board.<br>
