#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Mar 17 15:18:54 2017
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
import sip
import sys


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
        self.samp_rate = samp_rate = 32e3
        self.freq = freq = 434278100

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_range = Range(1e3, 60e3, 200, 32e3, 200)
        self._samp_rate_win = RangeWidget(self._samp_rate_range, self.set_samp_rate, "samp_rate", "counter_slider", float)
        self.top_layout.addWidget(self._samp_rate_win)
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
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_0, "LPDemodulatedSignal")
        self.qtgui_tab_widget_0_widget_1 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_1)
        self.qtgui_tab_widget_0_grid_layout_1 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_1.addLayout(self.qtgui_tab_widget_0_grid_layout_1)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_1, "FrequencyDomainOfDemodulatedSignal")
        self.qtgui_tab_widget_0_widget_2 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_2)
        self.qtgui_tab_widget_0_grid_layout_2 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_2.addLayout(self.qtgui_tab_widget_0_grid_layout_2)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_2, "TimeRepresentationOfCarrier")
        self.qtgui_tab_widget_0_widget_3 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_3)
        self.qtgui_tab_widget_0_grid_layout_3 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_3.addLayout(self.qtgui_tab_widget_0_grid_layout_3)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_3, "TimeDomainForDemodSignal")
        self.top_layout.addWidget(self.qtgui_tab_widget_0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 4000, 1, firdes.WIN_HAMMING, 6.76))
        self.blocks_probe_signal_x_0 = blocks.probe_signal_c()
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((2, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/asemwal/github/real_time_packet/signal/H.sig", True)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(900e6, analog.GR_COS_WAVE, 434278100, 10, 0)
        self.TimeDomainForDemodSignal_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.TimeDomainForDemodSignal_0.set_update_time(0.01)
        self.TimeDomainForDemodSignal_0.set_y_axis(-1.2, 1.2)
        
        self.TimeDomainForDemodSignal_0.set_y_label("Amplitude", "")
        
        self.TimeDomainForDemodSignal_0.enable_tags(-1, True)
        self.TimeDomainForDemodSignal_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.TimeDomainForDemodSignal_0.enable_autoscale(False)
        self.TimeDomainForDemodSignal_0.enable_grid(True)
        self.TimeDomainForDemodSignal_0.enable_control_panel(True)
        
        if not True:
          self.TimeDomainForDemodSignal_0.disable_legend()
        
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
                    self.TimeDomainForDemodSignal_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.TimeDomainForDemodSignal_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.TimeDomainForDemodSignal_0.set_line_label(i, labels[i])
            self.TimeDomainForDemodSignal_0.set_line_width(i, widths[i])
            self.TimeDomainForDemodSignal_0.set_line_color(i, colors[i])
            self.TimeDomainForDemodSignal_0.set_line_style(i, styles[i])
            self.TimeDomainForDemodSignal_0.set_line_marker(i, markers[i])
            self.TimeDomainForDemodSignal_0.set_line_alpha(i, alphas[i])
        
        self._TimeDomainForDemodSignal_0_win = sip.wrapinstance(self.TimeDomainForDemodSignal_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._TimeDomainForDemodSignal_0_win)
        self.TimeDomainForDemodSignal = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.TimeDomainForDemodSignal.set_update_time(0.01)
        self.TimeDomainForDemodSignal.set_y_axis(-1.2, 1.2)
        
        self.TimeDomainForDemodSignal.set_y_label("Amplitude", "")
        
        self.TimeDomainForDemodSignal.enable_tags(-1, True)
        self.TimeDomainForDemodSignal.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.TimeDomainForDemodSignal.enable_autoscale(False)
        self.TimeDomainForDemodSignal.enable_grid(True)
        self.TimeDomainForDemodSignal.enable_control_panel(True)
        
        if not True:
          self.TimeDomainForDemodSignal.disable_legend()
        
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
                self.TimeDomainForDemodSignal.set_line_label(i, "Data {0}".format(i))
            else:
                self.TimeDomainForDemodSignal.set_line_label(i, labels[i])
            self.TimeDomainForDemodSignal.set_line_width(i, widths[i])
            self.TimeDomainForDemodSignal.set_line_color(i, colors[i])
            self.TimeDomainForDemodSignal.set_line_style(i, styles[i])
            self.TimeDomainForDemodSignal.set_line_marker(i, markers[i])
            self.TimeDomainForDemodSignal.set_line_alpha(i, alphas[i])
        
        self._TimeDomainForDemodSignal_win = sip.wrapinstance(self.TimeDomainForDemodSignal.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._TimeDomainForDemodSignal_win)
        self.LPDemodulatedSignal_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	1e9, #bw
        	"", #name
        	1 #number of inputs
        )
        self.LPDemodulatedSignal_0.set_update_time(0.10)
        self.LPDemodulatedSignal_0.set_y_axis(-140, 10)
        self.LPDemodulatedSignal_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.LPDemodulatedSignal_0.enable_autoscale(True)
        self.LPDemodulatedSignal_0.enable_grid(True)
        self.LPDemodulatedSignal_0.set_fft_average(1.0)
        self.LPDemodulatedSignal_0.enable_control_panel(True)
        
        if not True:
          self.LPDemodulatedSignal_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.LPDemodulatedSignal_0.set_plot_pos_half(not True)
        
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
                self.LPDemodulatedSignal_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.LPDemodulatedSignal_0.set_line_label(i, labels[i])
            self.LPDemodulatedSignal_0.set_line_width(i, widths[i])
            self.LPDemodulatedSignal_0.set_line_color(i, colors[i])
            self.LPDemodulatedSignal_0.set_line_alpha(i, alphas[i])
        
        self._LPDemodulatedSignal_0_win = sip.wrapinstance(self.LPDemodulatedSignal_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._LPDemodulatedSignal_0_win)
        self.LPDemodulatedSignal = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	433.92e6, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.LPDemodulatedSignal.set_update_time(0.10)
        self.LPDemodulatedSignal.set_y_axis(-140, 10)
        self.LPDemodulatedSignal.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.LPDemodulatedSignal.enable_autoscale(True)
        self.LPDemodulatedSignal.enable_grid(True)
        self.LPDemodulatedSignal.set_fft_average(1.0)
        self.LPDemodulatedSignal.enable_control_panel(True)
        
        if not True:
          self.LPDemodulatedSignal.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.LPDemodulatedSignal.set_plot_pos_half(not True)
        
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
                self.LPDemodulatedSignal.set_line_label(i, "Data {0}".format(i))
            else:
                self.LPDemodulatedSignal.set_line_label(i, labels[i])
            self.LPDemodulatedSignal.set_line_width(i, widths[i])
            self.LPDemodulatedSignal.set_line_color(i, colors[i])
            self.LPDemodulatedSignal.set_line_alpha(i, alphas[i])
        
        self._LPDemodulatedSignal_win = sip.wrapinstance(self.LPDemodulatedSignal.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._LPDemodulatedSignal_win)
        self.FrequencyDomainOfDemodulatedSignal = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	1000e6, #bw
        	"", #name
        	1 #number of inputs
        )
        self.FrequencyDomainOfDemodulatedSignal.set_update_time(0.10)
        self.FrequencyDomainOfDemodulatedSignal.set_y_axis(-140, 10)
        self.FrequencyDomainOfDemodulatedSignal.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.FrequencyDomainOfDemodulatedSignal.enable_autoscale(True)
        self.FrequencyDomainOfDemodulatedSignal.enable_grid(True)
        self.FrequencyDomainOfDemodulatedSignal.set_fft_average(1.0)
        self.FrequencyDomainOfDemodulatedSignal.enable_control_panel(True)
        
        if not True:
          self.FrequencyDomainOfDemodulatedSignal.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.FrequencyDomainOfDemodulatedSignal.set_plot_pos_half(not True)
        
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
                self.FrequencyDomainOfDemodulatedSignal.set_line_label(i, "Data {0}".format(i))
            else:
                self.FrequencyDomainOfDemodulatedSignal.set_line_label(i, labels[i])
            self.FrequencyDomainOfDemodulatedSignal.set_line_width(i, widths[i])
            self.FrequencyDomainOfDemodulatedSignal.set_line_color(i, colors[i])
            self.FrequencyDomainOfDemodulatedSignal.set_line_alpha(i, alphas[i])
        
        self._FrequencyDomainOfDemodulatedSignal_win = sip.wrapinstance(self.FrequencyDomainOfDemodulatedSignal.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._FrequencyDomainOfDemodulatedSignal_win)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.LPDemodulatedSignal_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.TimeDomainForDemodSignal_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.FrequencyDomainOfDemodulatedSignal, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_probe_signal_x_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.LPDemodulatedSignal, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.TimeDomainForDemodSignal, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.LPDemodulatedSignal.set_frequency_range(433.92e6, self.samp_rate)
        self.TimeDomainForDemodSignal.set_samp_rate(self.samp_rate)
        self.TimeDomainForDemodSignal_0.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 4000, 1, firdes.WIN_HAMMING, 6.76))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq


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
