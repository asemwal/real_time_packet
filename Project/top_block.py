#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Mar  8 10:00:01 2017
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

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import time


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 10e3
        self.freq = freq = 2e3

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_range = Range(1e3, 40e3, 200, 10e3, 200)
        self._samp_rate_win = RangeWidget(self._samp_rate_range, self.set_samp_rate, "samp_rate", "counter_slider", float)
        self.top_layout.addWidget(self._samp_rate_win)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(37.2, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(10000, 0)
          
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=4,
                decimation=3,
                taps=None,
                fractional_bw=0.45,
        )
        self.qtgui_tab_widget_0 = Qt.QTabWidget()
        self.qtgui_tab_widget_0_widget_0 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_0)
        self.qtgui_tab_widget_0_grid_layout_0 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_0.addLayout(self.qtgui_tab_widget_0_grid_layout_0)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_0, "Time")
        self.qtgui_tab_widget_0_widget_1 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_1)
        self.qtgui_tab_widget_0_grid_layout_1 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_1.addLayout(self.qtgui_tab_widget_0_grid_layout_1)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_1, "Frequency")
        self.top_layout.addWidget(self.qtgui_tab_widget_0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 10, 1, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((2, ))
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 434.015e6, 1, 0)
        self.Time_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.Time_0.set_update_time(0.10)
        self.Time_0.set_y_axis(-1, 1)
        
        self.Time_0.set_y_label("Amplitude", "")
        
        self.Time_0.enable_tags(-1, True)
        self.Time_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.Time_0.enable_autoscale(True)
        self.Time_0.enable_grid(True)
        self.Time_0.enable_control_panel(True)
        
        if not True:
          self.Time_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.Time_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.Time_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.Time_0.set_line_label(i, labels[i])
            self.Time_0.set_line_width(i, widths[i])
            self.Time_0.set_line_color(i, colors[i])
            self.Time_0.set_line_style(i, styles[i])
            self.Time_0.set_line_marker(i, markers[i])
            self.Time_0.set_line_alpha(i, alphas[i])
        
        self._Time_0_win = sip.wrapinstance(self.Time_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._Time_0_win)
        self.Time = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.Time.set_update_time(0.10)
        self.Time.set_y_axis(-1, 1)
        
        self.Time.set_y_label("Amplitude", "")
        
        self.Time.enable_tags(-1, True)
        self.Time.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.Time.enable_autoscale(True)
        self.Time.enable_grid(True)
        self.Time.enable_control_panel(True)
        
        if not True:
          self.Time.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Time.set_line_label(i, "Data {0}".format(i))
            else:
                self.Time.set_line_label(i, labels[i])
            self.Time.set_line_width(i, widths[i])
            self.Time.set_line_color(i, colors[i])
            self.Time.set_line_style(i, styles[i])
            self.Time.set_line_marker(i, markers[i])
            self.Time.set_line_alpha(i, alphas[i])
        
        self._Time_win = sip.wrapinstance(self.Time.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._Time_win)
        self.Frequency_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	1000e6, #bw
        	"", #name
        	1 #number of inputs
        )
        self.Frequency_0.set_update_time(0.10)
        self.Frequency_0.set_y_axis(-140, 10)
        self.Frequency_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, 0.0, 0, "")
        self.Frequency_0.enable_autoscale(True)
        self.Frequency_0.enable_grid(True)
        self.Frequency_0.set_fft_average(1.0)
        self.Frequency_0.enable_control_panel(True)
        
        if not True:
          self.Frequency_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.Frequency_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Frequency_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.Frequency_0.set_line_label(i, labels[i])
            self.Frequency_0.set_line_width(i, widths[i])
            self.Frequency_0.set_line_color(i, colors[i])
            self.Frequency_0.set_line_alpha(i, alphas[i])
        
        self._Frequency_0_win = sip.wrapinstance(self.Frequency_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._Frequency_0_win)
        self.Frequency = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.Frequency.set_update_time(0.10)
        self.Frequency.set_y_axis(-140, 10)
        self.Frequency.set_trigger_mode(qtgui.TRIG_MODE_NORM, 0.0, 0, "")
        self.Frequency.enable_autoscale(True)
        self.Frequency.enable_grid(True)
        self.Frequency.set_fft_average(1.0)
        self.Frequency.enable_control_panel(True)
        
        if not True:
          self.Frequency.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.Frequency.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Frequency.set_line_label(i, "Data {0}".format(i))
            else:
                self.Frequency.set_line_label(i, labels[i])
            self.Frequency.set_line_width(i, widths[i])
            self.Frequency.set_line_color(i, colors[i])
            self.Frequency.set_line_alpha(i, alphas[i])
        
        self._Frequency_win = sip.wrapinstance(self.Frequency.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._Frequency_win)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0, 0), (self.Time_0, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.Frequency_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.Frequency, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.Time, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_multiply_xx_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.Frequency.set_frequency_range(0, self.samp_rate)
        self.Time.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 10, 1, firdes.WIN_HAMMING, 6.76))
        self.Time_0.set_samp_rate(self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.rtlsdr_source_0.set_center_freq(self.freq, 0)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
