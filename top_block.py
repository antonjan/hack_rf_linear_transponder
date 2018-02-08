#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Linear Transponder
# Author: Anton JAnovsky
# Description: Satellite Linear Transponder
# Generated: Thu Feb  8 21:38:01 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Linear Transponder")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.tx_freq = tx_freq = 438.1e6
        self.squelch_level = squelch_level = -12
        self.samp_rate = samp_rate = 2e6
        self.rx_freq = rx_freq = 145.3e6
        self.rtl_rf_gain = rtl_rf_gain = 50
        self.rtl_if_gain = rtl_if_gain = 50
        self.rf_gain = rf_gain = 50
        self.if_gain = if_gain = 50
        self.bb_gain = bb_gain = 50

        ##################################################
        # Blocks
        ##################################################
        _tx_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tx_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tx_freq_sizer,
        	value=self.tx_freq,
        	callback=self.set_tx_freq,
        	label='TX Freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tx_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tx_freq_sizer,
        	value=self.tx_freq,
        	callback=self.set_tx_freq,
        	minimum=430e6,
        	maximum=440e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tx_freq_sizer)
        _squelch_level_sizer = wx.BoxSizer(wx.VERTICAL)
        self._squelch_level_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_squelch_level_sizer,
        	value=self.squelch_level,
        	callback=self.set_squelch_level,
        	label='squelch evel',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._squelch_level_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_squelch_level_sizer,
        	value=self.squelch_level,
        	callback=self.set_squelch_level,
        	minimum=-70,
        	maximum=30,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_squelch_level_sizer)
        _rx_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rx_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rx_freq_sizer,
        	value=self.rx_freq,
        	callback=self.set_rx_freq,
        	label='RX Freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rx_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rx_freq_sizer,
        	value=self.rx_freq,
        	callback=self.set_rx_freq,
        	minimum=144e6,
        	maximum=146e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rx_freq_sizer)
        _rtl_rf_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rtl_rf_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rtl_rf_gain_sizer,
        	value=self.rtl_rf_gain,
        	callback=self.set_rtl_rf_gain,
        	label='RTL RF Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rtl_rf_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rtl_rf_gain_sizer,
        	value=self.rtl_rf_gain,
        	callback=self.set_rtl_rf_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rtl_rf_gain_sizer)
        _rtl_if_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rtl_if_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rtl_if_gain_sizer,
        	value=self.rtl_if_gain,
        	callback=self.set_rtl_if_gain,
        	label='RTL IF Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rtl_if_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rtl_if_gain_sizer,
        	value=self.rtl_if_gain,
        	callback=self.set_rtl_if_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rtl_if_gain_sizer)
        _rf_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rf_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	label='RF Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rf_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rf_gain_sizer)
        _if_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._if_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_if_gain_sizer,
        	value=self.if_gain,
        	callback=self.set_if_gain,
        	label='IF Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._if_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_if_gain_sizer,
        	value=self.if_gain,
        	callback=self.set_if_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_if_gain_sizer)
        _bb_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._bb_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_bb_gain_sizer,
        	value=self.bb_gain,
        	callback=self.set_bb_gain,
        	label='BB Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._bb_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_bb_gain_sizer,
        	value=self.bb_gain,
        	callback=self.set_bb_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_bb_gain_sizer)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(rx_freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(2, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(rtl_rf_gain, 0)
        self.rtlsdr_source_0.set_if_gain(rtl_if_gain, 0)
        self.rtlsdr_source_0.set_bb_gain(50, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(tx_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(rf_gain, 0)
        self.osmosdr_sink_0.set_if_gain(if_gain, 0)
        self.osmosdr_sink_0.set_bb_gain(bb_gain, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 100000, 50000, firdes.WIN_HAMMING, 6.76))
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(squelch_level, 1e-4, 0, True)
        self.analog_agc_xx_0 = analog.agc_cc(1e-4, 1.0, 1.0)
        self.analog_agc_xx_0.set_max_gain(2)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.analog_pwr_squelch_xx_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.osmosdr_sink_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_agc_xx_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))    

    def get_tx_freq(self):
        return self.tx_freq

    def set_tx_freq(self, tx_freq):
        self.tx_freq = tx_freq
        self._tx_freq_slider.set_value(self.tx_freq)
        self._tx_freq_text_box.set_value(self.tx_freq)
        self.osmosdr_sink_0.set_center_freq(self.tx_freq, 0)

    def get_squelch_level(self):
        return self.squelch_level

    def set_squelch_level(self, squelch_level):
        self.squelch_level = squelch_level
        self._squelch_level_slider.set_value(self.squelch_level)
        self._squelch_level_text_box.set_value(self.squelch_level)
        self.analog_pwr_squelch_xx_0.set_threshold(self.squelch_level)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 100000, 50000, firdes.WIN_HAMMING, 6.76))

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self._rx_freq_slider.set_value(self.rx_freq)
        self._rx_freq_text_box.set_value(self.rx_freq)
        self.rtlsdr_source_0.set_center_freq(self.rx_freq, 0)

    def get_rtl_rf_gain(self):
        return self.rtl_rf_gain

    def set_rtl_rf_gain(self, rtl_rf_gain):
        self.rtl_rf_gain = rtl_rf_gain
        self._rtl_rf_gain_slider.set_value(self.rtl_rf_gain)
        self._rtl_rf_gain_text_box.set_value(self.rtl_rf_gain)
        self.rtlsdr_source_0.set_gain(self.rtl_rf_gain, 0)

    def get_rtl_if_gain(self):
        return self.rtl_if_gain

    def set_rtl_if_gain(self, rtl_if_gain):
        self.rtl_if_gain = rtl_if_gain
        self._rtl_if_gain_slider.set_value(self.rtl_if_gain)
        self._rtl_if_gain_text_box.set_value(self.rtl_if_gain)
        self.rtlsdr_source_0.set_if_gain(self.rtl_if_gain, 0)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self._rf_gain_slider.set_value(self.rf_gain)
        self._rf_gain_text_box.set_value(self.rf_gain)
        self.osmosdr_sink_0.set_gain(self.rf_gain, 0)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self._if_gain_slider.set_value(self.if_gain)
        self._if_gain_text_box.set_value(self.if_gain)
        self.osmosdr_sink_0.set_if_gain(self.if_gain, 0)

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self._bb_gain_slider.set_value(self.bb_gain)
        self._bb_gain_text_box.set_value(self.bb_gain)
        self.osmosdr_sink_0.set_bb_gain(self.bb_gain, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
